def process_readings(readings):
    result = []

    for reading in readings:
        name = reading[0]
        value = reading[1]
        calibration_factor = reading[2]

        try:
            calibrated_value = value / calibration_factor

        except ZeroDivisionError:
            calibrated_value = "INVALID"

        except TypeError:
            raise ValueError("Calibration factor must be a number")

        result.append([name, calibrated_value])

    return result