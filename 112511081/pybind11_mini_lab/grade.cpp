// pybind11 Mini Lab
// 題目：從 Python 呼叫 C++ 的成績分析工具

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>   // Python list <-> std::vector 轉換

#include <algorithm>
#include <cstddef>
#include <stdexcept>
#include <vector>

namespace py = pybind11;

// Task 1：加分，最高 100 分 (C1)
double add_bonus(double score, double bonus) {
    return std::min(100.0, score + bonus);
}

// Task 2：計算平均 (C2-C4)
double average_scores(const std::vector<double>& scores) {
    if (scores.empty()) {                                   // C2
        throw std::invalid_argument("scores cannot be empty");
    }
    double total = 0.0;                                     // C3
    for (double s : scores) {
        total += s;
    }
    return total / static_cast<double>(scores.size());      // C4
}

// Task 3：GradeBook 類別 (C5-C7)
class GradeBook {
public:
    void add(double score) { scores_.push_back(score); }        // C5
    std::size_t count() const { return scores_.size(); }        // C6
    double average() const { return average_scores(scores_); }  // C7

private:
    std::vector<double> scores_;
};

// pybind11 綁定 (C8-C10)
PYBIND11_MODULE(gradecpp, m) {
    m.doc() = "C++ grade analysis with pybind11";

    m.def("add_bonus", &add_bonus);                 // C8
    m.def("average_scores", &average_scores);       // C9

    py::class_<GradeBook>(m, "GradeBook")           // C10
        .def(py::init<>())
        .def("add", &GradeBook::add)
        .def("count", &GradeBook::count)
        .def("average", &GradeBook::average);
}
