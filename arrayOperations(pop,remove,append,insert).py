import array as arr
a=arr.array('i',[1,2,3,4])
print("created array is:",end=" ")
for i in range(0,4):
    print(a[i],end=" ")
a.insert(4,1)
print("\nafter inserting:")
for i in range(0,5):
    print(a[i],end=" ")
list=["abc","def","ghi"]
list.append("jkl")
print("\nafter appending:")
for i in range(0,4):
    print(list[i],end=" " )
a.remove(1)
print("\nafter removing:")
for i in range(0,4):
    print(a[i],end=" ")
a.pop(3)
print("\nafter pop:")
for i in range(0,3):
    print(a[i],end=" ")
