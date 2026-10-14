#!/usr/bin/env bash
# 環境檢查：驗收前先跑 make doctor，看到 ENV OK 就可以了。
bad=0
ok()   { echo "  [OK]   $1"; }
err()  { echo "  [FAIL] $1"; bad=1; }

echo "========== 環境檢查 =========="

# 1. 工具
for t in g++ make git; do
  if command -v "$t" >/dev/null 2>&1; then
    ok "$t：$("$t" --version | head -1)"
  else
    err "找不到 $t。請執行：sudo apt update && sudo apt install -y build-essential git"
  fi
done

# 2. AddressSanitizer 與 LeakSanitizer 真的能用
if command -v g++ >/dev/null 2>&1; then
  tmp="$(mktemp -d)"
  cat > "$tmp/good.cpp" << 'CPP'
int main() { int *p = new int[3]; delete[] p; return 0; }
CPP
  cat > "$tmp/leak.cpp" << 'CPP'
int main() { int *p = new int[3]; p[0] = 1; p = nullptr; return 0; }
CPP
  if g++ -std=c++11 -fsanitize=address -o "$tmp/good" "$tmp/good.cpp" 2>/dev/null && "$tmp/good" >/dev/null 2>&1; then
    ok "AddressSanitizer 可以編譯並執行"
    g++ -std=c++11 -fsanitize=address -o "$tmp/leak" "$tmp/leak.cpp" 2>/dev/null
    if "$tmp/leak" >/dev/null 2>&1; then
      err "洩漏偵測沒有作用（故意漏掉的記憶體沒被抓到）。請找助教"
    else
      ok "洩漏偵測正常"
    fi
  else
    err "AddressSanitizer 無法使用。請確認已安裝 build-essential"
  fi
  rm -rf "$tmp"
fi

echo "------------------------------"
if [ $bad -eq 0 ]; then echo "ENV OK"; else echo "ENV NOT OK（請處理上面標示 [FAIL] 的項目）"; exit 1; fi
