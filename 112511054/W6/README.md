# W6 MOOS-IvP Lab

- 學號：112511054（沿用本工作區的作業資料夾）
- 教材：[MOOS-IvP intro.，2026 AOOP W6](https://docs.google.com/presentation/d/1x8wc8snRqeBkyieUpvco9AnM9ukjIADRn-8jp79Byxg/edit)
- 版本：MOOS-IvP v24.8.1
- 本資料夾由 AI 協助製作任務設定與說明；執行結果見 `verification.md`。

## 啟動方式

在這台電腦的 PowerShell 執行：

```powershell
wsl -d Ubuntu -- bash /mnt/c/Users/nick0/OneDrive/Desktop/AOOP/112511054/W6/launch.sh
```

也可在 WSL 執行：

```bash
cd /mnt/c/Users/nick0/OneDrive/Desktop/AOOP/112511054/W6
bash launch.sh
```

視窗出現後按 **DEPLOY** 開始航行，按 **MUCHSLO** 或 **MUCHFST** 切換速度，按 **RETURN** 返回起點。結束時在啟動終端按 Ctrl+C。日誌會寫到本資料夾的 `MOOSLog_*` 子資料夾。

## 四項實作

1. **船身顏色**：在 `alpha.moos` 的 `pNodeReporter` 區塊設定 `platform_color = dodger_blue`，由船舶回報傳給 `pMarineViewer`。
2. **正方形航線**：在 `alpha.bhv` 的 `waypt_survey` 設定 `polygon = 60,-40:60,-160:180,-160:180,-40:60,-40`。相鄰四角距離都是 120 公尺，最後重複第一點以完成閉合一圈。完成後觸發原有返航行為。
3. **速度按鈕**：保留 SLOWER／FASTER，新增 `button_five = MUCHSLO # WPT_UPDATE=speed=1.0` 與 `button_six = MUCHFST # WPT_UPDATE=speed=4.0`。`waypt_survey` 透過 `updates = WPT_UPDATE` 接收更新。將 `use_alt_speed = false`，避免範例原本的備用速度 1.2 m/s 蓋過設定。按鈕設定的是目標速度；實際速度在加速及轉彎時會有暫態差異。速度按鈕控制巡航行為，返航行為仍使用原設定 2.0 m/s。
4. **轉向反應**：說明如下。

## 如何改變船隻的轉向反應

轉向包含「控制器算出舵角」與「模擬器根據舵角改變航向」兩個階段。

- `pMarinePIDV22` 的 `yaw_pid_kp` 是比例增益。增大通常會讓航向誤差引發更強的舵角修正，但太大可能造成超越與擺動。
- `yaw_pid_kd` 是微分增益，可抑制快速變化與震盪，但太大可能對量測雜訊敏感。
- `yaw_pid_ki` 是積分增益，用來補償持續誤差；太大可能造成積分累積與超越，因此也要配合 `yaw_pid_integral_limit`。
- `maxrudder` 限制舵角命令大小，減小可限制急轉，但也可能增加轉彎半徑。
- `uSimMarineV22` 的 `turn_rate` 控制模擬船隻的轉向能力，範例為 95，有效範圍是 0～100。若想觀察較慢的轉向，可改為 50，再重啟任務比較。
- `turn_spd_loss` 控制舵角造成的速度損失，範例為 0.4；數值越大，急轉時減速越明顯。

依 v24.8.1 的 `SimEngine.cpp`，航向增量先由舵角、依速度調整後的轉向率與時間間隔計算，再乘上推力因素，最後加上外部旋轉漂移。因此 `turn_rate=95` 不代表船在任何速度及舵角下都會以每秒 95 度轉彎。

建議比較方式：先用原設定完成一圈，再只將 `turn_rate` 從 95 改為 50，保持相同目標速度，觀察角落的航跡與轉彎半徑。航點是正方形，但船有有限轉向能力，實際航跡在角落會圓滑或偏離，不會是理想的尖角。

## 與 OOP 的關係

MOOS 應用程式繼承基底應用類別，透過 `OnNewMail`、`Iterate`、`OnStartUp` 等虛擬函式提供各自的行為，呈現繼承與多型。應用程式封裝自身狀態，透過 MOOSDB 發布／訂閱資料，降低程式間的直接依賴。IvP 行為也使用共同的行為介面，例如 `BHV_Waypoint`，讓 Helm 可以整合不同導航行為的目標。

## 環境

本機已有 Ubuntu WSL 2 與 WSLg。原始碼安裝於 `/home/nick0/moos-ivp`，執行檔位於其 `bin` 資料夾；已在 `~/.bashrc` 加入 PATH。任務檔以官方 `ivp/missions/s1_alpha` 為基礎，保留原始作者註記。

本簡報未列出明確繳交格式或期限。公告中的期末分組仍需要本人確認組員；這份 Lab 不代替分組確認。
