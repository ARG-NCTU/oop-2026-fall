# Week 6 — AI Tutor Learning Record (Part B)

- 學號：112511246
- Name：張中愷
- Date：2026-10-20
- Topic：Lecture 10 — 理解程式效率（一）（Understanding Program Efficiency, Part 1）
- 程式檔：[w6.py](w6.py)
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## 1. Today's Challenge

**Core concept from today's OCW lecture:**

用 Big O 描述輸入變大時程式的步數成長多快。一段程式包在另一段裡面時複雜度相乘（乘法規則），課堂的 `intersect`、`is_subset` 就是「拿 L1 的每個元素去 L2 逐一比對」而成為 O(n²)。另外，對 list 使用 `in` 背後要逐一比對，是 O(n)；字典查詢 key 則幾乎是 O(1)。

**AI-generated coding challenge title:** Pair Sum（兩數之和）

### 題目

給一個整數 list `nums` 和整數 `target`，判斷 list 裡是否有兩個**不同位置**的數字加起來剛好等於 `target`。寫兩個結果相同的函式：

| 函式 | 要求 |
|---|---|
| `has_pair_slow(nums, target)` | 最直覺的寫法，O(n²) |
| `has_pair_fast(nums, target)` | 改成 O(n) |

- 輸入：`nums` 為整數 list，長度 0～10000，可能為空、可能有負數或重複；`target` 為整數。
- 輸出：`True` 或 `False`。

| 範例 | 輸入 | 輸出 | 說明 |
|---|---|---|---|
| 1 | `[3, 8, 1, 5]`, 9 | `True` | 8 + 1 = 9 |
| 2 | `[4, 2, 7]`, 8 | `False` | 只有一個 4，不能用兩次 |
| 3 | `[4, 2, 4]`, 8 | `True` | 兩個 4 在不同位置 |
| 4 | `[]`, 5 | `False` | |

## 2. My Initial Approach — Before AI Help

慢的版本用兩層 for 迴圈列出所有配對，內層從 `i + 1` 開始，這樣同一個位置不會跟自己配對，也不會重複檢查同一對。

## 3. AI Tutor Help

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**

想快的版本時，AI 換個角度說明慢的版本：拿到 `nums[i]` 時，其實需要的是 `target - nums[i]`，內層迴圈只是在 list 裡「找」這個數字，找一次 O(n)、外層 n 次，所以是 O(n²)，跟課堂的 `intersect` 是同一個原因。要變快，就要讓「找」變快，而字典的 `in` 是 O(1)。

我第一版的快版本答案正確，但 AI 讓兩個版本跑「湊不到」的最壞情況，資料量每次加倍：我的快版本從 0.020 秒 → 0.079 秒 → 0.318 秒，**n 變 2 倍時間變 4 倍**，說明它其實還是 O(n²)。AI 問我：`pair.values()` 拿到的是什麼？「字典的 `in` 是 O(1)」指的是在 key 裡找還是在 value 裡找？

**It helped me realize that:**

字典只有查 **key** 才是 O(1)；`x in d.values()` 要一個一個看 value，跟 list 的 `in` 一樣是 O(n)，又是一個「藏起來的迴圈」。所以要把「需要檢查的東西」存成 key。

## 4. My Revision

- [ ] No
- [x] Yes

**What did you change, and why?**

第一版的快版本存的是「key：看過的數字，value：它需要的另一半」，再用 `if i in pair.values()` 檢查目前的數字是不是某個人需要的另一半。邏輯正確，但 `values()` 的 `in` 是 O(n)，整體仍是 O(n²)。

我改成把「需要的另一半」`target - i` 直接存成 key（value 用不到，放 `None`），再用 `if i in pair` 檢查目前的數字是否在 key 裡，這樣每次檢查都是 O(1)，整體變成 O(n)。

### 最終程式

```python
def has_pair_slow(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i]+nums[j] == target:
                return True
    return False


def has_pair_fast(nums, target):
    pair = {}
    for i in nums:
        if i in pair:
            return True
        pair[target-i] = None
    return False
```

## 5. Verification

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

另外測試的邊界情況（兩個版本都測）：

| 測試 | 輸入 | 預期輸出 | 實際輸出 |
|---|---|---|---|
| 只有一個數字 | `[5]`, 10 | `False` | `False` |
| 兩個相同數字 | `[5, 5]`, 10 | `True` | `True` |
| 兩個 0 | `[0, 0]`, 0 | `True` | `True` |
| 兩個負數 | `[-5, -5]`, -10 | `True` | `True` |
| 有負數 | `[-3, 7, 1]`, 4 | `True` | `True` |
| 湊不到 | `[1, 2, 3]`, 100 | `False` | `False` |
| 隨機測資 | 長度 0～8、數字 -10～10 的隨機 list，與窮舉所有配對的答案比對 | 全部一致 | 全部一致 |

**One edge case I tested:**

- Input：`has_pair_fast([5], 10)`
- Expected output：`False`
- Actual output：`False`

5 + 5 = 10，但只有一個 5。因為迴圈是先檢查 `5 in pair`（此時字典是空的），之後才把 `10 - 5 = 5` 放進字典，所以 5 不會跟自己配對。

### 執行時間（最壞情況：湊不到）

| n | `has_pair_slow` | 第一版 fast（查 `values()`） | 最終版 fast（查 key） |
|---|---|---|---|
| 2,500 | 0.089 秒 | 0.020 秒 | 0.0001 秒 |
| 5,000 | 0.339 秒 | 0.079 秒 | 0.0002 秒 |
| 10,000 | 1.378 秒 | 0.318 秒 | 0.0004 秒 |
| 1,000,000 | （未執行） | （未執行） | 0.062 秒 |

慢的版本和第一版 fast 都是 n 變 2 倍、時間變約 4 倍（O(n²)）；最終版是 n 變 2 倍、時間變約 2 倍（O(n)）。

### Why my solution works

`has_pair_slow`：外層 i 走過每個位置，內層 j 從 `i + 1` 開始，列出所有不同位置的配對，任一對相加等於 `target` 就回傳 True。

`has_pair_fast`：從左往右走，字典的 key 記錄「目前為止看過的數字需要的另一半」。走到數字 `i` 時，先檢查 `i` 是否是之前某個數字需要的另一半，是就找到一對；不是再把 `target - i` 存進去。因為先檢查再放入，同一個位置不會跟自己配對。

### Time complexity

- `has_pair_slow`：兩層迴圈，外層 n 次、內層最多 n 次，**O(n²)**。
- `has_pair_fast`：一個迴圈 n 次，每次只做字典的 key 查詢和放入，都是 O(1)，**O(n)**。

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

字典的 `in` 是 O(1)、list 的 `in` 是 O(n)。課堂的 `intersect` 因為在 list 裡逐一尋找而是 O(n²)；這題把「找另一半」改成查字典的 key，就從 O(n²) 降到 O(n)。

**One thing I understand better now:**

答案正確不代表複雜度正確。第一版的快版本答案都對，但 `pair.values()` 的 `in` 藏了一個迴圈；實際把 n 加倍看時間變幾倍，就能看出是 O(n) 還是 O(n²)。

**One thing I am still unsure about:**

最終版字典的 value 都放 `None`，其實只用到 key。有沒有只需要存 key、不用放 value 的資料結構可以做同樣的事？
