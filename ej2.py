""" 3.b. Se desea calcular la distancia recorrida (m) por un móvil que tiene velocidad (float) 
constante (m/s) durante un tiempo (int) t (s), considerar que es un MRU (Movimiento Rectilíneo Uniforme).
Se sabe que el cálculo de la velocidad en MRU es por formula: V = D/T,
despejando la distancia se tiene: D = V * T """


print("calcularemos la distancia \n")

velocidad = float(input("ingrese la velocidad en m/s \n"))
tiempo = int(input("ingrese el tiempo \n"))

distancia = velocidad * tiempo

print(f"la distancia fue de {distancia} metros")