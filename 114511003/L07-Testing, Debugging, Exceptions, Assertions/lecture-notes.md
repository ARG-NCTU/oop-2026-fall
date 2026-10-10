# L7 - Testing, debugging, exceptions, and assertions

> 本講重點是：先把程式設計成容易測試，再用測試找出錯誤；遇到無法產生合法結果的情況時，用例外處理或 assertions 清楚地表達問題。

## 1. 本講在處理什麼問題？

寫完程式不代表程式正確。程式可能有三種問題：

1. **測試與驗證（testing / validation）**：檢查實際輸出是否符合規格。
2. **除錯（debugging）**：研究錯誤是怎麼發生的，找出原因並修正。
3. **防禦式程式設計（defensive programming）**：在程式中明確寫出假設，及早檢查輸入、輸出與資料狀態。

投影片用煮湯來比喻：

- 檢查湯裡有沒有蟲，對應 testing。
- 把鍋蓋蓋好，對應 defensive programming。
- 清理廚房、移除蟲的來源，對應消除 bug 的根因。

這三件事解決的是不同問題。測試可以告訴我們程式在哪些輸入下不符合規格，除錯則要繼續追查錯誤的來源。

## 2. 先把程式設計成容易測試

從一開始就要考慮測試和除錯：

- 把大程式拆成可以獨立測試的函式或模組。
- 為每個函式寫清楚輸入限制與輸出保證。
- 記錄程式設計時採用的假設。
- 讓函式有明確、可觀察的輸入與輸出，避免所有工作都混在一個大函式裡。

例如，與其寫一個同時讀檔、計算平均、格式化輸出的函式，不如拆成幾個小函式。這樣可以單獨測試「平均值計算」是否正確，而不必每次都準備完整檔案。

### 2.1 什麼時候可以開始測試？

至少要先做到：

- 移除 syntax errors，例如括號或引號沒有關閉。
- 移除 static semantic errors，例如變數名稱或運算子用錯。
- 準備一組預期結果，包括測試輸入，以及每個輸入應得到的輸出。

測試不是只執行程式然後看它有沒有當掉。程式能執行，只代表它通過目前這組執行路徑，不能證明輸出符合規格。

## 3. 測試的層次

### 3.1 Unit testing

逐一測試程式中的小單位，通常是每個函式。這種測試容易定位錯誤，因為失敗的範圍較小。

### 3.2 Regression testing

每次找到並修好一個 bug，就增加一個測試案例。以後修改其他程式碼時，這個測試可以檢查同一個錯誤是否又出現。

### 3.3 Integration testing

把多個函式或模組接在一起，檢查整體程式是否正常。這一步不能取代 unit testing，否則整體測試失敗時，會很難知道是哪個小單位出了問題。

建議的順序是：先測試每個函式，再進行整合測試。

## 4. 測試案例怎麼選？

測試案例不能只挑「看起來正常」的輸入。先根據函式規格找出問題空間中的自然分區，再從各分區選案例。

例如函式規格是：

```python
def is_bigger(x, y):
    """Assumes x and y are ints.
    Returns True if y is less than x, else False.
    """
```

可以考慮：

- `x > y`
- `x == y`
- `x < y`
- 負數與正數
- 兩個相同的負數

如果問題沒有明顯的分區，才可能使用隨機測試。但測試數量增加不等於測試品質一定足夠，仍然要思考邊界和規格中的特殊情況。

## 5. Black-box testing

Black-box testing 只根據函式的規格設計測試，不查看實作程式碼。這種方式的重點是檢查「函式對外承諾的行為」。

以平方根函式為例：

```python
def sqrt(x, eps):
    """Assumes x and eps are floats, x >= 0, eps > 0.
    Returns res such that x - eps <= res * res <= x + eps.
    """
```

可以設計以下測試：

| 類別 | `x` | `eps` | 想檢查的情況 |
| --- | ---: | ---: | --- |
| 邊界 | `0` | `0.0001` | 最小合法 `x` |
| 完全平方數 | `25` | `0.0001` | 結果應接近 `5` |
| 小於 1 | `0.05` | `0.0001` | 小數輸入 |
| 無理數平方根 | `2` | `0.0001` | 不能用有限小數精確表示 |
| 極小或極大值 | `2**64`、`2**-64` | 同樣範圍 | 數值極端情況 |

Black-box testing 的優點：

- 不受實作細節限制。
- 可以由沒有寫出原始程式的人設計，降低實作者的偏見。
- 實作改變時，規格測試通常仍然可以重用。

測試時要特別注意 boundary conditions，例如空 list、只有一個元素的 list、大數、小數、空字串，以及合法範圍的最小值和最大值。

## 6. Glass-box testing

Glass-box testing 直接查看程式碼，依照程式中的分支和迴圈設計測試。若每條可能的程式路徑都至少走過一次，稱為 path-complete test suite。

這種方法有兩個限制：

- 迴圈可能執行任意多次，路徑數量可能非常大。
- 即使走過所有程式分支，也可能漏掉規格中的邊界錯誤。

例如：

```python
def abs_value(x):
    """Assumes x is an int. Returns |x|."""
    if x < -1:
        return -x
    return x
```

用 `2` 和 `-2` 可以走過 `if` 的兩條路徑，但 `abs_value(-1)` 仍然錯誤，因為結果會是 `-1`。因此 glass-box testing 不能取代根據規格設計的 boundary tests。

設計 glass-box tests 時，至少要注意：

- `if` 的每個分支。
- `for` 迴圈執行 0 次、1 次和多次的情況。
- `while` 迴圈不進入、執行一次和正常結束的情況。
- 每個條件附近的邊界值。

## 7. 系統化除錯

除錯不是隨意修改程式直到它剛好通過目前測試。比較有效的方法是用科學方法縮小錯誤範圍：

1. 觀察可重現的錯誤。
2. 使用最簡單的輸入重現問題。
3. 提出一個關於錯誤原因的假設。
4. 設計可以驗證假設的實驗。
5. 根據結果修正假設，再重複測試。

與其問「哪裡壞了」，可以問：

- 我預期哪個結果？實際得到哪個結果？
- 錯誤第一次出現在哪一行或哪一個函式？
- 這個錯誤是否屬於某一類輸入？
- 最近一次改動是什麼？

### 7.1 使用 print statement 定位錯誤

在下列位置印出資訊：

- 進入函式時。
- 函式收到的參數。
- 函式即將回傳的結果。
- 重要條件判斷前後的變數值。

也可以用 bisection method。先在程式中間加入輸出，判斷錯誤發生在前半段還是後半段，再把範圍縮小。這比一次檢查整個程式更有效率。

### 7.2 常見的簡單錯誤

| 錯誤 | 常見原因 |
| --- | --- |
| `SyntaxError` | Python 無法解析程式，例如括號或引號未關閉 |
| `IndexError` | 使用超出 list 範圍的 index |
| `NameError` | 參考不存在的變數名稱 |
| `TypeError` | 物件型別不適合目前操作，例如用字串除以整數 |
| `ValueError` | 型別正確，但值不合法，例如把不適合的字串轉成整數 |
| `AttributeError` | 物件沒有被使用的 attribute |
| `IOError` | 輸入輸出系統發生問題，例如檔案不存在 |

Logic error 通常更難找，因為程式可以執行，也可能沒有拋出例外，只是計算結果錯誤。畫出資料變化、休息一下，或向別人逐行說明程式，都可能幫助找出假設錯誤。向 rubber duck 說明程式的做法，本質上是把隱藏在腦中的推理明確說出來。

## 8. Exceptions

當程式執行時遇到不符合預期的情況，Python 會產生 exception。例如：

```python
values = [1, 7, 4]
values[4]       # IndexError

int("hello")    # ValueError

unknown_name    # NameError

"a" / 4         # TypeError
```

如果函式無法產生符合規格的結果，應該清楚表示錯誤，而不是悄悄回傳一個看似正常的值。

### 8.1 `try` 和 `except`

```python
try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print(a / b)
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Can't divide by zero.")
```

`try` 區塊中的任何敘述發生對應例外時，Python 會跳到相應的 `except`。只寫空白的 `except:` 可以捕捉很多例外，但通常會掩蓋真正的程式錯誤。除非有明確理由，應該優先捕捉具體的例外型別。

### 8.2 `else` 和 `finally`

```python
try:
    result = compute()
except ValueError:
    handle_bad_value()
else:
    use(result)
finally:
    release_resources()
```

- `else` 只在 `try` 沒有發生例外時執行。
- `finally` 幾乎一定會執行，適合放清理工作，例如關閉檔案。
- 如果 `try`、`except` 或 `else` 中執行 `return`、`break` 或 `continue`，`finally` 仍會先執行。

## 9. `raise`：把錯誤交給呼叫者

處理錯誤有幾種政策：

1. 靜默忽略錯誤，繼續執行或使用預設值。這通常會讓使用者不知道資料已經不可靠。
2. 回傳特殊的 error value。這會要求每個呼叫者都檢查特殊值，也可能和正常資料混淆。
3. 直接拋出例外，讓呼叫者決定如何處理。

Python 可以用 `raise`：

```python
raise ValueError("input does not satisfy the function specification")
```

### 9.1 範例：計算兩個 list 的比值

```python
def get_ratios(left, right):
    """Assumes left and right are equal-length lists of numbers."""
    ratios = []
    for index in range(len(left)):
        try:
            ratios.append(left[index] / right[index])
        except ZeroDivisionError:
            ratios.append(float("nan"))
        except (TypeError, IndexError):
            raise ValueError("get_ratios called with bad arguments")
    return ratios
```

這裡對除以零採取明確政策，放入 `nan`。其他不符合輸入假設的情況則轉成 `ValueError`，讓呼叫者知道函式沒有拿到合法參數。

要注意，這段示範是課堂概念的簡化版。實務上也可以在函式開始時先檢查兩個 list 的長度和元素型別，讓錯誤更早被發現。

## 10. Worked example：處理沒有成績的學生

假設每位學生的資料是：

```python
[
    ["first name", "last name"],
    [assignment_grade_1, assignment_grade_2, ...],
]
```

我們想產生：姓名、原始成績，以及平均分數。

先寫出正常版本：

```python
def avg(grades):
    return sum(grades) / len(grades)


def get_stats(class_list):
    new_stats = []
    for student in class_list:
        new_stats.append([student[0], student[1], avg(student[1])])
    return new_stats
```

對一般輸入可以工作：

```python
class_list = [
    [["peter", "parker"], [80.0, 70.0, 85.0]],
    [["bruce", "wayne"], [100.0, 80.0, 74.0]],
]
```

但是，如果資料包含：

```python
[["deadpool"], []]
```

`len(grades)` 是 0，`sum(grades) / len(grades)` 會產生 `ZeroDivisionError`。這不是單純的 Python 細節，而是需要先決定的資料政策。沒有成績時，平均分數應該是什麼？

### 10.1 政策 A：警告並回傳 `None`

```python
def avg(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        print("warning: no grades data")
        return None
```

這表示「平均分數不存在」。後續程式必須能正確處理 `None`。

### 10.2 政策 B：警告並把平均分數定為 0

```python
def avg(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        print("warning: no grades data")
        return 0.0
```

這表示「沒有成績的學生按照 0 分計算」。這是業務規則，不是例外處理本身自動決定的結果。不同需求可能需要不同政策。

### 10.3 若空 list 是程式錯誤，使用 assertion

```python
def avg(grades):
    assert len(grades) != 0, "no grades data"
    return sum(grades) / len(grades)
```

這個版本不把空 list 當成可正常處理的資料，而是立即停止並指出違反的假設。

## 11. Assertions

Assertion 用來檢查程式設計者認為「此時一定成立」的條件：

```python
assert condition, "message shown when condition is false"
```

如果 `condition` 是 `False`，Python 會產生 `AssertionError`。例如：

```python
def avg(grades):
    assert len(grades) != 0, "no grades data"
    return sum(grades) / len(grades)
```

### 11.1 Assertions 適合檢查什麼？

- 參數的型別或數值限制。
- 資料結構的不變量，例如 list 必須沒有重複值。
- 函式輸出的限制。
- 程序執行過程中應該持續成立的條件。

Assertions 的目標是讓 bug 在剛出現的位置停下來，並留下較清楚的錯誤位置。它們可以檢查輸入，也可以檢查輸出，避免錯誤值繼續傳到其他函式。

### 11.2 Exception 和 assertion 的差別

| 工具 | 適合表達的情況 | 典型做法 |
| --- | --- | --- |
| `raise` / `try` / `except` | 使用者可能提供不合法資料，且程式有可選的處理方式 | 捕捉、顯示訊息、重試或交給呼叫者 |
| `assert` | 程式內部的假設被破壞，通常代表 bug | 立即停止，保留錯誤位置 |

不要用 assertion 取代所有輸入驗證。使用者輸入錯誤通常是可預期的情況，應該使用明確的例外型別和適當的錯誤訊息處理。

## 12. 建議的開發流程

可以用以下循環處理一個新功能：

1. 寫出函式規格和輸入限制。
2. 先列出正常案例、邊界案例與預期失敗案例。
3. 寫一個小函式。
4. 做 unit testing。
5. 發現 bug 時，把它加入 regression tests。
6. 用最小輸入重現問題，觀察錯誤第一次出現的位置。
7. 修正根因，再跑完整測試。
8. 多個函式都通過後，才做 integration testing。

不要等到整個程式寫完才第一次測試。也不要修改程式後忘記記錄改了什麼，否則下一次失敗時很難比較新舊版本。

## 13. 常見錯誤

1. 只測試正常輸入，沒有測試空值、極端值和邊界值。
2. 只做 integration testing，沒有先做 unit testing。
3. 看到例外就用空白的 `except:` 把它吞掉。
4. 以特殊回傳值代表錯誤，卻沒有要求每個呼叫者檢查它。
5. 把使用者輸入錯誤和程式內部 bug 混用同一種處理方式。
6. 以為 path-complete 就代表測試完整，忽略規格中的邊界案例。
7. 使用 assertion 代替所有正式的輸入驗證。
8. 修改程式直到某次測試通過，卻沒有先提出可驗證的錯誤假設。

## 14. Self-check

先不要看答案，自己寫出理由：

1. Unit testing、regression testing 和 integration testing 各自要回答什麼問題？
2. 為什麼 `abs_value(2)` 和 `abs_value(-2)` 的 path-complete 測試仍可能漏掉 `abs_value(-1)` 的錯誤？
3. 什麼時候應該用 `raise ValueError(...)`，什麼時候比較適合用 `assert`？
4. `try`、`except`、`else`、`finally` 的執行條件各是什麼？
5. 如果沒有成績的學生應該顯示「沒有資料」，而不是得到 0 分，`avg([])` 應該採用什麼政策？
6. 請為一個「計算 list 平均值」的函式列出至少四個測試案例，包含一個預期失敗案例。

### 參考答案

1. Unit testing 測試單一函式或模組；regression testing 確認已修好的 bug 沒有重現；integration testing 檢查組合後的整體行為。
2. 因為條件 `x < -1` 的分支雖然被走過，但 `-1` 正好位於錯誤邊界，規格測試仍需要另外測試它。
3. `raise` 適合把可處理的非法輸入或失敗狀況通知呼叫者；`assert` 適合檢查程式內部應該成立、若不成立通常代表 bug 的假設。
4. `try` 先執行；發生對應例外時進入 `except`；沒有例外時執行 `else`；`finally` 在最後執行，用於一定要完成的清理工作。
5. 回傳 `None` 並顯示警告，或直接拋出明確的例外，取決於呼叫者是否能處理「沒有資料」。重點是先明確定義政策，而不是讓 `ZeroDivisionError` 意外決定結果。
6. 例如 `[1, 2, 3] -> 2.0`、`[5] -> 5.0`、`[0, 0] -> 0.0`、`[] -> 預期拋出 ValueError 或 AssertionError`。實際選哪種例外要和函式規格一致。

## 15. 來源與範圍

本筆記根據 MIT OpenCourseWare 6.0001 Fall 2016 Lecture 7 的投影片與課程頁面整理。投影片中的課堂提示，例如下載程式檔案跟著做，屬於原課程的學習建議，不是本 repository 自動新增的作業要求。

- MIT OCW 課程頁面：<https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-7-testing-debugging-exceptions-and-assertions/>
- 本地講義：`L7-Testing, Debugging, Exceptions, and Assertions .pdf`
