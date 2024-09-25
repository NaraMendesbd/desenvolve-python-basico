#Usando a função embutida map e criando uma função lambda, transforme uma lista com os raios de múltiplas circunferências 
# em uma nova lista com as respectivas áreas. O cálculo de cada área é dado por: pi*(raio**2)

# Use a constante pi da biblioteca math
# Arredonde o resultado para 2 casas decimais

import math
raios = [2, 3 ,4 ,5, 6]
áreas = list(map(lambda r: round(math.pi*(r**2), 2), raios))
print(áreas)