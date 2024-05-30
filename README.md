# Soft-Spherical-Force-and-Contact-Sensor-for-legged-robots
In this repository you can find the code and videos about the article “Robust Soft Spherical Force and Contact Sensor for legged robots” which is a sensor based on flexible conductive membranes, has the ability to simultaneously provide the position of the contact point and the force exerted.

## Abstract
Currently, research on legged robots, especially quadrupeds, has seen a significant increase due to the many advantages they offer over their wheeled or crawled counterparts in a variety of fields and for a variety of tasks. These robots are more adaptable to uneven terrain and cause less damage to the ground, making them ideal for complex and delicate environments. Proprioception and perception of the environment are key aspects in these robots, as they must maintain dynamic balance while moving. Access to more information about the environment allows for more precise and efficient control. In this context, the present work proposes a novel soft contact and force sensor for the pads (end effectors) of the legs of these robots. This innovative sensor, based on flexible conductive membranes, has the ability to simultaneously provide the contact point position and the force exerted, giving the robot the ability to make decisions based on the specific situation. In addition, the smooth and spherical nature of this sensor not only improves its capabilities compared to the state of the art, but also allows it to better adapt to the terrain, improve grip, and has a sensing surface that covers 83.3% of the sphere, this sensor is able to detect contact with the ground, as well as lateral and even upper leg interactions. These features provide the robot with a more robust and versatile tool for navigating and operating in complex environments.

<img src="imagen2.png" width="500"/>

The figure shows a graphical representation of different situations that could lead to a contact at the same position but in different situations, and the response of the proposed sensor. a) no contact, b) contact with a corner or wall, c) contact with a rigid surface, d) contact with a moving or flexible surface.

## Sensor structure and testing
### Sensor structure
![Sensor structure](str.gif)
### Operating Sensor
![Operating Sensor](ope.gif)

## Requerimets
The package is made for ROS, the development board is an arduino mega 2560 and the manometric pressure sensor is a Mps20n0040d with Hx710b.

## Reference
If this code is useful for you please consider citing our work appropriately. Thanks.

## Contact
For more questions, please feel free to contact us.

* hugoamj@gmail.com
* luisandresmj@gmail.com
* gflorescolunga@gmail.com
