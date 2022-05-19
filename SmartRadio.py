# 1. 무전기 대신 조끼에 내장되어 있는 형태의 스마트 무전기
# 2. 2차원 전극 소재로 반도체가 구성되어 있어 고성능·저전력 상보성 논리회로가 구현가능하다. 
# 3. 근처에 가까운 비상벨과 통신하여 각각의 디바이스에서 일정 반경내의 벨이 울린다면 위치를 파악하고 파출소 센터로 전송한다.
# 4. 무전기에 달려있는 카메라를 통해 바디캠의 역할을 할 수 있다.
# 4-2. 평상시에 절전모드에 있다가 순찰차와 블루투스 연결이 되었을 때, 스스로 on/off도 버튼을 통해 가능
import random

Bluetooth = 0                    # 블루투스 연결O : 1, 블루투스 연결X : 0
Camera = 0                       # 카메라 연결O : 1, 카메라 연결X : 0
Manual = 0                       # 수동으로 연결O : 1, 수동으로 연결X : 0
Emergency_Bell = 0               # 비상벨 연결O : 1, 비상벨 연결X : 0
Latitude = random.uniform(-90, 90)       # 위도, -90 <= 위도 <= 90
Longitude = random.uniform(-180, 180)    # 경도, -180 <= 경도 <= 180
Q_Bluetooth = 0
Q_Manual = 0
Q_Bell = 0
Q_Car = 0
status = 1           # 0: 카메라의 연결 상태, 1: 비상벨의 호출 상태

while 1:
    if status == 0:
        while 1:
            Q_Bluetooth = input("Bluetooth 연결 되었습니까? ")
            if Q_Bluetooth == "y" or Q_Bluetooth == "Y":
                Bluetooth = 1
                Manual = 0
                Camera = 1
                print("카메라가 켜졌습니다.\n")
                break
    
            elif Q_Bluetooth == "n" or Q_Bluetooth == "N":
                Bluetooth = 0
                Manual = 0
                Camera = 0
                print("카메라가 꺼졌습니다.\n")
        
                while 1:
                    Q_Manual = input("수동으로 작동시키겠습니까? ")
                    if Q_Manual == "y" or Q_Manual == "Y":
                        Manual = 1
                        Camera = 1
                        print("카메라가 켜졌습니다.\n")
                        break
        
                    elif Q_Manual == "n" or Q_Manual == "N":
                        Manual = 0
                        Camera = 0
                        print("카메라가 꺼졌습니다.\n")
                        break
            
                    else:
                        Bluetooth = 0
                        Manual = 0
                        Camera = 0
                        print("다시 입력해주시기 바랍니다.\n")
            else:
                Bluetooth = 0
                Manual = 0
                Camera = 0
                print("다시 입력해주시기 바랍니다.\n")
            
            break
        break
        
    elif status == 1:
        while 1:
            Q_Bell = input("근처에서 비상벨이 호출되었습니까? ")
            if Q_Bell == "y" or Q_Bell == "Y":
                
                Q_Car = input("순찰차에 탑승했습니까? ")
                if Q_Car == "y" or Q_Car == "Y":
                    print("비상벨 호출 장소로 이동중입니다.\n")
                    print("비상벨 호출 좌표는 {{{:.4f}/{:.4f}}} 입니다.\n".format(Latitude, Longitude))
                    print("센터로 해당 좌표 {{{:.4f}/{:.4f}}} 를 전송합니다.\n".format(Latitude, Longitude))
                    status = 0

                elif Q_Car == "n" or Q_Car == "N":
                    print("비상벨 호출 장소로 이동중입니다.\n")
                    print("비상벨 호출 좌표는 {{{:.4f}/{:.4f}}} 입니다.\n".format(Latitude, Longitude))
                    print("센터로 해당 좌표 {{{:.4f}/{:.4f}}} 를 전송합니다.\n".format(Latitude, Longitude))
                    status = 0
                
            elif Q_Bell == "n" or Q_Bell == "N":
                print("관할 구역을 순찰중입니다.\n")
                print("접수된 신고를 우선 처리합니다.\n")
                break
            
            else:
                Bluetooth = 0
                Manual = 0
                Camera = 0
                print("다시 입력해주시기 바랍니다.\n")
            break