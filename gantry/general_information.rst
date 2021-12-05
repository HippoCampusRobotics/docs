
General Information
###################

Coordinate System
=================

The reference point of the gantry is the edge of the z-axis spindle mount as depicted in the image below.

.. image:: /res/images/gantry_reference_frame_annotation.jpg

The offset to the tank's coordinate system is measured relative to the tank's walls (**not** the steel frame).

According to the `localization package <https://github.com/HippoCampusRobotics/mu_auv_localization/blob/main/scripts/generate_tag_poses_yaml>`__ the offset in x-direction is 0.144m and 0.342m in y-direction. 

Motors
======

The axes are driven by Faulhaber motors. For the x- and z-axis the motor model is 3564k024b. The nominal rotational speed is 7700 RPM (`datasheet <https://www.faulhaber.com/fileadmin/Import/Media/DE_3564_B_CX_DFF.pdf>`__). The y-axis is driven by a newer model of the 3268 BX4 series. Its nominal rotational speed is 4890 (`datasheet <https://www.faulhaber.com/fileadmin/Import/Media/EN_3268_BX4_DFF.pdf>`__). 

