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