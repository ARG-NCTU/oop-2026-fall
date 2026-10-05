// AI-assisted implementation prepared on 2026-10-05.
#include <iostream>
#include <vector>

class Device {
public:
    virtual ~Device() = default;
    virtual bool use(int cost) = 0;
    virtual int remaining() const = 0;
};

class StandardDevice : public Device {
    int energy;

public:
    explicit StandardDevice(int initial) : energy(initial) {}

    bool use(int cost) override {
        if (cost > energy) return false;
        energy -= cost;
        return true;
    }

    int remaining() const override { return energy; }
};

class EfficientDevice : public Device {
    int energy;

public:
    explicit EfficientDevice(int initial) : energy(initial) {}

    bool use(int cost) override {
        const int required = cost / 2 + cost % 2;
        if (required > energy) return false;
        energy -= required;
        return true;
    }

    int remaining() const override { return energy; }
};

int main() {
    int device_count, request_count;
    if (!(std::cin >> device_count >> request_count)) return 0;

    std::vector<Device*> devices;
    for (int i = 0; i < device_count; ++i) {
        char kind;
        int initial;
        std::cin >> kind >> initial;
        if (kind == 'S') devices.push_back(new StandardDevice(initial));
        else devices.push_back(new EfficientDevice(initial));
    }

    for (int i = 0; i < request_count; ++i) {
        int index, cost;
        std::cin >> index >> cost;
        Device* device = devices[index];
        const bool accepted = device->use(cost);
        std::cout << (accepted ? "ACCEPT " : "REJECT ")
                  << device->remaining() << '\n';
    }

    for (Device* device : devices) delete device;
}
