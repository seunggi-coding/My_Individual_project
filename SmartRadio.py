# 1. 무전기 대신 조끼에 내장되어 있는 형태의 스마트 무전기
# 2. 2차원 전극 소재로 반도체가 구성되어 있어 고성능·저전력 상보성 논리회로가 구현가능하다. 
# 3. 근처에 가까운 비상벨과 통신하여 각각의 디바이스에서 일정 반경내의 벨이 울린다면 위치를 파악하고 파출소 센터로 전송한다.
# 4. 무전기에 달려있는 카메라를 통해 바디캠의 역할을 할 수 있다.
# 4-2. 평상시에 절전모드에 있다가 순찰차와 블루투스 연결이 되었을 때, 스스로 on/off도 버튼을 통해 가능

Bluetooth = 0        # 블루투스 연결O : 1, 블루투스 연결X : 0
Camera = 0           # 카메라 연결O : 1, 카메라 연결X : 0
Manual = 0           # 수동으로 연결O : 1, 수동으로 연결X : 0
Emergency_Bell = 0   # 비상벨 연결O : 1, 비상벨 연결X : 0
Latitude = 0         # 위도, -90 <= 위도 <= 90
Longitude = 0        # 경도, -180 <= 경도 <= 180
Q_Bluetooth = 0
Q_Manual = 0
status = 0           # 0: 카메라의 연결 상태, 1: 비상벨의 호출 상태

while 1:
    if status == 0:
        while 1:
            Q_Bluetooth = input("Bluetooth 연결이 되어 있습니까? ")
            if Q_Bluetooth == "y" or Q_Bluetooth == "on":
                Bluetooth = 1
                Manual = 0
                Camera = 1
                print("카메라가 켜져있습니다.\n")
                status = 1
                break
    
            elif Q_Bluetooth == "n" or Q_Bluetooth == "off":
                Bluetooth = 0
                Manual = 0
                Camera = 0
                print("카메라가 꺼져있습니다.\n")
                status = 1
        
                while 1:
                    Q_Manual = input("수동으로 작동시키겠습니까? ")
                    if Q_Manual == "y" or Q_Manual == "turn on":
                        Manual = 1
                        Camera = 1
                        print("카메라가 켜졌습니다.\n")
                        status = 1
                        break
        
                    elif Q_Manual == "n" or Q_Manual == "turn off":
                        Manual = 0
                        Camera = 0
                        print("카메라가 꺼졌습니다.\n")
                        status = 1
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
        
    elif status == 1:
        print(status)
        break