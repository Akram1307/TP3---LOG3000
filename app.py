"""Flask server for the web calculator.

Serves the calculator page and evaluates the expression the user submits.
An expression is two numbers separated by one operator (+, -, *, /),
for example "12*3".
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Maps each operator symbol typed in the UI to the function that computes it.
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """Evaluate a single-operator arithmetic expression.

    Args:
        expr (str): Expression of the form "<number><operator><number>",
            for example "3+4". Spaces are ignored.

    Returns:
        float: The result of applying the operator to the two numbers.

    Raises:
        ValueError: If the expression is empty, has more than one operator,
            has no operator, starts or ends with an operator, or if an
            operand is not a number.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Only one operator is supported, so a second one makes the input invalid.
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Render the calculator page and evaluate submitted expressions.

    On GET, shows the calculator with an empty display. On POST, reads the
    expression from the "display" form field, evaluates it and shows the
    result in the display.

    Returns:
        str: The rendered index.html page.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # Show the error in the display instead of crashing the page.
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Debug mode reloads the server on code changes; for development only.
    app.run(debug=True)