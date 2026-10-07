#!/usr/bin/env python3
"""比對 repo 內的資料夾名稱與學號名單。

用法：
    python3 check_students.py [roster.txt] [--dir 路徑]

roster 預設為腳本旁的 roster.txt，也可以是任何文字檔（例如從 Google Sheets 匯出的 CSV）。
每行抓出 9 位數學號，學號後面的第一個欄位（tab 或逗號分隔）視為姓名。
"""
import argparse
import re
import sys
from pathlib import Path

ID_PATTERN = re.compile(r"(?<!\d)\d{9}(?!\d)")


def load_roster(path):
    """回傳 {學號: 姓名}，沒有姓名時為空字串。"""
    roster = {}
    for line in Path(path).read_text(encoding="utf-8-sig").splitlines():
        m = ID_PATTERN.search(line)
        if not m:
            continue
        fields = [f.strip() for f in re.split(r"[\t,]", line[m.end():])]
        roster[m.group()] = next((f for f in fields if f), "")
    return roster


def load_folders(root):
    return {
        p.name
        for p in Path(root).iterdir()
        if p.is_dir() and not p.name.startswith(".")
    }


def find_repo_root():
    here = Path(__file__).resolve().parent
    for p in (here, *here.parents):
        if (p / ".git").exists():
            return p
    return here


def print_section(title, items, names=None):
    names = names or {}
    print(f"\n{title}（{len(items)}）")
    for item in sorted(items):
        print(f"  {item}  {names.get(item, '')}".rstrip())


def main():
    parser = argparse.ArgumentParser(description="比對資料夾名稱與學號名單")
    parser.add_argument("roster", nargs="?",
                        default=Path(__file__).resolve().parent / "roster.txt",
                        help="學號名單檔案（預設為腳本旁的 roster.txt）")
    parser.add_argument("--dir", default=find_repo_root(),
                        help="要檢查的資料夾（預設為 repo 根目錄）")
    args = parser.parse_args()

    roster = load_roster(args.roster)
    if not roster:
        sys.exit(f"在 {args.roster} 中找不到任何 9 位數學號")
    folders = load_folders(args.dir)

    ids = set(roster)
    matched = ids & folders
    missing = ids - folders
    unknown_ids = {f for f in folders - ids if ID_PATTERN.fullmatch(f)}
    others = folders - ids - unknown_ids

    print(f"名單學號數：{len(roster)}，資料夾數：{len(folders)}")
    print_section("✅ 已建立資料夾", matched, roster)
    print_section("❌ 名單中有、但沒有資料夾", missing, roster)
    print_section("⚠️ 資料夾是學號格式、但不在名單中", unknown_ids)
    print_section("❓ 非學號格式的資料夾", others)


if __name__ == "__main__":
    main()
