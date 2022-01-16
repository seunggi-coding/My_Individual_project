# 지능형 CCTV의 시나리오를 작성함

# 1. 공개수배자가 포착되면 이동 경로로 경찰을 출동시킨다.
# 2. 같은 장소에 일정 기간 이상 배회하고 나타나는 인물이 있다면 배회하는 기간에 따라
#    다른 조치가 이루어질 수 있게 한다.
# 3. 만약 빌라 단지 앞의 CCTV이면서 밤이 된다면 적외선 센서에 감지되어 불이 켜지는 방향으로 
#    CCTV의 각도를 조절한다.

import random

criminal = random.randint(0, 1)           # 범죄자 포착여부
strange = random.randint(0, 1)           # 거동수상자 포착여부
stranger = random.choice("가나다")
day = random.randint(5, 20)               # 같은 장소를 배회한 일수
road = random.choice("ABC")
direction = random.choice("동서남북")
angle = ""
day_night = random.choice("낮밤")

wanted_person = random.randint(1, 3)

while True:
    if criminal == 0 and strange == 0 and day_night == "낮":
        print("\n특이사항 없습니다.\n")
        break
    
    elif criminal == 0 and strange == 0 and day_night == "밤":
        print("\n특이사항 없습니다.\n")
        break
    
    elif criminal == 1 and strange == 0 and day_night == "낮":
        print("\n현재 시간은 {}입니다.\n".format(day_night))
        print("공개수배자가 포착되었습니다.")
        print("얼굴을 분석하여 범죄자를 특정중입니다.\n")
        if wanted_person == 1:
            print("CCTV에 포착된 범죄자는 \"김OO\" 입니다.")
            if road == "A":
                print("김OO은 A도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
            elif road == "B":
                print("김OO은 B도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
            elif road == "C":
                print("김OO은 C도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
                
        elif wanted_person == 2:
            print("CCTV에 포착된 범죄자는 \"박OO\" 입니다.")
            if road == "A":
                print("박OO은 A도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
            elif road == "B":
                print("박OO은 B도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
            elif road == "C":
                print("박OO은 C도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
                
        elif wanted_person == 3:
            print("CCTV에 포착된 범죄자는 \"이OO\" 입니다.")
            if road == "A":
                print("이OO은 A도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
            elif road == "B":
                print("이OO은 B도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
            elif road == "C":
                print("이OO은 C도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
    
    elif criminal == 1 and strange == 0 and day_night == "밤":
        print("\n현재 시간은 {}입니다.\n".format(day_night))
        print("OO빌라 1층 주차공간에 동작이 감지되었습니다.")
        print("OO빌라 1층은 {}쪽입니다.".format(direction))
        angle = direction
        print("CCTV의 각도를 {}쪽으로 조절합니다.".format(angle))
        
        print("\n공개수배자가 포착되었습니다.")
        print("얼굴을 분석하여 범죄자를 특정중입니다.\n")
        if wanted_person == 1:
            print("CCTV에 포착된 범죄자는 \"김OO\" 입니다.")
            if road == "A":
                print("김OO은 A도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
            elif road == "B":
                print("김OO은 B도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
            elif road == "C":
                print("김OO은 C도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
                
        elif wanted_person == 2:
            print("CCTV에 포착된 범죄자는 \"박OO\" 입니다.")
            if road == "A":
                print("박OO은 A도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
            elif road == "B":
                print("박OO은 B도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
            elif road == "C":
                print("박OO은 C도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
                
        elif wanted_person == 3:
            print("CCTV에 포착된 범죄자는 \"이OO\" 입니다.")
            if road == "A":
                print("이OO은 A도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
            elif road == "B":
                print("이OO은 B도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
            elif road == "C":
                print("이OO은 C도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                break
    
    elif criminal == 0 and strange == 1 and day_night == "낮":
        print("\n현재 시간은 {}입니다.".format(day_night))
        print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
        if day >= 5 and day < 10:
            print("해당 인물을 주의해야 할 필요가 있습니다.\n")
            break
        elif day >= 10 and day < 15:                
            print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
            break
        else:
            print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
            break
            
    elif criminal == 0 and strange == 1 and day_night == "밤":
        print("\n현재 시간은 {}입니다.\n".format(day_night))
        print("OO빌라 1층 주차공간에 동작이 감지되었습니다.")
        print("OO빌라 1층은 {}쪽입니다.".format(direction))
        angle = direction
        print("CCTV의 각도를 {}쪽으로 조절합니다.".format(angle))
        
        print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
        if day >= 5 and day < 10:
            print("해당 인물을 주의해야 할 필요가 있습니다.\n")
            break
        elif day >= 10 and day < 15:                
            print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
            break
        else:
            print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
            break
    
    elif criminal == 1 and strange == 1 and day_night == "낮":
        print("\n현재 시간은 {}입니다.\n".format(day_night))
        print("공개수배자와 거동수사자가 포착되었습니다.")
        print("얼굴을 분석하여 범죄자를 특정중이며 거동수상자 또한 추적중입니다.\n")
        if wanted_person == 1:
            print("CCTV에 포착된 범죄자는 \"김OO\" 입니다.")
            if road == "A":
                print("김OO은 A도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break
                    
            elif road == "B":
                print("김OO은 B도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break

            elif road == "C":
                print("김OO은 C도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break
                
        elif wanted_person == 2:
            print("CCTV에 포착된 범죄자는 \"박OO\" 입니다.")
            if road == "A":
                print("박OO은 A도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break

            elif road == "B":
                print("박OO은 B도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break

            elif road == "C":
                print("박OO은 C도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break
                
        elif wanted_person == 3:
            print("CCTV에 포착된 범죄자는 \"이OO\" 입니다.")
            if road == "A":
                print("이OO은 A도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break

            elif road == "B":
                print("이OO은 B도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break

            elif road == "C":
                print("이OO은 C도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break
                    
    elif criminal == 1 and strange == 1 and day_night == "밤":
        print("\n현재 시간은 {}입니다.\n".format(day_night))
        print("OO빌라 1층 주차공간에 동작이 감지되었습니다.")
        print("OO빌라 1층은 {}쪽입니다.".format(direction))
        angle = direction
        print("CCTV의 각도를 {}쪽으로 조절합니다.".format(angle))
        
        print("공개수배자와 거동수사자가 포착되었습니다.")
        print("얼굴을 분석하여 범죄자를 특정중이며 거동수상자 또한 추적중입니다.\n")
        if wanted_person == 1:
            print("CCTV에 포착된 범죄자는 \"김OO\" 입니다.")
            if road == "A":
                print("김OO은 A도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break
                    
            elif road == "B":
                print("김OO은 B도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break

            elif road == "C":
                print("김OO은 C도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break
                
        elif wanted_person == 2:
            print("CCTV에 포착된 범죄자는 \"박OO\" 입니다.")
            if road == "A":
                print("박OO은 A도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break

            elif road == "B":
                print("박OO은 B도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break

            elif road == "C":
                print("박OO은 C도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break
                
        elif wanted_person == 3:
            print("CCTV에 포착된 범죄자는 \"이OO\" 입니다.")
            if road == "A":
                print("이OO은 A도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break

            elif road == "B":
                print("이OO은 B도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break

            elif road == "C":
                print("이OO은 C도로 방향으로 이동하고 있습니다.")
                print("해당 위치로 경찰을 출동시켰습니다.\n")
                print("\n{}일 이상 같은 장소 {}에서 배회하는 인물 \"{}\" 이/가 있습니다.".format(day, road, stranger))
                if day >= 5 and day < 10:
                    print("해당 인물을 주의해야 할 필요가 있습니다.\n")
                    break
                elif day >= 10 and day < 15:                
                    print("해당 인물이 장기간 머물고 있습니다. 접근금지 명령을 받은 인물인지 확인바랍니다.\n")
                    break
                else:
                    print("수상한 인물입니다. 출동하여 확인바랍니다.\n")
                    break