"""AI-assisted implementation prepared on 2026-10-05."""


class Parcel:
    next_tracking = 1

    def __init__(self, weight):
        self.weight = weight
        self.tracking = Parcel.next_tracking
        Parcel.next_tracking += 1

    def quote(self):
        raise NotImplementedError

    def __str__(self):
        return f"{self.tracking:03d}:{self.quote()}"


class StandardParcel(Parcel):
    def quote(self):
        return 5 + 2 * self.weight


class ExpressParcel(Parcel):
    def quote(self):
        return 10 + 3 * self.weight


def shipping_quotes(descriptions):
    parcels = []
    for kind, weight in descriptions:
        if kind == "S":
            parcels.append(StandardParcel(weight))
        else:
            parcels.append(ExpressParcel(weight))

    labels = []
    total = 0
    for parcel in parcels:
        labels.append(str(parcel))
        total += parcel.quote()
    return labels, total
