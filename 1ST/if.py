while True:
    luck_num = 17
    input_num = int(input ("Input the number num:"))

    if input_num == luck_num:
        print("Bingo")
        break
    elif input_num > luck_num:
        print("the real number is samller . ")
    else:
        print("the real num is bigger . ")