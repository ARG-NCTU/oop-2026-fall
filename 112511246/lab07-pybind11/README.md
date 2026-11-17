# Lab07：pybind11 成績分析工具

用 pybind11 把 C++ 寫的函式和類別編譯成 Python 模組 `gradecpp`，再從 Python 呼叫。

## 三個任務

| 任務 | C++（`grade.cpp`） | Python（`lab.py`） |
|---|---|---|
| Task 1：加分 | `add_bonus(score, bonus)`，用 `std::min(100.0, score + bonus)` 限制最高 100 分 | `add_bonus(78, 10)` → 88、`add_bonus(95, 10)` → 100 |
| Task 2：平均 | `average_scores(scores)`，加總後除以筆數；空的就 `throw std::invalid_argument` | 傳入 list `[60, 80, 100]` → 80；傳入空 list 會變成 `ValueError` |
| Task 3：成績簿 | `GradeBook` 類別，用 `std::vector<double>` 存成績，提供 `add()`、`count()`、`average()` | 建立物件、加入三筆成績、查詢筆數和平均 |

## 重點

| 寫法 | 作用 |
|---|---|
| `m.def("add_bonus", &add_bonus)` | 把 C++ 函式公開給 Python，Python 端名稱也叫 `add_bonus` |
| `#include <pybind11/stl.h>` | 讓 Python 的 list 自動轉成 C++ 的 `std::vector` |
| `py::class_<GradeBook>(m, "GradeBook")` | 把 C++ 類別公開給 Python |
| `.def(py::init<>())` | 讓 Python 可以用 `GradeBook()` 建立物件 |
| `.def("add", &GradeBook::add)` | 把類別的方法一個一個公開 |
| `std::invalid_argument` | pybind11 會自動轉成 Python 的 `ValueError`，所以 Python 端可以用 `except ValueError` 接住 |

`GradeBook::average()` 直接重用 `average_scores(scores_)`，空的成績簿也會丟出同樣的例外。

## 編譯與執行（macOS）

```bash
python -m venv .venv
source .venv/bin/activate
pip install pybind11
EXT=$(python -c "import sysconfig; print(sysconfig.get_config_var('EXT_SUFFIX'))")
c++ -O2 -Wall -shared -std=c++17 -fPIC -undefined dynamic_lookup \
    $(python -m pybind11 --includes) grade.cpp -o "gradecpp${EXT}"
python lab.py
```

macOS 要多加 `-undefined dynamic_lookup`，讓 Python 的符號在載入模組時才去找，否則連結時會出錯。編譯出來的 `.so` 檔不上傳。

## 結果

```text
[PASS] Task 1 / 基本函式
[PASS] Task 2 / list 與 vector
[PASS] Task 3 / C++ Class

結果：3/3 關通過
```
