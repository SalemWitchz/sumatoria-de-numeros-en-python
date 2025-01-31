NUM = 8
nums = [0]*8*NUM
total=0
for i in range(NUM):
    nums[i]= int(input("ingrese un digito: "))
    total+=nums[i]
    print("el total de numero es: ",total)