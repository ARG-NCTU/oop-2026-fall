def uncalibrated_readings(readings, calibrations, tol):
    ans = []
    for r in readings:
        calibrated = False
        for c in calibrations:
            if c <= r:
                if r - c <= tol:
                    calibrated = True
                    break
            else:
                if c - r <= tol:
                    calibrated = True
                    break
                else: break
        if not calibrated and r not in ans:
            ans.append(r)
    return ans

readings = [25, 25, 25]
calibrations = [5]
tol = 2

print(uncalibrated_readings(readings, calibrations, tol))