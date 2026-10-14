// W5 transfer challenge: polymorphic task scheduling.
// Implementation prepared with AI assistance.
#include <iostream>

void clamp_nonnegative(int &value) {
  if (value < 0) value = 0;
}

class BaseTask {
 public:
  explicit BaseTask(int work) : m_remaining(work) {}
  virtual ~BaseTask() {}
  virtual void Step() = 0;
  int Remaining() const { return m_remaining; }

 protected:
  void Consume(int amount) {
    m_remaining -= amount;
    clamp_nonnegative(m_remaining);
  }

 private:
  int m_remaining;
};

class SlowTask : public BaseTask {
 public:
  explicit SlowTask(int work) : BaseTask(work) {}
  void Step() override { Consume(1); }
};

class FastTask : public BaseTask {
 public:
  explicit FastTask(int work) : BaseTask(work) {}
  void Step() override { Consume(2); }
};

int main() {
  int n, rounds;
  if (!(std::cin >> n >> rounds)) return 1;
  if (n < 0 || n > 1000 || rounds < 0 || rounds > 1000) return 1;

  BaseTask **tasks = new BaseTask *[n];
  for (int i = 0; i < n; ++i) {
    int type, work;
    if (!(std::cin >> type >> work) || (type != 1 && type != 2) ||
        work < 0 || work > 1000) {
      for (int j = 0; j < i; ++j) delete tasks[j];
      delete[] tasks;
      return 1;
    }
    if (type == 1) tasks[i] = new SlowTask(work);
    else tasks[i] = new FastTask(work);
  }

  for (int r = 0; r < rounds; ++r) {
    for (int i = 0; i < n; ++i) tasks[i]->Step();
  }

  int total = 0;
  for (int i = 0; i < n; ++i) {
    total += tasks[i]->Remaining();
    delete tasks[i];
  }
  delete[] tasks;
  std::cout << total << '\n';
  return 0;
}
