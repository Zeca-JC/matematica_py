planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'makemake'}
print(planeta_anao)

qtd = len(planeta_anao)
print(qtd)

print('Ceres' in planeta_anao)
print('Eris' not in planeta_anao)


for astros in planeta_anao:
    print(astros.upper())

astros = ['lua', 'vênus', 'sirius', 'marte', 'lua']
astrosSet = set(astros)
print(f'Conjuntos: {astrosSet}')

p1 = {'terra', 'venus', 'mercurio', 'marte', 'netuno'}
p2 = {'terra', 'jupiter', 'urano', 'marte', 'saturno'}
p3 = {'jupiter', 'urano', 'saturno'}
p4 = p1.copy()
print(p1 | p2)
print(p1.union(p2))
print(p1 & p2) #intercecção
print(p1.intersection(p2)) #intercecção
print(p1.difference(p2)) # diferença
print(p1 ^ p2) # doferença simétrica
print(p1.symmetric_difference(p2)) # o mesmo acima
print(p1.isdisjoint(p2))
print(p1.isdisjoint(p3))
print(p4)
p1.add('jupiter')
print(p1)
p1.remove('terra') #remover
p1.discard('marte')  #remover
p1.pop() # remove qualquer
p1.clear()

# Conjuntos
ciencias = (['Canal do Pirula', 'Manual do mundo', 'Nunca vi 1 cientista'], ['Ciências', 'Fisica', 'Biologia'])
ciencias2 = (['universo discreto', 'python'])
cientistas = set(ciencias2)
print(ciencias)
print(ciencias[0])
cientistas.add('universo')
print(cientistas)


