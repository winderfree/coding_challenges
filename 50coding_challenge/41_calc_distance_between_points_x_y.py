# 41. Create a function to calculate the distance 
# between two points defined by their x, y 
# coordinates
import math
def distance_between(*coor):
    distance = pow(coor[0]-coor[1], 2) + pow(coor[2]-coor[3], 2)
    print(f'Raiz de {distance}')
    return math.sqrt(distance)
print(distance_between(-3,2,2,1))
# # print(distance_between(-3,2,2,1))
"""
El cálculo de distancia entre dos puntos es una herramienta esencial en diversos campos, desde la geometría hasta la navegación y la ciencia de datos. Nos permite medir la separación entre dos ubicaciones en un espacio, ya sea en un plano bidimensional o en un espacio tridimensional. Esta noción de distancia no solo es fundamental en matemáticas, sino que también tiene aplicaciones prácticas en el mundo real, como calcular la distancia entre ciudades en un mapa, determinar la proximidad entre objetos en un espacio tridimensional o incluso evaluar similitudes entre conjuntos de datos.

Ya sea que te sumerjas en el mundo de las coordenadas cartesianas en el plano o que explores las dimensiones más allá, el cálculo de distancia entre dos puntos te proporcionará una base sólida para comprender las relaciones espaciales y aplicar tus conocimientos en una variedad de disciplinas. ¡Comencemos a medir distancias y a explorar la importancia de este concepto fundamental!
"""