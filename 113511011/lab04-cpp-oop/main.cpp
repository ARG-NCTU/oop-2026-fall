// main.cpp — 驗收檢查程式（學生請勿修改）
#include <cstdio>
#include <string>
#include "lab.h"

static const int TOTAL = 4;
static int g_passed = 0;

static void begin(const char *title) {
  std::printf("%s ", title);
  std::fflush(stdout);
}
static void pass() {
  std::printf("PASS\n");
  std::fflush(stdout);
  ++g_passed;
}
static void fail(const std::string &why, const char *hint) {
  std::printf("FAIL\n       原因：%s\n       提示：%s\n", why.c_str(), hint);
  std::fflush(stdout);
}
static std::string num(double d) {
  char buf[64];
  std::snprintf(buf, sizeof buf, "%g", d);
  return buf;
}

// ---------- 1. 參考 ----------
static void test_reference() {
  begin("[1/4] 參考 clamp_value ........");
  const char *hint = "GUIDE.md 第 1 節；v 是參考，直接修改 v 就會改到呼叫者的變數";
  double v = 15;
  clamp_value(v, 0, 10);
  if (v != 10) return fail("clamp_value(15, 0, 10) 後應為 10，實際是 " + num(v), hint);
  v = -5;
  clamp_value(v, 0, 10);
  if (v != 0) return fail("clamp_value(-5, 0, 10) 後應為 0，實際是 " + num(v), hint);
  v = 5;
  clamp_value(v, 0, 10);
  if (v != 5) return fail("範圍內的值不該被改動，5 變成了 " + num(v), hint);
  pass();
}

// ---------- 2. 封裝與建構子 ----------
static void test_battery() {
  begin("[2/4] 封裝與建構子 Battery ....");
  const char *hint = "GUIDE.md 第 2 節；建構子用初始化清單，setLevel 要在入口擋壞值";
  Battery b(50);
  const Battery &cb = b;
  if (cb.getLevel() != 50) return fail("Battery(50) 之後 getLevel() 應為 50，實際是 " + num(cb.getLevel()), hint);
  if (b.setLevel(120)) return fail("setLevel(120) 應該回傳 false（超出 0~100）", hint);
  if (b.setLevel(-1)) return fail("setLevel(-1) 應該回傳 false（超出 0~100）", hint);
  if (cb.getLevel() != 50) return fail("被拒絕的值不應該改動 m_level，目前是 " + num(cb.getLevel()), hint);
  if (!b.setLevel(30)) return fail("setLevel(30) 是合法值，應該回傳 true", hint);
  if (cb.getLevel() != 30) return fail("setLevel(30) 之後 getLevel() 應為 30，實際是 " + num(cb.getLevel()), hint);
  if (!b.setLevel(0) || !b.setLevel(100)) return fail("邊界值 0 與 100 都是合法的", hint);
  pass();
}

// ---------- 3. 繼承與 virtual ----------
static void test_virtual() {
  begin("[3/4] 繼承與 virtual MyApp .....");
  const char *hint = "GUIDE.md 第 3 節；寫 class MyApp : public BaseApp，覆寫時加 override";
  BaseApp *app = make_app();
  if (app == nullptr) return fail("make_app() 回傳 nullptr，還沒完成", hint);
  if (app->Name() != "MyApp") {
    std::string why = "Name() 應回傳 \"MyApp\"，實際是 \"" + app->Name() + "\"";
    delete app;
    return fail(why, hint);
  }
  for (int i = 0; i < 3; i++) {
    if (!app->Iterate()) {
      delete app;
      return fail("Iterate() 應該回傳 true", hint);
    }
  }
  int c = app->Count();
  delete app;  // 透過基底指標刪除，基底解構子是 virtual
  if (c != 3) return fail("呼叫 Iterate() 3 次後 Count() 應為 3，實際是 " + std::to_string(c), hint);
  pass();
}

// ---------- 4. new / delete ----------
static void test_heap() {
  begin("[4/4] new[] / delete[] ........");
  const char *hint = "GUIDE.md 第 4 節；用 new double[n] 配置，free_buffer 要用 delete[]";
  double *p = make_buffer(5);
  if (p == nullptr) return fail("make_buffer(5) 回傳 nullptr，還沒完成", hint);
  for (int i = 0; i < 5; i++) {
    if (p[i] != i) {
      std::string why = "p[" + std::to_string(i) + "] 應為 " + std::to_string(i) + "，實際是 " + num(p[i]);
      free_buffer(p);
      return fail(why, hint);
    }
  }
  free_buffer(p);
  pass();
}

int main() {
  test_reference();
  test_battery();
  test_virtual();
  test_heap();
  std::printf("通過 %d/%d 項\n", g_passed, TOTAL);
  return g_passed == TOTAL ? 0 : 1;
}
