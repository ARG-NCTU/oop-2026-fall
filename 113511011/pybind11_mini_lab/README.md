# pybind11 Mini Lab：Python 呼叫 C++ 成績分析工具


## 這次要做什麼？

同一組「成績分析」小工具，分成 3 關：

| 關卡 | C++ 要完成 | Python 要完成 | 學到的 pybind11 觀念 |
|---|---|---|---|
| Task 1 | 加分函式、`m.def()` | 呼叫函式 | C++ 函式綁定 |
| Task 2 | `std::vector` 平均、`m.def()` | 傳入 `list` | Python list ↔ C++ vector |
| Task 3 | `GradeBook` 類別、`.def()` | 建立物件、呼叫方法 | C++ class 綁定 |

請依照程式中的 `TODO C1–C10`、`TODO P1–P7` 逐一填空。

## 0. 檔案結構

```text
pybind11_mini_lab/
├── grade.cpp     # C++ 演算法 + pybind11 綁定【要寫】
├── lab.py        # Python 呼叫與三關驗收【要寫】
└── README.md     # 這份說明
```

編譯後會多出一個 `gradecpp.cpython-xxx-...so`，它是自動產生的 **Python 擴充模組**，不必手寫。

## 1. 第一次安裝（Ubuntu / WSL 裡的終端機）

> 已有 Python、WSL 的同學直接在 **WSL Ubuntu** 操作；不要把下面的 Linux 指令輸入 Windows PowerShell。第一次安裝需要網路。

```bash
# 先確定 C++ 編譯工具、Python 開發標頭與虛擬環境齊全
sudo apt update
sudo apt install -y build-essential python3-dev python3-venv

# 在本 Lab 資料夾中執行（先用 cd 切到這裡）
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pybind11
```

每次**重新開 WSL 終端機**，只需要回到 Lab 資料夾並執行：

```bash
source .venv/bin/activate
```

檢查是否成功安裝：

```bash
python -m pybind11 --includes
```

成功時會印出 Python 與 pybind11 的 `-I...` 標頭檔路徑。

## 2. 編譯 C++ → Python 模組

先 `cd` 到 `grade.cpp` 所在資料夾，確認虛擬環境已啟用，貼上以下 **兩行**：

```bash
EXT=$(python -c 'import sysconfig; print(sysconfig.get_config_var("EXT_SUFFIX"))')
g++ -O2 -Wall -shared -std=c++17 -fPIC $(python -m pybind11 --includes) grade.cpp -o "gradecpp${EXT}"
```

> `PYBIND11_MODULE(gradecpp, m)` 的 `gradecpp`、產物的 `gradecpp*.so`、Python 的 `import gradecpp` **必須相同**。
>
> **每改一次 `grade.cpp` 都要重新執行編譯指令**；只改 `lab.py` 不需要重新編譯。

## 3. 執行 / 驗收

```bash
python lab.py
```

三關完成後應看到：

```text
[PASS] Task 1 / 基本函式
[PASS] Task 2 / list 與 vector
[PASS] Task 3 / C++ Class

結果：3/3 關通過
```

開始時看到 `FAIL` 是正常的：因為你還沒填完 TODO；請從 Task 1 依序完成。

## 4. Hint

- **Task 1：** `m.def("Python 的函式名稱", &C_plus_plus_函式名稱);`
- **Task 2：** 記得 `#include <pybind11/stl.h>`；C++ 的 `std::invalid_argument` 在 Python 端會轉為 `ValueError`。
- **Task 3：** `py::class_<GradeBook>(m, "GradeBook").def(py::init<>()).def("方法名稱", &GradeBook::方法名稱);`
- 在 Python 中，`gradecpp` 就像一般模組：可以使用 `gradecpp.add_bonus(...)`，也能使用 `gradecpp.GradeBook()`。

## 5. 最常見的錯誤

| 錯誤訊息 | 建議處理方式 |
|---|---|
| `No module named pybind11` | `source .venv/bin/activate` 再 `python -m pip install pybind11` |
| `Python.h: No such file or directory` | `sudo apt install python3-dev`；確認虛擬環境的 Python 版本與標頭相容 |
| `No module named gradecpp` | 確認 **已編譯** 且 `.so` 和 `lab.py` 在同一個資料夾；模組名稱都為 `gradecpp` |
| `AttributeError: module 'gradecpp' has no attribute ...` | 先完成對應 `m.def(...)` / `.def(...)`，並 **重新編譯** |
| 改了 C++，執行結果卻沒更新 | 重新執行第 2 節的兩行編譯指令 |

## 6. DEMO
給助教DEMO並回答助教的問題

---

官方參考：[pybind11 安裝](https://pybind11.readthedocs.io/en/stable/installing.html)｜[pybind11 手動編譯](https://pybind11.readthedocs.io/en/stable/compiling.html)｜[pybind11 基礎綁定](https://pybind11.readthedocs.io/en/stable/basics.html)
