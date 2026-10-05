# 觀念說明
這次的上機將為下禮拜會使用到的函式進行複習 / 說明。請按照以下步驟進行：

1. 細讀「為什麼需要」與「觀念」
2. 看範例，回答「想一想」（先自己想，再點開答案）
3. 到 `student.cpp` 完成對應的 "TODO"
4. 執行 `make check`，確認那一項顯示 `PASS`

*範例省略了 `#include` 與 `main()`。

---

## 第 1 節　參考（reference）

### 為什麼需要

假設我們今天寫一個以下的 swap 程式，其實在執行的事情是「複製係數」，更改的是副本，當被呼叫時，變數並不會實際改變：

```cpp
void swap_bad(int a, int b) { int t = a; a = b; b = t; }

int x = 1, y = 2;
swap_bad(x, y);   // x、y 沒有交換
```

正確的解法是使用「傳指標」的方式，呼叫時要寫 `&`，函式裡要寫 `*`：

```cpp
void swap_c(int *a, int *b) { int t = *a; *a = *b; *b = t; }
swap_c(&x, &y);
```

### 觀念

在 C++ 裡面多了一種寫法：**傳參考**。參數型別後面加 `&`，參數就變成呼叫者那個變數的「別名」！

```cpp
void swap_cpp(int &a, int &b) { int t = a; a = b; b = t; }
swap_cpp(x, y);   // x、y 真的交換了
```

「參考」的規則：

- 宣告時就必須綁定一個變數，之後不能改綁別的變數
- 不會是空的（指標可以是 `nullptr`，但是在這裡不行）
- 用起來和一般變數一樣，不用寫 `*`；呼叫時也不用寫 `&`

### 想一想

```cpp
void add_one(int &n) { n = n + 1; }
int k = 5;
add_one(k);
```

`k` 現在是多少？如果把 `int &n` 改成 `int n` 呢？

<details><summary>答案</summary>

`k` 是 6，因為 `n` 就是 `k` 的別名。若改成 `int n` ， `k` 還是 5，因為函式只改到副本。

</details>

### 動手：TODO 1　`clamp_value`

把 `v` 限制在 `lo` 到 `hi` 之間：

- `v < lo` 時，`v` 變成 `lo`
- `v > hi` 時，`v` 變成 `hi`
- 其他情況不動

```cpp
double x = 15;
clamp_value(x, 0, 10);   // 根據規則 x 應該是 10！
```

想想看！x 的值應不應該被改到？

---

## 第 2 節　封裝與建構子

### 為什麼需要

C 的 struct 欄位誰都能改，沒有東西能阻止別人寫入不合理的值：

```cpp
struct Account { double balance; };
struct Account a;
a.balance = -100;   // 語言不會攔你
```

而且 C 的區域變數不會自動初始化，忘了設值就會被指派為隨機值。

### 觀念 1：public 與 private

`class` 可以把資料藏起來（`private`），只開放函式（`public`）。
外部想改資料只能呼叫函式，函式就能在入口檢查，拒絕壞值：

```cpp
class Account {
 public:
  bool deposit(double amt) {
    if (amt <= 0) return false;   // 在入口擋壞值，不改動資料
    m_balance += amt;
    return true;
  }
  double getBalance() const { return m_balance; }

 private:
  double m_balance;
};

Account a;
a.deposit(50);        // OK
a.m_balance = -100;   // 編譯失敗：m_balance 是 private
```

- `struct` 與 `class` 唯一的差別是預設權限：`struct` 預設 `public`，`class` 預設 `private`
- `m_` 前綴只是慣例，用來分辨「成員變數」與「區域變數」

### 觀念 2：const 成員函式

函式名稱後面加 `const`（例如 `getBalance() const`），表示這個函式**保證不修改物件**。
如果你手上只有 const 物件或 const 參考，就只能呼叫 const 成員函式。

### 觀念 3：建構子與初始化清單

**建構子**的名稱與類別相同、沒有回傳型別，物件被建立時會自動呼叫。
冒號後面那一段叫**初始化清單**，在進入函式本體之前就把成員設好值：

```cpp
class Account {
 public:
  Account() : m_balance(0) {}               // Account a;      呼叫這個
  Account(double init) : m_balance(init) {} // Account b(100); 呼叫這個
  // ...
 private:
  double m_balance;
};
```

當類別定義在 `.h`、函式寫在 `.cpp` 時，要在名稱前面加上 `類別名::`：

```cpp
Account::Account(double init) : m_balance(init) {}

bool Account::deposit(double amt) {
  // ...
}
```

### 想一想

`Account b(100); b.deposit(-5);` 之後，`deposit` 回傳什麼？`m_balance` 是多少？

<details><summary>答案</summary>

回傳 `false`，`m_balance` 還是 100。壞值在入口就被擋下來，資料沒有被改動。

</details>

### 動手：TODO 2　`Battery`

`lab.h` 已經宣告好 `Battery`，`m_level` 是 private。在 `student.cpp` 完成：

- **(a) 建構子**：用初始化清單把 `m_level` 設成參數 `level`
- **(b) `setLevel`**：
  - `level` 不在 0 到 100 之間（0 與 100 本身是合法的）→ 回傳 `false`，而且**不能**改動 `m_level`
  - 反之則把 `m_level` 設成 `level`，回傳 `true`

`getLevel()` 已經寫好了。

---

## 第 3 節　繼承與 virtual

### 為什麼需要

假設有一個框架負責「每隔一段時間呼叫一次你的程式」。框架是別人寫的，它不可能事先知道你的類別叫什麼。
我們需要一種寫法：**框架只認得一個共同的基底類別，卻能呼叫到你寫的版本。**

### 觀念 1：繼承

```cpp
class Shape {
 public:
  Shape(double size) : m_size(size) {}
 protected:
  double m_size;   // protected：子類別可以存取，外部不行
};

class Square : public Shape {   // Square 是一種 Shape
 public:
  Square(double s) : Shape(s) {}   // 先呼叫父類別的建構子
  double area() const { return m_size * m_size; }
};
```

| 權限 | 誰能存取 |
| --- | --- |
| `public` | 任何人 |
| `protected` | 自己與子類別 |
| `private` | 只有自己 |

### 觀念 2：沒有 virtual 時

```cpp
class Shape  { public: std::string name() const { return "shape"; } };
class Circle : public Shape { public: std::string name() const { return "circle"; } };

Circle c;
Shape *p = &c;
std::cout << p->name();
```

<details><summary>想一想：印出 shape 還是 circle？</summary>

印出 `shape`。`p` 的宣告型別是 `Shape*`，編譯器在編譯時就決定呼叫 `Shape::name`。

</details>

### 觀念 3：加上 virtual

在基底類別的函式前面加 `virtual`，呼叫時就會依照**物件實際的型別**決定執行哪個版本：

```cpp
class Shape  { public: virtual std::string name() const { return "shape"; } };
class Circle : public Shape { public: std::string name() const override { return "circle"; } };

Circle c;
Shape *p = &c;
std::cout << p->name();   // 印出 circle
```

- **指標的型別**決定你能呼叫哪些函式
- **物件的型別**決定（有 virtual 時）實際執行哪個版本

底層原理：含有 virtual 函式的物件裡藏著一個指標（vptr），指向一張函式指標表（vtable）。
呼叫 virtual 函式時，程式會透過這張表找到正確的版本。

### 觀念 4：override

子類別覆寫時，在函式後面加 `override`，請編譯器檢查「這個函式真的覆寫了父類別的 virtual 函式」。
名稱、參數或 `const` 寫錯時，沒加 `override` 會悄悄變成另一個函式；加了就會直接編譯失敗。

```cpp
class Shape  { public: virtual double area() const; };
class Square : public Shape { public: double area() override; };   // 少了 const → 編譯錯誤
```

本次上機的 Makefile 設定成：**覆寫時少了 `override` 就編譯失敗**。

### 觀念 5：純虛擬函式與抽象類別

```cpp
class Shape {
 public:
  virtual ~Shape() {}
  virtual double area() const = 0;   // = 0：純虛擬函式，只宣告、不實作
};
```

- 有純虛擬函式的類別是**抽象類別**，不能直接建立（`Shape s;` 會編譯失敗）
- 子類別必須把**每一個**純虛擬函式都實作出來，否則子類別也是抽象的
- 基底類別的解構子要寫成 `virtual`，透過基底指標 `delete` 時才會正確呼叫子類別的解構子

### 想一想

```cpp
std::vector<Shape *> shapes;
shapes.push_back(new Circle(2));
shapes.push_back(new Square(3));
for (unsigned i = 0; i < shapes.size(); i++)
  total += shapes[i]->area();
```

要新增 `Triangle`，這個迴圈需要修改嗎？

<details><summary>答案</summary>

不用。迴圈只認得 `Shape`，新增 `Triangle` 只要寫一個新類別並實作 `area()`。這就是多型的好處。

</details>

### 動手：TODO 3　`MyApp`

`lab.h` 裡的 `BaseApp` 為「框架只認得的基底類別」：

```cpp
class BaseApp {
 public:
  virtual ~BaseApp() {}
  virtual std::string Name() const = 0;
  virtual bool Iterate() = 0;
  virtual int Count() const = 0;
};
```

在 `student.cpp` 寫一個 `MyApp` 繼承 `BaseApp`，三個函式都要覆寫，並加上 `override`：

| 函式 | 要做的事 |
| --- | --- |
| `Name()` | 回傳 `"MyApp"` |
| `Iterate()` | 每呼叫一次，`m_count` 加 1，回傳 `true` |
| `Count()` | 回傳 `m_count` |

最後讓 `make_app()` 回傳 `new MyApp`。`new` 會在 heap 上建立一個物件並回傳它的位址，第 4 節會詳細說明。
`MyApp*` 可以直接當成 `BaseApp*` 回傳，因為 MyApp 是一種 BaseApp。

---

## 第 4 節　new 與 delete

### 為什麼需要

區域變數放在 **stack**，離開作用域就自動消失。
如果需要「函式結束後還留著」的資料，或大小在執行時才知道，就要向 **heap** 要記憶體。

```
+----------------------+
| stack                |   int n;            <- 離開函式就消失
|                      |   double *p;        <- 指標本身也在 stack
+----------------------+
| heap                 |   new double[n]     <- p 指向這裡，要手動釋放
+----------------------+
```

C 用 `malloc` / `free`，但它們只管記憶體，不會呼叫建構子與解構子，還要自己算大小、自己轉型。

### 觀念

C++ 用 `new` / `delete`：

```cpp
Account *a = new Account(100);   // 配置記憶體 + 呼叫建構子
a->deposit(50);
delete a;                        // 呼叫解構子 + 釋放記憶體

int *arr = new int[10];          // 配置 10 個 int 的陣列
arr[0] = 1;                      // 用起來跟一般陣列一樣
delete[] arr;                    // 陣列要用 delete[]
```

四條規則：

1. 每個 `new` 都要有對應的 `delete`
2. `new[]` 一定配 `delete[]`，不能混用
3. 同一塊記憶體不能 `delete` 兩次
4. `delete` 之後就不能再使用那塊記憶體

**記憶體洩漏**：指標消失了，但它指向的記憶體沒有被釋放。

```cpp
void leak() {
  int *p = new int[100];
}   // 離開函式，p 消失了，但那 100 個 int 還留在 heap 上
```

本次上機用 `-fsanitize=address` 編譯，洩漏、混用 `delete`/`delete[]`、重複 `delete` 都會被抓出來並報錯。

### 想一想

```cpp
double *make() {
  double *p = new double[3];
  return p;
}
```

函式結束時，`p` 指向的那 3 個 double 還在嗎？誰要負責釋放它？

<details><summary>答案</summary>

還在。`p` 這個指標變數消失了，但 heap 上的記憶體不會自動釋放。
接到回傳值的人要負責在用完之後 `delete[]`。

</details>

### 動手：TODO 4　`make_buffer` / `free_buffer`

- `make_buffer(n)`：用 `new` 配置 `n` 個 `double`，讓 `p[i]` 的值等於 `i`，回傳 `p`
- `free_buffer(p)`：釋放 `p`（想一想該用 `delete` 還是 `delete[]`）

---

## 附錄：常見編譯錯誤

| 訊息裡出現 | 通常代表 |
| --- | --- |
| `is private within this context` | 從外部存取了 private 成員 |
| `marked 'override', but does not override` | 函式名稱、參數或 `const` 和基底類別不一致 |
| `can be marked override` | 覆寫時忘了加 `override` |
| `invalid new-expression of abstract class type` | 子類別還有純虛擬函式沒有實作 |
| `expected ';'` | 上一行少了分號（錯誤常常報在下一行） |

編譯失敗時，從**第一個** error 開始看，修好之後後面的錯誤通常會一起消失。
