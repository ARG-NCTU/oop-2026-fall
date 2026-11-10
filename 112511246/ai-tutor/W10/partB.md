# Week 10 — AI Tutor Learning Record (Part B)

- 學號：112511246
- Name：張中愷
- Date：2026-11-10
- Topic：MIT 6.0002 Lecture 2 — Optimization Problems（決策樹、動態規劃、記憶化）
- 程式檔：[w10.py](w10.py)
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## 1. Today's Challenge

**Core concept from today's OCW lecture:**

用決策樹（遞迴）窮舉所有選擇一定能找到最佳解，但子問題會被重複計算，是指數時間。如果問題具有最佳子結構和重疊子問題，就可以用記憶化（memoization）把算過的子問題答案存在字典裡，之後直接查表，這就是動態規劃。課堂的 `fastFib` 和 `fastMaxVal` 都是這樣把指數時間降下來的。

**AI-generated coding challenge title:** Minimum Coin Change（最少硬幣找零）

### 題目

延續 W9：貪婪法在 [1, 3, 4] 這類面額下不一定找到最少硬幣，暴力法又太慢。用給定的面額湊出指定金額，回傳**最少需要幾枚硬幣**；湊不出來回傳 `-1`。

| 函式 | 要做什麼 |
|---|---|
| `min_coins_naive(coins, amount)` | 單純遞迴：試每一種「第一枚拿哪個面額」，取最少的 |
| `min_coins(coins, amount)` | 同樣的遞迴，加上字典記憶化 |

- 限制：面額為正整數，`amount` 為 0～500 的整數。

| 呼叫 | 結果 | 說明 |
|---|---|---|
| `min_coins([1, 3, 4], 6)` | `2` | 3 + 3，貪婪法會給 3 枚 |
| `min_coins([1, 5, 10, 50], 68)` | `6` | 50 + 10 + 5 + 1 + 1 + 1 |
| `min_coins([5, 10], 3)` | `-1` | 湊不出來 |
| `min_coins([2], 0)` | `0` | 不用任何硬幣 |
| `min_coins([1, 7, 10], 14)` | `2` | 7 + 7，貪婪法會給 5 枚 |

## 2. My Initial Approach — Before AI Help

湊出金額 `amount` 的最少硬幣數，等於「先拿一枚面額 c，再湊出 `amount - c` 的最少硬幣數，加 1」，對每一種面額 c 都試一次取最小值。金額 0 需要 0 枚（base case）；所有面額都比剩下的金額大，代表湊不出來，回傳 `-1`。這就是課堂決策樹的想法：每一層決定「這一枚拿哪個面額」。

## 3. AI Tutor Help

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**

AI 提醒：湊 6 元時，「先拿 1 再湊 5」和「先拿 1、再拿 1、再湊 4」等不同路徑，都會走到「湊 4 元」這個子問題，而它的答案每次都一樣。課堂的 `fastMaxVal` 正是用字典記住這種重複出現的子問題。並問：這題的記憶化 key 應該是什麼？

**It helped me realize that:**

這題的子問題只由「剩下的金額」決定（面額清單從頭到尾不變），所以字典的 key 用剩下的金額就夠了。這跟背包問題不同：背包的子問題還要看剩下哪些物品，所以課堂用 `(len(toConsider), avail)` 當 key。

## 4. My Revision

- [ ] No
- [x] Yes

**What did you change, and why?**

第一版 `min_coins_naive` 是單純的遞迴，答案正確，但呼叫次數爆炸：湊 30 元要呼叫 255 萬次、花 0.74 秒，而且金額每增加 10，呼叫次數就變成原本的一百多倍。

第二版 `min_coins` 加上字典 `memo`：進入函式先檢查 `amount` 是否已經算過，算過就直接回傳；沒算過才遞迴計算，算完存進 `memo`。邏輯跟第一版完全一樣，只多了「查表」和「存表」兩個步驟。`memo=None` 再在函式裡建立新字典，是為了避免 Python 預設參數只建立一次、不同呼叫共用同一個字典的問題。

### 最終程式

```python
def min_coins_naive(coins, amount):
    if amount == 0:
        return 0
    best = -1
    for c in coins:
        if c <= amount:
            sub = min_coins_naive(coins, amount - c)
            if sub != -1 and (best == -1 or sub + 1 < best):
                best = sub + 1
    return best


def min_coins(coins, amount, memo=None):
    if memo is None:
        memo = {}
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    best = -1
    for c in coins:
        if c <= amount:
            sub = min_coins(coins, amount - c, memo)
            if sub != -1 and (best == -1 or sub + 1 < best):
                best = sub + 1
    memo[amount] = best
    return best
```

## 5. Verification

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

**正確性：** 用 W9 的暴力法 `best_coins_brute` 當標準答案，對 5 組面額（[1, 3, 4]、[1, 7, 10]、[2, 5]、[3, 7]、[1, 5, 12]）的金額 0～19 共 100 個情況比對，`min_coins` 和 `min_coins_naive` 全部一致。

**呼叫次數與時間（面額 [1, 3, 4]）：**

| 金額 | `min_coins_naive` 呼叫次數 | 時間 | `min_coins` 呼叫次數 | 時間 |
|---|---|---|---|---|
| 10 | 168 | 0.0000 秒 | 26 | 0.00001 秒 |
| 20 | 20,736 | 0.0059 秒 | 56 | 0.00002 秒 |
| 30 | 2,550,408 | 0.7374 秒 | 86 | 0.00005 秒 |
| 500 | （跑不完） | | — | 0.0004 秒（答案 125 枚） |

記憶化版本的呼叫次數大約是「金額 × 面額數」，金額增加 10，呼叫次數只多 30。

**One edge case I tested:**

- Input：`min_coins([5, 10], 3)`
- Expected output：`-1`
- Actual output：`-1`

所有面額都比 3 大，迴圈裡沒有任何面額可以拿，`best` 保持 `-1` 並存進 `memo`，之後再遇到「湊 3 元」也會直接查到 `-1`。

**仍需注意的限制：** `min_coins([1], 1200)` 會出現 `RecursionError`，因為只有面額 1 時遞迴深度等於金額，超過 Python 預設約 1000 層的上限；金額 900 時正常。所以題目的金額上限設為 500。

### Why my solution works

最少硬幣數具有最佳子結構：如果湊出 `amount` 的最佳解第一枚是 c，那剩下的硬幣一定是湊出 `amount - c` 的最佳解，否則換成更好的湊法就能更少。函式對每一種第一枚的選擇都遞迴求最佳解並取最小，所以結果是最少的。記憶化不改變計算邏輯，只是讓每個金額的答案只計算一次，之後查表取得，因此答案和單純遞迴完全相同。

### Time complexity

- `min_coins_naive`：每一層都對 k 種面額往下遞迴，同樣的金額被重複計算非常多次，是指數時間。
- `min_coins`：不同的子問題只有 0～amount 共 amount + 1 個，每個只真正計算一次，每次走過 k 種面額，複雜度 **O(amount × k)**。

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

課堂 `fastMaxVal` 的記憶化：先用決策樹的遞迴寫出正確但很慢的版本，再用字典記住重複出現的子問題。這題的決策是「這一枚拿哪個面額」，子問題是「剩下的金額」。

**One thing I understand better now:**

記憶化的 key 要剛好能代表一個子問題。這題只看剩下的金額，背包問題則要同時看剩下的物品和容量。另外，W9 的貪婪法很快但會出錯，暴力法正確但太慢，動態規劃同時做到正確又夠快。

**One thing I am still unsure about:**

遞迴加記憶化會受到遞迴深度的限制（金額 1200 就出錯）。如果改成用迴圈從金額 0 開始往上填表，應該就沒有這個問題，但我還不確定要怎麼改寫。
