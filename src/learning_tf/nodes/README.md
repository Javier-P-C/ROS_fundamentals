#Cómo obtener número de colisiones
Corre el programa de launch en una nueva terminal: roslaunch learning_tf start_demo.launch
Después en terminal ejecuta el comando 

```
rostopic echo rosout_agg | grep msg > colisiones.txt
```

Una vez que termine de usar los nodos de turtlesim mata el comando anterior con ctrl+c
Finalmente ejecuta el comando

```
wc -l colisiones.txt
```
