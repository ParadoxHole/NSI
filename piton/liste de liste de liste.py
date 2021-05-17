list1=[10,20,30]
list2=["luc","laly","lalie"]
list3=[[11,5,21],[1],[2,13]]

print(list2[0])
print(list3[0])
print(list3[-1])
print(list3[0][-1])
print(list3[0][1])
print(list3[-1][-1])

list4 = [i+1 for i in range(20)]
print(str(list4))
print(str(list4[1:20:2]))

list5=[0]*100
for i in range (100):
    list5[i]=i+1
print(list5)

def f(x):
    return 2*x**2+x/2-4
list=[ i/4 for i in range(5)]
images=[f(i) for i in list]
print(list,images)