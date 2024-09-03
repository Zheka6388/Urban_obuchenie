immutable_var=1,3,5,'aplle','module'
tuple_=(immutable_var)
print('Immutable tuple:', tuple_)
#tuple_[0]=200-при попытке замены элемента будет выходить ошибка,т.к. кортеж нельзя изменять по элементам.
#print(tuple_)
mutable_list=[3,7,9,'module']
mutable_list[2]=3
print('Mutable list: ',mutable_list)



