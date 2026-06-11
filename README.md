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


##▶️ How to Run the Project
Step 1: Install Requirements
pip install flask
Step 2: Run Backend Server
python server.py
Step 3: Open Frontend

Open the file:
compiler.html
OR if the server is running, visit:http://localhost:5000
---
##💡 How It Works
1.User enters code in the web interface
2.Frontend sends code to server.py
3.Server processes it through:
4.lexer.py → token generation
5.parser.py → syntax validation
6.executor.py → code execution
7.Output is returned back to the user in the correct format
---
## 🎥 Demo Video

👉 [Watch Demo Video](https://youtu.be/S63RfeQkLwY)
---
