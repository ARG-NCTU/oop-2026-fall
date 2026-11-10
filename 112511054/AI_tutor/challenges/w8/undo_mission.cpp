#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

struct State {
    std::int64_t energy;
    std::int64_t completed;
};

class Mission {
public:
    Mission(std::int64_t capacity, std::int64_t initial)
        : capacity_(capacity), current_{initial, 0} {}

    void charge(std::int64_t amount) {
        const auto delta = std::min(amount, capacity_ - current_.energy);
        if (delta == 0) return;
        history_.push_back(current_);
        current_.energy += delta;
    }

    void run(std::int64_t cost) {
        if (cost > current_.energy) return;
        history_.push_back(current_);
        current_.energy -= cost;
        ++current_.completed;
    }

    void undo() {
        if (history_.empty()) return;
        current_ = history_.back();
        history_.pop_back();
    }

    void print(std::ostream& out) const {
        out << current_.energy << ' ' << current_.completed << ' '
            << history_.size() << '\n';
    }

private:
    std::int64_t capacity_;
    State current_;
    std::vector<State> history_;
};

class Event {
public:
    virtual ~Event() = default;
    virtual void apply(Mission& mission) const = 0;
};

class ChargeEvent : public Event {
public:
    explicit ChargeEvent(std::int64_t amount) : amount_(amount) {}
    void apply(Mission& mission) const override { mission.charge(amount_); }
private:
    std::int64_t amount_;
};

class RunEvent : public Event {
public:
    explicit RunEvent(std::int64_t cost) : cost_(cost) {}
    void apply(Mission& mission) const override { mission.run(cost_); }
private:
    std::int64_t cost_;
};

class UndoEvent : public Event {
public:
    void apply(Mission& mission) const override { mission.undo(); }
};

void dispatch(const Event& event, Mission& mission) {
    event.apply(mission);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::int64_t capacity, initial;
    int n;
    if (!(std::cin >> capacity >> initial >> n)) return 0;
    Mission mission(capacity, initial);
    for (int i = 0; i < n; ++i) {
        std::string type;
        std::cin >> type;
        if (type == "UNDO") {
            UndoEvent event;
            dispatch(event, mission);
        } else {
            std::int64_t value;
            std::cin >> value;
            if (type == "CHARGE") {
                ChargeEvent event(value);
                dispatch(event, mission);
            } else {
                RunEvent event(value);
                dispatch(event, mission);
            }
        }
    }
    mission.print(std::cout);
}
