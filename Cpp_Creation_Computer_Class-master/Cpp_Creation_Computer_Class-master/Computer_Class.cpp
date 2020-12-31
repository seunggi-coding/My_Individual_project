#include <iostream>
#include <time.h>

using namespace std;

class Computer {

public:
	char consecutive_numbers[11];		//일련번호

	int CPU_State(int d);
	void hardware_state();
	void turnOn();
	void turnOff();
	void monitorOn();
	void monitorOff();

private:
	int CPU_Degree;
};

int Computer::CPU_State(int d) {
	CPU_Degree = d;
	return CPU_Degree;
}


void Computer::hardware_state() {
	if (CPU_Degree > 30) {
		cout << "\n---\t---\t---\n\n" << "CPU가 고장났습니다.\n" << "\n---\t---\t---\n\n";
	}
	else
		cout << "\n---\t---\t---\n\n" << "CPU 상태가 정상입니다.\n" << "\n---\t---\t---\n\n";
};

void Computer::turnOn() {
	cout << ".........\n" << "전원이 켜졌습니다.\n";
};

void Computer::turnOff() {
	cout << "전원이 꺼졌습니다." << endl;
};

void Computer::monitorOn() {
	cout << ".........\n" << "모니터가 켜졌습니다.\n";
};

void Computer::monitorOff() {
	cout << "모니터가 꺼졌습니다.\n";
};

int main() {
	Computer computer;
	int d;

	srand(time(0));
	d = rand() % 50 + 10;

	cout << "컴퓨터의 일련번호를 입력하시오. ";
	cin.getline(computer.consecutive_numbers, 11, '\n');

	if (strcmp(computer.consecutive_numbers, "abcd1234") == 0) {
		cout << endl;
		computer.turnOn();
		computer.monitorOn();

		cout << "\n현재 CPU의 온드는 " << d << "'C 입니다." << endl;
		computer.CPU_State(d);
		computer.hardware_state();

		cout << "\n전원 버튼을 눌렀습니다.\n";
		computer.turnOff();
		computer.monitorOff();

	}
	else {
		cout << "올바른 일련번호가 아닙니다.\n";
	}
	
}