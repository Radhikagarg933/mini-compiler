

# 🧠 MiniComp-Custom Compiler

This project is built using **Python and HTML** that simulates basic compiler phases like lexical analysis, syntax parsing, and code execution. It provides a simple web interface where users can input code and see processed output in real time. The project helps in understanding compiler design and backend–frontend integration.

---

## 🚀 Features

- 🔤 Lexical Analysis (Token generation)
- 🧾 Syntax Parsing
- ⚙️ Code Execution Engine
- 🌐 Web-based Interface
- 🔗 Backend–Frontend Integration using Python server
- 📂 Modular compiler design

---

## 🛠️ Tech Stack

- Python 3
- HTML5
- CSS (optional)
- JavaScript (optional)
- Flask / Python HTTP Server

---

## 📂 Project Structure

```bash
mini-compiler/
│
├── compiler.html        # Frontend UI for input/output
├── server.py            # Backend server (connects frontend with compiler)
│
├── lexer.py             # Lexical analysis (token generation)
├── parser.py            # Syntax analysis
├── executor.py          # Code execution engine
│
├── sample_codes.emi     # Sample test programs
│
├── README.md            # Documentation file
└── __pycache__/         # Python cache files

```
## ▶️ How to Run the Project

### 1️⃣ Install Requirements

pip install flask
2️⃣ Run Backend Server
python server.py
3️⃣ Open Frontend

Open this file:

compiler.html

OR visit:

http://localhost:5000
💡 How It Works
User enters code in the web interface
Frontend sends code to server.py
Server processes it through:
lexer.py → token generation
parser.py → syntax validation
executor.py → code execution
Output is returned back to the user in real time
🎥 Demo Video

👉 Watch Demo Video
