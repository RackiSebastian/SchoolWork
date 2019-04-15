import matplotlib.pyplot as plt


############################################################################################################
#THIS IS THE LONGER PART I LATER REDUCED IT AND MADE NORMAL VARIABLE NAMES AND ALSO COMMENTED IT OUT
############################################################################################################
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
############################################################################################
#THIS IS THE SHORTER SOLUTION THAT MAKES WAY MORE SENSE!!!
###########################################################################################

def regression_line(no_of_values):
    list_exs =[]
    list_ys=[]
    for numbers in range(int(no_of_values) * 2 ):  #Seeing as there is two values(x,y) i will have number of values*2 
        if numbers >= int(no_of_values): #If number is greater or equal to the number of values inputed that means i can move on to Y
            list_ys.append(int(input("Now please Enter Your Y's")))
        else:
            list_exs.append(int(input("Please Enter your X's")))

    sum_of_ex = 0
    sqrt_ex = 0
    for sum_x in range(len(list_exs)):
        sum_of_ex+= list_exs[sum_x]          #Adding x's at position [0,1,2,3,...,n]
        sqrt_ex += list_exs[sum_x] ** 2      #Getting The Square Root At Position [0,1,2,3,...,n]

    sum_of_y = 0
    sqrt_of_y = 0
    for sum_y in range(len(list_ys)):         #Same as Above
        sum_of_y += list_ys[sum_y]
        sqrt_of_y += list_ys[sum_y] ** 2


    x_y = 0
    for both in range(len(list_ys)):           
        x_y += list_exs[both] * list_ys[both]



     #Here i will be getting the average of all the values and this will only work if the list is the same length and it has to be for the 
    #least regression square
    avg_x = sum_of_ex/len(list_exs)           
    avg_y = sum_of_y/len(list_ys)
    avg_x_y = x_y/len(list_exs)
    avg_sqrt_x = sqrt_ex/len(list_exs)
    avg_sqrt_y = sqrt_of_y/len(list_ys)
    avg_both = x_y/len(list_exs)
    
    #Formula = (y=ax+b)

    a = ((avg_x_y) -(avg_x * avg_y))/(avg_sqrt_x-((avg_x)**2))
    b = avg_y - ((a) * (avg_x))
    
    #Here i am getting the new points by substituting my x values into the formula y = ax+b
    new_points_for_line = []
    for new_points in range(len(list_exs)):
        new_points_for_line.append((a * list_exs[new_points]) + b)

    # this is graph down here(You must import matplotlib)
    plt.scatter(list_exs, list_ys, s=40)
    
    #Had to update the below because it wasnt giving me the line of best fit but now it works!
    #I was mixing up the x and y values 
    plt.plot(list_exs,new_points_for_line)
    plt.show()
    return list_exs,list_ys,new_points_for_line

#Just testing
regression_line(4)
regression_line(10)
regression_line(16)
regression_line(0)
regression_line(6)
regression_line(7)





