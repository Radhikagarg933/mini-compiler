# executor.py

variables = {}

def evaluate(expr):
    expr_str = " ".join(expr).strip()

    # Array creation
    if expr_str.startswith("[") and expr_str.endswith("]"):
        inside = expr_str[1:-1].strip()
        if inside == "":
            return []
        elements = inside.split(",")
        return [int(e.strip()) for e in elements]

    # Array indexing
    if len(expr) == 1 and "[" in expr[0] and "]" in expr[0]:
        token = expr[0]
        arr_name = token.split("[")[0]
        idx_str = token.split("[")[1].replace("]", "")

        if arr_name not in variables:
            raise Exception(f"Undefined array: {arr_name}")

        if idx_str.isdigit():
            idx = int(idx_str)
        elif idx_str in variables:
            idx = variables[idx_str]
        else:
            raise Exception(f"Invalid index: {idx_str}")

        return variables[arr_name][idx]

    # Single value
    if len(expr) == 1:
        token = expr[0]
        if token.isdigit():
            return int(token)
        if token in variables:
            return variables[token]
        raise Exception(f"Undefined variable: {token}")

    # Binary operations
    if len(expr) == 3:
        left, op, right = expr
        left_val = evaluate([left])
        right_val = evaluate([right])

        if op == "➕": return left_val + right_val
        elif op == "➖": return left_val - right_val
        elif op == "✖": return left_val * right_val
        elif op == "➗": return left_val / right_val
        elif op == "🔺": return left_val > right_val
        elif op == "🔻": return left_val < right_val
        elif op == "🤝": return left_val == right_val
        else: raise Exception(f"Unknown operator: {op}")

    raise Exception(f"Invalid expression: {expr}")


def execute(instructions):
    for inst in instructions:
        if inst[0] == "assign":
            try:
                value = evaluate(inst[2])
                variables[inst[1]] = value
            except Exception as e:
                print(f"Error in assignment to {inst[1]} →", e)

        elif inst[0] == "print":
            try:
                print(evaluate(inst[1]))
            except Exception as e:
                print("Print error →", e)

        elif inst[0] == "input":
            try:
                variables[inst[1]] = int(input(f"{inst[1]}: "))
            except:
                print("Invalid input")

        elif inst[0] == "if":
            try:
                condition = evaluate(inst[1])
                if condition:
                    execute(inst[2])
                else:
                    execute(inst[3])
            except Exception as e:
                print("Error in if →", e)

        elif inst[0] == "while":
            try:
                while evaluate(inst[1]):
                    execute(inst[2])
            except Exception as e:
                print("Error in while →", e)

        elif inst[0] == "switch":
            try:
                var_value = variables.get(inst[1], None)
                for case_val, block in inst[2].items():
                    if str(var_value) == str(case_val):
                        execute(block)
                        break
            except Exception as e:
                print("Error in switch →", e)
