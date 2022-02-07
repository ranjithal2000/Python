taking user input
 list=[]
 n=int(input("enter the number of elements:"))
 for i in range(1,n+1):
     b=int(input("enter elements:"))
     list.append(b)
 list.sort()
 print("second largest is:",list[-2])
