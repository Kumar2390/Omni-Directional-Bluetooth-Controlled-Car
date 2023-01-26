# 🌐Omni-Directional-Bluetooth-Controlled-Car
An omni-directional robot can move in any direction, forward/backward but also sideways left/right, and turn on the spot, thanks to its wheels, giving the robot omnidirectional capabilities for movement on the horizontal axis on a drivetrain, as well as forward and backward movement

---

## 🗒️ Introduction Of the IOT based Project

It is a vehicle used to move in all directions. Our project aims at designing a Omni
directional robot equipped with four Omni wheels, mounted at 90 degree apart. These
wheels are mounted on DC motors which will be driven by L298N motor drivers.
 Application control vehicle is a high-tech product based on Bluetooth control, which is
a new product combining electronic technology, information technology and vehicle
control technology. The vehicle digital control technology is to make full use of the
characteristics of digital technology, such as accuracy, speed and easy to transmit. It
can change the driver's intention and vehicle operation status information into code
through intelligent detection device, and convert and process these codes through
computer, and finally complete the vehicle control through the Executive device. Key
technical issues include vehicle automatic operation technology, remote transmission
technology, motor drive technology, etc

The development of this project is a Mecanum Wheel based car that can be controlled
by Bluetooth, which is convenient to explore some places that are not convenient for
people to enter. At the same time, the adaptability of this Bluetooth controlled car to
the road is better than that of the general four-wheel car. The sports platform can be
equipped with wireless camera, manipulator and other modules to complete more
complex functions

---
## ❓ Problem identification and Problem Formulation:
- The design is based on 51 series single-chip microcomputer control. The tracked
vehicle has two modes of Bluetooth remote control and autonomous driving. In the
remote control mode, the control signal is sent out through the Bluetooth module
controller. The Bluetooth module on the car decodes the received information, feeds
back the information to the single-chip microcomputer, which processes the obtained
information, and then uses the DC motor driver to control the start and stop of the directcurrent motor and the speed adjustment through PWM
- In the autonomous motion
mode, the tracked vehicle can use its own infrared sensor to complete the autonomous
scanning of the area. This design mainly from the mecanum wheel based body design,
mobile application control, PWM speed control and other aspects of the design and
development. 
- Turn on the car switch, select the Bluetooth signal emitted by the corresponding key of
the remote control in the remote control mode, and the infrared receiving module
receives the Bluetooth signal. The single chip microcomputer analyzes the received
Bluetooth signal to determine whether it is the manual mode or the automatic mode.
When entering the manual mode, press the command button on the mobile application
to send out the corresponding Bluetooth signal.

---


## :fire: Objective of the Project:

- In this project, we will learn how to make a Bluetooth control car with a Raspberry Pico
board. For that, I used the Bluetooth module and a mobile application to control the car.
But, you have to use HC-05 module. After that only we can control the car using any
mobile application. Also, I used four gear motors, and the two L298N motor driver and
three DC 7-12V battery was used to power up these motors.
- You can use a car chassis for this project. But I built this car with a low budget.
Therefore, I have used a piece of Sun board for this car

---

## :bulb: Technologies Used

### Micro-Python

### Components/Items Required:

<img src="Omni-Directional Bluetooth Controlled Car/Photo/Components.png" >



---
## :iphone: Screenshots



<img src="Omni-Directional Bluetooth Controlled Car/Photo/L298n Motor Module Connection with Mecanum wheels.png">
<img src="Omni-Directional Bluetooth Controlled Car/Photo/Raspberry Pi Pico Connected to the L298n Motor Module.png">
<img src="Omni-Directional Bluetooth Controlled Car/Photo/Mecanum wheel with motor.png">
<img src="Omni-Directional Bluetooth Controlled Car/Photo/HC-05 Pinned in Raspberry Pi Pico.png">
<img src="Omni-Directional Bluetooth Controlled Car/Photo/L298n Motor driver connected with Pico.png">
<img src="Omni-Directional Bluetooth Controlled Car/Photo/Position of all four wheels.png">
<img src="Omni-Directional Bluetooth Controlled Car/Photo/Three 3.7V Battery Giving the power to the motor.png">
<img src="Omni-Directional Bluetooth Controlled Car/Photo/Final Prototype of the Project.png">
<img src="Omni-Directional Bluetooth Controlled Car/Photo/Final Packaging.jpg">


---

## :man: Project Created & Maintained By

<img src = "Omni-Directional Bluetooth Controlled Car/Photo/profile.jpg"  height="130" alt=""> <br>Ashwini Kumar Behera
<p>
<a href = "https://github.com/Kumar2390"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/ashwini-kumar-behera-14a9a4215/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
