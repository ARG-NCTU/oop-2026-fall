CXX ?= g++
CXXFLAGS := -std=c++11 -g -Wall -Wextra -Werror -fsanitize=address,undefined -fno-omit-frame-pointer

.PHONY: check clean

device_dispatcher: device_dispatcher.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

check: device_dispatcher
	python3 test_device_dispatcher.py

clean:
	rm -f device_dispatcher
