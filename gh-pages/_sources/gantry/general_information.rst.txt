
General Information
###################

Coordinate System
=================

The reference point of the gantry is the edge of the z-axis spindle mount as depicted in the image below.

.. image:: /res/images/gantry_reference_frame_annotation.jpg

The offset to the tank's coordinate system is measured relative to the tank's walls (**not** the steel frame).

According to the `localization package <https://github.com/HippoCampusRobotics/mu_auv_localization/blob/main/scripts/generate_tag_poses_yaml>`__ the offset in x-direction is 0.144m and 0.342m in y-direction. 

Motion Controllers
==================

The x- and z-axis are driven by Motion Controllers V1.0. The manual of these controllers is hard to come by these days. So :download:`here </res/manuals/mcdc2805.pdf>` is the PDF. The y-axis has a newer conroller. Probably V2.5. Faulhaber has an Application Note `AN103 <https://www.faulhaber.com/fileadmin/Import/Media/AN103_EN.pdf>`__ describing the differences between the older and the newer controller types. Can't say it is of much use (Lennart)

.. note:: If you use the Motion Manager, keep in mind that you need Motion Manager 5 for the older MCs instead of version 6. 

Motors
======

The axes are driven by Faulhaber motors. For the x- and z-axis the motor model is 3564k024b. The nominal rotational speed is 7700 RPM (`datasheet <https://www.faulhaber.com/fileadmin/Import/Media/DE_3564_B_CX_DFF.pdf>`__). The y-axis is driven by a newer model of the 3268 BX4 series. Its nominal rotational speed is 4890 (`datasheet <https://www.faulhaber.com/fileadmin/Import/Media/EN_3268_BX4_DFF.pdf>`__). 

