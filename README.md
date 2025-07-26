# 🤖 Django Chatbot

A customizable AI-powered chatbot built using Django and OpenAI's GPT API. This web-based chatbot features user authentication, real-time interaction, and chat history tracking — making it an ideal foundation for AI assistants, customer service bots, educational helpers, or personal productivity tools.

---

## 🚀 Features

- 🔐 User Authentication (Login/Signup)
- 💬 Chat interface with OpenAI GPT integration
- 🕓 Persistent conversation history (per user)
- 🎨 Clean, responsive frontend UI using Django templates
- ⚙️ Easily extendable for new features and APIs

---

## 📸 Screenshots

<img src="https://github.com/tomitokko/django-chatbot/blob/main/screenshots/login.png" width="400" />
<img src="https://github.com/tomitokko/django-chatbot/blob/main/screenshots/chat.png" width="400" />

---

## 🛠️ Tech Stack

- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JavaScript (with Django templating)
- **Database:** SQLite (default, can be changed)
- **AI Engine:** OpenAI API (GPT)

---

## 🧩 Installation

### 🔗 Prerequisites

- Python 3.8+
- pip
- Git
- OpenAI API Key (create one at [platform.openai.com](https://platform.openai.com))

### 📦 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/tomitokko/django-chatbot.git
cd django-chatbot

# Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variable for OpenAI key
# On Linux/macOS:
export OPENAI_API_KEY=your_openai_key_here

# On Windows (CMD):
set OPENAI_API_KEY=your_openai_key_here

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
