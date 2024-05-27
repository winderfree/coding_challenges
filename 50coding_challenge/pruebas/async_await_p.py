import asyncio
import time
async def  fun_asyn(nombre):
    print("before sleep")
    time.sleep(4)
    print(" after sleep")
    saludo = f'Hola {nombre}, a las {time.process_time()}'
    print (saludo)
asyncio.run(fun_asyn("Juan Casado")) 

# diccionario = {}
# diccionario.update({"nombre": "Juan"})
# print(diccionario["nombre"])