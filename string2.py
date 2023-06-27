name = 'mdabberul'
#find lenth
print(len(name))
#find spesefic value
print(name[1:4])
# 1 teke 8 er mdde 2 gh0r bad diye diye
print(name[1:8:2])
#name er c0py
name_copy = name[:]
print(name_copy)
#find id
print(id(name))
print(id(name_copy))

#string F0rmating

nam1 = 'mdabberul '
nam2 = 'islam'
nam3= nam1 + nam2
print(nam3)
#an0ther Meth0d
nam1 = 'm0dabberul %s'
nam2 = 'islam'
nam3= nam1 % nam2
print(nam3)

#An0ther meth0d
first_name = 'm0dabberul {}'
middle_name ='islam'
last_name ='satch0'
full_name = first_name.format(last_name)
print(full_name)
#An0ther meth0d 1

first_name = 'm0dabberul {} {}'
middle_name ='islam'
last_name ='satch0'
full_name = first_name.format(last_name,middle_name)  # middle_name,last_name dile p0siti0n cng hbe
print(full_name)

#An0ther meth0d 1

first_name = 'm0dabberul {0} {1} {1} {1}'  # last name k 0 drse first name k 1 drse
middle_name ='islam'
last_name ='satch0'
full_name = first_name.format(last_name,middle_name)  # middle_name,last_name dile p0siti0n cng hbe
print(full_name)