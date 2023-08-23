import random
record={"win":0,"lose":0,"draw":0}
while True:
    computer=random.randint(1,300)
    computer_str=""
    if computer<=100:
        computer_str="가위"
    elif computer>=101 and computer<=200:
        computer_str="바위"
    elif computer>=201:
        computer_str="보"
    user_str=input("가위,바위,보 중 한가지를 내세요 : ")
    user_int=0
    if user_str=="가위":
        user_int=1
        if computer==1:
            print(f"비겼습니다! 컴퓨터도 {computer_str}를 냈어요!")
            record["draw"]+=1
        elif computer==2:
            print(f"졌습니다ㅠㅠ.컴퓨터는 {computer_str}를 냈어요...")
            record["lose"]+=1
        elif computer==3:
            print(f"이겼습니다!!대단하세요!!컴퓨터는 {computer_str}를 냈어요!")
            record["win"]+=1
    elif user_str=="바위":
        user_int=2
        if computer==1:
            print(f"이겼습니다!!대단하세요!!컴퓨터는 {computer_str}를 냈어요!")
            record["win"]+=1
        elif computer==2:
            print(f"비겼습니다! 컴퓨터도 {computer_str}를 냈어요!")
            record["draw"]+=1
        elif computer==3:
            print(f"졌습니다ㅠㅠ.컴퓨터는 {computer_str}를 냈어요...")
            record["lose"]+=1
    elif user_str=="보":
        user_int=3
        if computer==1:
            print(f"졌습니다ㅠㅠ.컴퓨터는 {computer_str}를 냈어요...")
            record["lose"]+=1
        elif computer==2:
            print(f"이겼습니다!!대단하세요!!컴퓨터는 {computer_str}를 냈어요!")
            record["win"]+=1
        elif computer==3:
            print(f"비겼습니다! 컴퓨터도 {computer_str}를 냈어요!")
            record["draw"]+=1
    win_rate=round(record["win"]*100/(record["win"]+record["draw"]+record["lose"]),2)
    print(f"현재 user님의 승률 : {win_rate}%입니다!")
    print(f"승 : {record['win']}\n무 : {record['draw']}\n패 : {record['lose']}")
    go_stop=input("게임을 또 하고싶으신가요?(y/n)")
    if go_stop=='y':
        print("---------------------새게임-----------------------")
        continue
    elif go_stop=='n':
        print(f"안녕히 게세요! 게임을 종료합니다.")
        break
