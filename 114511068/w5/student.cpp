// student.cpp — 只改這個檔案。每個 TODO 大約 1~3 行。
// 做每個 TODO 之前，先讀 GUIDE.md 對應的那一節。
// 改完後在終端機執行：make check
#include "lab.h"

// ====================================================================
// TODO 1：參考（GUIDE.md 第 1 節）
// 把 v 夾在 lo 與 hi 之間：v < lo 就變成 lo，v > hi 就變成 hi，其他不動。
// ====================================================================
void clamp_value(double &v, double lo, double hi) {
  if (v < lo)
        v = lo;
    else if (v > hi)
        v = hi;
}

// ====================================================================
// TODO 2：封裝與建構子（GUIDE.md 第 2 節）
// (a) 建構子：用初始化清單把 m_level 設成 level
// (b) setLevel：level 不在 0 ~ 100 之間就回傳 false，而且不能改 m_level；
//               否則設定 m_level 並回傳 true
// ====================================================================
Battery::Battery(double level) :  m_level(level) {}

bool Battery::setLevel(double level) {
  if (level < 0 || level > 100)
    {
        return false;
    }
    m_level = level;
    return true;
}

double Battery::getLevel() const {
  return m_level;
}

// ====================================================================
// TODO 3：繼承與 virtual（GUIDE.md 第 3 節）
// 把下面的 MyApp 取消註解，補完三個 ???，再把 make_app() 的 return nullptr 改成 return new MyApp;
// ====================================================================

class MyApp : public BaseApp {
 public:
  std::string Name() const override { return"MyApp"; }
  bool Iterate() override { ++m_count; return true; }
  int Count() const override { return m_count; }

 private:
  int m_count = 0;
};

BaseApp *make_app() {
  return new MyApp;  // TODO
}

// ====================================================================
// TODO 4：new 與 delete（GUIDE.md 第 4 節）
// make_buffer(n)：配置 n 個 double，讓 p[i] 的值等於 i，回傳 p
// free_buffer(p)：釋放 p
// ====================================================================
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
