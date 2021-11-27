def main():

    class Robot:

        def __init__(self, valor_articulacion, articulacion_nombre, robot_name):
            self.valor_articulacion = valor_articulacion
            self.articulacion_nombre = articulacion_nombre
            self.robot_name = robot_name

        def set_name(self):
            self.robot_name = input("Introduce el nuevo nombre del robot:\n")
            return self.robot_name

        def get_articulacion(self):
            return self.valor_articulacion
        

    Pose = Robot([[1.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
                [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 
                [0.0, 0.0, 1.0, 0.0, 0.0, 0.0], 
                [0.0, 0.0, 0.0, 1.0, 0.0, 0.0], 
                [0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 
                [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], ["Art1", "Art2", "Art3", "Art4", "Art5", "Art6"], "ROS Robot")

    Pose.set_name()
    Pose.get_articulacion()
    print("Nombre del robot: ", Pose.robot_name)

    for i in range (5):
        print(Pose.articulacion_nombre[i], Pose.valor_articulacion[i])

if __name__ == '__main__':
    main()