// pybind11 Mini Lab — 學生版
// 題目：從 Python 呼叫 C++ 的成績分析工具
// 只要修改 TODO，請勿修改 PYBIND11_MODULE(gradecpp, m) 的模組名稱。

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>   // 讓 Python list 自動轉為 std::vector

#include <algorithm>
#include <cstddef>
#include <stdexcept>
#include <vector>

namespace py = pybind11;

// ──────────────────────────────────────────────
// Task 1：單一數值（Python float ↔ C++ double）
// 例如：add_bonus(78, 10) == 88
//       add_bonus(95, 10) == 100（最高 100 分）
// ──────────────────────────────────────────────
double add_bonus(double score, double bonus) {
    // TODO C1：回傳 score + bonus，但最高只能 100 分。
    // 提示：可用 std::min(100.0, score + bonus)
    return -1.0;  // ← 替換這一行
}

// ──────────────────────────────────────────────
// Task 2：Python list → C++ std::vector
// 例如：average_scores({60, 80, 100}) == 80
// 如果輸入空清單，應拋出 std::invalid_argument。
// ──────────────────────────────────────────────
double average_scores(const std::vector<double>& scores) {
    if (scores.empty()) {
        // TODO C2：拋出 std::invalid_argument("scores cannot be empty");
    }

    double total = 0.0;
    for (double score : scores) {
        // TODO C3：把 score 加進 total。
    }

    // TODO C4：回傳平均分數（total / scores.size()）。
    return -1.0;  // ← 替換這一行
}

// ──────────────────────────────────────────────
// Task 3：讓 Python 使用 C++ 類別
// ──────────────────────────────────────────────
class GradeBook {
public:
    void add(double score) {
        // TODO C5：把 score 存入 scores_。
    }

    std::size_t count() const {
        // TODO C6：回傳目前成績筆數。
        return 0;  // ← 替換這一行
    }

    double average() const {
        // TODO C7：重用上方的 average_scores(scores_)。
        return -1.0;  // ← 替換這一行
    }

private:
    std::vector<double> scores_;
};

// ──────────────────────────────────────────────
// pybind11 綁定：把 C++ 內容公開給 Python
// 注意：gradecpp 必須與編譯產生的模組檔名相同。
// ──────────────────────────────────────────────
PYBIND11_MODULE(gradecpp, m) {
    m.doc() = "C++ grade analysis with pybind11";

    // TODO C8：用 m.def(...) 匯出 add_bonus，Python 名稱也叫 add_bonus。

    // TODO C9：用 m.def(...) 匯出 average_scores，Python 名稱也叫 average_scores。

    py::class_<GradeBook>(m, "GradeBook")
        .def(py::init<>())
        // TODO C10：接著鏈結三個 .def(...)：
        //   Python 的 "add"     ↔ &GradeBook::add
        //   Python 的 "count"   ↔ &GradeBook::count
        //   Python 的 "average" ↔ &GradeBook::average
        ;
}
