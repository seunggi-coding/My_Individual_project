#include <iostream>
#include <time.h>
#include "StudyCaffe_Class.h"

using namespace std;

int main() {
	StudyCaffe studycaffe;
	int a, d, l, u;

	cout << "사용자의 정보를 입력하세요. ";
	cin.getline(studycaffe.user_id, 6, '\n');
	cout << endl;

	studycaffe.setAircon(3);
	studycaffe.setDesk(20);
	studycaffe.setLight(40);

	srand(time(0));
	u = (rand() % studycaffe.getDesk() + 1);

	studycaffe.setUser(u);

	cout << "-----스터디 카페 시설 현황-----" << endl;
	cout << "스터디카페의 에어컨 개수는 " << studycaffe.getAircon() << "입니다.\n";
	cout << "스터디카페의 전등 개수는 " << studycaffe.getLight() << "입니다.\n";
	studycaffe.item_state();

	cout << "-----이용자 관점-----" << endl;
	studycaffe.work_state();
	cout << "스터디카페를 이용중인 이용자는 " << studycaffe.getUser() << "명 입니다.\n";
	cout << "이용 가능한 책상의 수는 " << studycaffe.getDesk() - u << "입니다.\n";

	cout << "\n\n.....!! 에어컨 고장 !!.....\n\n";
	studycaffe.occur_event(studycaffe.getAircon());
	
}