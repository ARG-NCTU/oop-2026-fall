# Lab03：Pytest 與單元測試

本實驗使用 pytest 檢查 Python 函式，練習以 `assert` 驗證結果、以 `pytest.raises` 驗證例外，並透過參數化測試涵蓋多組輸入與成績級距的邊界值。

> 整理來源：課程提供的 `Lab03_PyTest.pptx`

## 學習目標

- 了解單元測試如何檢查一小段功能。
- 掌握 pytest 的測試檔與測試函式命名規則。
- 測試正常結果、邊界值與預期例外。
- 使用 `@pytest.mark.parametrize` 減少重複測試程式碼。
- 閱讀測試結果，定位失敗案例。

## 教材任務與實作範圍

教材先以 `calculator.py` 練習加法測試及除以零的例外測試，最後要求完成 `grade.py` 與 `test_grade.py`。

| 函式 | 功能 | 例外規則 |
|---|---|---|
| `add(a, b)` | 計算兩數和 | 教材未另訂規則 |
| `divide(a, b)` | 計算兩數相除 | 除數為零時拋出 `ValueError`，配合教材範例 |
| `letter_grade(score)` | 將分數轉為 A、B、C、D、F | 分數不在 0～100 時拋出 `ValueError` |
| `average(scores)` | 計算數值 list 的算術平均 | 空 list 時拋出 `ValueError` |

`average()` 依教材明示的空 list 規則實作，假設元素為數值；本版沒有額外要求每個元素都在 0～100，也沒有擴充字串輸入的轉換功能。

## 檔案結構

依教材建議，函式與測試檔放在同一個資料夾：

```text
lab03/
├── README.md
├── .gitignore
├── requirements.txt
├── calculator.py
├── test_calculator.py
├── grade.py
└── test_grade.py
```

教材投影片未附在此資料夾中。`.gitignore` 排除 Python 快取、pytest 快取與虛擬環境。

## 環境與執行方式

需求為 Python 3.10 以上；`requirements.txt` 固定使用本次驗證的 pytest 9.2.0。

進入 `lab03` 資料夾後執行：

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

若環境使用 `python3`，將以上指令中的 `python` 改為 `python3`。建議使用同一個 Python 執行安裝與測試，避免套件安裝到其他環境。

### 常用指令

```bash
python -m pytest --collect-only -q       # 只列出收集到的測試
python -m pytest -v                      # 執行全部測試並顯示案例名稱
python -m pytest test_grade.py -v        # 只執行成績測試
python -m pytest -q                      # 精簡結果
```

請在本資料夾執行，避免把其他 Lab 的檔案一起納入測試。

## 單元測試的寫法

### 1. 用 assert 檢查結果

```python
from calculator import add

def test_add_two_numbers():
    assert add(2, 3) == 5
```

測試檔以 `test_` 開頭，函式也以 `test_` 開頭，pytest 就能自動找到本專案的測試。若收集不到案例，可先檢查命名、所在資料夾與匯入是否正確。

### 2. 用 pytest.raises 檢查例外

```python
import pytest
from calculator import divide

def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(10, 0)
```

此測試預期函式拋出 `ValueError`。若沒有拋出，或拋出其他類型的例外，測試就會失敗。Python 直接計算 `10 / 0` 會拋出 `ZeroDivisionError`，因此本版 `divide()` 依教材約定先檢查除數，再明確拋出 `ValueError`。

### 3. 用參數化測試檢查多組資料

```python
@pytest.mark.parametrize(
    "score, expected",
    [(90, "A"), (89, "B"), (60, "D"), (59, "F")],
)
def test_letter_grade_boundaries(score, expected):
    assert letter_grade(score) == expected
```

每一組資料都會獨立成為一個測試案例，方便辨識哪個分數的判斷出了問題。完整測試也涵蓋其他級距與合法範圍的兩端。

## 成績級距與邊界值

依教材的級距邊界整理如下；比較條件也適用於數值小數分數：

| 分數範圍 | 等第 |
|---|---|
| `90 <= score <= 100` | A |
| `80 <= score < 90` | B |
| `70 <= score < 80` | C |
| `60 <= score < 70` | D |
| `0 <= score < 60` | F |
| 小於 0 或大於 100 | `ValueError` |

邊界測試包含 `90/89`、`80/79`、`70/69`、`60/59`，以及 `0`、`100`、`-1`、`101`。這些案例可抓出把 `>=` 誤寫為 `>`，或級距順序錯誤等問題。

平均值與除法可能產生浮點數，因此相關測試使用 `pytest.approx()` 比較結果，允許合理的浮點誤差。

## 測試涵蓋內容

| 測試項目 | 案例數 |
|---|---:|
| 加法：一般值、負數、零 | 3 |
| 除法：一般值、小數結果、負數、零被除數 | 4 |
| 除以零 | 1 |
| 一般成績 | 5 |
| 成績邊界值 | 10 |
| 非法成績 `-1`、`101` | 2 |
| 平均值：多筆、單筆、範圍兩端、全零、小數結果 | 5 |
| 空 list | 1 |
| **合計** | **31** |

## 結果判讀

- `PASSED`：該案例符合預期。
- `FAILED`：測試階段的斷言不成立，或出現未預期的例外等失敗情況。
- `ERROR`：常見於測試收集、匯入或測試準備／清理階段發生錯誤。

看到錯誤時，先讀測試名稱，再檢查失敗行、實際值與預期值，修正後重新執行。

## 本次驗證紀錄

本次在 Windows、Python 3.12.14、pytest 9.2.0 環境執行完整測試，成功收集 31 個案例，全部通過：

```text
collected 31 items
31 passed
```

## 學習重點整理

測試案例應同時包含一般輸入、容易判斷錯的邊界值，以及應該拋出例外的輸入。測試通過表示程式符合目前案例的預期；仍需檢查案例是否涵蓋需求，才能避免漏測。
