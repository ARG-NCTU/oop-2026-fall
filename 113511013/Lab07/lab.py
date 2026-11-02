"""
先完成 grade.cpp 的 TODO，再完成這個檔案的 TODO。
每修改 C++ 一次，都需要重新編譯（README 有指令）。
"""

import gradecpp  # ← 編譯後才會出現的 C++ 模組


def task_1():
    """Task 1：呼叫 C++ 的 add_bonus。"""
    # TODO P1：透過 gradecpp.add_bonus(...) 計算 78 + 10。
    result = None  # ← 替換這一行

    # TODO P2：測試 95 + 10，必須被限制在 100 分。
    capped = None  # ← 替換這一行

    assert result == 88, f"預期 88，實際 {result!r}"
    assert capped == 100, f"預期 100，實際 {capped!r}"


def task_2():
    """Task 2：傳 Python list 給 C++ std::vector。"""
    scores = [60, 80, 100]

    # TODO P3：呼叫 gradecpp.average_scores(scores)。
    avg = None  # ← 替換這一行

    # TODO P4：呼叫同一個 C++ 函式，計算 [70, 90] 的平均。
    avg_2 = None  # ← 替換這一行

    assert avg == 80, f"預期 80，實際 {avg!r}"
    assert avg_2 == 80, f"預期 80，實際 {avg_2!r}"

    # 額外確認：C++ 的 std::invalid_argument 會轉為 Python ValueError。
    try:
        gradecpp.average_scores([])
    except ValueError:
        pass
    else:
        raise AssertionError("空清單應觸發 ValueError")


def task_3():
    """Task 3：建立並操作 C++ GradeBook 物件。"""
    # TODO P5：用 gradecpp.GradeBook() 建立 book。
    book = None  # ← 替換這一行

    # TODO P6：呼叫 book.add(...)，依序加入 60、80、100。

    # TODO P7：呼叫 book.count() 與 book.average()。
    n = None  # ← 替換這一行
    avg = None  # ← 替換這一行

    assert n == 3, f"預期 3 筆，實際 {n!r}"
    assert avg == 80, f"預期平均 80，實際 {avg!r}"


def main():
    tasks = [("Task 1 / 基本函式", task_1),
             ("Task 2 / list 與 vector", task_2),
             ("Task 3 / C++ Class", task_3)]
    passed = 0

    for label, task in tasks:
        try:
            task()
        except Exception as exc:
            print(f"[FAIL] {label}: {type(exc).__name__}: {exc}")
        else:
            passed += 1
            print(f"[PASS] {label}")

    print(f"\n結果：{passed}/{len(tasks)} 關通過")
    if passed != len(tasks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
