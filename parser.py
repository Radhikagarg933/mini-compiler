# parser.py

def parse(lines):
    instructions = []
    i = 0

    while i < len(lines):
        tokens = lines[i]

        # Skip empty lines
        if not tokens:
            i += 1
            continue

        # Assignment
        if len(tokens) >= 3 and tokens[1] == "is":
            instructions.append(("assign", tokens[0], tokens[2:]))

        # Show / Print
        elif tokens[0] in ("show", "print"):
            instructions.append(("print", tokens[1:]))

        # Input
        elif tokens[0] == "input":
            instructions.append(("input", tokens[1]))

        # If-Else
        elif tokens[0] == "if":
            condition = tokens[1:]
            block = []
            else_block = []

            i += 1
            while i < len(lines) and (lines[i] and lines[i][0] not in ("else", "end")):
                block.append(lines[i])
                i += 1

            if i < len(lines) and lines[i] and lines[i][0] == "else":
                i += 1
                while i < len(lines) and (lines[i] and lines[i][0] != "end"):
                    else_block.append(lines[i])
                    i += 1

            instructions.append(("if", condition, parse(block), parse(else_block)))

        # While
        elif tokens[0] == "while":
            condition = tokens[1:]
            block = []

            i += 1
            while i < len(lines) and (lines[i] and lines[i][0] != "end"):
                block.append(lines[i])
                i += 1

            instructions.append(("while", condition, parse(block)))

        # Switch
        elif tokens[0] == "switch":
            var = tokens[1]
            cases = {}
            i += 1

            while i < len(lines) and (lines[i] and lines[i][0] != "end"):
                if lines[i][0] == "case":
                    val = lines[i][1]
                    i += 1
                    block = []
                    while i < len(lines) and (lines[i] and lines[i][0] not in ("case", "end")):
                        block.append(lines[i])
                        i += 1
                    cases[val] = parse(block)
                else:
                    i += 1

            instructions.append(("switch", var, cases))

        i += 1

    return instructions
