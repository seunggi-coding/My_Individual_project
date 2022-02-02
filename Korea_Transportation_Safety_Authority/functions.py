import random

distance = 1000
total_distance = random.randint(1000, 30000)
num = total_distance // distance + 1

def Accident_Scene():
    accident = random.randint(0, 1)        #사고가 찍히면 1, 아니면 0
    
    return accident

def Traffic_Jam():
    jam = random.randint(0, 1)            #교통 정체가 발생하면 1, 아니면 0
    
    return jam

def CCTV_Num():
    print("해당 도로의 총 길이는 {:.2f}km이며 CCTV는 {}km 마다 설치되어 있습니다.".format(total_distance/1000, distance/1000))
    print("해당 도로에 설치된 CCTV의 개수는 {}개입니다.".format(num))
    
def Report():
    print("구조대와 견인 차량을 출동시켰습니다.")
    print("운전자 및 동승자는 모두 갓길에 대피해야 합니다.")
    
def Traffic_Signs():
    fine_dust = random.randint(0, 200)
    acc_location = random.randint(1, num)
    
    if Accident_Scene() == 0:
        if Traffic_Jam() == 0:
            if fine_dust >= 0 and fine_dust <= 80:
                print("현재 미세먼지의 양은 {}㎍/㎥ 단계로 좋음 ~ 보통 단계입니다.".format(fine_dust))
                print("또한 도로 내에 정체되어 있는 부분은 없습니다.")
            elif fine_dust >= 81 and fine_dust <= 150:
                print("현재 미세먼지의 양은 {}㎍/㎥ 단계로 나쁨 단계입니다.".format(fine_dust))
                print("또한 도로 내에 정체되어 있는 부분은 없습니다.")
            else:
                print("현재 미세먼지의 양은 {}㎍/㎥ 단계로 매우나쁨 단계입니다.".format(fine_dust))
                print("또한 도로 내에 정체되어 있는 부분은 없습니다.")
        else:
            if fine_dust >= 0 and fine_dust <= 80:
                print("현재 미세먼지의 양은 {}㎍/㎥ 단계로 좋음 ~ 보통 단계입니다.".format(fine_dust))
                print("{}번 혹은 {}번 CCTV 위치에 사고가 발생했을 가능성이 있습니다.".format(acc_location+2, acc_location+1))
                Report()
                print("도로 내에 정체되어 있는 부분은 있으므로 사고 예방을 위해 서행해주시고, 전방주시 부탁드립니다.")
            elif fine_dust >= 81 and fine_dust <= 150:
                print("현재 미세먼지의 양은 {}㎍/㎥ 단계로 나쁨 단계입니다.".format(fine_dust))
                print("{}번 혹은 {}번 CCTV 위치에 사고가 발생했을 가능성이 있습니다.".format(acc_location+2, acc_location+1))
                Report()
                print("도로 내에 정체되어 있는 부분은 있으므로 사고 예방을 위해 서행해주시고, 전방주시 부탁드립니다.")
            else:
                print("현재 미세먼지의 양은 {}㎍/㎥ 단계로 매우나쁨 단계입니다.".format(fine_dust))
                print("{}번 혹은 {}번 CCTV 위치에 사고가 발생했을 가능성이 있습니다.".format(acc_location+2, acc_location+1))
                Report()
                print("도로 내에 정체되어 있는 부분은 있으므로 사고 예방을 위해 서행해주시고, 전방주시 부탁드립니다.")

    elif Accident_Scene() == 1:
        if fine_dust >= 0 and fine_dust <= 80:
            print("사고 위치는 {}번 CCTV입니다.".format(acc_location))
            Report()
            print("\n현재 미세먼지의 양은 {}㎍/㎥ 단계로 좋음 ~ 보통 단계입니다.".format(fine_dust))
            print("사고 발생으로 일부 구간이 정체되어 있습니다.")
            print("2차 사고 예방을 위해 서행해주시고, 전방주시 부탁드립니다.")
        elif fine_dust >= 81 and fine_dust <= 150:
            print("사고 위치는 {}번 CCTV입니다.".format(acc_location))
            Report()
            print("\n현재 미세먼지의 양은 {}㎍/㎥ 단계로 나쁨 단계입니다.".format(fine_dust))
            print("사고 발생으로 일부 구간이 정체되어 있습니다.")
            print("2차 사고 예방을 위해 서행해주시고, 전방주시 부탁드립니다.")
        else:
            print("사고 위치는 {}번 CCTV입니다.".format(acc_location))
            Report()
            print("\n현재 미세먼지의 양은 {}㎍/㎥ 단계로 매우나쁨 단계입니다.".format(fine_dust))
            print("사고 발생으로 일부 구간이 정체되어 있습니다.")
            print("2차 사고 예방을 위해 서행해주시고, 전방주시 부탁드립니다.")
   