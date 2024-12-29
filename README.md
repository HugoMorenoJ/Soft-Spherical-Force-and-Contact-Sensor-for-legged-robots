# Soft Spherical Paw Sensor for Enhanced Proprioception and Force Measurement in Legged Robots.
In this repository you can find the code and videos about the article “Soft Spherical Paw Sensor for Enhanced Proprioception and Force Measurement in Legged Robots” which is a sensor based on flexible conductive membranes, has the ability to simultaneously provide the position of the contact point and the force exerted.

## Abstract

The adaptability of legged robots to uneven terrain and their minimal ground impact have driven significant research advancements, establishing them as ideal solutions for complex and delicate environments. Proprioception and environmental perception are critical for enhancing robot performance, as they are essential for maintaining dynamic balance and achieving precise control. This paper presents a novel soft contact and force sensor designed for quadrupedal robot legs' pads (end effectors). The innovative soft sensitive paw, made from flexible conductive membranes, simultaneously measures force and contact point position, enabling environmentally aware decision-making. Experimental tests demonstrate its soft, spherical design provides excellent adaptability and grip on various terrains. Its sensing surface covers 83.3\% of the sphere’s area, with a measurement error of only 0.14\%. This capability allows the sensitive paw to detect ground contact and lateral and upper leg interactions, offering a robust and versatile tool for navigation and operation in complex environments.
<img src="imagen2.png" width="500"/>

The figure shows a graphical representation of different situations that could lead to a contact at the same position but in different situations, and the response of the proposed sensor. a) no contact, b) contact with a corner or wall, c) contact with a rigid surface, d) contact with a moving or flexible surface.

## Sensor structure and testing
### Sensor structure
![Sensor structure](str.gif)
### Operating Sensor
![Operating Sensor](ope.gif)

### Demonstration video
https://github.com/HugoMorenoJ/Soft-Spherical-Force-and-Contact-Sensor-for-legged-robots/assets/20323834/2d300e93-8197-4f58-8291-f6e77cbac087
### Demonstration video
[![](https://markdown-videos.deta.dev/youtube/8-yymz5p5xQ&ab_channel=LAPYRCIO)](https://youtu.be/8-yymz5p5xQ?si=GBHS42JLNzOGRN_0)
## Requerimets
The package is made for ROS, the development board is an arduino mega 2560 and the manometric pressure sensor is a Mps20n0040d with Hx710b.

## Reference
If this code is useful for you please consider citing our work appropriately. Thanks.

## Contact
For more questions, please feel free to contact us.

* hugoamj@gmail.com
* luisandresmj@gmail.com
* gflorescolunga@gmail.com
