# 🚀 **SLM Chatbot - A Lightweight AI Chatbot Powered by Small Language Models (SLMs) 🤖**  

Welcome to the **SLM Chatbot**, a simple yet efficient chatbot that leverages **Small Language Models (SLMs)** like **Phi-2, Mistral-7B, DistillGPT, and more** via **Inference API calls**. Designed to run on **CPUs**, this chatbot is ideal for those looking to deploy AI assistants **without requiring expensive GPUs!** 💡⚡  

---

## 🔥 **Features**  
✅ **Multi-Model Support** – Switch between different SLMs dynamically! 🤯  
✅ **Fast & Efficient** – No heavy computing power required! 🖥️💨  
✅ **Built with Django** – A powerful backend framework for seamless API calls. ⚙️🛠️  
✅ **Simple Frontend** – Interactive UI using HTML, CSS, and JavaScript! 🎨📜  
✅ **Stop Sequences Handling** – Prevents infinite text generation & hallucinations! 🚦🔍  
✅ **Error Handling & Retry Mechanism** – Ensures stable chatbot responses! 🔄✅  

---

## 🏗 **Tech Stack**  
- **Backend:** Django (Python) 🐍  
- **Frontend:** HTML, CSS, JavaScript 🎨  
- **API Calls:** Hugging Face Inference API 🌐  
- **Models Used:** Phi-2 🤖  

---

## 📦 **Installation & Setup**  

### 🔹 1. Clone the Repository  
```bash
git clone https://github.com/yourusername/slm-chatbot.git
cd slm-chatbot
```

### 🔹 2. Set Up Virtual Environment

bash

CopyEdit

`python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate` 

### 🔹 3. Install Dependencies

bash

CopyEdit

`pip install -r requirements.txt` 

### 🔹 4. Add API Key

Create a `.env` file and add your Hugging Face API key:

ini

CopyEdit

`HUGGINGFACE_API_KEY=your_api_key_here` 

### 🔹 5. Run the Server

bash

CopyEdit

`python manage.py runserver` 

🚀 Your chatbot is now live at **http://127.0.0.1:8000/**! 🎉

* * *

🔗 **How to Use the Chatbot?**
------------------------------

1️⃣ Open the chatbot interface in your browser. 🌍  
2️⃣ Select an **SLM model** (e.g., Phi-2, Mistral-7B, etc.). 🤖  
3️⃣ Type your question and hit send. 💬⚡  
4️⃣ Get an AI-powered response! 🎯

* * *

⚠️ **Known Issues & Challenges**
--------------------------------

⚡ **Longer responses may cause timeouts** – Optimizations are in progress! ⏳  
⚡ **Some API calls take time** – Implementing better caching and retry mechanisms. 🔄  
⚡ **Handling larger queries** – Enhancing model selection logic for different use cases! 🛠

* * *

🚀 **Future Improvements**
--------------------------

🔹 Optimize API calls for **faster response times** ⚡  
🔹 Add **more models like TinyLlama & Gemma 2B** 🤖  
🔹 Implement **chat history & conversation memory** 🧠  
🔹 Deploy a **hosted version for real-world use** 🌎

* * *

📢 **Contributing**
-------------------

We welcome contributions! 🎉 If you'd like to improve the chatbot, feel free to **fork the repo, submit PRs, or open issues.**

📧 Contact: vigneshlakshmanababu@gmail.com
🌟 Don't forget to **star the repo** if you find it useful! ⭐

* * *

📌 **License**
--------------

This project is **MIT licensed**. Feel free to use, modify, and distribute!

Happy Coding! 🚀🤖💡
