# test-repo

学習・テスト用のリポジトリです。

## 機能一覧

### 1. 関数電卓 (`calculator.py`)

インタラクティブな関数電卓です。

**対応機能:**
- 四則演算 (`+`, `-`, `*`, `/`)
- べき乗 (`**`)、剰余 (`%`)
- 三角関数 (`sin`, `cos`, `tan`, `asin`, `acos`, `atan`) ※引数は「度」
- 平方根 (`sqrt`)、対数 (`log`, `ln`)
- その他 (`abs`, `ceil`, `floor`, `deg`, `rad`)
- 定数 (`pi`, `e`)

**実行方法:**
```
python calculator.py
```

**使用例:**
```
> 3 + 5 * 2
= 13
> sin(90)
= 1
> sqrt(2)
= 1.41421
```

---

### 2. ニュートン法ソルバー (`newton.py`)

ニュートン法 (Newton-Raphson法) で方程式 `f(x) = 0` の数値解を求めます。

**収録例題:**
| 例題 | 方程式 | 解 |
|---|---|---|
| sqrt(2) | x² - 2 = 0 | ≈ 1.4142135624 |
| cbrt(5) | x³ - 5 = 0 | ≈ 1.7099759467 |
| cos(x) = x | cos(x) - x = 0 | ≈ 0.7390851332 |
| e^x = 3 | e^x - 3 = 0 | ≈ 1.0986122887 |

**実行方法:**
```
python -X utf8 newton.py
```

**`newton()` 関数の使い方:**
```python
from newton import newton

f  = lambda x: x**2 - 2       # 解きたい関数
df = lambda x: 2*x             # その導関数
sol, iters = newton(f, df, x0=1.0)
print(sol)  # 1.4142135623730951
```
