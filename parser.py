# parser.py

def parse(token_lines):
    """
    token_lines: list of lists. Each inner list is raw tokens from a line.
    """
    instructions = []
    i = 0

    while i < len(token_lines):
        tokens = token_lines[i]

        # Skip empty lines
        if not tokens:
            i += 1
            continue

        # Assignment: a is 10  or  c is a ➕ b
        if len(tokens) >= 3 and tokens[1] == "is":
            var_name = tokens[0]
            expr = tokens[2:]
            instructions.append(("assign", var_name, expr))

        # Show / Print: show x  or  print x
        elif len(tokens) >= 1 and tokens[0] in ("show", "print"):
            expr = tokens[1:]
            instructions.append(("print", expr))

        # Input: input x
        elif len(tokens) >= 1 and tokens[0] == "input":
            var_name = tokens[1] if len(tokens) > 1 else None
            instructions.append(("input", var_name))

        # If-Else
        elif len(tokens) >= 1 and tokens[0] == "if":
            condition = tokens[1:]
            block = []
            else_block = []

            i += 1
            while i < len(token_lines) and token_lines[i]:
                if token_lines[i][0] in ("else", "end"):
                    break
                block.append(token_lines[i])
                i += 1

            if i < len(token_lines) and token_lines[i] and token_lines[i][0] == "else":
                i += 1
                while i < len(token_lines) and token_lines[i]:
                    if token_lines[i][0] == "end":
                        break
                    else_block.append(token_lines[i])
                    i += 1

            instructions.append(("if", condition, parse(block), parse(else_block)))

        # While
        elif len(tokens) >= 1 and tokens[0] == "while":
            condition = tokens[1:]
            block = []

            i += 1
            while i < len(token_lines) and token_lines[i]:
                if token_lines[i][0] == "end":
                    break
                block.append(token_lines[i])
                i += 1

            instructions.append(("while", condition, parse(block)))

        # Switch
        elif len(tokens) >= 1 and tokens[0] == "switch":
            var = tokens[1] if len(tokens) > 1 else None
            cases = {}
            i += 1

            while i < len(token_lines) and token_lines[i]:
                if token_lines[i][0] == "end":
                    break
                if token_lines[i][0] == "case":
                    case_val = token_lines[i][1] if len(token_lines[i]) > 1 else None
                    i += 1
                    block = []
                    while i < len(token_lines) and token_lines[i]:
                        if token_lines[i][0] in ("case", "end"):
                            break
                        block.append(token_lines[i])
                        i += 1
                    cases[case_val] = parse(block)
                else:
                    i += 1

            instructions.append(("switch", var, cases))

        i += 1

    return instructions
