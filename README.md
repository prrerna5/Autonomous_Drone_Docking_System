
# Autonomous Drone Docking System
<img width="711" height="800" alt="image" src="https://github.com/user-attachments/assets/8f783ee2-8142-4206-a46d-e3e44d3b9505" />

Overview

The Autonomous Drone Docking System is an intelligent unmanned aerial vehicle (UAV) platform developed using a Pixhawk Flight Controller and a Raspberry Pi companion computer.

The system is designed to improve autonomous drone operations through intelligent battery monitoring and mission management. By continuously tracking battery status during flight, the drone can make autonomous decisions to ensure safe operation without constant human supervision.

This project demonstrates the integration of embedded systems, autonomous flight control, MAVLink communication, and Python-based mission logic into a modular UAV platform suitable for long-duration operations.


# Problem Statement
Battery life remains one of the biggest challenges in autonomous drone operations. Applications such as military surveillance, disaster response, industrial inspection, and agricultural monitoring require drones to operate reliably over extended periods while minimizing manual intervention.

# Solution
The system continuously monitors the drone's battery level during flight. When the battery reaches a predefined threshold, the mission controller initiates an autonomous return procedure, ensuring safe recovery of the drone.


Features
- Custom-built quadcopter
- Pixhawk Flight Controller
- Raspberry Pi Companion Computer
- MAVLink Communication
- Autonomous Battery Monitoring
- Intelligent Mission Management
- GPS Navigation
- Return-to-Launch Logic
- Modular Python Architecture


Hardware Used
- Pixhawk 2.4.8 Flight Controller
- Raspberry Pi
- GPS Module
- Brushless Motors
- Electronic Speed Controllers (ESCs)
- LiPo Battery
- Telemetry Module
- Radio Controller


Software Stack
- Python
- DroneKit
- MAVLink
- ArduPilot
- Mission Planner


 Applications
- Military Surveillance
- Disaster Management
- Agriculture
- Industrial Inspection
- Border Security
- Search and Rescue



## Author
Prerna Rudra


