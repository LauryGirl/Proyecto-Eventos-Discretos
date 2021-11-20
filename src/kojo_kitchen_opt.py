from utils.random_var_generation import uniform_generate, exp_generate
from random import choice
from utils.time_take import get_time

choice_ = [1, 2]

#cliente, mean
time_mean_2 = {}
totally_clients_2 = 0

def first_choice_take(SS, S, choice_):
    for i in range(4, len(SS)):
        if S[SS[i]] == choice_:
            return SS[i]
    return -1

def kojo_kitchen_sim_2(T):
    global choice_
    global time_mean_2
    global totally_clients_2

    t = Na = C1 = C2 = C3 = 0
    SS = [0]
    A = {}
    D = {}
    S = {}

    T0 = exp_generate(2)
    ta = T0
    t1 = t2 = t3 = float("inf")


    while True:
        if ta == min(ta, t1, t2, t3) and ta < T: #llega un nuevo cliente
            t = ta
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
        
            if len(SS) == 1 and SS[0] == 0:
                if select == 1:
                    SS.clear()
                    SS.append(1)
                    SS.append(Na)
                    SS.append(0)
                    SS.append(0)
                    Y1 = uniform_generate(3, 5)
                    t1 = t + Y1
                else:
                    SS.clear()
                    SS.append(1)
                    SS.append(0)
                    SS.append(Na)
                    SS.append(0)
                    Y2 = uniform_generate(5, 8)
                    t2 = t + Y2

            elif select == 1 and SS[1] == 0:
                SS[0] += 1
                SS[1] = Na
                Y1 = uniform_generate(3, 5)
                t1 = t + Y1
            
            elif select == 2 and SS[2] == 0:
                SS[0] += 1
                SS[2] = Na
                Y2 = uniform_generate(5, 8)
                t2 = t + Y2

            elif pick_hour and SS[0] >= 1 and SS[3] == 0:
                SS[0] += 1
                SS[3] = Na

                if select == 1:
                    Y3 = uniform_generate(3, 5)
                    t3 = t + Y3
                else:
                    Y3 = uniform_generate(5, 8)
                    t3 = t + Y3

            elif SS[0] > 1:
                SS[0] += 1
                SS.append(Na)
            
            """
            food_select = 'sandwich' if select == 1 else 'suchi'
            print("Llega el cliente " + str(Na) + " en el tiempo " + get_time(t) + " a realizar su pedido de " + food_select)
            """

        elif len(SS) > 1 and SS[1] != 0 and (t1 == min(ta, t1, t2, t3) or t1 == min(t1, t2, t3)): #se va un cliente del servidor 1
            t = t1
            C1 += 1

            ss = SS[1]

            D[SS[1]] = t

            if D[ss] - A[ss] - 5 >= 5:
                time_mean_2[ss] = D[ss] - A[ss] - 5

            if SS[0] == 1:
                SS.clear()
                SS.append(0)
                t1 = float("inf")

            elif SS[0] <= 3 and len(SS) < 5:
                n = SS[0] - 1
                i2 = SS[2]
                i3 = SS[3]
                SS.clear()
                SS.append(n)
                SS.append(0)
                SS.append(i2)
                SS.append(i3)
                t1 = float("inf")

            elif SS[0] >= 3:
                SS[0] -= 1
                i = first_choice_take(SS, S, 1)

                if i == -1:
                    SS[1] = 0
                    t1 = float("inf")
                else:
                    SS.remove(i)
                    SS[1] = i
                    Y1 = uniform_generate(3, 5)
                    t1 = t + Y1
            
            """
            food_select = 'sandwich' if S[ss] == 1 else 'suchi'

            if t > T:
                print("Restaurante cerrado: Se va el cliente " + str(ss) + " en el tiempo " + get_time(t) + " con su pedido de " + food_select + " (1)")
            else:
                print("Se va el cliente " + str(ss) + " en el tiempo " + get_time(t) + " con su pedido de " + food_select + " (1)")
            """

        elif len(SS) > 2 and SS[2] != 0 and (t2 == min(ta, t1, t2, t3) or t2 == min(t1, t2, t3)): #se va un cliente del servidor 2
            t = t2
            C2 += 1

            ss = SS[2]

            D[SS[2]] = t

            if D[ss] - A[ss] - 8 >= 5:
                time_mean_2[ss] = D[ss] - A[ss] - 8

            if SS[0] == 1:
                SS.clear()
                SS.append(0)
                t2 = float("inf")

            elif SS[0] <= 3 and len(SS) < 5:
                n = SS[0]
                i1 = SS[1]
                i3 = SS[3]
                SS.clear()
                SS.append(n - 1)
                SS.append(i1)
                SS.append(0)
                SS.append(i3)
                t2 = float("inf")
            
            elif SS[0] >= 3:
                SS[0] -= 1
                i = first_choice_take(SS, S, 2)
                if i == -1:
                    SS[2] = 0
                    t2 = float("inf")
                else:
                    SS.remove(i)
                    SS[2] = i
                    Y2 = uniform_generate(5, 8)
                    t2 = t + Y2
            
            food_select = 'sandwich' if S[ss] == 1 else 'suchi'

            """
            if t > T:
                print("Restaurante cerrado: Se va el cliente " + str(ss) + " en el tiempo " + get_time(t) + " con su pedido de " + food_select + " (2)")
            else:
                print("Se va el cliente " + str(ss) + " en el tiempo " + get_time(t) + " con su pedido de " + food_select + " (2)")
            """

        elif len(SS) > 3 and SS[3] != 0 and (t3 == min(ta, t1, t2, t3) or t3 == min(t1, t2, t3)): #se va un cliente del servidor 3
            t = t3
            C3 += 1

            ss = SS[3]

            D[SS[3]] = t

            if S[ss] == 1 and D[ss] - A[ss] - 5 >= 5:
                time_mean_2[ss] = D[ss] - A[ss] - 5
            elif S[ss] == 2 and D[ss] - A[ss] - 8 >= 5:
                time_mean_2[ss] = D[ss] - A[ss] - 8

            if SS[0] == 1:
                SS.clear()
                SS.append(0)
                t3 = float("inf")

            elif SS[0] <= 3 and len(SS) < 5:
                n = SS[0]
                i1 = SS[1]
                i2 = SS[2]
                SS.clear()
                SS.append(n - 1)
                SS.append(i1)
                SS.append(i2)
                SS.append(0)
                t3 = float("inf")
            
            elif SS[0] >= 3 and len(SS) >= 4:
                SS[0] -= 1
                i4 = SS[4]
                SS.remove(i4)
                SS[3] = i4
                if S[i4] == 1:
                    Y3 = uniform_generate(3, 5)
                    t3 = t + Y3
                else:
                    Y3 = uniform_generate(5, 8)
                    t3 = t + Y3
            """
            food_select = 'sandwich' if S[ss] == 1 else 'suchi'

            if t > T:
                print("Restaurante cerrado: Se va el cliente " + str(ss) + " en el tiempo " + get_time(t) + " con su pedido de " + food_select + " (3)")
            else:
                print("Se va el cliente " + str(ss) + " en el tiempo " + get_time(t) + " con su pedido de " + food_select + " (3)")
            """

        elif ta > T and t1 == float("inf") and t2 == float("inf") and t3 == float("inf"):
            #print("Restaurante cerrado, ya no quedan mas clientes en la cola")
            break
        
    
    totally_clients_2 = Na
    
    """
    print()
    print()

    print('****************************************************')
    print("Analisis de los clientes que esperan mas de 5 minutos:")
    print('****************************************************')

    print()
    print()

    for item in time_mean_2.keys():
        print( "El cliente " + str(item) + " espera mas de 5 minutos, exactamente " + str(int(time_mean_2[item])) + " minutos ")

    print()
    print()

    print('****************************************************')
    print("El porciento de los clientes que esperan mas de 5 min es " + str(len(time_mean_2.keys()) * 100 / totally_clients_2) + "%.")
    """

    return len(time_mean_2.keys()) * 100 / totally_clients_2, totally_clients_2
