# AI Tutor Learning Record (Part A)

- 學號：[請填入學號]
- Name：[請填入姓名]
- Date：2026-11-16
- Topic：MIT 6.0002 Lecture 2 — Optimization Problems（搜尋樹、動態規劃、備忘錄法）
- 教材：MIT OCW 6.0002 Fall 2016, Lecture 2（採逐題互動、提示後修正流程）
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## Part A: True or False

### ① Check My Understanding

- Questions completed: 5 / 5
- Answers revised after AI hints: 1 / 5（第 5 題經提示後，從「物品數量少」進一步精算出重量總和上限為 $500$，補足複雜度推理）

### 題目與解答

#### 第 1 題：純搜尋樹遞迴的空間複雜度

**題目：** 在決策搜尋樹遞迴實作 `maxVal(toConsider, avail)` 中，若總共有 $N$ 個物品，整棵搜尋樹會探索多達 $O(2^N)$ 個節點。因為演算法透過遞迴呼叫堆疊走訪所有分支，記憶體在最深處必須同時容納這 $O(2^N)$ 個節點，因此空間複雜度與時間複雜度一樣都是 $O(2^N)$。

**答案：錯（False）。**

課堂的 `maxVal` 採用**左優先、深度優先（Left-first, depth-first）**的遞迴走訪，並不會在記憶體中真正建立整棵樹，而是用區域變數 `result` 記錄目前最佳解。每當一條分支探索完畢回傳後，該層的 Call Stack 空間就會立刻釋放回收。因此任何時間點記憶體最多只會保存從樹根到葉節點的單一路徑（深度 $N$），僅看遞迴深度為 $O(N)$；即使計入 Python 串列切片 `toConsider[1:]` 在各層複製出的空間總和 $N + (N-1) + \dots + 1$，空間複雜度也僅為 $O(N^2)$，遠小於指數級的時間複雜度 $O(2^N)$。

#### 第 2 題：浮點數重量對動態規劃效能的影響

**題目：** 假設 0/1 背包問題中 $N = 100$、背包上限 $W = 50$。若所有物品的重量皆為帶有 10 位小數的隨機浮點數（例如 `3.1415926535`），使用備忘錄法的 `fastMaxVal(toConsider, avail, memo)` 依然能靠著大量的重疊子問題快速查表，將運算次數壓在數千次以內。

**答案：錯（False）。**

`fastMaxVal` 的執行時間取決於 `memo` 中不重複鍵值對 `<toConsider, avail>` 的總數，而 `avail` 的可能取值取決於「物品重量能湊出多少種不同的總和」。當重量是 $1$ 到 $50$ 的正整數時，`avail` 最多只有 $51$ 種可能；但當重量變成精細的 $10$ 位小數浮點數時，不同路徑扣掉重量後剩餘的 `avail` 幾乎不可能完全相等，導致子問題無法重疊、快取命中率趨近於零，演算法直接退化回指數級搜尋。

#### 第 3 題：附加「首尾組合獎勵」對備忘錄狀態的影響

**題目：** 若在 0/1 背包問題上新增「組合獎勵規則」：只要最終背包同時包含第一個物品 `Item_A` 與最後一個物品 `Item_Z`，總價值就額外加贈 $50$ 分。此時若沿用 `(len(toConsider), avail)` 作為 `memo` 的 key，只在葉節點檢查是否同時包含兩者並加分，依然保證能找到全域最佳解。

**答案：錯（False）。**

這個規則破壞了動態規劃所需的**「無後效性」**。原本的背包問題中，過去拿了哪些物品完全不會影響未來剩餘物品的價值；但加入組合獎勵後，「過去有沒有拿 `Item_A`」會改變未來選 `Item_Z` 的得分。若「沒拿 `Item_A`」的分支先算完某個子問題並存入 `memo`，之後「有拿 `Item_A`」的分支走到相同 `(len(toConsider), avail)` 直接查表時，就會錯過原本較低分、但加贈 $50$ 分後能反超成為全域最佳解的組合。若要正確求解，必須把 `has_Item_A` 也納入狀態 key 中。

#### 第 4 題：新增第二個獨立資源限制的狀態設計

**題目：** 若 0/1 背包問題除了熱量上限 `avail_cal` 之外，還新增了第二個獨立的背包體積上限 `avail_vol`，演算法就無法再單純記錄剩餘數值來定義子問題狀態，而必須把「已選物品清單」放入 `memo` 的 key 中，導致動態規劃失效退化回 $O(2^N)$。

**答案：錯（False）。**

只要過去已選的物品不會影響未來物品的價值，無論新增幾個獨立的資源限制，歷史已選清單都不需要放進狀態裡。在 Python 中，只要將 `memo` 的 key 擴充為不可變（Hashable）的巢狀或三元素 Tuple，例如 `(len(toConsider), (avail_cal, avail_vol))`，依然能唯一描述子問題並共享重疊狀態，將狀態數上限控制在 $O(N \times C \times V)$。

#### 第 5 題：巨大容量上限與偽多項式時間的真實邊界

**題目：** 假設 $N = 100$，每個物品的重量皆為 $1$ 到 $5$ 之間的正整數，但背包耐重上限設為極大的 $W = 10,000,000$。這會導致 `memo` 必須儲存高達 $100 \times 10,000,000 = 10^9$ 種狀態組合，進而讓程式記憶體耗盡或超時崩潰。

**答案：錯（False）。**

`fastMaxVal` 的狀態數並不是無條件等於 $N \times W$，而是受限於**「物品重量能湊出的不同總和數量（distinct sums of weights）」**。雖然 $N = 100$ 的暴力組合高達 $2^{100}$，但因為每個物品重量只有 $1$ 到 $5$，就算 $100$ 個物品全拿，總重量最多也只會消耗 $100 \times 5 = 500$。因此 `avail` 的數值只會落在 $9,999,500$ 到 $10,000,000$ 之間，最多只會出現 $501$ 種不同的剩餘容量，實際狀態數不超過 $50,100$ 種，程式在幾毫秒內即可完成求解。

### ② My Misconception

- **Before（原本想法）：** 對 `memo` 的 key 為什麼不需要記錄「已選物品」還不夠直覺，也容易直覺把「搜尋樹走訪的總節點數（時間）」與「記憶體同時佔用的空間」混為一談。
- **Now（觀念整理）：** 理解了動態規劃狀態設計的「無後效性」——`memo` 儲存的是「從剩餘清單中最多還能再榨出的最佳增量」，過去路徑由上層遞迴回傳時再自行拼裝，因此 key 只需記錄影響未來的變數 `(len(sub_features), rem_hours)`。同時釐清了記憶體會隨遞迴回傳不斷回收，空間只看單次最深快照，時間則是所有分支的累積。

### ③ Challenge the AI

- **Question examined：** 第 2 題（物品重量為 $10$ 位小數浮點數時，備忘錄法是否仍能靠查表快速求解）。
- **Why：** Too easy（太簡單）。
- **Brief explanation：** 只要掌握了 `memo` 依賴「剩餘容量 `avail` 重疊」的核心原理，看到「$10$ 位小數隨機浮點數」就能立刻反應出兩條路徑幾乎不可能扣出完全相同的剩餘容量，轉折較少、難度偏低。

### ④ One-Minute Reflection

- **One thing I am still unsure about（課中釐清的疑問）：** 原本對於「為何 Python 串列切片 `toConsider[1:]` 的空間複雜度是 $O(N^2)$ 卻遠小於 $O(2^N)$」以及「為何 $O(N \times W)$ 被稱為偽多項式時間」感到難以想像。經討論後釐清：時間是跨分支累積、空間則隨 DFS 釋放重用（以 $N=30$ 為例，空間僅需 $30^2 = 900$ 單位，時間卻達 $2^{30} \approx 10.7$ 億次）；而電腦輸入數字 $W$ 只需 $b = \log_2 W$ 個 bits，因此 $O(N \times W) = O(N \times 2^b)$ 在輸入位元長度上其實是指數級增長，故稱為「偽多項式時間」。

---

# AI Tutor Learning Record (Part B)

- 學號：[請填入學號]
- Name：[請填入姓名]
- Date：2026-11-16
- Topic：MIT 6.0002 Lecture 2 — Optimization Problems（搜尋樹、動態規劃、備忘錄法）
- 程式檔：`sprint_optimizer.py`
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## 1. Today's Challenge

**Core concept from today's OCW lecture:**

當 0/1 最佳化問題（如產品功能排程）面對較大的輸入規模（$N = 60$）時，貪婪演算法容易陷入區域最佳解陷阱，而純搜尋樹枚舉則會遭遇 $O(2^N)$ 指數爆炸。利用問題具備「最佳子結構」與「重疊子問題」的特性，透過搜尋樹遞迴結合字典備忘錄（Memoization），即可在多項式／偽多項式時間內求得全域最佳解。

**AI-generated coding challenge title:** Product Sprint Feature Optimization（產品衝刺功能排程最佳化）

### 題目

在固定的衝刺週期工時上限 `max_hours` 內，從候選功能清單中挑選要開發的功能（每個功能只能完整開發 `1` 或不做 `0`），求能獲得的**最高商業影響力總和**與**對應的 `Feature` 物件元組**。

| 類別 / 函式 | 功能說明 |
|---|---|
| `Feature(name, impact, hours)` | 封裝單一產品功能的名稱、商業影響力分數與開發工時 |
| `optimize_sprint(features, max_hours)` | 使用搜尋樹與字典備忘錄法，回傳 `(最大總影響力, 選取的 Feature 元組)` |

- 限制條件：$0 \le \text{len}(features) \le 100$，$1 \le \text{hours} \le 500$，$0 \le \text{max\_hours} \le 1000$，且 $N=60$ 時須在 $1$ 秒內完成。

| 測試情境 | 輸入 (`features`, `max_hours`) | 預期結果 | 說明 |
|---|---|---|---|
| Example 1（貪婪陷阱） | `AI_Search(70, 41h)`, `Payment(65, 40h)`, `Live_Chat(65, 40h)`, `max=80` | `(130, (Payment, Live_Chat))` | 貪婪法選 `AI_Search` 僅得 $70$ 分；DP 跳過後選後兩者可得 $130$ 分 |
| Example 2（重疊子問題） | `Auth(6, 3h)`, `Billing(7, 3h)`, `Analytics(8, 2h)`, `Mobile(9, 5h)`, `max=5` | `(15, (Billing, Analytics))` | 選 `Billing` 與 `Analytics` 剛好用滿 $5\text{h}$ 得最高 $15$ 分 |
| Example 3（單品超時） | `Legacy_Migration(100, 50h)`, `max=20` | `(0, ())` | 無法容納任何功能，回傳 $0$ 分與空元組 |

## 2. My Initial Approach — Before AI Help

先參考 AI 提供的 Subset Sum（子集和）備忘錄範例，將決策拆成「選取當前功能（左分支）」與「不選當前功能（右分支）」，並在外層函式內建立乾淨的字典 `memo = {}`（避免 Python 預設可變參數在多次呼叫時殘留舊快取），以 `state = (len(sub_features), rem_hours)` 作為子問題的 key。

## 3. AI Tutor Help

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**

1. 指出 `0/1 背包問題` 的限制是不等式（`<= max_hours`），不需要像 Subset Sum 那樣要求剛好扣到 `0`，因此不需要額外回傳布林值 `found`。
2. 指出終止條件回傳 `(True, 0, 0)` 會導致 Tuple 串接時發生 `TypeError`，以及刪掉 `found` 時誤刪終止條件會引發 `IndexError: list index out of range`。

**It helped me realize that:**

可行性問題（要求嚴格等於目標值）需要布林旗標區分「成功空籃子」與「死胡同」；但最佳化問題只要透過剪枝確保不超時，每條走到底的分支都是合法解，終止條件只需統一回傳 `(0, ())`，再由上層比較左右分支的總影響力即可。

## 4. My Revision

- [ ] No
- [x] Yes

**What did you change, and why?**

1. **移除多餘的 `found` 布林值並修正回傳格式**：將回傳值統一改為題目規範的雙元素元組 `(total_impact, selected_features_tuple)`，解決無法剛好塞滿 `max_hours` 時誤判為 $0$ 分的邏輯盲點。
2. **補回終止條件並修正型別與縮排錯誤**：在 `helper` 開頭補上 `if len(sub_features) == 0 or rem_hours <= 0: memo[state] = (0, ()); return memo[state]`，避免 `sub_features[0]` 索引越界以及整數與 Tuple 相加的 `TypeError`，同時修正外層 `return helper(features, max_hours)` 的縮排。

### 最終程式

```python
class Feature:
    def __init__(self, name: str, impact: int, hours: int):
        self.name = name
        self.impact = impact
        self.hours = hours

    def __repr__(self):
        return f"Feature({self.name!r}, impact={self.impact}, hours={self.hours})"


def optimize_sprint(features, max_hours):
    memo = {}

    def helper(sub_features, rem_hours):
        # 定義子問題狀態：(剩餘功能個數, 剩餘可用工時)
        state = (len(sub_features), rem_hours)

        # 【步驟 1：查表】算過就直接回傳
        if state in memo:
            return memo[state]

        # 【步驟 2：終止條件】無剩餘功能或無剩餘工時
        if len(sub_features) == 0 or rem_hours <= 0:
            memo[state] = (0, ())
            return memo[state]

        first = sub_features[0]
        rest = sub_features[1:]

        # 【步驟 3：右分支 — 不選 first】
        impact_without, features_unselected = helper(rest, rem_hours)

        # 【步驟 3：左分支 — 若工時足夠，嘗試選 first 並比較總影響力】
        if first.hours <= rem_hours:
            impact_with, features_selected = helper(rest, rem_hours - first.hours)
            if impact_with + first.impact > impact_without:
                memo[state] = (impact_with + first.impact, (first,) + features_selected)
                return memo[state]

        # 【步驟 4：存表並回傳較佳結果】
        memo[state] = (impact_without, features_unselected)
        return memo[state]

    return helper(features, max_hours)
```

## 5. Verification

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

| 測試項目 | 輸入規模 / 情境 | 執行結果 / 耗時 | 狀態 |
|---|---|---|---|
| Example 1 | $3$ 個功能，`max_hours = 80`（貪婪陷阱） | `(130, (Payment_Gateway, Live_Chat))` | 通過 |
| Example 2 | $4$ 個功能，`max_hours = 5`（重疊子問題） | `(15, (Billing, Analytics))` | 通過 |
| Example 3 | $1$ 個超時功能（$50\text{h}$），`max_hours = 20` | `(0, ())` | 通過 |
| Edge Case 4 | 空串列 `[]` 或 `max_hours = 0` | `(0, ())` | 通過 |
| Stress Test | 隨機生成 $N = 60$ 個功能，`max_hours = 1000` | 最佳總分 $96850$（選 $15$ 項），耗時 **$0.2714$ 秒** | 通過 |

**One edge case I tested:**

- Input：`optimize_sprint([Feature("Legacy_Migration", impact=100, hours=50)], 20)`
- Expected output：`(0, ())`
- Actual output：`(0, ())`

### Why my solution works

演算法透過搜尋樹完整比較每個功能「選」與「不選」的分支，確保滿足**最佳子結構**以找出全域最佳解；同時利用 `memo` 字典儲存已計算過的 `(len(sub_features), rem_hours)` 子問題最佳解，當不同決策路徑遇到相同剩餘功能與剩餘工時時直接查表回傳，成功避開指數級的重複運算。

### Time complexity

- **時間複雜度**：**$O(N \times W)$**（偽多項式時間），其中 $N$ 為候選功能數量，$W$ 為總工時上限 `max_hours`。`memo` 中不重複狀態數受限於剩餘功能數（最多 $N$ 種）與工時能湊出的不同總和數（上限為 $W$）。

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

將 Lecture 2 的 **搜尋樹（Search Tree）** 遞迴分支架構與 **重疊子問題（Overlapping Subproblems）** 的雙變數狀態 `(len(sub_features), rem_hours)` 備忘錄法，轉移到產品衝刺功能排程的 0/1 最佳化問題中。

**One thing I understand better now:**

清楚區分了「嚴格等於目標（Subset Sum，需用布林值區分死胡同）」與「不超過上限即可（0/1 Knapsack，直接比較左右分支價值）」在遞迴終止條件設計上的差異，也體會到記憶化在 $N=60$ 時從指數超時壓縮到 $0.27$ 秒的巨大威力。

**One thing I am still unsure about:**

目前是用由上往下的遞迴加字典（Top-down Memoization）實作；如果改用由下往上的二維表格迴圈（Bottom-up Tabulation）撰寫，在回溯找出「具體選了哪些 `Feature` 物件」時的實作細節還需要多加練習。