// student.cpp
#include "lab.h"

// ============================================================
// TODO 1：參考
// ============================================================

void clamp_value(double &v, double lo, double hi) {
    if (v < lo)
        v = lo;
    else if (v > hi)
        v = hi;
}


// ============================================================
// TODO 2：封裝與建構子
// ============================================================

Battery::Battery(double level) : m_level(level) {}

bool Battery::setLevel(double level) {
    if (level < 0 || level > 100)
        return false;

    m_level = level;
    return true;
}

double Battery::getLevel() const {
    return m_level;
}


// ============================================================
// TODO 3：繼承與 virtual
// ============================================================

class MyApp : public BaseApp {
public:
    MyApp() : m_count(0) {}

    std::string Name() const override {
        return "MyApp";
    }

    bool Iterate() override {
        m_count++;
        return true;
    }

    int Count() const override {
        return m_count;
    }

private:
    int m_count;
};

BaseApp *make_app() {
    return new MyApp;
}


// ============================================================
// TODO 4：new 與 delete
// ============================================================

double *make_buffer(int n) {
    double *p = new double[n];

    for (int i = 0; i < n; i++) {
        p[i] = i;
    }

    return p;
}

void free_buffer(double *p) {
    delete[] p;
}
