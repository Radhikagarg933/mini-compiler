from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import json
import re

# Import the compiler components
from lexer import tokenize
from parser import parse
from executor import execute, variables

app = Flask(__name__)
CORS(app)

def classify_token(token):
    """Classify token into TYPE for detailed tokenization display"""
    token = str(token).strip()
    
    # Keywords (must match lexer.py)
    keywords = {'show', 'print', 'is', 'if', 'else', 'end', 'while', 'for', 'switch', 'case', 'input', 'do', 'break', 'continue', 'function', 'return', 'true', 'false', 'null', 'and', 'or', 'not', 'in'}
    if token.lower() in keywords:
        return ('KEYWORD', token)
    
    # Numbers
    if re.match(r'^-?\d+(\.\d+)?$', token):
        return ('NUMBER', token)
    
    # Strings (quoted)
    if (token.startswith('"') and token.endswith('"')) or (token.startswith("'") and token.endswith("'")):
        return ('STRING', token)
    
    # Operators (including emoji operators)
    operators = {'+', '-', '*', '/', '%', '==', '!=', '<', '>', '<=', '>=', '=', '+=', '-=', '*=', '/=', '++', '--', '&&', '||', '!', '&', '|', '^', '~', '<<', '>>', '➕', '➖', '✖️', '➗', '✨', '💯'}
    if token in operators:
        return ('OPERATOR', token)
    
    # Delimiters
    delimiters = {'(', ')', '[', ']', '{', '}', ',', ';', '.', ':', '?', '->'}
    if token in delimiters:
        return ('DELIMITER', token)
    
    # Identifiers (variables/functions)
    if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token):
        return ('IDENTIFIER', token)
    
    # Default
    return ('UNKNOWN', token)


def calculate_size(value):
    """Calculate the size of a value"""
    if isinstance(value, list):
        return len(value)  # Array length
    elif isinstance(value, str):
        return len(value)  # String length
    elif isinstance(value, dict):
        return len(value)  # Object/map property count
    else:
        return 1  # Scalar values have size 1


def get_variable_scope(var_name, all_variables):
    """Determine the scope of a variable"""
    # In a basic implementation, all variables are global unless we track function scopes
    # This can be enhanced if you implement function-level scoping in your executor
    
    # Check if variable is a function (optional - depends on your executor)
    if f"FUNCTION:{var_name}" in str(all_variables):
        return "function"
    
    # Default to global scope
    return "global"


@app.route('/run', methods=['POST'])
def run():
    try:
        data = request.get_json()
        code = data.get('code', '')
        
        if not code.strip():
            return jsonify({
                'success': False,
                'error': 'No code provided'
            })
        
        # ─────────────────────────────────────────────
        # PHASE 1: TOKENIZATION (Lexer)
        # ─────────────────────────────────────────────
        lines = code.split('\n')
        token_lines = []
        all_tokens_tracked = {}  # Track operators and keywords only (not identifiers)
        
        for line in lines:
            if line.strip():  # Skip empty lines for display
                tokens = tokenize(line)
                classified_tokens = []
                
                for token in tokens:
                    token_type, token_val = classify_token(token)
                    classified_tokens.append(f"<{token_type}, {token_val}>")
                    
                    # Track only operators, keywords, and numbers - NOT identifiers
                    if token_type in ('OPERATOR', 'KEYWORD', 'NUMBER', 'DELIMITER', 'STRING'):
                        key = f"{token_type}:{token_val}"
                        if key not in all_tokens_tracked:
                            all_tokens_tracked[key] = {
                                'type': token_type,
                                'value': token_val,
                                'occurrences': 1
                            }
                        else:
                            all_tokens_tracked[key]['occurrences'] += 1
                
                token_lines.append({
                    'raw': line.strip(),
                    'tokens': classified_tokens
                })
        
        # ─────────────────────────────────────────────
        # PHASE 2: PARSING (Parser)
        # ─────────────────────────────────────────────
        tokens_for_parser = [tokenize(line) for line in lines if line.strip()]
        instructions = parse(tokens_for_parser)
        
        # ─────────────────────────────────────────────
        # PHASE 3: EXECUTION (Executor)
        # ─────────────────────────────────────────────
        # Clear variables for fresh run
        variables.clear()
        
        output = execute(instructions)
        
        # ─────────────────────────────────────────────
        # PHASE 4: SYMBOL TABLE (Operators, Keywords, Variables with Scope & Size)
        # ─────────────────────────────────────────────
        symbol_table = {}
        
        # Add all tracked tokens (operators, keywords, numbers, etc.)
        for key, info in all_tokens_tracked.items():
            symbol_table[key] = {
                'type': info['type'],
                'value': info['value'],
                'occurrences': info['occurrences'],
                'scope': 'global',  # Tokens are always global
                'size': 1  # Tokens have size 1
            }
        
        # Add runtime variables with their values, scope, and size
        for var_name, var_value in variables.items():
            scope = get_variable_scope(var_name, variables)
            size = calculate_size(var_value)
            
            if isinstance(var_value, list):
                symbol_table[f"VARIABLE:{var_name}"] = {
                    'type': 'array',
                    'value': var_value,
                    'scope': scope,
                    'size': size
                }
            elif isinstance(var_value, str):
                symbol_table[f"VARIABLE:{var_name}"] = {
                    'type': 'string',
                    'value': var_value,
                    'scope': scope,
                    'size': size
                }
            elif isinstance(var_value, bool):
                symbol_table[f"VARIABLE:{var_name}"] = {
                    'type': 'boolean',
                    'value': str(var_value).lower(),
                    'scope': scope,
                    'size': 1
                }
            elif isinstance(var_value, (int, float)):
                symbol_table[f"VARIABLE:{var_name}"] = {
                    'type': 'number',
                    'value': var_value,
                    'scope': scope,
                    'size': 1
                }
            elif var_value is None:
                symbol_table[f"VARIABLE:{var_name}"] = {
                    'type': 'null',
                    'value': 'null',
                    'scope': scope,
                    'size': 1
                }
            else:
                symbol_table[f"VARIABLE:{var_name}"] = {
                    'type': 'object',
                    'value': str(var_value),
                    'scope': scope,
                    'size': calculate_size(var_value)
                }
        
        return jsonify({
            'success': True,
            'tokenization': token_lines,
            'instructions': instructions,
            'symbol_table': symbol_table,
            'output': output
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })


if __name__ == '__main__':
    app.run(debug=False, port=5000, host='127.0.0.1')
