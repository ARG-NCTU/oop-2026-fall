# Lab 03: PyTest and Unit Test

本次 lab 會使用 VS Code 在 WSL 中撰寫 Python 程式，並使用 pytest 執行單元測試。這版不使用虛擬環境，也不需要提交 GitHub。流程很單純：在 VS Code 寫完 `.py` 檔案後，在 VS Code 下方 Terminal 執行 pytest，最後讓助教看到測試全部通過即可。

## 1. Lab 目標

完成本次 lab 後，你應該能夠：

- 在 WSL 中確認 Python3 與 pytest 可以使用。
- 使用 VS Code 開啟 WSL 專案資料夾。
- 說明 pytest 如何尋找測試檔與測試函式。
- 使用 `assert` 檢查函式輸出。
- 測試正常案例、邊界值與錯誤輸入。
- 看懂 pytest 的 pass、fail 與錯誤訊息。

## 2. 需要的工具

本次會用到：

- WSL Ubuntu。
- Python3。
- pytest。
- VS Code。
- VS Code 的 WSL 擴充功能。
- VS Code 的 Python 擴充功能。

## 3. 安裝 Python3 與 pytest

打開 Ubuntu 終端機，執行：

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-pytest
```

確認 Python3 可用：

```bash
python3 --version
```

確認 pytest 可用：

```bash
python3 -m pytest --version
```

這版 lab 不使用虛擬環境，所以後面執行測試時都用：

```bash
python3 -m pytest
```

## 4. 安裝與開啟 VS Code

如果 Windows 還沒有 VS Code，先下載並安裝：

<https://code.visualstudio.com/>

安裝後，請在 VS Code 的 Extensions 裡搜尋並安裝：

- WSL
- Python

接著在 Ubuntu 終端機建立 lab 資料夾：

```bash
mkdir -p ~/lab03-pytest
cd ~/lab03-pytest
code .
```

如果 `code .` 無法執行，請先確認 VS Code 已安裝 WSL 擴充功能，並重新開啟 Ubuntu 終端機後再試一次。

## 5. 本次操作流程

請照這個順序做：

1. 在 VS Code 新增 Python 檔案。
2. 在 VS Code 編輯程式碼。
3. 在 VS Code 下方 Terminal 執行 pytest。
4. 看 pytest 結果。
5. 修正程式或測試。
6. 再跑一次 pytest。
7. 全部通過後給助教看。

在 VS Code 裡打開 Terminal：

```text
Terminal > New Terminal
```

請確認 terminal 的路徑是在 lab 資料夾：

```bash
pwd
```

如果不是 `~/lab03-pytest`，請切換過去：

```bash
cd ~/lab03-pytest
```

## 6. pytest 會找什麼

pytest 會自動尋找符合規則的測試：

- 測試檔案通常以 `test_` 開頭，例如 `test_calculator.py`。
- 測試函式也要以 `test_` 開頭，例如 `test_add_two_numbers()`。
- 測試內通常使用 `assert` 檢查結果是否正確。

如果你執行 pytest 後看到：

```text
collected 0 items
```

通常代表檔名或函式名稱沒有符合 `test_` 規則。

## 7. 第一個被測試的程式

在 VS Code 新增 `calculator.py`：

```python
def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b
```

這個檔案是被測試的程式。

## 8. 第一個測試檔

在 VS Code 新增 `test_calculator.py`：

```python
import pytest

from calculator import add, divide


def test_add_two_positive_numbers():
    assert add(2, 3) == 5


def test_divide_two_numbers():
    assert divide(10, 2) == 5


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(10, 0)
```

這個檔案是測試檔。

## 9. 執行 pytest

在 VS Code 下方 Terminal 執行：

```bash
python3 -m pytest
```

如果想看更詳細的結果：

```bash
python3 -m pytest -v
```

你應該會看到類似：

```text
test_calculator.py::test_add_two_positive_numbers PASSED
test_calculator.py::test_divide_two_numbers PASSED
test_calculator.py::test_divide_by_zero_raises_error PASSED
```

## 10. assert 在做什麼

`assert` 的意思是：我期待這個條件成立。

例如：

```python
assert add(2, 3) == 5
```

如果 `add(2, 3)` 的結果是 `5`，測試通過。

如果結果不是 `5`，pytest 會標示 failed，並告訴你實際結果和預期結果不一樣。

## 11. 測試例外

如果你期待某個輸入會造成錯誤，可以使用 `pytest.raises`：

```python
def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(10, 0)
```

這段測試的意思是：

- 執行 `divide(10, 0)`。
- 期待它丟出 `ValueError`。
- 如果真的丟出 `ValueError`，測試通過。
- 如果沒有丟出錯誤，測試失敗。

## 12. 測試邊界值

寫測試時不要只測很普通的輸入，也要測容易出錯的位置。

例如成績轉換可能有這些邊界：

| 分數 | 預期 |
| --- | --- |
| 90 | A |
| 89 | B |
| 80 | B |
| 79 | C |
| 60 | D |
| 59 | F |

邊界值可以幫你確認判斷式有沒有寫錯。

## 13. 使用 parametrize 減少重複

如果很多組資料都測同一個規則，可以用 `pytest.mark.parametrize`：

```python
import pytest

from grade import letter_grade


@pytest.mark.parametrize(
    "score, expected",
    [
        (95, "A"),
        (80, "B"),
        (60, "D"),
        (59, "F"),
    ],
)
def test_letter_grade_valid_scores(score, expected):
    assert letter_grade(score) == expected
```

這樣一個測試函式可以跑多組資料。若某一組失敗，pytest 會指出是哪一組輸入造成問題。

## 14. 最後任務：成績轉換小工具

請在 VS Code 完成 `grade.py` 與 `test_grade.py`。

`grade.py` 需要提供兩個函式：

```python
def letter_grade(score):
    ...


def average(scores):
    ...
```

`letter_grade(score)` 的規則：

| 分數範圍 | 回傳 |
| --- | --- |
| 90 到 100 | `"A"` |
| 80 到 89 | `"B"` |
| 70 到 79 | `"C"` |
| 60 到 69 | `"D"` |
| 0 到 59 | `"F"` |

如果 `score` 小於 0 或大於 100，請丟出 `ValueError`。

`average(scores)` 的規則：

- 輸入是一個分數 list，例如 `[80, 90, 100]`。
- 回傳平均分數。
- 如果 list 是空的，請丟出 `ValueError`。

## 15. 測試項目

至少測以下內容：

```python
letter_grade(95) == "A"
letter_grade(80) == "B"
letter_grade(60) == "D"
letter_grade(59) == "F"
letter_grade(-1) raises ValueError
letter_grade(101) raises ValueError
average([80, 90, 100]) == 90
average([]) raises ValueError
```


## 17. 給助教檢查

最後請在 VS Code 下方 Terminal 執行：

```bash
python3 -m pytest -v
```

助教只需要看到所有測試都是 `PASSED` 即可。

本次不用提交 GitHub。

## 18. 常見問題

### python3: command not found

請重新安裝 Python3：

```bash
sudo apt update
sudo apt install -y python3
```

### No module named pytest

請安裝 pytest：

```bash
sudo apt install -y python3-pytest
```

### collected 0 items

請檢查：

- 測試檔名是否以 `test_` 開頭。
- 測試函式是否以 `test_` 開頭。
- 目前 terminal 是否在 lab 專案資料夾。

### ModuleNotFoundError

請檢查：

- `calculator.py` 和 `test_calculator.py` 是否在同一層資料夾。
- `grade.py` 和 `test_grade.py` 是否在同一層資料夾。
- 檔名是否拼錯。
