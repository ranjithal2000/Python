def Break(arr):
    for i in arr:
        if i==5:
            break
        print(i)
    print("")

def Continue(arr):
    for i in arr:
        if i==5:
            continue
        print(i)
    print("")
arr=[1,2,3,5,6,7]
print("output of break function is")
Break(arr)
print("output of continue function is")
Continue(arr)
