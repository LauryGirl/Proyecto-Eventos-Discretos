from utils.random_var_generation import exp_generate, uniform_generate
from random import choice
from utils.time_take import get_time

#cliente, mean
time_mean = {}
totally_clients = 0

choice_ = [1, 2]

def kojo_kitchen_sim_1(T):
    global totally_clients
    global time_mean

    t = 0

    Na = 0
    Nd = 0

    Na_1 = []
    Na_2 = []

    n = 0
    A = {}
    D = {}
    S = {}
    
    Tp = 0

    T0 = exp_generate(2)
    ta = T0
    t1 = t2 = float("inf")
    C1 = C2 = 0

    while True:
        if ta == min(ta, t1, t2) and ta < T: #llega un nuevo cliente
            t = ta
            n += 1
            Na += 1

            pick_hour = (t >= (1.5 * 60) and t <= (3.5 * 60)) or (t >= (8 * 60) and t <= (10 * 60))

            if pick_hour:
                Tt = exp_generate(1/5)
            else:
                Tt = exp_generate(1/60)

            ta = t + Tt
            A[Na] = t

            select = choice(choice_)   
            S[Na] = select   

            if select == 1:
                if len(Na_1) == 0:
                    Y1 = uniform_generate(3, 5)
                    t1 = t + Y1
                Na_1.append(Na)
            else:
                if len(Na_2) == 0:
                    Y2 = uniform_generate(5, 8)
                    t2 = t + Y2
                Na_2.append(Na)

            """
            food_select = 'sandwich' if select == 1 else 'suchi'
            print("Llega el cliente " + str(Na) + " en el tiempo " + get_time(t) + " a realizar su pedido de " + food_select)
            """

        if t1 == min(ta, t1, t2) and t1 <= T:
            #se va un cliente del sandwich
            if n > 0 and len(Na_1) > 0:
                t = t1
                Nd += 1
                n -= 1
                N = Na_1[0]
                Na_1.remove(N)
                C1 += 1
                D[N] = t

                if D[N] - A[N] - 5 >= 5:
                    time_mean[N] = D[N] - A[N] - 5

                """
                food_select = 'sandwich' if S[N] == 1 else 'suchi'
                print("Se va el cliente " +  str(N) +  " en el tiempo " + get_time(t) + " con su pedido de " + food_select)
                """

                if len(Na_1) == 0:
                    t1 = float("inf")
                else:
                    Y1 = uniform_generate(3, 5)
                    t1 = t + Y1
            else:
                t1 = float("inf")
 

        if t2 == min(ta, t1, t2) and t2 <= T:
            #se va un cliente del suchi
            if n > 0 and len(Na_2) > 0:
                t = t2
                Nd += 1
                n -= 1
                N = Na_2[0]
                Na_2.remove(N)
                C2 += 1
                D[N] = t

                if D[N] - A[N] - 8 >= 5:
                    time_mean[N] = D[N] - A[N] - 8

                """
                food_select = 'sandwich' if S[N] == 1 else 'suchi'
                print("Se va el cliente " +  str(N) +  " en el tiempo " + get_time(t) + " con su pedido de " + food_select)
                """

                if len(Na_2) == 0:
                    t2 = float("inf")
                else:
                    Y2 = uniform_generate(5, 8)
                    t2 = t + Y2
            else:
                t2 = float("inf")

        if t1 == min(ta, t1, t2) > T and len(Na_1) > 0:
            #se acabo el tiempo y se terminan de atender los clientes del sandwich
            t = t1
            Nd += 1
            n -= 1
            C1 += 1
            N = Na_1[0]
            Na_1.remove(N)
            D[N] = t

            """
            food_select = 'sandwich' if S[N] == 1 else 'suchi'
            print("Restaurante cerrado: Se va el cliente " +  str(N) +  " en el tiempo " + get_time(t) + " con su pedido de " + food_select)
            """

            if len(Na_1) == 0:
                t1 = float("inf")
            else:
                Y1 = uniform_generate(3, 5)
                t1 = t + Y1

            if D[N] - A[N] - 5 > 5:
                time_mean[N] = D[N] - A[N] - 5

        if t2 == min(ta, t1, t2) > T and len(Na_2) > 0:
            #se acabo el tiempo y se terminan de atender los clientes del suchi
            t = t2
            Nd += 1
            n -= 1
            C2 += 1
            N = Na_2[0]
            Na_2.remove(N)
            D[N] = t

            """
            food_select = 'sandwich' if S[N] == 1 else 'suchi'
            print("Restaurante cerrado: Se va el cliente " +  str(N) +  " en el tiempo " + get_time(t) + " con su pedido de " + food_select)
            """

            if len(Na_2) == 0:
                t2 = float("inf")
            else:
                Y2 = uniform_generate(5, 8)
                t2 = t + Y2

            if D[N] - A[N] - 8 > 5:
                time_mean[N] = D[N] - A[N] - 8

            
        if min(ta, t1, t2) > T and n == 0: #se acabo el tiempo para recibir clientes y ya se atendieron los q quedaban
            #Tp es el tiempo q se atendieron clientes luego de T
            #print("Restaurante cerrado y ya no quedan clientes")
            Tp = max(t - T, 0)
            break
    
    totally_clients = Nd

    """
    print()
    print()

    print('****************************************************')
    print("Analisis de los clientes que esperan mas de 5 minutos:")
    print('****************************************************')

    print()
    print()

    for item in time_mean.keys():
        print( "El cliente " + str(item) + " espera mas de 5 minutos, exactamente " + str(int(time_mean[item])) + " minutos ")

    print()
    print()

    print('****************************************************')
    print("El porciento de los clientes que esperan mas de 5 min es " + str(len(time_mean.keys()) * 100 / totally_clients) + "%.")
    """

    return len(time_mean.keys()) * 100 / totally_clients, totally_clients