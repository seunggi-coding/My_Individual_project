#include <iostream>
#include "Phone.h"

using namespace std;

void Phone::turnOn() {
	cout << "휴대폰이 켜졌습니다." << endl;
}

void Phone::turnOff() {
	cout << "휴대폰이 꺼졌습니다." << endl;
}

int main() {
	Phone phone;

	phone.CPU_Degree = 21;
	cout << "비밀번호를 입력하시오. ";
	cin.getline(phone.password, 11, '\n');
	cout << "사용자 이름을 입력하시오. ";
	cin.getline(phone.user, 11, '\n');

	phone.turnOn();
	phone.turnOff();
	cout << "휴대폰의 CPU 온도는 " << phone.CPU_Degree << "입니다.\n";
	cout << "휴대폰의 비밀번호는 " << phone.password << "입니다.\n";
	cout << "휴대폰의 사용자는 " << phone.user << "입니다.\n";

}