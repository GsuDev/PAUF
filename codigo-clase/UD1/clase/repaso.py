x = 1
y = 2
lista = ['Marta', 'Victor', 'Cristina', 'Noelia']
lista2 = ['Ian', 'Diego']
lista.append('Javi')
lista.remove('Javi')
alumno = lista.pop()
del lista[1]
lista.insert(1, 'Diego')
lista.append('Javi')
lista.append('Javi')
lista.append('Javi')
print(lista)
print('DESPIERTA')
del lista[:2]
print(alumno)
print(lista)

lista.extend(lista2)
print(lista)
print('AHORA ORDENO')
lista.sort(reverse=True)
print(lista)
