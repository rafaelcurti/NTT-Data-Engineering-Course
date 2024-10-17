# Operadores Lógicos

# and, or, not

print(1, True and True) 
print(2, True and False) 
print(3, False and False and False) 
print(4, False and False and True) 
print(5, True or True) 
print(6, True or False)
print(7, False or False)
print(8, False or False or True)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp2)
