import random
import math

def uniform_generate(a, b):
    u = random.random()
    return a + (b - a) * u

def normal(mean, var):
    x = 0
    while True:
        y = exp_generate(1)
        u = random()
        c = math.exp((-(y - 1)**2) / 2)
        if u <= c:
            x = mean + var*y
            break 
    return x

def exp_generate(lambda_):
    u = random.random()
    return - (1 / lambda_) * math.log(u)

def poisson_process_generate(T, lambda_):
    t = 0
    I = 0 # numero de eventos que ocurrieron en T unidades de tiempo
    S = {} # tiempos de ocurrencia de cada evento en orden creciente

    while True:
        u = random.random()
        t = t - (1 / lambda_) * math.log(u)
        if t > T:
            break
        I += 1
        S[I] = t
    
    return I, S

def poisson_process_heterogeneous_generate(T, lambda_func):
    lambda_ = max(lambda_func)
    t = 0
    I = 0
    S = {}

    while True:
        u = uniform_generate(0, 1)
        t = t - (1 / lambda_) * math.log(u)
        if t > T:
            break
        
        u1 = random.random()
        if u1 <= lambda_func[int(t)] / lambda_:
            I += 1
            S[I] = t
    
    return I, S
