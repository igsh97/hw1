import random
random_number=random.randint(1,100)
count=0
record=0
while True:
    count+=1
    num=input("숫자를 입력하세요 : ")
    num=int(num)
    if num<random_number:
        print(f"업! {num}보다 큰 수를 입력하세요!")
    elif num>random_number:
        print(f"다운! {num}보다 작은 수를 입력하세요!")
    else:
        print(f"정답입니다! 시도횟수:{count}")
        if record==0:
            record=count
        else :
            if count<record:
                record=count
        go_stop=input("게임을 또 하고싶으신가요?(y/n)")
        if go_stop=='y':
            count=0
            print(f"현재 제일 좋은 기록:{record}")
            random_number=random.randint(1,100)
            print("---------------------새게임-----------------------")
            continue
        elif go_stop=='n':
            print(f"안녕히 게세요! 제일 좋은 기록은 {record}입니다!")
            break