#include <iostream>

class ParkingBill {
 public:
  explicit ParkingBill(int minutes) : m_minutes(minutes) {}
  virtual ~ParkingBill() {}
  virtual int Fee() const = 0;

 protected:
  int Minutes() const { return m_minutes; }

 private:
  int m_minutes;
};

class RegularBill : public ParkingBill {
 public:
  explicit RegularBill(int minutes) : ParkingBill(minutes) {}
  int Fee() const override {
    int fee = ((Minutes() + 59) / 60) * 20;
    return fee > 200 ? 200 : fee;
  }
};

class ShortStayBill : public ParkingBill {
 public:
  explicit ShortStayBill(int minutes) : ParkingBill(minutes) {}
  int Fee() const override {
    int paid_minutes = Minutes() > 30 ? Minutes() - 30 : 0;
    int fee = ((paid_minutes + 29) / 30) * 15;
    return fee > 180 ? 180 : fee;
  }
};

int main() {
  int n;
  if (!(std::cin >> n) || n < 0 || n > 1000) return 1;
  int total = 0;
  for (int i = 0; i < n; ++i) {
    int type, minutes;
    if (!(std::cin >> type >> minutes) || (type != 1 && type != 2) ||
        minutes < 0 || minutes > 1440) return 1;
    ParkingBill *bill;
    if (type == 1) bill = new RegularBill(minutes);
    else bill = new ShortStayBill(minutes);
    total += bill->Fee();
    delete bill;
  }
  std::cout << total << '\n';
}
