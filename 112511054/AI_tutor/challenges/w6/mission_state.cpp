#include <iostream>
#include <string>

class MessageApp {
 public:
  virtual ~MessageApp() {}
  virtual void OnNewMail(const std::string &key, int value) = 0;
  virtual void Iterate() const = 0;
};

class MissionApp : public MessageApp {
 public:
  void OnNewMail(const std::string &key, int value) override {
    if (key == "DEPLOY") {
      m_deployed = true;
      m_returning = false;
      m_manual = false;
      m_done = false;
    } else if (key == "RETURN") {
      if (m_deployed) m_returning = true;
    } else if (key == "SPEED") {
      m_survey_speed = value;
    } else if (key == "MANUAL") {
      m_manual = value == 1;
    } else if (key == "REACHED" && m_deployed && !m_manual) {
      if (!m_returning) {
        m_returning = true;
      } else {
        m_deployed = false;
        m_returning = false;
        m_done = true;
      }
    }
  }

  void Iterate() const override {
    if (!m_deployed) std::cout << (m_done ? "DONE" : "PARK") << " 0\n";
    else if (m_manual) std::cout << "PARK 0\n";
    else if (m_returning) std::cout << "RETURN 2\n";
    else std::cout << "SURVEY " << m_survey_speed << '\n';
  }

 private:
  bool m_deployed = false;
  bool m_returning = false;
  bool m_manual = true;
  bool m_done = false;
  int m_survey_speed = 3;
};

int main() {
  int n;
  if (!(std::cin >> n) || n < 0 || n > 100000) return 1;
  MissionApp mission;
  MessageApp &app = mission;
  for (int i = 0; i < n; ++i) {
    std::string command;
    int value = 0;
    if (!(std::cin >> command)) return 1;
    if (command == "SPEED" || command == "MANUAL") {
      if (!(std::cin >> value)) return 1;
      if (command == "SPEED" && (value < 0 || value > 4)) return 1;
      if (command == "MANUAL" && value != 0 && value != 1) return 1;
    } else if (command != "DEPLOY" && command != "RETURN" && command != "REACHED") {
      return 1;
    }
    app.OnNewMail(command, value);
  }
  app.Iterate();
}
