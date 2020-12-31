#include <iostream>
#include <time.h>

using namespace std;

class Computer {

public:
	char consecutive_numbers[11];		//�Ϸù�ȣ

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
		cout << "\n---\t---\t---\n\n" << "CPU�� ���峵���ϴ�.\n" << "\n---\t---\t---\n\n";
	}
	else
		cout << "\n---\t---\t---\n\n" << "CPU ���°� �����Դϴ�.\n" << "\n---\t---\t---\n\n";
};

void Computer::turnOn() {
	cout << ".........\n" << "������ �������ϴ�.\n";
};

void Computer::turnOff() {
	cout << "������ �������ϴ�." << endl;
};

void Computer::monitorOn() {
	cout << ".........\n" << "����Ͱ� �������ϴ�.\n";
};

void Computer::monitorOff() {
	cout << "����Ͱ� �������ϴ�.\n";
};

int main() {
	Computer computer;
	int d;

	srand(time(0));
	d = rand() % 50 + 10;

	cout << "��ǻ���� �Ϸù�ȣ�� �Է��Ͻÿ�. ";
	cin.getline(computer.consecutive_numbers, 11, '\n');

	if (strcmp(computer.consecutive_numbers, "abcd1234") == 0) {
		cout << endl;
		computer.turnOn();
		computer.monitorOn();

		cout << "\n���� CPU�� �µ�� " << d << "'C �Դϴ�." << endl;
		computer.CPU_State(d);
		computer.hardware_state();

		cout << "\n���� ��ư�� �������ϴ�.\n";
		computer.turnOff();
		computer.monitorOff();

	}
	else {
		cout << "�ùٸ� �Ϸù�ȣ�� �ƴմϴ�.\n";
	}
	
}