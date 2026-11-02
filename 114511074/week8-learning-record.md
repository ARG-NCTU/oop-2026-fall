# Week 8 Learning Record

## Topic: pybind11 — Using C++ in Python

### 1. What I Learned

This week, I learned how to use pybind11 to connect C++ with Python. Before this lab, I had mostly used these two languages separately, so I wasn't very familiar with how they could work together.

Through this lab, I learned that C++ code can be compiled into a Python module, allowing Python to call C++ functions and classes.

### 2. What I Did

First, I set up the environment in Ubuntu and installed pybind11. I also downloaded the lab files from GitHub.

In Task 1, I implemented an `add_bonus()` function in C++ and used `m.def()` to make it available in Python.

In Task 2, I practiced passing a Python list to a C++ vector and calculating the average score.

In Task 3, I worked on the `GradeBook` class, which allows users to add scores, count the number of scores, and calculate their average.

### 3. Problems I Encountered

At first, Ubuntu couldn't connect to GitHub, so I had trouble downloading the files. After checking the network settings and changing the WSL networking mode, I was able to download the project.

I also encountered some errors while editing the code. For example, I misplaced a bracket in C++, which caused a compilation error. Later, I had an indentation error in Python.

These problems helped me realize the importance of checking error messages carefully.

### 4. Reflection

This lab helped me understand the basic process of connecting Python and C++ using pybind11. I also became more familiar with compiling C++ code and testing it through Python.

Although I still need to refer to the instructions when writing some parts of the code, I feel that I have a better understanding of how the two languages can work together. I hope to become more comfortable with debugging and writing code independently through future labs.
