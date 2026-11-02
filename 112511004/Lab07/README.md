# LAB07：pybind11 成績分析工具

本 Lab 使用 pybind11 將 C++ 函式與類別編譯成 Python 擴充模組，讓 Python 可以呼叫 C++ 實作的成績分析功能。三個任務涵蓋函式綁定、Python list 與 C++ vector 的轉換，以及 C++ 類別綁定。

## 功能與實作

| 任務 | C++ 實作 | Python 呼叫與驗收 | 對應 TODO |
| --- | --- | --- | --- |
| Task 1：加分 | `add_bonus(score, bonus)` 回傳加分結果，最高為 100 分 | 驗證一般加分與超過上限的情況 | C1、C8；P1–P2 |
| Task 2：平均分數 | `average_scores(scores)` 加總並計算平均，空清單拋出例外 | 傳入 list，驗證平均與空清單例外 | C2–C4、C9；P3–P4 |
| Task 3：成績簿 | `GradeBook` 儲存成績，提供 `add()`、`count()`、`average()` | 建立物件、加入三筆成績並查詢結果 | C5–C7、C10；P5–P7 |

### Task 1：加分函式

使用 `std::min(100.0, score + bonus)` 限制結果最高為 100 分，再透過 `m.def()` 公開給 Python。

```python
gradecpp.add_bonus(78, 10)  # 88.0
gradecpp.add_bonus(95, 10)  # 100.0
```

此函式只限制最高分數，沒有額外設定最低分數。

### Task 2：平均分數與例外處理

Python list 透過 `pybind11/stl.h` 轉成 `std::vector<double>`。C++ 將成績加總後除以筆數，回傳平均值。

```python
gradecpp.average_scores([60, 80, 100])  # 80.0
gradecpp.average_scores([70, 90])       # 80.0
```

輸入空清單時，C++ 拋出 `std::invalid_argument("scores cannot be empty")`，pybind11 會將其轉為 Python 的 `ValueError`。

### Task 3：GradeBook 類別

`GradeBook` 使用私有的 `std::vector<double>` 儲存成績：

- `add(score)`：使用 `push_back()` 新增一筆成績。
- `count()`：使用 `size()` 回傳成績筆數。
- `average()`：重用 `average_scores()` 計算平均。

使用 `py::class_` 綁定類別，並公開無參數建構子與上述三個方法。

```python
book = gradecpp.GradeBook()
book.add(60)
book.add(80)
book.add(100)

print(book.count())    # 3
print(book.average())  # 80.0
```

若尚未新增成績就呼叫 `average()`，也會因為空清單而觸發 `ValueError`。

## 檔案結構

```text
LAB07/
├── grade.cpp       # C++ 函式、類別與 pybind11 綁定
├── lab.py          # Python 呼叫與三個任務的驗收程式
└── README.md       # 專案說明
```

安裝與編譯後還會產生 `.venv/` 虛擬環境，以及 `gradecpp*.so` 擴充模組。

## 環境需求

- WSL Ubuntu 或本機 Ubuntu
- Python 3
- 支援 C++17 的 g++ 編譯器
- Python 開發標頭與 venv 套件
- pybind11

以下指令請在 Ubuntu 終端機執行。

## 安裝方式

先下載專案檔案，並在終端機切換到 `grade.cpp` 與 `lab.py` 所在的資料夾。若從 WSL 使用 Windows C 槽的檔案，路徑會以 `/mnt/c/` 開頭；路徑含有空格時，請用雙引號包住整段路徑。

安裝系統套件：

```bash
sudo apt update
sudo apt install -y build-essential python3-dev python3-venv
```

在 Lab 資料夾建立並啟用虛擬環境，再安裝 pybind11：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pybind11
```

每次重新開啟終端機後，回到 Lab 資料夾並執行 `source .venv/bin/activate`，即可再次使用此環境。

## 編譯 C++ 模組

確認虛擬環境已啟用，且目前位於 `grade.cpp` 所在的資料夾，執行：

```bash
PYBIND_HEADER_DIR=$(python -c 'import pybind11; print(pybind11.get_include())')
PYTHON_HEADER_DIR=$(python -c 'import sysconfig; print(sysconfig.get_path("include"))')
EXT=$(python -c 'import sysconfig; print(sysconfig.get_config_var("EXT_SUFFIX"))')

g++ -O2 -Wall -shared -std=c++17 -fPIC \
  -I"$PYBIND_HEADER_DIR" \
  -I"$PYTHON_HEADER_DIR" \
  grade.cpp -o "gradecpp${EXT}"
```

這個指令將標頭路徑加上雙引號，可處理專案資料夾名稱含有空格的情況。編譯成功後會產生 `gradecpp*.so`，完整檔名會依 Python 版本與平台而不同。

模組名稱必須一致：C++ 使用 `PYBIND11_MODULE(gradecpp, m)`，編譯產物以 `gradecpp` 開頭，Python 則使用 `import gradecpp`。

每次修改 `grade.cpp` 後都需要重新編譯。若只修改 `lab.py`，重新執行 Python 即可。

## 執行與驗收結果

編譯成功後，在同一個資料夾執行：

```bash
python lab.py
```

本次已在本機 WSL 環境執行，三個任務全部通過：

```text
[PASS] Task 1 / 基本函式
[PASS] Task 2 / list 與 vector
[PASS] Task 3 / C++ Class

結果：3/3 關通過
```

驗收涵蓋：

| 測試項目 | 預期結果 |
| --- | --- |
| `add_bonus(78, 10)` | 88 |
| `add_bonus(95, 10)` | 100 |
| `average_scores([60, 80, 100])` | 80 |
| `average_scores([70, 90])` | 80 |
| `average_scores([])` | 拋出 `ValueError` |
| 新增 60、80、100 後呼叫 `book.count()` | 3 |
| 新增 60、80、100 後呼叫 `book.average()` | 80 |

`lab.py` 使用 `assert` 檢查結果，並捕捉空清單的 `ValueError`。若任一任務失敗，程式會以退出碼 1 結束。

## 遇到的問題與解決方式

| 問題 | 原因與處理方式 |
| --- | --- |
| `cd: too many arguments` | 路徑含有空格。WSL 路徑應使用 `/`，並以雙引號包住整段路徑。 |
| `pybind11/pybind11.h: No such file or directory` | 本次因專案路徑含有空格，編譯時的標頭路徑被拆開。改用上方將 `-I` 路徑加上引號的編譯指令。 |
| `No module named gradecpp` | 本次因 C++ 編譯失敗而未產生模組。先成功編譯，並確認 `.so` 與 `lab.py` 位於同一個資料夾。 |
| 測試顯示「實際 None」 | Python 的 TODO 還留著 `None`。補上 C++ 函式呼叫、物件建立與方法呼叫，儲存後重新執行。 |
| `No module named pybind11` | 確認已啟用 `.venv`，並在該環境執行 `python -m pip install pybind11`。 |
| 修改 C++ 後結果未更新 | 重新編譯 `grade.cpp`，再執行 `python lab.py`。 |

## 學習重點

- 使用 `m.def()` 將 C++ 函式公開給 Python。
- 使用 `pybind11/stl.h` 轉換 Python list 與 C++ vector；此轉換涉及資料複製，`const &` 不會消除跨語言轉換的複製成本。
- 理解 C++ `std::invalid_argument` 與 Python `ValueError` 的對應。
- 使用 `py::class_` 公開 C++ 類別、建構子與成員方法。
- 區分 C++ 原始碼、編譯後的擴充模組與 Python 呼叫程式之間的關係。

## 原始教材

本 Lab 依據 [ARG-NCTU / pybind11_mini_lab](https://github.com/ARG-NCTU/pybind11_mini_lab) 完成。
