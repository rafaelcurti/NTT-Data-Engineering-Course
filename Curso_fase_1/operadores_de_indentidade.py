#Operadores de Identidade
# Verifica se ocupa a mesma posição de "memória"
# Operadores 'is' e 'is not'

saldo = 1000
limite = 1000

print(1, saldo is limite)
print(2, saldo is not limite)

saldo = 1000
limite = 500

print(1, saldo is limite)
print(2, saldo is not limite)