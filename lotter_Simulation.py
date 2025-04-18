import random
import matplotlib.pyplot as plt

acc=0
x=[]
y=[]

for i in range(30):
    x.append(i+1)

    bet=random.randint(1,10)
    lucky_no=random.randint(1,10)
    if bet==lucky_no:
        acc=acc+900-100
    else:
        acc=acc-100

    y.append(acc)

plt.plot(x,y)
plt.show()
print(acc)