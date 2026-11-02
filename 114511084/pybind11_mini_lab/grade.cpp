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
    return std::min(100.0, score + bonus);
}

// ──────────────────────────────────────────────
// Task 2：Python list → C++ std::vector
// 例如：average_scores({60, 80, 100}) == 80
// 如果輸入空清單，應拋出 std::invalid_argument。
// ──────────────────────────────────────────────
double average_scores(const std::vector<double>& scores) {
    if (scores.empty()) {
        throw std::invalid_argument("scores cannot be empty");
    }

    double total = 0.0;
    for (double score : scores) {
        total += score;
    }

    return total / scores.size();
}

// ──────────────────────────────────────────────
// Task 3：讓 Python 使用 C++ 類別
// ──────────────────────────────────────────────
class GradeBook {
public:
    void add(double score) {
        scores_.push_back(score);
    }

    std::size_t count() const {
        return scores_.size();
    }

    double average() const {
        return average_scores(scores_);
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

    m.def("add_bonus", &add_bonus);

    m.def("average_scores", &average_scores);

    py::class_<GradeBook>(m, "GradeBook")
        .def(py::init<>())
        .def("add", &GradeBook::add)
        .def("count", &GradeBook::count)
        .def("average", &GradeBook::average);
}
