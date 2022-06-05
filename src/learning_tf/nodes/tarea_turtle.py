#!/usr/bin/env python  

import turtle_tf_listener
import subprocess

import time
exec(open("/home/javier/ROS_catkin_ws/src/learning_tf/nodes/turtle_tf_listener.py").read())


#p = subprocess.Popen(['python', '/home/javier/ROS_catkin_ws/src/learning_tf/nodes/turtle_tf_listener.py', 'arg1', 'arg2'])
#time.sleep(10)
#p.terminate()

#Suscribirse a rosout_agg
#rostopic echo /rosout_agg | grep msg > archivo.txt
#Detener ejecución de turtlesim
#Contar líneas del archivo wc -l archivo.txt
