# DAY 0

## Goal

- Able to run `ros2` commands without errors
- Able to run a ROS 2 demo (turtlesim / minimal pub-sub)

## Done

- on my M2 Macbook, installed
  - UTM
  - Ubuntu: 22.04.5 LTS (more compatible with ROS 2 Humble, while 24.04 is for Jazzy)
  - both Ubuntu Server and Desktop
  - ROS
  - colcon
- ran the two demos: turtlesim / minimal pub-sub

## Learned

- What are the differences between: Perception / Planning / Control
- understand what layer cmd_vel is in
- ROS 2 vs bare metal
- know what is Nav2
- real-time vs. fast (Deterministic Latency)

# DAY 1

## Goal

- Understand the core ROS2 communication model: Topic-based publish/subscribe
- Learn how to debug using the CLI
- Set up Mac IDE for ROS2 development on Ubuntu VM

## Done

- Troubleshot why the UTM shared folder is not accessible
  - not compatible with Mac's ARM64 architecture
- Changed to use SSHFS
  - successfully mounted the shared folder
- Tried CLI commands (echo, hz, info, etc.)
- Created a workspace and package from scratch

## Learned

- setup SSHFS
- create a new workspace and package


# DAY 2

## Goal

- Learn how to use ROS2 services
- Understand the difference between services and topics
- Implement a simple service server and client

## Done
- Created a service server that adds two integers
- Created a service client that calls the add_two_ints service
- Tested the service using the CLI and Python scripts

## Learned
* **Nodes** are the fundamental building blocks, acting as individual microservices that handle specific tasks like sensing or planning.
* **Topics** enable asynchronous, many-to-many data streams ideal for continuous information like sensor feeds.
* **Services** provide a synchronous request-response mechanism for one-off tasks such as toggling a switch or checking status.
* **Actions** manage long-running, cancelable goals that require continuous progress feedback, such as navigating to a room.
* **Perception** nodes process raw data from sensors to create a high-level understanding of the robot's environment.
* **Planning** nodes use perception data to make high-level decisions and calculate the optimal path to a goal.
* **Controllers** translate abstract paths into concrete velocity commands, commonly referred to as **cmd_vel**.
* **QoS (Quality of Service)** settings allow you to tune communication to prioritize the latest data over guaranteed delivery.
* **TF (Transform)** is a system for tracking and calculating the mathematical relationships between different coordinate frames.
* **Odom** is a local reference frame that provides smooth, continuous movement data but drifts over time.
* **Map** is a globally accurate reference frame used by SLAM systems to correct errors in the odometer’s position.


# DAY 3
## Goal
* learn Action and how it differs from Service and Topic

## Done
* played with Fibonacci Action example
* found out that ROS2 CLI does not support Action yet

## Learned
* Why are "map" and "odom" separated?
* Why does SLAM only modify the "map -> odom" transform?
* Why should the local controller not depend on the "map" frame?
* Why should loop closure not affect the continuity of motion?
* Understood TF tree and different kinds of "TF tree is broken"
* lenrned robotic system architecture: power -> mcu -> linux -> ros2 -> application -> cloud