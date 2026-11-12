class NavigationMonitor:
    _FIELDS = ("NAV_X", "NAV_Y")

    def __init__(self):
        self._state = {}          # 每個物件各自建立自己的 dict

    def update(self, name, value):
        if name not in self._FIELDS:
            return False          # 未知名稱：狀態不變
        self._state[name] = value # 重複更新 → 覆蓋為最新值
        return True

    def ready(self):
        # 以「key 是否存在」判斷，而非值的真假，所以 0 也算收到
        return all(f in self._state for f in self._FIELDS)

    def snapshot(self):
        return dict(self._state)  # 回傳新 dict（值皆為不可變數字，淺拷貝即可）

    def reset(self):
        self._state.clear()


def check(label, actual, expected):
    ok = actual == expected
    print(f"{'PASS' if ok else 'FAIL'} | {label:<38} | 預期 {expected!r:<28} | 實際 {actual!r}")
    return ok


if __name__ == "__main__":
    r = []
    # 範例 1
    m = NavigationMonitor()
    r.append(check("Ex1 初始 ready()", m.ready(), False))
    r.append(check("Ex1 初始 snapshot()", m.snapshot(), {}))
    r.append(check("Ex1 update NAV_X=0", m.update("NAV_X", 0), True))
    r.append(check("Ex1 只有 X 時 ready()", m.ready(), False))
    r.append(check("Ex1 update NAV_Y=3", m.update("NAV_Y", 3), True))
    r.append(check("Ex1 兩者皆有 ready()", m.ready(), True))
    r.append(check("Ex1 snapshot()", m.snapshot(), {"NAV_X": 0, "NAV_Y": 3}))
    # 範例 2
    m = NavigationMonitor()
    m.update("NAV_X", 1); m.update("NAV_X", 5)
    r.append(check("Ex2 重複更新 snapshot()", m.snapshot(), {"NAV_X": 5}))
    r.append(check("Ex2 ready()", m.ready(), False))
    # 範例 3
    m = NavigationMonitor()
    m.update("NAV_X", 2)
    r.append(check("Ex3 update OTHER", m.update("OTHER", 9), False))
    r.append(check("Ex3 snapshot() 未被 OTHER 影響", m.snapshot(), {"NAV_X": 2}))
    m.reset()
    r.append(check("Ex3 reset 後 snapshot()", m.snapshot(), {}))
    r.append(check("Ex3 reset 後 ready()", m.ready(), False))
    # 額外 1：先 Y 後 X
    m = NavigationMonitor()
    m.update("NAV_Y", 7)
    r.append(check("Add1 只有 Y 時 ready()", m.ready(), False))
    m.update("NAV_X", -4.5)
    r.append(check("Add1 Y→X 後 ready()", m.ready(), True))
    r.append(check("Add1 snapshot()", m.snapshot(), {"NAV_X": -4.5, "NAV_Y": 7}))
    # 額外 2：兩個值都是 0
    m = NavigationMonitor()
    m.update("NAV_X", 0); m.update("NAV_Y", 0.0)
    r.append(check("Add2 兩值皆 0 ready()", m.ready(), True))
    r.append(check("Add2 snapshot()", m.snapshot(), {"NAV_X": 0, "NAV_Y": 0.0}))
    # 額外 3：修改 snapshot 不影響物件
    m = NavigationMonitor()
    m.update("NAV_X", 1); m.update("NAV_Y", 2)
    s = m.snapshot()
    s["NAV_X"] = 999; del s["NAV_Y"]; s["EXTRA"] = 1
    r.append(check("Add3 改 snapshot 後物件 snapshot()", m.snapshot(), {"NAV_X": 1, "NAV_Y": 2}))
    r.append(check("Add3 改 snapshot 後 ready()", m.ready(), True))
    # 額外 4：reset 不影響舊 snapshot
    m = NavigationMonitor()
    m.update("NAV_X", 3); m.update("NAV_Y", 4)
    old = m.snapshot()
    m.reset()
    r.append(check("Add4 reset 後舊 snapshot", old, {"NAV_X": 3, "NAV_Y": 4}))
    r.append(check("Add4 reset 後物件 snapshot()", m.snapshot(), {}))
    # 額外 5：兩個物件互相獨立
    a, b = NavigationMonitor(), NavigationMonitor()
    a.update("NAV_X", 10); a.update("NAV_Y", 20)
    r.append(check("Add5 a.ready()", a.ready(), True))
    r.append(check("Add5 b.ready()", b.ready(), False))
    r.append(check("Add5 b.snapshot()", b.snapshot(), {}))
    b.update("NAV_X", -1); a.reset()
    r.append(check("Add5 a.reset 後 b.snapshot()", b.snapshot(), {"NAV_X": -1}))
    r.append(check("Add5 a.reset 後 a.snapshot()", a.snapshot(), {}))
    print(f"\n{sum(r)}/{len(r)} passed")
