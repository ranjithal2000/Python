#one
try:
    a=5
    b=0
    print(a/b)
except ZeroDivisionError:
    print("Not allowed")

#two
try:
    x=int(input('Enter value upto 50:'))
    if x>50:
        raise ValueError(x)
except ValueError:
    print(x,'out of range')
else:
    print(x,'within the range')

#three
a=[5,'r',0,7,'n',3]
length=len(a)
print(length)
for n in a:
    try:
        a=length/n
        print(a)
    except ZeroDivisionError:
        print('cannot be divided by zero')
    except TypeError:
        print('it is a character')

#four
try:
    a=[2,4,5]
    print(a[2])
except LookupError:
    print('Index out of bond')
else:
    print("success")

#five
try:
    age=int(input('enter age: '))
    if age < 18:
        raise ValueError(age)
    else:
        print("eligible to vote")
except ValueError:
   print("not eligible to vote")
    print("not eligible to vote")
