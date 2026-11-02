#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <algorithm>
#include <cstddef>
#include <stdexcept>
#include <vector>

namespace py = pybind11;

// Task 1：加分，最高 100 分
double add_bonus(double score, double bonus) {
    // C1
    return std::min(100.0, score + bonus);
}

// Task 2：計算平均，空清單拋出例外
double average_scores(const std::vector<double>& scores) {
    if (scores.empty()) {
        // C2
        throw std::invalid_argument("scores cannot be empty");
    }

    double total = 0.0;
    for (double score : scores) {
        // C3
        total += score;
    }

    // C4
    return total / scores.size();
}

// Task 3：成績簿
class GradeBook {
public:
    void add(double score) {
        // C5
        scores_.push_back(score);
    }

    std::size_t count() const {
        // C6
        return scores_.size();
    }

    double average() const {
        // C7
        return average_scores(scores_);
    }

private:
    std::vector<double> scores_;
};

// 將 C++ 函式與類別公開給 Python
PYBIND11_MODULE(gradecpp, m) {
    m.doc() = "C++ grade analysis with pybind11";

    // C8
    m.def("add_bonus", &add_bonus);

    // C9
    m.def("average_scores", &average_scores);

    // C10
    py::class_<GradeBook>(m, "GradeBook")
        .def(py::init<>())
        .def("add", &GradeBook::add)
        .def("count", &GradeBook::count)
        .def("average", &GradeBook::average);
}