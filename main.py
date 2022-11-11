from random import uniform

from modulos.function_menus import *

# saldos en pesos y dolares generados de manera aleatoria con uniform() del modulo random
saldo = round(uniform(1, 30000),2)
dolar= round(uniform(0, 2000),2)


# menu ejecucion del cajero
menu_bienvenida(saldo,dolar)