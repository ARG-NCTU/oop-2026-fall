// Lab04 supplemental examples, written while organizing the course record.
// Topics: pointers, references, encapsulation, polymorphism and ownership.
#include <cstddef>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>

namespace {

void require(bool condition, const char* message) {
    if (!condition) {
        throw std::runtime_error(message);
    }
}

void increment_by_value(int value) {
    ++value;  // Only the local copy changes.
}

void increment_by_pointer(int* value) {
    if (value != nullptr) {
        ++(*value);
    }
}

void increment_by_reference(int& value) {
    ++value;
}

class Battery {
public:
    explicit Battery(double level) : level_(level) {
        if (!(level >= 0 && level <= 100)) {
            throw std::out_of_range("battery level must be between 0 and 100");
        }
    }

    bool set_level(double level) {
        if (!(level >= 0 && level <= 100)) {
            return false;
        }
        level_ = level;
        return true;
    }

    double level() const {
        return level_;
    }

private:
    double level_;
};

class BaseApp {
public:
    BaseApp() {
        std::cout << "  BaseApp constructed\n";
    }

    virtual ~BaseApp() {
        std::cout << "  BaseApp destroyed\n";
    }

    virtual std::string name() const = 0;
    virtual void iterate() = 0;
    virtual int count() const = 0;
};

class MyApp : public BaseApp {
public:
    MyApp() : count_(0) {
        std::cout << "  MyApp constructed\n";
    }

    ~MyApp() override {
        std::cout << "  MyApp destroyed\n";
    }

    std::string name() const override {
        return "MyApp";
    }

    void iterate() override {
        ++count_;
    }

    int count() const override {
        return count_;
    }

private:
    int count_;
};

void demo_parameters() {
