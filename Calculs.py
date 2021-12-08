a = 5 
b = 10
R = a + b
f'{R} = {a} + {b}'
if a + b == 15:
    print(f'(la réponse est {R})')
else:
    print("la réponse est {a+b}")

value1 = 15 # la donnée à modifier pour changer les rapports 
for i in range(value1, R+5):
    print(R)
if value1 >= R:
    print("Le résultat est le même que le résultat de a + b")
elif value1 < R:
    print(f'{value1} est plus petit que {R}')
else:
    print("il n\'y a pas de différences entre c\'est 2 chiffres")
