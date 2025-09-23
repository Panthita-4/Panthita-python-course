import random

def test_random():
    #สร้างตัวแปร random_number ตัวแปรสุ่มเลขระหว่าง 1-10
    random_number = random.randint(1, 10)
    user_number = input("Guess your number:")
    user_number = int(user_number)
    if random_number == user_number:
        print("congratulation")
    elif random_number < user_number:
        print("Too high")
    elif random_number > user_number:
        print("Too low")
