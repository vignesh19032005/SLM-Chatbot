# views.py
import requests
import time
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core.cache import cache
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# API configuration
API_URL = "https://api-inference.huggingface.co/models/microsoft/phi-2"
API_KEY = "Your_HuggingFace_API_Key"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Configure retry strategy
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
)

# Create session with retry strategy
def create_session():
    session = requests.Session()
    adapter = HTTPAdapter(
        max_retries=retry_strategy,
        pool_connections=10,
        pool_maxsize=10
    )
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session

def format_prompt(user_input):
    """Format the prompt to guide the model's response format."""
    return (
        "You are a helpful AI assistant. Provide clear, direct responses. "
        "For complex topics, break down the information into digestible parts.\n\n"
        f"User: {user_input}\nAssistant:"
    )

def clean_response(response_text):
    """Clean and format the model's response."""
    # Remove any system prompts or role indicators
    cleaned = response_text.replace("Assistant:", "").replace("User:", "").strip()
    
    # Remove any meta-instructions that might appear in parentheses
    if "(" in cleaned and ")" in cleaned:
        cleaned = cleaned.split("(")[0].strip()
    
    return cleaned

@require_http_methods(["POST"])
def chatbot_response(request):
    """Handle chatbot responses with improved connection handling."""
    try:
        user_input = request.POST.get("message", "").strip()
        if not user_input:
            return JsonResponse({"error": "Please enter a message"}, status=400)

        # Adjust max_length based on input length
        input_length = len(user_input)

        payload = {
            "inputs": format_prompt(user_input),
            "parameters": {
                "max_length": 4096,
                "temperature": 0.7,
                "top_p": 0.9,
                "return_full_text": False,
                "stop": ["\nUser:", "\nAssistant:", "<|endoftext|>"]
            }
        }

        # Use session with retry strategy
        session = create_session()
        
        # Increase timeout for longer queries
        timeout = 45 if input_length > 100 else 30
        
        response = session.post(
            API_URL,
            headers=HEADERS,
            json=payload,
            timeout=timeout
        )

        if response.status_code == 200:
            response_data = response.json()
            generated_text = response_data[0].get("generated_text", "").strip()
            cleaned_response = clean_response(generated_text)
            return JsonResponse({"response": cleaned_response})

        elif response.status_code == 503:
            return JsonResponse({
                "error": "Model is loading. Please try again in a few seconds."
            }, status=503)

        else:
            return JsonResponse({
                "error": f"API error: {response.status_code}"
            }, status=response.status_code)

    except requests.exceptions.Timeout:
        return JsonResponse({
            "error": "The request took too long to process. Please try a shorter question or try again later."
        }, status=504)

    except requests.exceptions.RequestException as e:
        return JsonResponse({
            "error": f"Connection error: {str(e)}"
        }, status=500)

    except Exception as e:
        return JsonResponse({
            "error": f"Unexpected error: {str(e)}"
        }, status=500)

def chatbot_ui(request):
    """Render chatbot UI."""
    return render(request, "chatbot/chat.html")