表格一：Part A — AI Tutor Learning Record (True / False)
① Check My Understanding
Questions completed：5 / 5

Answers revised after AI hints：1 / 5

② My Misconception
Before: I thought…

只要子類別有實作與父類別同名的函式，透過父類別指標（Base Pointer）呼叫時就會自動執行子類別的版本。

Now: I understand…

C++ 預設是靜態綁定（Early Binding）。基底類別的函式必須宣告為 virtual，程式執行時才會透過虛擬函式表（vtable）達成動態綁定（Late Binding），進而呼叫到子類別覆寫的版本；且覆寫時標註 override 能讓編譯器確保函式簽名一致。

③ Challenge the AI
One AI-generated question I challenged：

「當基底類別含有純虛擬函式（= 0）時，該基底類別完全不能擁有任何函式實作，否則無法編譯。」

Why?

[x] Technically questionable

[ ] Ambiguous

[ ] Oversimplified

[ ] Too easy

Brief explanation：

技術上純虛擬解構子（pure virtual destructor）或純虛擬函式在 C++ 中依然可以提供函式本體實作，只是該類別仍為抽象類別無法被實例化，題意將「純虛擬函式宣告」與「完全不能有實作」混為一談。

④ One-Minute Reflection
One thing I am still unsure about：

當多重繼承遇到虛擬繼承（Virtual Inheritance）時，物件內部 vptr 與虛擬基底指標（vbtable）在記憶體中的具體配置與呼叫開銷。

表格二：Part B — AI Tutor Learning Record (LeetCode-Style Challenge)
1. Today’s Challenge
Core concept from today’s OCW lecture：

使用抽象基底類別定義統一介面（Pure Virtual Interface）結合動態記憶體管理（new[]/delete[]），在執行期處理多型物件與資源管理。

AI-generated coding challenge title：

Custom Polymorphic Dynamic Buffer Processor

2. My Initial Approach — Before AI Help
My approach：

設計一個基底抽象處理器 BaseProcessor，定義純虛擬函式 virtual void process(double* data, int size) = 0;。實作子類別 ScaleProcessor 與 ClampProcessor，透過動態配置陣列傳入資料，並在主程式利用基底指標陣列逐一呼叫多型運算。

3. AI Tutor Help
Did you ask the AI Tutor for help?

[x] Yes — I received one or more hints

[ ] No — I solved it independently

The most useful hint/question from AI was：

「如果外部持有 BaseProcessor* 並在結束時呼叫 delete processor;，基底類別缺少什麼會導致子類別資源釋放不完全？」

It helped me realize that：

基底類別必須將解構子宣告為 virtual ~BaseProcessor() {}，否則透過基底指標釋放子類別物件時會引發未定義行為（Undefined Behavior）並造成記憶體洩漏。

4. My Revision
Did you change your approach or code after interacting with AI?

[x] Yes

[ ] No

What did you change, and why?

在 BaseProcessor 補上 virtual ~BaseProcessor() = default;，同時確認動態配置的連續緩衝區在釋放時嚴格使用 delete[] 而非 delete，確保符合記憶體安全檢查規範。

5. Verification
My final program：

[x] Passed the provided examples

[x] Passed additional edge cases

[ ] Still has unresolved problems

One edge case I tested：

Input：size = 0, buffer = nullptr

Expected output：處理器安全返回，不進行記憶體越界寫入，成功釋放。

Actual output：處理器安全返回，記憶體檢查工具無任何報錯與洩漏（AddressSanitizer clean）。

6. One-Minute Reflection
What idea from the OCW lecture did you transfer to this new problem?

將實驗中的 BaseApp 介面導向設計與 make_buffer / free_buffer 的動態陣列管理，轉移到資料管線（Pipeline）架構的設計中。

One thing I understand better now：

理解了為何在現代 C++ 框架中，基底指標生命週期管理必須嚴格搭配虛擬解構子與正確的 delete[] 配對。

One thing I am still unsure about：

在需要頻繁建立大量多型小物件時，相較於 raw pointer 與 new，使用智慧指標（如 std::unique_ptr）或物件池（Object Pool）在效能與記憶體碎裂上的具體取捨。
