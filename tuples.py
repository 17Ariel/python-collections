
tanks=("E100","IS-4","IS-7","60TP Lewandowskiego","Progetto 65")
print(tanks)
print(tanks[0])
print(tanks[0:3])
print(tanks[-1])
print(tanks[:2])
print(tanks[3:])
#convert tuples to be able to update the first element in the tuples
tank=list(tanks)
tank[0]=['Maus']
print(tank[0])
#unpacking tuple
# (E100,IS4,IS7,TP,Prog)=tanks
(E100,*Prog)=tanks
print(E100)