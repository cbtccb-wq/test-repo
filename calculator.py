import math

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("0で割ることはできません")
    return a / b
def power(a, b): return a ** b
def mod(a, b):
    if b == 0:
        raise ValueError("0で割ることはできません")
    return a % b

OPERATIONS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power,
    '%': mod,
}

# 関数電卓: 引数1つ
UNARY_FUNCTIONS = {
    'sin':   math.sin,
    'cos':   math.cos,
    'tan':   math.tan,
    'asin':  math.asin,
    'acos':  math.acos,
    'atan':  math.atan,
    'sqrt':  math.sqrt,
    'log':   math.log10,
    'ln':    math.log,
    'abs':   abs,
    'ceil':  math.ceil,
    'floor': math.floor,
    'deg':   math.degrees,
    'rad':   math.radians,
}

CONSTANTS = {
    'pi': math.pi,
    'e':  math.e,
}

HELP = """
  四則演算:  3 + 5 / 2 * 4 - 1  (通常の式として計算)
  べき乗:    2 ** 8
  剰余:      10 % 3
  関数:      sin(90)  sqrt(2)  log(100)  ln(2.718)
             ※三角関数の引数は「度」
  定数:      pi, e
  終了:      q
"""

def evaluate(expr):
    """式を評価する (単純な二項演算 or 関数呼び出し or 定数)"""
    expr = expr.strip()

    # 定数
    if expr in CONSTANTS:
        return CONSTANTS[expr]

    # 関数呼び出し: func(arg)
    for name, func in UNARY_FUNCTIONS.items():
        if expr.startswith(name + '(') and expr.endswith(')'):
            inner = expr[len(name)+1:-1]
            val = evaluate(inner)
            if name in ('sin', 'cos', 'tan'):
                val = math.radians(val)  # 度→ラジアン変換
            return func(val)

    # 二項演算子 (優先度低い順に右から探して再帰)
    for op in ('+', '-', '*', '/', '**', '%'):
        # 右から検索して左辺・右辺に分割
        idx = expr.rfind(op)
        if idx > 0:
            left = expr[:idx].strip()
            right = expr[idx+len(op):].strip()
            if left and right:
                try:
                    a = evaluate(left)
                    b = evaluate(right)
                    return OPERATIONS[op](a, b)
                except Exception:
                    pass

    # 数値リテラル
    return float(expr)

def main():
    print("関数電卓 (ヘルプ: h, 終了: q)")
    while True:
        expr = input("\n> ").strip()
        if not expr:
            continue
        if expr.lower() == 'q':
            break
        if expr.lower() == 'h':
            print(HELP)
            continue
        try:
            result = evaluate(expr)
            print(f"= {result:g}")
        except Exception as e:
            print(f"エラー: {e}")

if __name__ == "__main__":
    main()
