// lab.h — 介面宣告（老師提供，學生請勿修改）
#ifndef LAB_H
#define LAB_H

#include <string>

// ---- 第 1 項：參考 ----
void clamp_value(double &v, double lo, double hi);

// ---- 第 2 項：封裝與建構子 ----
class Battery {
 public:
  Battery(double level);
  bool setLevel(double level);
  double getLevel() const;

 private:
  double m_level;
};

// ---- 第 3 項：繼承與 virtual ----
// 這個基底類別的形狀仿照 MOOS 的 CMOOSApp：
// 框架只認得基底類別，由它透過指標呼叫你覆寫的 Iterate()。
class BaseApp {
 public:
  virtual ~BaseApp() {}
  virtual std::string Name() const = 0;
  virtual bool Iterate() = 0;
  virtual int Count() const = 0;
};

BaseApp *make_app();

// ---- 第 4 項：new / delete ----
double *make_buffer(int n);
void free_buffer(double *p);

#endif
