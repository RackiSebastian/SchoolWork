import matplotlib.pyplot as plt
'''n = int(input("How many values do you have?"))

list_exs =[]
list_ys =[]

b = 0


for exos in range(n):
    v = int(input("input all your X's now"))
    list_exs.append(v)

for yois in range(n):
    k = int(input("input all your Y's now"))
    list_ys.append(k)


print(list_exs,list_ys)

sum_x = 0
sqrt_x = 0
for i in range(len(list_exs)):
    sum_x += list_exs[i]
    sqrt_x += list_exs[i] ** 2

sum_y = 0
sqrt_y = 0
for go in range(len(list_ys)):
    sum_y += list_ys[go]
    sqrt_y += list_ys[go] ** 2

x_y = 0
for both in range(len(list_ys)):
    x_y += list_exs[both] * list_ys[both]



avrg_x = sum_x/len(list_exs)
avrg_y = sum_y/len(list_ys)
avrg_sqrt_x = sqrt_x/len(list_exs)
avrg_sqrt_y = sqrt_y/len(list_ys)
avrg_x_y= x_y/len(list_ys)



print(sum_x)
print(sum_y)
print(sqrt_x)
print(sqrt_y)
print(x_y)
print(avrg_x)
print(avrg_y)
print(avrg_sqrt_x)
print(avrg_sqrt_y)
print(avrg_x_y)

#formula = y = ax+b

a = ((avrg_x_y)-((avrg_x)*(avrg_y)))/(avrg_sqrt_x)-((avrg_x) ** 2)
b = avrg_y - ((a) * (avrg_x))

print("a is",round(a,5))
print("b is", round(b,5))

print("y ="+str(a)+"x +"+str(b))

new_points_for_line = []
for g in range(len(list_exs)):
    new_points_for_line.append((a * list_exs[g]) + b)


#this is graph things down here(have to import matplotlib)
plt.scatter(list_exs,list_ys,s=40)
plt.plot(new_points_for_line,list_exs)
plt.show()'''


def regression_line(no_of_values):
    list_exs =[]
    list_ys=[]
    for numbers in range(int(no_of_values) * 2 ):
        if numbers >= 4:
            list_ys.append(int(input("Now please Enter Your Y's")))
        else:
            list_exs.append(int(input("Please Enter your X's")))

    sum_of_ex = 0
    sqrt_ex = 0
    for sum_x in range(len(list_exs)):
        sum_of_ex+= list_exs[sum_x]
        sqrt_ex += list_exs[sum_x] ** 2

    sum_of_y = 0
    sqrt_of_y = 0
    for sum_y in range(len(list_ys)):
        sum_of_y += list_ys[sum_y]
        sqrt_of_y += list_ys[sum_y] ** 2


    x_y = 0
    for both in range(len(list_ys)):
        x_y += list_exs[both] * list_ys[both]




    avg_x = sum_of_ex/len(list_exs)
    avg_y = sum_of_y/len(list_ys)
    avg_x_y = x_y/len(list_exs)
    avg_sqrt_x = sqrt_ex/len(list_exs)
    avg_sqrt_y = sqrt_of_y/len(list_ys)
    avg_both = x_y/len(list_exs)

    a = ((avg_x_y) -(avg_x * avg_y))/(avg_sqrt_x-((avg_x)**2))
    b = avg_y - ((a) * (avg_x))

    new_points_for_line = []
    for new_points in range(len(list_exs)):
        new_points_for_line.append((a * list_exs[new_points]) + b)

    # this is graph shiet down here
    plt.scatter(list_exs, list_ys, s=40)
    plt.plot(new_points_for_line, list_exs)
    plt.show()
    return list_exs,list_ys,new_points_for_line

regression_line(4)





