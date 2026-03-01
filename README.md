# 🚀 Domain-Specific AI Assistant  

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Groq](https://img.shields.io/badge/LLM-Groq-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> An intelligent FastAPI-based AI web assistant that adapts responses based on selected domain using prompt engineering and Groq LLM.

---

## 🧠 Overview

**Domain-Specific AI Assistant** is a modular AI web application that generates intelligent, structured responses tailored to specific domains such as:

- 📘 Academic Tutor  
- 💼 Placement Mentor  
- 🔬 Research Explainer  
- 🐞 Code Debugger  
- 💡 Startup Evaluator  

Instead of switching models, this system dynamically modifies the **prompt engineering layer** based on domain selection.

This project demonstrates:

- Prompt Routing
- Domain-Specific AI Behavior
- Modular LLM Architecture
- Clean FastAPI Application Structure

---

## 🛠 Tech Stack

- ⚡ FastAPI (Backend)
- 🧠 Groq API (Llama 3.1)
- 🎨 HTML + CSS (Frontend UI)
- 🔐 Python Dotenv (Environment Variables)
- 🧩 Prompt Routing Architecture

---

## 📂 Project Structure

```
Domain-Specific-AI-Assistant/
│
├── main.py              # FastAPI app
├── llm_layer.py         # Groq API integration
├── prompt_router.py     # Domain-based prompt logic
├── templates/
│   └── index.html       # Frontend UI
├── static/
│   └── style.css        # Styling
├── .env                 # API key file
└── README.md
```

---

## 🔥 Features

✅ Select domain from predefined categories  
✅ Dynamic domain-based prompt generation  
✅ Clean interactive UI  
✅ Modular backend architecture  
✅ Easily extendable  
✅ Ready for SaaS scaling  

---

## 🧩 Architecture Flow

```
User Input + Selected Domain
              ↓
       Prompt Router
              ↓
   Groq LLM (Llama 3.1)
              ↓
      Structured AI Output
              ↓
        Rendered in UI
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Chethumalli/Domain-specific-AI-assistant.git
cd Domain-specific-AI-assistant
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
```

Activate:

**Windows**
```bash
env\Scripts\activate
```

**Mac/Linux**
```bash
source env/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn groq python-dotenv jinja2
```

---

### 4️⃣ Add Environment Variables

Create `.env` file:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

### 5️⃣ Run Application

```bash
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 🧠 Example Domain Behaviors

### 📘 Academic Mode
Explains concepts clearly with examples and step-by-step logic.

### 💼 Placement Mode
Provides structured interview answers and preparation tips.

### 🔬 Research Mode
Breaks down papers into:
- Abstract
- Methodology
- Results
- Conclusion

### 🐞 Debug Mode
Identifies code issues and explains fixes clearly.

### 💡 Startup Mode
Evaluates:
- Problem
- Market
- Competition
- Revenue model
- Risks

---

## 📈 Future Improvements

- 🔐 Add Authentication
- 💬 Chat history support
- 📚 Integrate RAG (Retrieval-Augmented Generation)
- ⚡ Streaming responses
- 🌐 Deploy to Render / Railway
- 💳 Convert into SaaS product

---

## 🌍 Deployment Guide (Optional)

### Deploy using Render

1. Push code to GitHub
2. Create new Web Service on Render
3. Add environment variable:
   ```
   GROQ_API_KEY
   ```
4. Set Start Command:
   ```
   uvicorn main:app --host 0.0.0.0 --port 10000
   ```

---

## 🎯 Learning Outcomes

This project helps you understand:

- Prompt Engineering
- Domain-based AI Routing
- FastAPI architecture design
- LLM integration workflow
- Modular AI system development

---

## 🏆 Resume Value

This project demonstrates:

✔ Practical LLM integration  
✔ Backend AI architecture  
✔ Prompt engineering expertise  
✔ API integration skills  
✔ Modular AI application design  

---

## 🤝 Contributing

Pull requests are welcome.  
If you found this useful, consider giving it a ⭐ star!

---

## 👨‍💻 Author

**Chethan C Malli**  
AI & ML Enthusiast  
Building scalable AI systems 🚀  

GitHub: https://github.com/Chethumalli  


