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
	if (desk == 20 && light == 40 && aircon == 3) {		//�繰�� �� �������� �繰�� ����
		cout << "��� �繰���� ���� �۵��մϴ�.\n\n";
	}
	else if (desk < 20 || light < 40 || aircon < 3) {
		cout << "�繰�� �� ���峭 ���� �����մϴ�.\n\n";
	}
}

void StudyCaffe::work_state() {
	if (light > 1 && user >= 1) {						//���� �ϳ� �̻� ������, �̿��ڰ� �Ѹ� �̻�
		cout << "���͵�ī�信 �̿��ڰ� �ֽ��ϴ�.\n";
	}
	else 
		cout << "���͵�ī�信 �̿��ڰ� �����ϴ�.\n";
}

void StudyCaffe::occur_event(int a) {
	int i = 0;
	srand(time(0));
	i = rand() % a + 1;

	cout << "������ " << i << " �밡 ���峵���ϴ�.\n";
	cout << "�������� " << a - i << " �� ���� �۵��մϴ�.\n";
}