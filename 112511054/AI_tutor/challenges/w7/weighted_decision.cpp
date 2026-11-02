#include <iostream>

int main() {
  int n, m;
  if (!(std::cin >> n >> m) || n < 0 || n > 14760 || m < 1 || m > 20)
    return 1;

  long long weights[20];
  for (int j = 0; j < m; ++j) {
    if (!(std::cin >> weights[j]) || weights[j] < 0 || weights[j] > 1000000000LL)
      return 1;
  }

  bool found = false;
  int best_heading = 0, best_speed = 0;
  long long best_score = 0;
  for (int i = 0; i < n; ++i) {
    int heading, speed, allowed;
    if (!(std::cin >> heading >> speed >> allowed) ||
        heading < 0 || heading > 359 || speed < 0 || speed > 40 ||
        (allowed != 0 && allowed != 1)) return 1;

    long long score = 0;
    for (int j = 0; j < m; ++j) {
      int utility;
      if (!(std::cin >> utility) || utility < 0 || utility > 100) return 1;
      score += weights[j] * utility;
    }

    if (allowed == 0) continue;
    if (!found || score > best_score ||
        (score == best_score && speed < best_speed) ||
        (score == best_score && speed == best_speed && heading < best_heading)) {
      found = true;
      best_heading = heading;
      best_speed = speed;
      best_score = score;
    }
  }

  if (!found) std::cout << "-1\n";
  else std::cout << best_heading << ' ' << best_speed << ' ' << best_score << '\n';
}
