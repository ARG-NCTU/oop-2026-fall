"""Process usage requests for regular devices and devices with reserved quota."""


class Device:
    def __init__(self, device_id, quota):
        self.device_id = device_id
        self.quota = quota

    def use(self, amount):
        if 0 <= amount <= self.quota:
            self.quota -= amount
            return True
        return False


class ReservedDevice(Device):
    def __init__(self, device_id, quota, reserve):
        super().__init__(device_id, quota)
        self.reserve = reserve

    def use(self, amount):
        if self.quota - amount < self.reserve:
            return False
        return super().use(amount)


def process_requests(devices, requests):
    """Return one result per request and the remaining quotas in device order."""
    by_id = {device.device_id: device for device in devices}
    results = []
    for device_id, amount in requests:
        device = by_id.get(device_id)
        results.append(device is not None and device.use(amount))
    return results, [device.quota for device in devices]


if __name__ == "__main__":
    print(process_requests([Device("E", 5)], [("E", 5), ("E", 1)]))

