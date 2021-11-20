from kojo_kitchen_1 import kojo_kitchen_sim_1
from kojo_kitchen_opt import kojo_kitchen_sim_2

__author__ = 'Laura Brito Guerrero'

def start():
    """
    print("*****************************")
    print("Atendiendo dos empleados solamente (uno para el suchi y otro para el sandwich).")
    print("*****************************")
    """

    mean1, totally1 = kojo_kitchen_sim_1(11 * 60)

    """
    print()
    print()

    print("*****************************")
    print("Se emplea un tercer empleado para los periodos mas ocupados.")
    print("*****************************")
    """
    mean2, totally2 = kojo_kitchen_sim_2(11 * 60)

    return (mean1, totally1), (mean2, totally2)

if __name__ == '__main__':

    mean1, mean2 = start()
    print("El promedio de los clientes que esperan mas de 5 minutos en el puesto de comida con dos empleados solamente es de " + str(mean1[0]) + "% con " +  str(mean1[1]) + " clientes y cuando trabaja con un nuevo empleado en las horas pico es de " + str(mean2[0]) + "% con " + str(mean2[1]) + " clientes.")