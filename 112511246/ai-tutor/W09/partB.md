# Week 9 — AI Tutor Learning Record (Part B)

- 學號：112511246
- Name：張中愷
- Date：2026-11-10
- Topic：MIT 6.0002 Lecture 1 — Introduction and Optimization Problems
- 程式檔：[w9.py](w9.py)
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## 1. Today's Challenge

**Core concept from today's OCW lecture:**

最佳化問題有一個要最大化或最小化的目標，以及必須遵守的限制。課堂的 `greedy` 函式先依照某個標準（key function）把物品由好到壞排序，再依序挑選，放不下就跳過；它很快（O(n log n)），但只做局部最佳的選擇，不保證得到全域最佳解。暴力法列舉所有組合，一定找得到最佳解，但是指數時間。

**AI-generated coding challenge title:** Greedy Coin Change（貪婪找零）

### 題目

用給定的硬幣面額湊出指定金額，目標是**用的硬幣數量最少**，每種面額可以用無限多個。

| 函式 | 要做什麼 |
|---|---|
| `greedy_coins(coins, amount)` | 貪婪法：每次都拿「不超過剩餘金額的最大面額」。湊不出剛好的金額時回傳 `None` |
| `best_coins_brute(coins, amount)` | 暴力法：試遍所有拿法，回傳硬幣數最少的組合；湊不出來回傳 `None` |

接著比較兩者，找出貪婪法**不是最少硬幣**的例子。

- 限制：面額為正整數，`amount` 為 0 以上的整數；暴力法只用在小金額。

| 呼叫 | 結果 |
|---|---|
| `greedy_coins([1, 5, 10, 50], 68)` | `[50, 10, 5, 1, 1, 1]` |
| `greedy_coins([1, 3, 4], 6)` | `[4, 1, 1]`（3 枚） |
| `best_coins_brute([1, 3, 4], 6)` | `[3, 3]`（2 枚，比貪婪少） |
| `greedy_coins([5, 10], 3)` | `None`（湊不出來） |
| `greedy_coins([1, 5, 10], 0)` | `[]` |

## 2. My Initial Approach — Before AI Help

貪婪法對應課堂的 `greedy`：把面額由大到小排序（相當於 key 是面額本身、`reverse=True`），從最大的面額開始，只要剩下的金額還夠就一直拿，不夠了才換下一個面額；最後剩下的金額不是 0，就代表湊不出來。暴力法則是遞迴：對每一種面額，先拿一枚，剩下的金額交給自己繼續湊，在所有可行的拿法中選硬幣數最少的。

## 3. AI Tutor Help

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**

AI 建議不要只看題目給的例子，而是寫一個暴力法當作「標準答案」，對金額 0～24 逐一比較貪婪法和暴力法的硬幣數，自動找出貪婪法失敗的情況。

**It helped me realize that:**

貪婪法在台幣的面額（1、5、10、50）上一個錯都沒有，但換成 [1, 3, 4]、[1, 7, 10]、[1, 5, 12] 這些面額就會出錯。貪婪法對不對，取決於面額本身的結構，不是寫法的問題。

## 4. My Revision

- [ ] No
- [x] Yes

**What did you change, and why?**

第一版只寫了 `greedy_coins`，題目的例子都能跑出結果，但沒辦法判斷它是不是「最少」。第二版加上 `best_coins_brute` 作為對照，才發現 `greedy_coins([1, 3, 4], 6)` 用了 3 枚，而最少只要 2 枚（3 + 3）。

測試暴力法時也遇到一個問題：用 `best_coins_brute([1, 5, 10, 50], 68)` 時程式跑了超過兩分鐘都沒結束，只好中止，把暴力法的例子改成小金額（`[1, 5, 10]` 湊 18）。這直接體驗到暴力法是指數時間。

### 最終程式

```python
def greedy_coins(coins, amount):
    used = []
    for c in sorted(coins, reverse=True):
        while amount >= c:
            used.append(c)
            amount -= c
    if amount != 0:
        return None
    return used


def best_coins_brute(coins, amount):
    if amount == 0:
        return []
    best = None
    for c in coins:
        if c <= amount:
            rest = best_coins_brute(coins, amount - c)
            if rest is not None and (best is None or len(rest) + 1 < len(best)):
                best = [c] + rest
    return best
```

## 5. Verification

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

**貪婪法 vs 暴力法（金額 0～24 逐一比較）：**

| 面額 | 貪婪法不是最少的金額數 | 例子：貪婪 → 最少 |
|---|---|---|
| [1, 5, 10, 50] | 0 個 | 全部都是最少 |
| [1, 3, 4] | 5 個 | 6：`[4, 1, 1]` → `[3, 3]`；10：`[4, 4, 1, 1]` → `[4, 3, 3]` |
| [1, 7, 10] | 4 個 | 14：`[10, 1, 1, 1, 1]` → `[7, 7]` |
| [1, 5, 12] | 4 個 | 15：`[12, 1, 1, 1]` → `[5, 5, 5]` |

其他邊界情況：

| 測試 | 輸入 | 預期輸出 | 實際輸出 |
|---|---|---|---|
| 金額 0 | `greedy_coins([1, 5, 10], 0)` | `[]` | `[]` |
| 湊不出來 | `greedy_coins([5, 10], 3)` | `None` | `None` |
| 暴力法也湊不出來 | `best_coins_brute([5, 10], 3)` | `None` | `None` |
| 大金額 | `greedy_coins([1, 5, 10, 50], 1000000)` | 正常結束 | 0.001 秒 |

**One edge case I tested:**

- Input：`greedy_coins([1, 7, 10], 14)`
- Expected output（最少硬幣）：`[7, 7]`，2 枚
- Actual output：`[10, 1, 1, 1, 1]`，5 枚

貪婪法先拿最大的 10，剩下 4 只能用 4 個 1；但不拿 10、改拿兩個 7 只要 2 枚。這是貪婪法「選了就不回頭」造成的錯誤。

### Why my solution works

`greedy_coins` 依照面額由大到小，能拿就拿，所以它確實實作了「每一步選當下最大」的貪婪策略；最後剩餘金額不為 0 就回傳 `None`。`best_coins_brute` 對每一種「第一枚拿哪個面額」都遞迴求出剩下金額的最佳解，再取硬幣最少的，因為所有可能都試過，所以結果一定是最少的。兩者比較的結果說明：貪婪法很快，但不一定最佳。

### Time complexity

- `greedy_coins`：排序 k 種面額是 O(k log k)，之後每拿一枚硬幣做一次減法，若拿了 c 枚就是 O(c)，整體 O(k log k + c)。金額 100 萬時只要 0.001 秒。
- `best_coins_brute`：每一層都要對每種面額往下遞迴，呼叫次數隨金額呈指數成長，是指數時間。`[1, 5, 10, 50]` 湊 68 時已經超過兩分鐘跑不完。

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

課堂的貪婪演算法：依照某個標準排序後，從最好的開始挑，挑了就不回頭。這題的標準是「面額越大越好」。課堂用食物例子說明貪婪不保證最佳，這題用找零錢找出了具體的反例。

**One thing I understand better now:**

要判斷一個演算法是不是「最佳」，只看幾個例子跑得出結果是不夠的，要有一個保證正確的方法（例如暴力法）來對照。另外，同一個貪婪策略在某些面額下完全正確、在另一些面額下會出錯。

**One thing I am still unsure about:**

為什麼台幣面額（1、5、10、50）用貪婪法一定是最少硬幣，而 [1, 3, 4] 不行？什麼樣的面額組合才能保證貪婪法正確，我還不知道。
