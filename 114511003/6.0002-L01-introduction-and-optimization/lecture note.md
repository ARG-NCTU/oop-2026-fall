# Lecture 1：Introduction and optimization problems

本筆記整理 MIT 6.0002 Fall 2016 第一講，講者為 John Guttag。重點是把問題寫成最佳化模型，再比較窮舉法與貪婪法。中文說明、手算追蹤及練習是整理與補充，並非影片逐字稿。

## 課程來源與閱讀方式

- [Lecture 1 課程影片頁](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/resources/lecture-1-introduction-and-optimization-problems/)。
- [官方投影片與程式檔索引](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/pages/lecture-slides-and-files/)。
- 主要來源為提供的 [L_1-Introduction and Optimization Problems.pdf](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/pages/lecture-slides-and-files/)，共 31 頁。下文頁碼採 PDF 實際頁次，最後一頁為來源資訊。
- 附件中的課程行政事項是 MIT 2016 年課程內容，不代表 AOOP 的作業或考試規定。本筆記沒有新增作業要求。

注意資料版本：第 20 頁菜單與第 28 頁程式的 value 不同。第 28 頁還有 9 個名稱、8 個 value 和 8 個 calories，違反 `buildMenu` 的等長前提。以下統一採第 20 頁的 8 筆資料，不補造 cake 的數值。

## 1. 這堂課在學什麼？

來源：PDF 第 2–8 頁。

6.0002 延續 Python 基礎，開始用計算模型分析問題。課程預期學生熟悉物件導向、基本演算法與複雜度；本講也會用到把函式當參數傳遞，以及 `lambda`。

計算模型會挑出現實問題中要分析的變數和關係，讓我們可以進行實驗、解釋觀察或預測結果。課程列出三種模型方向：

| 模型 | 主要問題 | 本筆記的例子 |
|---|---|---|
| 最佳化模型 optimization model | 限制之下，哪個選擇最好？ | 熱量上限內如何選餐 |
| 統計模型 statistical model | 資料中的關係與不確定性是什麼？ | 用樣本推估整體，為補充例子 |
| 模擬模型 simulation model | 按規則運行後，系統可能如何變化？ | 模擬排隊時間，為補充例子 |

本講集中在最佳化。模型中的「最好」取決於目標如何定義；若把口味分數當價值，程式就不會自動考慮營養均衡。

## 2. 最佳化模型的組成

來源：PDF 第 9 頁。

建立模型時，要清楚寫出：

1. **決策變數**：哪些選擇由我們決定？
2. **目標函數 objective function**：要最大化或最小化什麼？
3. **限制條件 constraints**：哪些條件不能違反？限制也可能為空集合。

投影片用紐約到波士頓的旅程說明：目標是最短旅行時間，限制包括花費不超過 100 美元、下午 5 點前抵達。時間與花費扮演不同角色，不能混為同一個量。

滿足所有限制的解稱為可行解 feasible solution。所有可行解中，目標值最好的才是最佳解 optimal solution。可行不等於最佳；最佳解也可能不只一個。

## 3. 背包問題 knapsack problem

來源：PDF 第 10–14 頁。

每個物品都有價值 value 和重量 weight。背包容量有限，要決定帶哪些物品，使總價值最大。

| 變體 | 決策範圍 | 意義 |
|---|---|---|
| 0/1 背包 | 每個物品選 0 或 1 次 | 整件拿或不拿，不能切割 |
| 可分割背包 fractional knapsack | 每個物品可取 0 到 1 的比例 | 可只拿一部分 |

0/1 不是指物品的價值只能是 0 或 1，而是選擇變數只有兩種值。這裡每件物品最多取一次，也不是可以重複拿取的版本。

### 3.1 數學表示

設有 `n` 個物品，物品 `i` 的價值為 `v_i`、重量為 `w_i`，容量上限為 `W`。令 `x_i = 1` 表示選取，`x_i = 0` 表示不選。

$$
\max \sum_{i=0}^{n-1} x_i v_i
$$

限制為：

$$
\sum_{i=0}^{n-1} x_i w_i \leq W,\qquad x_i\in\{0,1\}.
$$

投影片用 `I` 表示物品向量、`V` 表示選擇向量。因此投影片的 `V[i]` 對應這裡的 `x_i`，不是物品本身的 value。

若選擇向量是 `[1, 0, 1]`，總價值為 `v_0 + v_2`，總重量為 `w_0 + w_2`。空集合也是候選解；在容量非負時，它的重量與價值均為 0。

## 4. 窮舉法 brute force

來源：PDF 第 15–17 頁。

做法是列出所有物品子集合，排除超重組合，再從剩下的組合挑選總價值最高者。所有子集合組成冪集合 power set。

每件物品都有選或不選兩種可能，因此有 `2^n` 個子集合，包含空集合。3 個物品有 8 種組合；100 個物品約有 `1.27 × 10^30` 種。

窮舉保證找到最佳解，因為它檢查了每一個可行候選。但候選數會隨 `n` 指數成長。

### 4.1 複雜度與投影片用語補充

逐一產生子集合、每次掃描最多 `n` 件物品計算重量與價值，時間為 `O(n 2^n)`。若一次保留所有子集合，空間可達 `O(n 2^n)`；逐一產生並只保留目前最佳組合，可把額外空間降為 `O(n)`。

第 17 頁把 0/1 背包描述為 inherently exponential。較精確的補充是：一般 0/1 背包的決策版為 NP-complete，最佳化版為 NP-hard；目前沒有已知的一般多項式時間精確演算法，不能說已證明所有解法都必須耗指數時間。

若重量和容量是非負整數，可用 `O(nW)` 時間的動態規劃。這是偽多項式時間，因為 `W` 的數值大小不等於它的二進位編碼長度。動態規劃是補充背景，本講尚未展開實作。

## 5. 貪婪法 greedy algorithm

來源：PDF 第 18、23–24、29–30 頁。

貪婪法每次依某個規則，優先選目前看起來最好的可行物品。已做的選擇不回頭修改，因此速度快，但可能錯過更好的組合。

本講比較三種排序規則：

| 策略 | 優先選擇 | 由大到小排序的 key | 可能忽略的因素 |
|---|---|---|---|
| 依價值 | value 較大者 | `Food.getValue` | 一件高價值物品可能太占容量 |
| 依成本 | calories 較少者 | `lambda x: 1 / x.getCost()` | 低成本物品可能幾乎沒有價值 |
| 依密度 | value / calories 較大者 | `Food.density` | 整件物品間的組合效果 |

密度 density 是每單位成本的價值。原程式一律用 `reverse=True`，所以成本策略取倒數，讓低成本取得較高 key。這要求成本大於 0；若允許零成本，倒數和密度需要另行處理。

### 5.1 選不到目前這件，要繼續看下一件

排序後逐件檢查，裝得下就選，裝不下就跳過。不能因為一件太重就直接停止，因為後面可能有較輕的物品。

迴圈中的不變量是 `totalCost <= maxCost`。每次加入前都檢查新的總成本，所以回傳的組合滿足容量限制。這只能證明可行性，不能證明價值最大。

### 5.2 時間與空間

假設讀取 value、cost、計算 key 及數值運算都是 `O(1)`，令 `n` 為物品數：

- 排序最壞時間為 `O(n log n)`，掃描為 `O(n)`，總時間為 `O(n log n)`。
- `sorted` 建立新 list，排序工作空間與結果 list 最壞也都是 `O(n)`，所以額外空間為 `O(n)`。
- `sorted` 不改變輸入 list 的順序，但新 list 仍參照原本的 `Food` 物件，並非深拷貝。

## 6. Python 實作與物件導向設計

來源：PDF 第 21–28 頁。以下保留 `Food`、`buildMenu`、`greedy` 的名稱與參數，整理縮排與迴圈寫法。另在 `buildMenu` 新增等長檢查，避免投影片的多餘名稱被默默忽略。

使用前提為 value 非負、calories 大於 0、容量非負。整理版沒有對所有資料型別另做完整驗證。

```python
class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue() / self.getCost()

    def __str__(self):
        return f"{self.name}: <{self.value}, {self.calories}>"


def buildMenu(names, values, calories):
    if not (len(names) == len(values) == len(calories)):
        raise ValueError("names, values, calories must have equal lengths")
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu


def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for item in itemsCopy:
        if totalCost + item.getCost() <= maxCost:
            result.append(item)
            totalCost += item.getCost()
            totalValue += item.getValue()
    return result, totalValue
```

`Food` 管理食物資料；`greedy` 只透過 `getCost()`、`getValue()` 取得成本與價值。`keyFunction` 則決定優先順序，同一個演算法可以替換不同策略，不必複製三份選取程式。

`Food.getValue` 是可呼叫的函式，排序時會收到食物物件。傳入 `Food.getValue` 並不會立即計算；寫成 `Food.getValue()` 則會因為缺少物件參數而出錯。

### 6.1 lambda 的意思

來源：PDF 第 27 頁。

`lambda x: 1 / x.getCost()` 建立一個接收 `x`、回傳成本倒數的匿名函式，等同於：

```python
def inverse_cost(x):
    return 1 / x.getCost()
```

`lambda` 適合簡短表達式。若需要多個步驟、條件或說明，使用 `def` 會比較容易閱讀。

## 7. 菜單演算範例

來源：PDF 第 19–20 頁的情境與資料。以下計算為整理時實際執行的結果。

將食物視為物品，value 視為喜好分數，calories 視為成本。每道菜最多取一份，總熱量不可超過上限，目標為最大總喜好分數。

| 食物 | value | calories | density，約值 |
|---|---:|---:|---:|
| wine | 89 | 123 | 0.724 |
| beer | 90 | 154 | 0.584 |
| pizza | 30 | 258 | 0.116 |
| burger | 50 | 354 | 0.141 |
| fries | 90 | 365 | 0.247 |
| coke | 79 | 150 | 0.527 |
| apple | 90 | 95 | 0.947 |
| donut | 10 | 195 | 0.051 |

```python
names = ["wine", "beer", "pizza", "burger", "fries", "coke", "apple", "donut"]
values = [89, 90, 30, 50, 90, 79, 90, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)

strategies = {
    "value": Food.getValue,
    "cost": lambda x: 1 / x.getCost(),
    "density": Food.density,
}
for label, key in strategies.items():
    taken, value = greedy(foods, 750, key)
    cost = sum(item.getCost() for item in taken)
    print(label, [item.name for item in taken], value, cost)
```

### 7.1 依密度的手算追蹤

容量設為 750，排序結果為 apple、wine、beer、coke、fries、burger、pizza、donut。

| 目前物品 | 操作 | 累積成本 | 累積價值 |
|---|---|---:|---:|
| apple | 加入 | 95 | 90 |
| wine | 加入 | 218 | 179 |
| beer | 加入 | 372 | 269 |
| coke | 加入 | 522 | 348 |
| fries | 加入會超過 750，跳過 | 522 | 348 |
| burger | 加入會超過 750，跳過 | 522 | 348 |
| pizza | 加入會超過 750，跳過 | 522 | 348 |
| donut | 加入 | 717 | 358 |

剩餘容量 33，沒有必要剛好用完容量。目標是最大化價值，並沒有要求總成本一定等於上限。

同分時 Python 的排序保留輸入順序。本例 value 同為 90 的 beer、fries、apple，會按原菜單順序接受檢查；不同的同分處理可能產生不同組合。

## 8. 密度最高也可能失敗

來源：PDF 第 29–30 頁提出「局部最佳不保證全域最佳」。以下數字是補充反例，不是原投影片菜單。

容量為 50，三件物品如下：

| 物品 | value | weight | density |
|---|---:|---:|---:|
| A | 60 | 10 | 6 |
| B | 100 | 20 | 5 |
| C | 120 | 30 | 4 |

依密度先取 A，再取 B，已用重量 30。剩餘容量 20 放不下 C，總價值為 160。

但 B 與 C 合計重量 50、價值 220，更優於 160。貪婪法不會主動移除 A 來換取 C，因此錯過最佳解。這一個反例就足以推翻「依密度一定能解出 0/1 背包最佳解」。

補充：若允許分割物品，且價值隨取用比例線性增加、重量為正，依密度選取可得到最佳解。本例可取 A、B，再取 `2/3` 的 C，價值為 `60 + 100 + 80 = 240`。這個結論依賴可分割前提，不能直接套到 0/1 版本。

## 9. 可執行檢查

以下是筆記補充的測試，不是作業。依序執行前面的程式區塊後，再執行本段。涵蓋正常情況、空輸入、容量邊界、跳過過重物品、預期失敗與貪婪反例。

```python
assert greedy([], 750, Food.getValue) == ([], 0.0)
assert greedy(foods, 0, Food.getValue) == ([], 0.0)
assert greedy([Food("heavy", 100, 751)], 750, Food.getValue) == ([], 0.0)

one = Food("exact", 7, 10)
assert greedy([one], 10, Food.getValue) == ([one], 7.0)

heavy, light = Food("heavy", 100, 11), Food("light", 5, 2)
assert greedy([heavy, light], 10, Food.getValue) == ([light], 5.0)

before = foods[:]
taken, value = greedy(foods, 750, Food.density)
assert [item.name for item in taken] == ["apple", "wine", "beer", "coke", "donut"]
assert value == 358
assert sum(item.getCost() for item in taken) == 717
assert foods == before

try:
    buildMenu(["a", "b"], [1], [10])
except ValueError:
    pass
else:
    raise AssertionError("Unequal lengths should raise ValueError")

counterexample = buildMenu(["A", "B", "C"], [60, 100, 120], [10, 20, 30])
assert greedy(counterexample, 50, Food.density)[1] == 160
assert counterexample[1].getCost() + counterexample[2].getCost() == 50
assert counterexample[1].getValue() + counterexample[2].getValue() == 220
print("All note checks passed")
```

## 10. 常見誤解與複習問題

| 誤解 | 正確理解 |
|---|---|
| greedy 的 key 就是整體目標函數 | key 只決定局部排序；整體目標仍是總價值 |
| 依成本就是直接把 cost 由大到小排 | 本講用成本倒數，讓低成本先出現 |
| `sorted` 的時間是 `O(n)` | 一般最壞為 `O(n log n)`，不能只計掃描迴圈 |
| 裝不下目前物品就結束 | 要繼續檢查，後面可能裝得下 |
| 選出合法組合就代表最佳 | 可行性和最佳性需要不同論證 |
| 幾次實驗都是 density 贏，就代表永遠贏 | 要普遍保證最佳性，需要證明；反例即可推翻保證 |
| 背包重量只能是真正的重量 | 也能代表熱量、金錢或其他資源成本 |

### 不使用 AI 的自我檢查

1. 用自己的話寫出選餐模型的決策變數、目標函數與限制條件。
2. 5 個物品有幾個子集合？為什麼不是 `5!`？
3. 不執行程式，追蹤第 7 節菜單在容量 750 時，依 value 選餐的順序與結果。
4. 說明 `Food.getValue` 與 `Food.getValue()` 的差別。
5. 為什麼迴圈保持 `totalCost <= maxCost`，仍不足以證明得到最佳解？
6. 自行列出第 8 節所有可行子集合，確認最佳值為 220。
7. 若 `keyFunction` 每次需要 `O(k)` 時間，Python 排序會為每件物品計算一次 key，整個 greedy 的時間上界應如何改寫？

<details>
<summary>完成後再看參考答案</summary>

1. 每道菜是否選取是變數；最大化總喜好分數；總熱量不得超過上限，每道菜最多一份。
2. `2^5 = 32`。這是每件物品選或不選，不是排列所有物品。
3. 依序取 beer、fries、apple、wine，累積成本 737、價值 359。其餘無法加入。同為 90 分時保留原始順序。
4. 前者傳遞函式，後者立即呼叫。在這個類別定義中，直接呼叫後者缺少 `self`。
5. 它只證明沒有超出容量，沒有比較其他可行組合的價值。
6. 可行集合為空集合、A、B、C、AB、AC、BC。ABC 重量 60，不可行；BC 的價值 220 最高。
7. 在其他操作仍為常數成本時，為 `O(nk + n log n)`。key 不是在每次比較時重新計算。

</details>

## 11. 一頁複習

- 建模時先分清楚選擇、目標和限制，再討論演算法。
- 0/1 背包每件物品只能整件選或不選；`n` 件物品有 `2^n` 個子集合。
- 窮舉檢查所有候選，保證最佳，但候選數成長太快。
- 本講的 greedy 先排序再掃描，最壞時間 `O(n log n)`、額外空間 `O(n)`。
- 價值、低成本、密度是不同的局部選擇規則，都不能一般性保證 0/1 背包最佳解。
- `keyFunction` 讓選取流程與優先規則分開；`lambda` 可用來寫簡短規則。
- 可分割背包在上述線性價值與正重量前提下，可以依密度求得最佳解。
