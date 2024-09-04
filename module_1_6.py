my_dict={'Egor':2006,'Matwey':2013,'Arseniy':2014,'Maksim':2016}
print(my_dict)
print(my_dict['Matwey'])
print(my_dict.get('Evgeniy'))
my_dict.update({'Ivan':2019,'Ira':2001})
a=my_dict.pop('Egor')
print(a)
print(my_dict)

my_set={5,2,8,'Aplle',2,8,(3,4,7)}
print(my_set)
my_set.update({9,1})
my_set.discard(5)
print(my_set)