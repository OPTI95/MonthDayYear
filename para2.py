while 1:
    daysInyear = int(input("Показать сколько дней в сумме в этом году? 1 - Да 2 - Нет"))
    year = int(input("Введите год: "))
    days = 0
    if(daysInyear == 2):
        print ("Выберите месяц из представленных: \n1 - Январь\n2 - Февраль\n3 - Март"
        "\n4 - Апрель\n5 - Май\n6 - Июнь\n7 - Июль\n8 - Август\n9 - Сентябрь\n10 - Октябрь\n11 - Ноябрь\n12 - Декабрь")
        month = int(input("Введите месяц: "))
        if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
                i = 1
                for i in range(32):
                    if(len(str(i))>1 ):
                        i = int(int(str(i)[0]) + int(str(i)[1]))
                    days+=i
                    i+=1
                print(days)
        if(month == 4 or month == 6 or month == 9 or month == 11):
                i = 1
                for i in range(31):
                    if(len(str(i))>1 ):
                        i = int(int(str(i)[0]) + int(str(i)[1]))
                    days+=i
                    i+=1
                print(days)
        if(month == 2):
                if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                    i = 1
                    for i in range(30):
                        if(len(str(i))>1 ):
                            i = int(int(str(i)[0]) + int(str(i)[1]))
                        days+=i
                        i+=1
                    print(days)
                else:
                    i = 1
                    for i in range(29):
                        if(len(str(i))>1 ):
                            i = int(int(str(i)[0]) + int(str(i)[1]))
                        days+=i
                        i+=1
                    print(days)
  

    if daysInyear == 1:
        s = 1
        for s in range(13):
            month = s
            if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
                i = 1
                for i in range(32):
                    if(len(str(i))>1 ):
                        i = int(int(str(i)[0]) + int(str(i)[1]))
                    days+=i
                    i+=1
            if(month == 4 or month == 6 or month == 9 or month == 11):
                i = 1
                for i in range(31):
                    if(len(str(i))>1 ):
                        i = int(int(str(i)[0]) + int(str(i)[1]))
                    days+=i
                    i+=1
            if(month == 2):
                if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                    i = 1
                    for i in range(30):
                        if(len(str(i))>1 ):
                            i = int(int(str(i)[0]) + int(str(i)[1]))
                        days+=i
                        i+=1
                else:
                    i = 1
                    for i in range(29):
                        if(len(str(i))>1 ):
                            i = int(int(str(i)[0]) + int(str(i)[1]))
                        days+=i
                        i+=1
                    
            s+=1
        print(days)
