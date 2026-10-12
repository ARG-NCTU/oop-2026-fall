Topic: MOOS-IvP Autonomous Navigation Framework and Mission Customization (s1_alpha)  Date: 2026-10-12

① Check My Understanding
* Questions completed: 4 / 4
* Answers revised after AI hints: 1 / 4

② My Misconception
* Before: I thought…
  我一開始以為調整載具的顏色以及自訂 GUI 按鈕需要修改複雜的原始程式碼，並且誤以為 pMarineViewer 內部可以直接支援 vehicles_color 參數。
* Now: I understand…
  載具的本體顏色是由 pNodeReporter 模組透過 platform_color 統一管理，而 pMarineViewer 的 GUI 按鈕則可透過宣告 button_three / button_four 綁定 WPT_UPDATE 變數來即時變更巡航速度。

③ Challenge the AI
* One AI-generated question I challenged: 關於 pMarinePIDV22 控制器中若未適度調整 yaw_pid_kd，當比例增益 Kp 過大時是否容易引發船隻轉向震盪的真偽題。
* Why?
  ☐ Ambiguous
  ☑ Too easy
  ☐ Technically questionable
  ☐ Oversimplified
* Brief explanation: 這是經典的自動控制閉迴路現象，概念很基礎，缺乏對多重變數耦合的深入探討。

④ One-Minute Reflection
* One thing I am still unsure about: 在多載具協同任務中，如何透過 pShare 在多個獨立的 MOOSDB 之間精確同步非同步變數。

---

Part B: MOOS-IvP Mission Customization (s1_alpha)

* Core concept from today's session: 後座駕駛架構（Backseat Driver）、發布-訂閱機制、航點行為（BHV_Waypoint）多邊形路徑設定，以及低階 pMarinePIDV22 控制器的轉向反應調校。
* AI-generated configuration challenge title: Customizing Autonomous Surface Vehicle Mission Parameters and PID Response Tuning in MOOS-IvP.

My Initial Approach – Before AI Help
* My approach: 透過 VS Code 直接打開 alpha.moos 與 alpha.bhv，試圖透過修改設定檔達成指定船體顏色、自訂速度控制按鈕及正方形航跡，並利用 pAntler 啟動檢驗。

AI Tutor Help
* Did you ask the AI Tutor for help?
  - [ ] No – I solved it independently
  - [x] Yes – I received one or more hints
* The most useful hint/question from AI was: 指出 pMarineViewer 設定區塊不支援 vehicles_color，並引導我前往 pNodeReporter 區塊修改 platform_color，同時修正按鈕語法。
* It helped me realize that: MOOS-IvP 各個模組設定檔都有嚴格對應的參數定義，設定錯誤的參數名稱會導致行程無法讀取並引發閃退。

My Revision
* Did you change your approach or code after interacting with AI?
  - [ ] No
  - [x] Yes
* What did you change, and why?: 移除了 pMarineViewer 中不合法的顏色參數，改至 pNodeReporter 設定 platform_color；並在 alpha.bhv 將原本的不規則多邊形 polygon 重新定義為正方形四頂點坐標。

Verification
* My final program:
  - [x] Passed the provided examples
  - [x] Passed additional edge cases
* One edge case I tested:
  - Input: 點擊右下角自訂的 MUCHSLO (1.0 m/s) 與 MUCHFST (4.0 m/s) 按鈕。
  - Expected output: pMarinePIDV22 即時更新速度目標，載具平順切換航速且不失控。
  - Actual output: 航速即時切換，且載具順利沿著正方形航點完整巡航。

One-Minute Reflection
* What idea from the session did you transfer to this new problem? 將高階決策導航（pHelmIvP）與低階運動控制（pMarinePIDV22）分離的模組化設計概念。
* One thing I understand better now: 清楚掌握了透過調整 PID 控制器的 Kp 與 Kd 增益值，以及行為設定檔中的 capture_radius 來控制載具轉向靈敏度與過衝抑制的方法。
* One thing I am still unsure about: 當載具遭遇動態海流乾擾時，積分項（Ki）飽和極限的最佳化設定細節。
