"""
ニュートン法 (Newton-Raphson法) による方程式の数値解を求めるプログラム

使い方:
  python newton.py
"""

def newton(f, df, x0, tol=1e-10, max_iter=100):
    """
    ニュートン法で f(x) = 0 の解を求める

    Args:
        f      : 対象の関数
        df     : f の導関数
        x0     : 初期値
        tol    : 収束判定の許容誤差
        max_iter: 最大反復回数

    Returns:
        (解, 反復回数)
    """
    x = x0
    for i in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ValueError(f"導関数が 0 になりました (x={x})")
        x_new = x - fx / dfx
        print(f"  反復 {i:3d}: x = {x_new:.10f}, f(x) = {f(x_new):.6e}")
        if abs(x_new - x) < tol:
            return x_new, i
        x = x_new
    raise RuntimeError(f"{max_iter} 回以内に収束しませんでした")


# ---- 例題 ----------------------------------------------------------------

EXAMPLES = [
    {
        "title"  : "sqrt(2) を求める (x^2 - 2 = 0)",
        "f"      : lambda x: x**2 - 2,
        "df"     : lambda x: 2*x,
        "x0"     : 1.0,
        "answer" : "≈ 1.4142135623730951",
    },
    {
        "title"  : "cbrt(5) を求める (x^3 - 5 = 0)",
        "f"      : lambda x: x**3 - 5,
        "df"     : lambda x: 3*x**2,
        "x0"     : 2.0,
        "answer" : "≈ 1.7099759466766968",
    },
    {
        "title"  : "cos(x) = x の解 (cos(x) - x = 0)",
        "f"      : lambda x: __import__('math').cos(x) - x,
        "df"     : lambda x: -__import__('math').sin(x) - 1,
        "x0"     : 1.0,
        "answer" : "≈ 0.7390851332151607 (不動点)",
    },
    {
        "title"  : "e^x = 3 の解 (e^x - 3 = 0)",
        "f"      : lambda x: __import__('math').exp(x) - 3,
        "df"     : lambda x: __import__('math').exp(x),
        "x0"     : 1.0,
        "answer" : "≈ 1.0986122886681098 (= ln 3)",
    },
]


def run_example(ex):
    print(f"\n{'='*55}")
    print(f"【例題】 {ex['title']}")
    print(f"  初期値 x0 = {ex['x0']}")
    print(f"  期待値   : {ex['answer']}")
    print()
    try:
        sol, iters = newton(ex["f"], ex["df"], ex["x0"])
        print(f"\n  → 解: {sol:.10f}  ({iters} 回で収束)")
    except Exception as e:
        print(f"\n  → エラー: {e}")


def main():
    print("ニュートン法による方程式の数値解法")
    for ex in EXAMPLES:
        run_example(ex)
    print(f"\n{'='*55}")


if __name__ == "__main__":
    main()
