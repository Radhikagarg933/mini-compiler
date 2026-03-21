from parser import parse
from executor import execute

def run(filename):
    with open(filename, encoding="utf-8") as f:
        code = f.read()

    lines = [line.strip().split() for line in code.strip().split("\n")]
    instructions = parse(lines)
    execute(instructions)

run("program.emj")
