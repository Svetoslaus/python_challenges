for i in range(1, 101):
    if(i % 3) == 0:
        print("teilbar durch 3")
    elif(i % 4) == 0:
        print("teilbar durch 4")
    elif(i % 3 and i % 4):
        print("teilbar 3 und 4")
    else:
        print(i)
