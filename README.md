# JobConnect AI Chatbot

JobConnect AI is a minimal, modular chatbot built with Flask and Python. It provides users with career-focused support through a clean web interface. While the current version uses mock responses, it’s built to be easily extended with LangChain, OpenAI, and other AI tools.

---

## 🌟 Features

- Clean and modern frontend with text input and response display
- Flask backend that handles chat logic and serves the UI
- Modular file structure for easy extension and customization
- Ready to integrate with LangChain + OpenAI

---

## 🧱 Project Structure

```
jobconnect-ai/
├── main.py             # Flask app
├── chatbot.py          # Mock chatbot logic (easy to replace with LangChain)
├── templates/
│   └── index.html      # Web interface
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```

---

## 🚀 How to Run Locally

1. **Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/jobconnect-ai-chatbot.git
cd jobconnect-ai-chatbot
```

2. **Set up virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the server**
```bash
python3 main.py
```

5. **Open your browser** to:  
[http://localhost:5000](http://localhost:5000)

---

## 🛠 Future Enhancements

- Replace mock responses with LangChain + OpenAI integration
- Extract skills from job descriptions
- Compare user resume to job requirements
- Add memory or chat history
- Deploy to Render/Railway for live demo

---

## 🙋‍♀️ Author

**Saanvi Goyal**  
AI + Career Tech Enthusiast | Software Engineer
