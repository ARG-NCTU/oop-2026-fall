# Lab04：C++ 物件導向與記憶體管理

本次整理涵蓋指標、參數傳遞、類別封裝、建構與解構、繼承、多型，以及動態記憶體管理。程式以四組可執行示範，觀察各種語法對變數、物件狀態與生命週期的影響。

> 整理來源：課程提供的 `Lab_04_C++_OOP.pdf`

## 學習目標

- 使用 `&` 取得位址、使用 `*` 解參考。
- 比較傳值、傳指標與傳參考對呼叫者變數的影響。
- 以 `private` 保護資料，透過公開函式管理物件狀態。
- 使用初始化清單與 `const` 成員函式。
- 透過基底類別指標呼叫衍生類別的虛擬函式。
- 理解建構、解構順序與 RAII 的資源管理方式。
- 正確配對 `new[]` 與 `delete[]`，並比較智慧指標的使用方式。

## 檔案結構

```text
lab04/
├── README.md
└── main.cpp
```

## 編譯與執行

本程式使用 C++11，不依賴第三方函式庫。建議在本機 Linux 或 WSL 使用 GCC 與 GNU Make。

在 `lab04` 資料夾執行：

```bash
g++ --version
make check
```

若不使用 Makefile，也可直接編譯執行：

```bash
g++ -std=c++11 -Wall -Wextra -Wpedantic main.cpp -o lab04_demo
./lab04_demo
```

程式內含功能檢查；不符合預期時會顯示 `FAIL` 並回傳非零結束碼。四組示範都完成時，最後會顯示 `ALL PASS (4/4)`。這個標記是本次示範程式自行提供的結果，並非教材指定的驗收格式。

### 記憶體與未定義行為檢查

在支援相關 sanitizer 的 GCC／Linux 環境執行：

```bash
make sanitize
```

此目標啟用 AddressSanitizer、UndefinedBehaviorSanitizer，並要求啟用記憶體洩漏偵測。可用以下指令清除本資料夾的兩個編譯產物：

```bash
make clean
```

## 四組程式示範

### 1. 指標與參數傳遞

同一個整數從 `5` 開始，依序進行下列操作：

| 操作 | 結果 | 原因 |
|---|---:|---|
| `increment_by_value(value)` | 5 | 函式只修改區域副本。 |
| `increment_by_pointer(&value)` | 6 | 透過指標解參考修改原變數。 |
| `increment_by_reference(value)` | 7 | 參考是原變數的別名。 |
| `*pointer = 8` | 8 | 透過位址寫入原變數。 |

`increment_by_pointer()` 額外檢查 `nullptr`，讓本示範可安全略過空指標。這是該函式自行定義的行為，並非所有接收指標的函式都會自動檢查。

### 2. 類別封裝與 const

`Battery` 將電量資料放在 `private` 區域，透過以下介面操作：

- 建構子以初始化清單設定電量。
- `set_level()` 接受 `0～100`，拒絕非法值且保留原狀態。
- `level() const` 提供讀取介面，允許透過 `const Battery&` 呼叫。
- 建構時若收到非法電量，拋出 `std::out_of_range`。

電量範圍與例外規則是本次示範的設計，用來呈現封裝與資料驗證；教材沒有指定這個類別或規則。程式檢查一般值、上下界、非法更新及非法建構。

### 3. 繼承、多型與 RAII

`BaseApp` 定義純虛擬介面，`MyApp` 使用 `override` 實作名稱、執行一次及計數功能。

```cpp
std::unique_ptr<BaseApp> app(new MyApp);
app->iterate();
```

持有者的型別是 `std::unique_ptr<BaseApp>`，虛擬呼叫仍會進入 `MyApp` 的實作。程式呼叫三次 `iterate()` 後，確認計數為 `3`。

輸出也呈現生命週期順序：先建構 `BaseApp`，再建構 `MyApp`；離開作用域時，先解構 `MyApp`，再解構 `BaseApp`。

`std::unique_ptr` 在離開作用域時自動釋放所管理的物件，示範 RAII。因為透過基底型別管理衍生物件，`BaseApp` 提供公開的虛擬解構子。

### 4. 動態陣列與所有權

程式先以 `new double[5]` 建立陣列，填入 `0～4`，確認總和為 `10`，再以 `delete[]` 釋放，並將原指標設為 `nullptr`。

接著使用陣列版本的智慧指標：

```cpp
std::unique_ptr<double[]> owned(new double[size]());
```

尾端的 `()` 讓陣列元素進行值初始化，這裡會得到零值；`unique_ptr<double[]>` 在離開作用域時自動使用 `delete[]`。單純的 `new double[size]` 不會替這些基本型別元素初始化數值，因此前面的手動配置範例會先逐一寫入，再讀取。

## 實際執行輸出

```text
[1/4] Pointers and parameter passing
  after value: 5
  after pointer: 6
  after reference: 7
  after dereference: 8
[2/4] Encapsulation and const
  invalid update preserves state; final level: 30
[3/4] Polymorphism and RAII
  BaseApp constructed
  MyApp constructed
  MyApp count: 3
  MyApp destroyed
  BaseApp destroyed
[4/4] Dynamic arrays and ownership
  raw array sum: 10; pointer reset
  unique_ptr array: zero initialized and automatically released
ALL PASS (4/4)
```

## 閱讀教材時的補充

以下補充讓教材的速查說法更精確：

| 主題 | 補充說明 |
|---|---|
| 空指標解參考 | 屬於未定義行為，不能保證一定以 Segmentation Fault 呈現。 |
| `const` 成員函式 | 一般成員不可透過此函式修改，但 `mutable` 成員是例外；指標所指向的外部物件也不會自動變成唯讀。 |
| 動態記憶體 | 可由智慧指標或標準容器管理，無須一律手動 `delete`。 |
| 釋放後設為 `nullptr` | 只更新該指標變數；其他指向同一塊記憶體的指標仍可能懸空。 |
| 多型刪除 | 以一般 `delete` 透過基底指標刪除衍生物件時，基底解構子須為虛擬；違反時屬未定義行為。 |
| vptr／vtable | 是常見的編譯器實作方式，C++ 標準沒有規定必須採用特定表格或記憶體布局。 |
| 物件切片 | 將衍生物件複製成基底物件時，只保留基底部分；以基底指標或參考使用物件可保留動態多型。 |

教材還介紹 `is-a` 與 `has-a`、建構／解構期間的虛擬呼叫、容器中裸指標的所有權等議題。本範例聚焦四組操作，沒有另外實作物件切片或錯誤解參考等示範。

## 本次驗證紀錄

本次使用本機 WSL Ubuntu 24.04、GCC 13.3.0，以 C++11 模式完成：

- `make check`：編譯成功，未出現編譯警告，四組功能檢查通過。
- `make sanitize`：四組功能檢查通過，AddressSanitizer 與 UndefinedBehaviorSanitizer 未回報錯誤；已設定 `ASAN_OPTIONS=detect_leaks=1`。


## 學習重點整理

參考與指標決定函式如何接觸原資料，封裝決定外部可以如何操作物件，多型讓共同介面對應不同實作，而 RAII 則將資源釋放綁定到物件生命週期。設計動態物件時，需要同時釐清「誰可以使用它」與「誰負責釋放它」。
