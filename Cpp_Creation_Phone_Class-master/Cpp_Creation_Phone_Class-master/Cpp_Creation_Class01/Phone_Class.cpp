#include <iostream>
#include "Phone.h"

using namespace std;

void Phone::turnOn() {
	cout << "�޴����� �������ϴ�." << endl;
}

void Phone::turnOff() {
	cout << "�޴����� �������ϴ�." << endl;
}

int main() {
	Phone phone;

	phone.CPU_Degree = 21;
	cout << "��й�ȣ�� �Է��Ͻÿ�. ";
	cin.getline(phone.password, 11, '\n');
	cout << "����� �̸��� �Է��Ͻÿ�. ";
	cin.getline(phone.user, 11, '\n');

	phone.turnOn();
	phone.turnOff();
	cout << "�޴����� CPU �µ��� " << phone.CPU_Degree << "�Դϴ�.\n";
	cout << "�޴����� ��й�ȣ�� " << phone.password << "�Դϴ�.\n";
	cout << "�޴����� ����ڴ� " << phone.user << "�Դϴ�.\n";

}