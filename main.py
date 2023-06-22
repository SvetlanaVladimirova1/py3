num = int(input("Сколько рядов у ёлки?"))
if num == 1:
    print("*")

elif num == 2:
    print("   *", end='\n  ***\n')

elif num == 3:
    print("   *", end='\n  ***\n')
    print(" *****")

elif num == 4:
    print("   *", end='\n  ***\n')
    print(" *****", end='\n*******\n')

elif num == 5:
    print("     *",  end='\n    ***\n')
    print("   *****", end='\n  *******\n')
    print(" ********* ")

elif num == 6:
    print("     *",  end='\n    ***\n')
    print("   *****", end='\n  *******\n')
    print(" ********* ", end='\n***********\n')

else:
    print("Таких елок не бывает")
