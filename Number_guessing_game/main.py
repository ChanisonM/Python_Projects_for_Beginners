import random 
print("สวัสดีค่ะ ยินดีต้อนรับสู่เกมของเรา! เกมนี้เป็นเกมทายตัวเลข คุณมีโอกาส 7 ครั้งในการทายตัวเลขเริ่มเกมกันเลย!")

number_to_guess = random.randrange(20)

chances = 7 #โอกาส

guess_counter = 0


while guess_counter < chances:
    
    guess_counter += 1
    
    my_guess = int(input('โปรดป้อนการทายของคุณ : '))

    if my_guess == number_to_guess: # Winner
        print(f'ตัวเลขคือ {number_to_guess} และคุณทายถูกแล้ว!!  {guess_counter} ในครั้งที่')
        break
    elif guess_counter >= chances and my_guess != number_to_guess :
        print(f'เสียใจด้วยค่ะ ตัวเลขคือ {number_to_guess} ขอให้โชคดีในครั้งหน้า')
    elif my_guess > number_to_guess :
         print('การทายของคุณสูงเกินไป ')
    elif my_guess < number_to_guess :
        print('การทายของคุณต่ำเกินไป')
