
# week7 Learning Record – MOOS-IvP

**Topic:** MOOS-IvP Behavior, PWT, and IvP Helm  
**Date:** 2026/10/19

## Part A: What I Learned

This week, I learned more about MOOS-IvP and how the IvP Helm makes decisions when different behaviors have different goals.

I learned that PWT represents the priority weight of a behavior. The IvP Helm combines the utility functions of different behaviors to choose a heading and speed.

I am still not very familiar with all the parameters, but I have a better understanding of how different PWT values affect the vehicle's movement.

## Part B: Demo Practice

**Task 1: Observe Different Cases**

I ran four simulation cases and observed the vehicle's behavior.

- Case 1: The vehicle moved northeast because the east and north behaviors had equal PWT values.
- Case 2: The vehicle moved more toward the east because the east behavior had a higher PWT.
- Case 3: The vehicle initially did not move.
- Case 4: The vehicle moved almost directly east because the north behavior had a PWT of zero.

**Task 2: Understand PWT Scaling**

I learned that multiplying both PWT values by the same positive number does not change their relative importance, so the decision should remain the same when only these two behaviors are considered.

**Task 3: Investigate Case 3**

In Case 3, the vehicle did not move because the behaviors did not provide a strong enough preference for a nonzero speed.

I learned that BHV_ConstantHeading mainly controls the heading rather than setting a specific target speed.

**Task 4: Make Case 3 Move**

I added BHV_ConstantSpeed in `meta_tug.bhv` and set the desired speed to 2.0 m/s with a PWT of 100.

I also used `#ifdef CASE 3` so the new behavior would only be included in Case 3.

After modifying the configuration, the vehicle successfully moved north at approximately 2.0 m/s without removing the original PWT values.

## Part C: Misconception (Before / After)

**Before:** I thought that setting a high priority for a heading behavior would always make the vehicle move in that direction.

**After:** I learned that heading and speed are different parts of the decision. A vehicle may have a preferred heading but still remain stationary if the resulting decision chooses zero speed.

## Part D: Reflection

I completed the simulation tasks by following the instructions step by step. At first, I did not understand why Case 3 was not moving, and I was not sure how to modify the behavior file.

After adding BHV_ConstantSpeed and testing the simulation again, I understood more about how different behaviors work together.

I still need more practice with MOOS-IvP configuration files, but this lab helped me understand how PWT and behavior settings affect the final movement of a vehicle.

## Part E: What I'm Unsure About

I am still unsure how the IvP Helm calculates the utility functions in detail and why some combinations of PWT values produce unexpected speeds.

I also want to learn more about how to choose suitable PWT values when several behaviors are active at the same time.
