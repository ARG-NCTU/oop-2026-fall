#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <cstdint>
#include <stdexcept>
#include <vector>

namespace py = pybind11;

class CargoLoader {
public:
    explicit CargoLoader(std::int64_t capacity) : capacity_(capacity) {
        if (capacity < 1 || capacity > 1000000000000LL)
            throw std::invalid_argument("capacity must be in [1, 10^12]");
    }

    std::vector<std::size_t> add_batch(const std::vector<std::int64_t>& weights) {
        // Validate the whole batch before changing object state.
        if (weights.size() > 100000)
            throw std::invalid_argument("batch is too large");
        for (auto weight : weights) {
            if (weight < 1 || weight > 1000000000000LL)
                throw std::invalid_argument("weight must be in [1, 10^12]");
        }
        std::vector<std::size_t> accepted;
        accepted.reserve(weights.size());
        for (std::size_t i = 0; i < weights.size(); ++i) {
            if (weights[i] <= capacity_ - load_) {
                load_ += weights[i];
                ++count_;
                accepted.push_back(i);
            }
        }
        return accepted;
    }

    std::int64_t load() const { return load_; }
    std::int64_t remaining() const { return capacity_ - load_; }
    std::size_t count() const { return count_; }
    void clear() { load_ = 0; count_ = 0; }

private:
    std::int64_t capacity_;
    std::int64_t load_ = 0;
    std::size_t count_ = 0;
};

PYBIND11_MODULE(cargocpp, m) {
    py::class_<CargoLoader>(m, "CargoLoader")
        .def(py::init<std::int64_t>())
        .def("add_batch", &CargoLoader::add_batch)
        .def("load", &CargoLoader::load)
        .def("remaining", &CargoLoader::remaining)
        .def("count", &CargoLoader::count)
        .def("clear", &CargoLoader::clear);
}
