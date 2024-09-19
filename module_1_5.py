immutable_var = 1, "summer", True
print (immutable_var)
immutable_var = 1, 2, 3
print (immutable_var)
#immutable_var[0] = 3
#print (immutable_var) #выводится ошибка, потому что кортеж не поддерживает изменение по элементам
mutable_list = ['rain', 'sun', 4]
print (mutable_list)
mutable_list [2] = 'car'
print (mutable_list)
mutable_list.extend('567')
print (mutable_list)
mutable_list.extend(['567', 'peach'])
print (mutable_list)
mutable_list.remove ('567')
print (mutable_list)
