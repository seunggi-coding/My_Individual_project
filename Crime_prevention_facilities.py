# 가로등과 바닥의 쏠라표지병, 비상벨, 로고젝터와 같이 범죄예방 시설에 관한 시나리오
# 1. 가로등과 쏠라표지병, 로고젝터는 일정 시간이 되면 불이 켜지며 이 구역이 범죄예방 시설이라는 
#    것을 지나가는 모두가 알 수 있도록 한다.
# 2. 비상벨은 2개 가로등 간격으로 존재하며 비상벨이 눌러지면 GPS 정보가 송신되어 근처의
#    가장 가까운 순찰중인 경찰이 출동한다.
# 3. 비상벨에는 마이크와 스피커가 내장되어 있어 출동중인 경찰과 통신이 가능하다.

import random

streetlight_num = random.randint(2, 10)
num = streetlight_num // 2
streetlight = random.randint(1, num)
push = random.randint(0, 1)
road = random.choice("ABC")
hour = random.randint(0, 24)

def bell():
    print("비상벨은 가로등 2개 간격마다 하나씩 부착되어 있습니다.")
    print("현재 이 범죄예방 시설에는 {}개의 비상벨이 부착되어 있습니다.".format(num))
    if push == 0:
        print("비상벨은 현재 눌리지 않았습니다.")
        print("특이사항은 없습니다.")
    elif push == 1:
        print("비상벨이 눌린 상태이며 위치는 {} 도로 {} 가로등입니다. ".format(road, streetlight))
        print("출동 신고와 위치를 자동으로 전송합니다. 비상벨 --> 경찰센터 --> 해당 가로등에서 가장 가까운 경찰")
        print("내장되어 있는 마이크와 스피커를 통해 비상벨 사용자와 통신을 시작합니다.")

while True:
    if hour >= 7 and hour <= 17:
        print("\n현재 시간은 {}시입니다.\n".format(hour))
        print("가로등, 쏠라표지병, 로고젝터는 꺼져있으며 태양광을 이용한 충전중입니다.\n")
        bell()
        print("\n")
        break
    else:
        print("\n현재 시간은 {}시입니다.\n".format(hour))
        print("가로등, 쏠라표지병, 로고젝터는 켜져있으며 해당 구역이 범죄예방 시설임을 강조하고 있습니다.\n")
        bell()
        print("\n")
        break
