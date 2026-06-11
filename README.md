

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
---

## ▶️ How to Run the Project

### 1️⃣ Install Requirements

```bash
pip install flask
```

### 2️⃣ Run Backend Server

```bash
python server.py
```

### 3️⃣ Open Frontend

Open this file:

```
compiler.html
```

OR visit:

```
http://localhost:5000
```

---

## 💡 How It Works

```
User Input  →  lexer.py  →  parser.py  →  executor.py  →  Output
               (tokens)     (syntax)       (execution)
```

1. User enters code in the web interface
2. Frontend sends code to `server.py`
3. Server processes it through:
   - `lexer.py` → token generation
   - `parser.py` → syntax validation
   - `executor.py` → code execution
4. Output is returned back to the user in real time

---

## 🎥 Demo Video

👉 [Watch Demo Video](https://youtu.be/S63RfeQkLwY?si=Gv7At-g21xgsjUXW)

---
