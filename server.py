# server.py
# ──────────────────────────────────────────
# Run once:   pip install flask flask-cors
# Every time: python server.py
# Then open:  compiler.html in your browser
# ──────────────────────────────────────────

import sys
import io
from flask import Flask, request, jsonify
from flask_cors import CORS
from parser import parse

# Import executor but patch print() so we can capture output
import executor

app = Flask(__name__)
CORS(app)


@app.route("/run", methods=["POST"])
def run_code():
    data = request.get_json()
    code = data.get("code", "").strip()

    if not code:
        return jsonify({"success": False, "error": "No code provided."})

    try:
        # Clear variables between every run
        executor.variables.clear()

        # Tokenize lines exactly like main.py does
        lines = [line.strip().split() for line in code.split("\n")]

        # Parse
        instructions = parse(lines)

        # Capture stdout (works with original executor that uses print())
        captured = io.StringIO()
        sys.stdout = captured

        try:
            executor.execute(instructions)
        finally:
            sys.stdout = sys.__stdout__   # always restore stdout

        output = captured.getvalue().strip()

        return jsonify({"success": True, "output": output})

    except Exception as e:
        sys.stdout = sys.__stdout__       # restore on error too
        return jsonify({"success": False, "error": str(e)})


if __name__ == "__main__":
    print("✅  MiniComp server running at http://localhost:5000")
    app.run(port=5000, debug=True)
