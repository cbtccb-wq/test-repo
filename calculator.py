def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("0で割ることはできません")
    return a / b

OPERATIONS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def main():
    print("シンプルな電卓 (終了するには 'q' を入力)")
    while True:
        expr = input("\n計算式を入力 (例: 3 + 5): ").strip()
        if expr.lower() == 'q':
            break
        parts = expr.split()
        if len(parts) != 3:
            print("形式エラー: '数値 演算子 数値' の形式で入力してください")
            continue
        a_str, op, b_str = parts
        if op not in OPERATIONS:
            print(f"未対応の演算子: {op}  (使用可能: +, -, *, /)")
            continue
        try:
            a, b = float(a_str), float(b_str)
            result = OPERATIONS[op](a, b)
            print(f"= {result:g}")
        except ValueError as e:
            print(f"エラー: {e}")

if __name__ == "__main__":
    main()
