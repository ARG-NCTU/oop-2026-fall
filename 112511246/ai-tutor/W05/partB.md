# Week 5 — AI Tutor Learning Record (Part B)

- 學號：112511246
- Name：張中愷
- Date：2026-10-14
- Topic：Lecture 9 — Python 類別與繼承（Python Classes and Inheritance）
- 程式檔：[w5.py](w5.py)
- 格式來源：[AI Tutor for AOOP 2026](https://github.com/ARG-NCTU/oop-python-nycu/blob/main/ai-tutor-2026.md)

## 1. Today's Challenge

**Core concept from today's OCW lecture:**

子類別繼承父類別的資料和方法，可以覆寫（override）同名方法；子類別有自己的 `__init__` 時，要呼叫 `父類別.__init__(self, ...)` 讓父類別設定它負責的資料。類別變數寫在 class 裡、方法外面，所有物件共用一份，課堂的 `Rabbit.tag` 就是用它幫每隻兔子編號。

**AI-generated coding challenge title:** Parking Lot（停車場收費）

### 題目

停車場有三種車，收費方式不同，每台車進場時拿一個全停車場共用的編號。

**父類別 `Vehicle`（一般汽車）**

| 名稱 | 要做什麼 |
|---|---|
| 類別變數 `next_id` | 下一台車的編號，從 1 開始，所有種類的車共用 |
| `__init__(self, plate, hours)` | 存車牌和停車時數，並拿一個編號存成 `self.vid` |
| `fee(self)` | 每小時 30 元 |
| `__str__(self)` | 印成 `#編號 車牌: 費用元`，例如 `#1 ABC-123: 60元` |

**子類別 `Motorcycle`（機車）**：`fee(self)` 改成每小時 10 元。

**子類別 `Truck`（卡車）**：`__init__(self, plate, hours, weight)` 多存重量（噸），車牌、時數、編號交給 `Vehicle`；`fee(self)` 每小時 50 元，重量超過 10 噸再加 100 元。

**函式 `total_fee(vehicles)`**：回傳 list 裡所有車的停車費總和。

- 限制：`hours`、`weight` 為至少 1 的整數；三種車共用同一套編號。

```python
c = Vehicle("ABC-123", 2)
m = Motorcycle("MOTO-1", 3)
t = Truck("TRK-9", 2, 12)
print(c)                      # #1 ABC-123: 60元
print(m)                      # #2 MOTO-1: 30元
print(t)                      # #3 TRK-9: 200元
print(total_fee([c, m, t]))   # 290
```

## 2. My Initial Approach — Before AI Help

AI 先問我三個問題，我的回答是：

- `__str__` 只寫在 `Vehicle`，要印出各種車自己的費用，就在 `__str__` 裡用 `self.fee()` 拿費用。
- `Truck` 的 `__init__` 呼叫 `Vehicle.__init__`，車牌、時數、編號交給父類別處理。
- 三種車共用編號，用 `Vehicle.next_id`。

## 3. AI Tutor Help

- [ ] No — I solved it independently
- [x] Yes — I received one or more hints

**The most useful hint/question from AI was:**

第一版三台車的編號都是 `#1`。AI 用課堂 Rabbit 的號碼牌機提醒我：每來一台車要做兩件事，① 抽號碼、② 號碼機跳下一號，我只做了 ①。

我接著問了兩個問題：為什麼讀 `next_id` 要加 `self.`，以及為什麼不能什麼都不加、直接寫 `next_id`。AI 說明：

- 方法裡直接寫 `next_id`，Python 只會找方法裡的變數和檔案最外層的變數，不會去找 class 裡的變數，所以會出現 `NameError`。這點跟 C++ 不同，C++ 的成員函式可以直接用 static 成員。
- `self.next_id` 讀得到，因為物件身上找不到時會往上找 class；但 `self.next_id = ...` 會在這台車身上另外建一個 `next_id`，共用的號碼機不會被改到。
- 要改共用的類別變數，一定要寫 `Vehicle.next_id`，讀和改都統一這樣寫最不容易出錯。

**It helped me realize that:**

類別變數「讀」和「改」的規則不一樣：讀的時候 `self.` 會往上找到 class，改的時候 `self.` 卻會在物件身上建新的變數。所以要改共用的資料，一定要明確寫出 class 名稱。

## 4. My Revision

- [ ] No
- [x] Yes

**What did you change, and why?**

第一版 `__init__` 只有 `self.vid = self.next_id`，沒有讓號碼機往下跳，所以每台車都拿到 1。我把它改成 `self.vid = Vehicle.next_id`，並加上 `Vehicle.next_id += 1`，讀和改都統一用 `Vehicle.next_id`。改完之後三台車的編號變成 1、2、3。

### 最終程式

```python
class Vehicle:
    next_id = 1

    def __init__(self, plate, hours):
        self.plate = plate
        self.hours = hours
        self.vid = Vehicle.next_id
        Vehicle.next_id += 1

    def fee(self):
        return self.hours * 30

    def __str__(self):
        return f"#{self.vid} {self.plate}: {self.fee()}元"


class Motorcycle(Vehicle):
    def fee(self):
        return self.hours * 10


class Truck(Vehicle):
    def __init__(self, plate, hours, weight):
        Vehicle.__init__(self, plate, hours)
        self.weight = weight
    def fee(self):
        if self.weight > 10:
            return self.hours * 50 + 100
        else:
            return self.hours * 50


def total_fee(vehicles):
    total = 0
    for i in vehicles:
        total = total + i.fee()
    return total
```

## 5. Verification

- [x] Passed the provided examples
- [x] Passed additional edge cases
- [ ] Still has unresolved problems

另外測試的邊界情況：

| 測試 | 輸入 | 預期輸出 | 實際輸出 |
|---|---|---|---|
| 三種車混著建立，編號連續 | 依序建立汽車、機車、卡車、卡車、汽車 | 編號 1、2、3、4、5 | 1、2、3、4、5 |
| 物件身上沒有多出自己的 `next_id` | 上面五台車 | 沒有 | 沒有 |
| 汽車 1 小時 | `Vehicle("A", 1).fee()` | `30` | `30` |
| 機車 1 小時 | `Motorcycle("B", 1).fee()` | `10` | `10` |
| 卡車剛好 10 噸，不加錢 | `Truck("C", 1, 10).fee()` | `50` | `50` |
| 卡車 11 噸，加 100 | `Truck("D", 1, 11).fee()` | `150` | `150` |
| 汽車 5 小時 | `Vehicle("E", 5).fee()` | `150` | `150` |
| 卡車的 `__str__` | `print(Truck("D", 1, 11))`（第 4 台） | `#4 D: 150元` | `#4 D: 150元` |
| 空 list | `total_fee([])` | `0` | `0` |
| 只有一台機車 | `total_fee([機車 1 小時])` | `10` | `10` |
| 五台車加總 | `total_fee([上面五台])` | `390` | `390` |
| 卡車身上有父類別設定的資料 | `Truck("D", 1, 11)` 的 plate、hours、weight | `("D", 1, 11)` | `("D", 1, 11)` |

**One edge case I tested:**

- Input：`Truck("C", 1, 10).fee()`
- Expected output：`50`
- Actual output：`50`

題目說「超過」10 噸才加 100 元，所以條件用 `self.weight > 10`，剛好 10 噸不加錢。

### Why my solution works

`Vehicle` 的 `__init__` 用類別變數 `Vehicle.next_id` 發編號並往下跳，三種車都經過這段（`Truck` 透過 `Vehicle.__init__`），所以編號是共用、連續的。`__str__` 只寫在 `Vehicle`，但它呼叫的是 `self.fee()`，Python 會從物件自己的 class 開始找 `fee`，所以機車和卡車會用各自覆寫的版本。`total_fee` 也是同樣的道理：每台車呼叫 `i.fee()` 時都用自己的 `fee`，不需要判斷是哪一種車。

### Time complexity

每台車的 `fee()` 只做固定幾次計算，是 O(1)；`total_fee` 對 n 台車各呼叫一次，整體為 **O(n)**。

## 6. One-Minute Reflection

**What idea from the OCW lecture did you transfer to this new problem?**

繼承、覆寫和類別變數。照課堂 Animal → Rabbit 的架構，`Vehicle` 當父類別，`Motorcycle`、`Truck` 覆寫 `fee`；`Truck` 像 `Person` 一樣在自己的 `__init__` 呼叫父類別的 `__init__`；編號用 Rabbit 的 `tag` 號碼牌機的做法。

**One thing I understand better now:**

寫在父類別裡的方法呼叫 `self.fee()` 時，`self` 還是那台機車或卡車，所以會用子類別的版本，這就是 C++ `virtual` 在做的事，Python 預設就是這樣。另外，方法裡要用類別變數一定要寫 `Vehicle.next_id`，不能直接寫 `next_id`，改的時候也不能寫 `self.next_id`。

**One thing I am still unsure about:**

如果卡車想要有自己的 `__str__`，在原本的格式後面多印出重量，要怎麼重複使用 `Vehicle` 的 `__str__`，而不是整段重寫一次，我還不確定。
