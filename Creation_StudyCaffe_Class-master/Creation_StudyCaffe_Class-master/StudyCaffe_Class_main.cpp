#include <iostream>
#include <time.h>
#include "StudyCaffe_Class.h"

using namespace std;

int main() {
	StudyCaffe studycaffe;
	int a, d, l, u;

	cout << "������� ������ �Է��ϼ���. ";
	cin.getline(studycaffe.user_id, 6, '\n');
	cout << endl;

	studycaffe.setAircon(3);
	studycaffe.setDesk(20);
	studycaffe.setLight(40);

	srand(time(0));
	u = (rand() % studycaffe.getDesk() + 1);

	studycaffe.setUser(u);

	cout << "-----���͵� ī�� �ü� ��Ȳ-----" << endl;
	cout << "���͵�ī���� ������ ������ " << studycaffe.getAircon() << "�Դϴ�.\n";
	cout << "���͵�ī���� ���� ������ " << studycaffe.getLight() << "�Դϴ�.\n";
	studycaffe.item_state();

	cout << "-----�̿��� ����-----" << endl;
	studycaffe.work_state();
	cout << "���͵�ī�並 �̿����� �̿��ڴ� " << studycaffe.getUser() << "�� �Դϴ�.\n";
	cout << "�̿� ������ å���� ���� " << studycaffe.getDesk() - u << "�Դϴ�.\n";

	cout << "\n\n.....!! ������ ���� !!.....\n\n";
	studycaffe.occur_event(studycaffe.getAircon());
	
}