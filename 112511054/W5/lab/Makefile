CXX      := g++
CXXFLAGS := -std=c++11 -g -Wall -Wsuggest-override -Werror=suggest-override -fsanitize=address -fno-omit-frame-pointer

.PHONY: check doctor clean

check: lab
	@echo "========== C++ 上機驗收 =========="
	@./lab; code=$$?; \
	echo "----------------------------------"; \
	if [ $$code -eq 0 ]; then \
	  echo "ALL PASS (4/4)  助教可簽過"; \
	else \
	  echo "NOT PASSED (exit code $$code)"; \
	  echo "若上方出現 AddressSanitizer / LeakSanitizer 報錯，代表第 4 項的記憶體管理有問題"; \
	  exit 1; \
	fi

lab: main.cpp student.cpp lab.h
	@$(CXX) $(CXXFLAGS) -o lab main.cpp student.cpp || { \
	  echo ""; \
	  echo "編譯失敗：請從「第一個」error 開始看，修好它，後面的錯誤通常會一起消失"; \
	  exit 1; }

doctor:
	@bash doctor.sh

clean:
	rm -f lab
