# executor.py

variables = {}


def evaluate(expr):
    """
    expr: list of raw tokens like ["a", "➕", "b"] or ["10"] or ["arr", "[", "0", "]"]
    """
    expr_list = list(expr)  # Make a copy
    expr_str = " ".join(expr_list).strip()

    # Array creation  [1, 2, 3]
    if expr_str.startswith("[") and expr_str.endswith("]"):
        inside = expr_str[1:-1].strip()
        if inside == "":
            return []
        elements = [e.strip() for e in inside.split(",")]
        result = []
        for e in elements:
            if e.lstrip("-").isdigit():
                result.append(int(e))
            else:
                result.append(e)
        return result

    # Array indexing  arr[0]  or  arr[i]
    if len(expr_list) >= 3 and "[" in expr_list:
        idx_bracket = expr_list.index("[")
        arr_name = expr_list[idx_bracket - 1]
        idx_str = expr_list[idx_bracket + 1]
        
        if arr_name not in variables:
            raise Exception(f"Undefined array: {arr_name}")
        
        idx = int(idx_str) if idx_str.lstrip("-").isdigit() else variables.get(idx_str)
        if idx is None:
            raise Exception(f"Invalid index: {idx_str}")
        
        return variables[arr_name][idx]

    # Single value
    if len(expr_list) == 1:
        token = expr_list[0]
        if token.lstrip("-").isdigit():
            return int(token)
        try:
            return float(token)
        except ValueError:
            pass
        if token in variables:
            return variables[token]
        raise Exception(f"Undefined variable: {token}")

    # Binary operations  left op right
    if len(expr_list) == 3:
        left, op, right = expr_list
        lv = evaluate([left])
        rv = evaluate([right])
        
        if op == "is":
            return rv  # Assignment operator returns right value
        elif op in ("➕", "+"):
            return lv + rv
        elif op in ("➖", "-"):
            return lv - rv
        elif op in ("✖️", "✖", "*"):
            return lv * rv
        elif op in ("➗", "/"):
            if rv == 0:
                raise Exception("Division by zero")
            return lv / rv
        elif op in ("🔺", ">"):
            return lv > rv
        elif op in ("🔻", "<"):
            return lv < rv
        elif op in ("🤝", "=="):
            return lv == rv
        else:
            raise Exception(f"Unknown operator: {op}")

    raise Exception(f"Cannot evaluate: {expr_list}")


def execute(instructions, out=None):
    """
    Execute compiled instructions.
    out: a list that collects every printed line.
         Always pass the SAME list so recursive calls
         (if / while / switch) all write to the same place.
    """
    if out is None:
        out = []

    for inst in instructions:
        kind = inst[0]

        # ── assign ──────────────────────────────────
        if kind == "assign":
            try:
                var_name = inst[1]
                expr = inst[2]
                variables[var_name] = evaluate(expr)
            except Exception as e:
                out.append(f"[Error] assign '{inst[1]}': {e}")

        # ── print / show ─────────────────────────────
        elif kind == "print":
            try:
                expr = inst[1]
                val = evaluate(expr)
                out.append(str(val))
            except Exception as e:
                out.append(f"[Error] show: {e}")

        # ── input ────────────────────────────────────
        elif kind == "input":
            var_name = inst[1]
            variables[var_name] = 0
            out.append(f"[input] '{var_name}' set to 0 (browser mode)")

        # ── if / else ────────────────────────────────
        elif kind == "if":
            try:
                condition = inst[1]
                then_block = inst[2]
                else_block = inst[3]
                
                if evaluate(condition):
                    execute(then_block, out)   # ← same out list
                else:
                    execute(else_block, out)   # ← same out list
            except Exception as e:
                out.append(f"[Error] if: {e}")

        # ── while ────────────────────────────────────
        elif kind == "while":
            try:
                condition = inst[1]
                block = inst[2]
                guard = 0
                
                while evaluate(condition):
                    guard += 1
                    if guard > 10000:
                        raise Exception("Infinite loop (>10000 iterations)")
                    execute(block, out)   # ← same out list
            except Exception as e:
                out.append(f"[Error] while: {e}")

        # ── switch ───────────────────────────────────
        elif kind == "switch":
            try:
                var_name = inst[1]
                cases = inst[2]
                val = str(variables.get(var_name, var_name))
                
                for case_val, block in cases.items():
                    if val == str(case_val):
                        execute(block, out)  # ← same out list
                        break
            except Exception as e:
                out.append(f"[Error] switch: {e}")

    return out   # always return the list
