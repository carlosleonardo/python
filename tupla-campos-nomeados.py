print("Tupla de campos nomeados (NamedTuple)")
from collections import namedtuple
# Definindo uma tupla de campos nomeados para representar um ponto 2D
Ponto = namedtuple('Ponto', ['x', 'y'])

# Criando uma instância da tupla de campos nomeados
ponto1 = Ponto(3, 4)
print("Ponto 1:", ponto1)
print("Coordenada x do ponto 1:", ponto1.x)
print("Coordenada y do ponto 1:", ponto1.y)