from django.urls import path
from .views import chatbot_ui, chatbot_response

urlpatterns = [
    path('', chatbot_ui, name='chatbot_ui'),
    path('chat/', chatbot_response, name='chatbot_response'),
]