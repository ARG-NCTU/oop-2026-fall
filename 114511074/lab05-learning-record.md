# Lab 05 Learning Record — MOOS-IvP

**Topic:** MOOS-IvP Introduction and Simulation  
**Date:** 2026/10/12

## Part A: What I Learned

This week, I learned some basic concepts of MOOS-IvP, which is a C++ framework for autonomous navigation. I learned that MOOSDB allows different applications to communicate, while the IvP Helm helps make navigation decisions.

I also practiced using Ubuntu to install MOOS-IvP and run a vehicle simulation. I am still not very familiar with the system, but I have a better understanding of how configuration files control vehicle behavior.

## Part B: Demo Practice

**Task 1: Change Vehicle Color**

I changed the vehicle color from yellow to blue by modifying `platform_color` in `alpha.moos`.

**Task 2: Create a Square Route**

I modified the waypoint coordinates in `alpha.bhv` to create a square route with four points.

**Task 3: Add Speed Buttons**

I added two buttons in `alpha.moos`:
- MUCHSLO: 1.0 m/s
- MUCHFST: 4.0 m/s

**Task 4: Change Turning Behavior**

I changed `turn_rate` from 95 to 50 and observed the vehicle turning during the simulation.

## Part C: Misconception (Before / After)

**Before:** I thought changing the vehicle's behavior required modifying complicated C++ code.

**After:** I learned that some behaviors can be changed by editing configuration files, such as `alpha.moos` and `alpha.bhv`.

## Part D: Reflection

I was able to complete the demo tasks by following the instructions step by step. However, I still need more practice because I am not familiar with many of the parameters. This lab helped me understand how different settings affect the simulated vehicle.

## Part E: What I'm Unsure About

I am still unsure how PID controllers affect the vehicle's turning behavior. I also want to understand more about how MOOSDB communicates with different applications.
