"""
CONSTANTE = "Variáveis" que não vão mudar
Evitar: para deixar o codigo menos complexo
Ter muitas condições no seu if
Ter muitas sub camadas 
Ex:
   Ex1:
       Ex2:
           ....
"""

velocidade = 61
local_carro = 90

RADAR_1 = 60 # velocidade maxima do radar é 1
LOCAL_1 = 100 # Local do radar
RADAR_RANGE = 1 # distância que o radar pega

MIN_RANGE = LOCAL_1 - RADAR_RANGE 
MAX_RANGE = LOCAL_1 + RADAR_RANGE 
multado = local_carro >= MIN_RANGE and MAX_RANGE

vel_acima = velocidade > RADAR_1

if vel_acima:
    ...#carro está com a velocidade acima

if multado and vel_acima :
    ...#carro foi multado
else:
    ...#carro passou