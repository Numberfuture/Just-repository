import random
Lotto_number = 0
My_Lotto_number = 1
i = 0

while (My_Lotto_number != Lotto_number):
        Lotto_number= random.randrange(1, 100000)
        My_Lotto_number = random.randrange(1, 100000)
        print(My_Lotto_number)
        print(Lotto_number)
        i+=1
        if (My_Lotto_number == Lotto_number) :
            print("You got 20 milion dolor. Congratulation!")
            My_spend_money = i*1000
            print("You tried : "+str(i))
            print("You spend : "+str(My_spend_money)+" won")
            break