import copy


def choose_heading(candidates, waypoint_pwt, heading_pwt):
    best_heading = None
    best_score = None
    for heading, waypoint_utility, heading_utility in candidates:
        score = waypoint_pwt * waypoint_utility + heading_pwt * heading_utility
        if (best_score is None
                or score > best_score
                or (score == best_score and heading < best_heading)):
            best_heading, best_score = heading, score
    if best_score is None:
        return None
    return {"heading": best_heading, "score": best_score}


def check(label, actual, expected):
    ok = actual == expected
    print(f"{'PASS' if ok else 'FAIL'} | {label:<30} | 預期 {expected!r:<32} | 實際 {actual!r}")
    return ok


if __name__ == "__main__":
    r = []
    r.append(check("Ex1", choose_heading([(0, 20, 100), (90, 100, 10)], 2, 1),
                   {"heading": 90, "score": 210}))
    r.append(check("Ex2 同分取小航向", choose_heading([(90, 100, 0), (0, 0, 100)], 1, 1),
                   {"heading": 0, "score": 100}))
    r.append(check("Ex3 空 list", choose_heading([], 1, 1), None))

    r.append(check("單一候選", choose_heading([(45, 10, 20)], 3, 2),
                   {"heading": 45, "score": 70}))

    three = [(0, 100, 0), (90, 0, 50), (180, 30, 80)]
    r.append(check("waypoint_pwt=0", choose_heading(three, 0, 5),
                   {"heading": 180, "score": 400}))
    r.append(check("heading_pwt=0", choose_heading(three, 5, 0),
                   {"heading": 0, "score": 500}))

    r.append(check("兩權重皆 0", choose_heading([(270, 90, 90), (30, 5, 0), (100, 100, 100)], 0, 0),
                   {"heading": 30, "score": 0}))

    r.append(check("同分反轉順序 A", choose_heading([(0, 0, 100), (90, 100, 0)], 1, 1),
                   {"heading": 0, "score": 100}))
    r.append(check("同分反轉順序 B (3 筆)", choose_heading([(300, 50, 50), (120, 60, 40), (200, 40, 60)], 1, 1),
                   {"heading": 120, "score": 100}))
    r.append(check("同分反轉順序 B 反轉", choose_heading([(200, 40, 60), (120, 60, 40), (300, 50, 50)], 1, 1),
                   {"heading": 120, "score": 100}))

    data = [(10, 50, 60), (20, 70, 30), (30, 10, 90)]
    before = copy.deepcopy(data)
    ids_before = [id(t) for t in data]
    res1 = choose_heading(data, 2, 3)
    res2 = choose_heading(data, 2, 3)
    r.append(check("輸入內容未改變", data, before))
    r.append(check("輸入元素身分未改變", [id(t) for t in data], ids_before))
    r.append(check("結果正確", res1, {"heading": 30, "score": 290}))
    r.append(check("每次回傳新的 dict", res1 is not res2, True))

    print(f"\n{sum(r)}/{len(r)} passed")
