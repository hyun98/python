Cro = {'c=':1,'c-':1,'dz=':1,'d-':1,'lj':1,'nj':1,'s=':1,'z=':1}
Cro_key = Cro.keys()
sen = input()
for i in Cro_key:
	sen = sen.replace(i,"a")
print(len(sen))