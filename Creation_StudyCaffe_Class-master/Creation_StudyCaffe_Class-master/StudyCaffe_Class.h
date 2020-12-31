#include <iostream>

class StudyCaffe {

private:
	int aircon;
	int light;
	int desk;
	int user;

public:
	char user_id[6];			//5ÀÚ¸® user id
	void item_state();
	void work_state();
	void occur_event(int);

	int getAircon();
	void setAircon(int a);
	
	int getLight();
	void setLight(int l);

	int getDesk();
	void setDesk(int d);
	
	int getUser();
	void setUser(int u);

};