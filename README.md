# 🧠 MiniComp-Custom Compiler 

This Project is  built using Python and HTML that simulates basic compiler phases like lexical analysis, syntax parsing, and code execution. It provides a simple web interface where users can input code and see processed output in real time. The project helps in understanding compiler design and backend-frontend integration
---

## 🚀 Features

- 🔤 Lexical Analysis (Token generation)
- 🧾 Syntax Parsing
- ⚙️ Code Execution Engine
- 🌐 Web-based Interface
- 🔗 Backend-Frontend Integration using Python server
- 📂 Modular compiler design

---

## 🛠️ Tech Stack

- Python 3
- HTML5
- CSS (optional)
- JavaScript (optional)
- Flask / Python HTTP Server

---
## 🎥 Demo Video

👉 [Watch Demo Video](https://youtu.be/S63RfeQkLwY)

## 📂 Project Structure

```bash
mini-compiler/
│
├── compiler.html        # Frontend UI for input/output
├── server.py            # Backend server (connects frontend with compiler)
│
├── lexer.py             # Converts code into tokens (Lexical Analysis)
├── parser.py            # Performs syntax analysis
├── executor.py          # Executes parsed code
│
├── sample_codes.emi     # Sample test programs
│
├── README.md            # Project documentation
│
├── __pycache__/         # Python cache files (auto-generated)
└── .git/                # Git version control folder

```
---
---

## ▶️ How to Run the Project

### Step 1: Install Requirements

```bash
pip install flask
Step 2: Run Backend Server
python server.py
Step 3: Open Frontend

Open:

compiler.html

OR if server is running:

http://localhost:5000
💡 How It Works
User enters code in the web interface
Frontend sends code to server.py
Server passes code to:
lexer.py → token generation
parser.py → syntax validation
executor.py → execution
Output is returned back to UI
