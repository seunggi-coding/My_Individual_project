#include <iostream>
#include <time.h>
#include "StudyCaffe_Class.h"

using namespace std;


void StudyCaffe::setAircon(int a) {
	aircon = a;
}

int StudyCaffe::getAircon() {
	return aircon;
}

void StudyCaffe::setLight(int l) {
	light = l;
}

int StudyCaffe::getLight() {
	return light;
}

void StudyCaffe::setDesk(int d) {
	desk = d;
}

int StudyCaffe::getDesk() {
	return desk;
}

void StudyCaffe::setUser(int u) {
	user = u;
}

int StudyCaffe::getUser() {
	return user;
}

void StudyCaffe::item_state() {
	if (desk == 20 && light == 40 && aircon == 3) {		//사물들 중 정상적인 사물의 개수
		cout << "모든 사물들이 정상 작동합니다.\n\n";
	}
	else if (desk < 20 || light < 40 || aircon < 3) {
		cout << "사물들 중 고장난 것이 존재합니다.\n\n";
	}
}

void StudyCaffe::work_state() {
	if (light > 1 && user >= 1) {						//불이 하나 이상 켜졌고, 이용자가 한명 이상
		cout << "스터디카페에 이용자가 있습니다.\n";
	}
	else 
		cout << "스터디카페에 이용자가 없습니다.\n";
}

void StudyCaffe::occur_event(int a) {
	int i = 0;
	srand(time(0));
	i = rand() % a + 1;

	cout << "에어컨 " << i << " 대가 고장났습니다.\n";
	cout << "에어컨이 " << a - i << " 대 정상 작동합니다.\n";
}