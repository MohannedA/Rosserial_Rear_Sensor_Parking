# Rosserial Rear Sensor Parking
Simple Turtlebot2 parking program using Rosserial rear sensor

## The Program Does The Following...

* [ros_range_sensor.ino](https://github.com/MohannedA/Rosserial_Rear_Sensor_Parking/blob/master/ros_range_sensor/ros_range_sensor.ino): publish Arduino ultrasonic sensor's recordings via Rosserial to 'ultrasound_range' topic.
* [arduino_echo_distance.py](https://github.com/MohannedA/Rosserial_Rear_Sensor_Parking/blob/master/arduino_echo_distance.py): subscribe to 'ultrasound_range' topic to get sensor's readings and slow as the robot get closer to an object and stop if distance < 0.7m.
