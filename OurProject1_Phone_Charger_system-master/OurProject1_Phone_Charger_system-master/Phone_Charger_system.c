#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#pragma warning(disable:4996)

typedef struct Phone {
    int CPU_Degree;
    char User_name[11];
    int Battery;
    struct Phone* link;
} Phone;

Phone* head;                        // 헤드포인터

Phone* getNode(int pos) {
    Phone* p;

    p = head;
    for (int i = 0; i < pos; i++) {
        if (p == NULL) {      //위치 오류(해당 되는 위치의 노드가 없음
            return NULL;      //호출함수는 없는 위치이므로, 에러 처리하여야 함
        }
        p = p->link;
    }
    return p;
}

void Init() {
    Phone* p, * removed;

    for (p = head; p != NULL;) {
        removed = p;
        p = p->link;
        free(removed);
    }

    head = NULL;
}

int cpu_degree(int degree) {
    int cpu_degree;
    cpu_degree = rand() % degree + 5;
    return cpu_degree;
}

Phone make_Phone(int degree) {   // Phone 생성 함수
    char name[11];
    Phone newPhone;

    scanf("%s", name);
    strcpy(newPhone.User_name, name);
    newPhone.CPU_Degree = cpu_degree(degree);
    newPhone.link = NULL;

    return newPhone;
}

int size() {
    Phone* p;
    int j = 0;
    for (p = head; p != NULL; p = p->link) {
        j = j + 1;
    }
    return j;
}

void insert_Phone(int pos, Phone item) {
    Phone* new;
    Phone* pre = getNode(pos - 1);

    new = (Phone*)malloc(sizeof(Phone));
    strcpy(new->User_name, item.User_name);
    new->CPU_Degree = item.CPU_Degree;

    if (pos == 0) {
        if (head == NULL) {
            head = new;
            new->link = NULL;

        }
        else {
            new->link = getNode(pos);
            head = new;
        }
    }
    else {
        if (pre != NULL) {
            new->link = pre->link;
            pre->link = new;
        }
    }
    if (pos > size()) {
        printf("삽입 위치 오류\n");
    }
}

//a는 우리가 입력한 현재 잔여 배터리량
//b는 우리가 입력한 현재 CPU 온도
void Charge_Degree(int a, int b) {

    while (a <= 100) {                           // 잔여 배터리량이 100%보다 작을 때
        if (a < 100) {
            if (b < 20) {
                printf("CPU 온도가 기준 온도보다 낮습니다.\n");
                printf("고속 충전이 진행중입니다.\n\n");
                b++;
                a += 2;
                printf("현재 CPU 온도는 : %d\n", b);
                printf("현재 배터리량은 : %d\n\n", a);
            }
            else if (b >= 20 && b < 40) {
                while (b <= 50) {
                    printf("CPU 온도가 기준 온도보다 높지만 과열 X.\n");
                    printf("고속 충전이 진행중입니다.\n");
                    b++;
                    a += 2;
                    printf("현재 CPU 온도는 : %d\n", b);
                    printf("현재 배터리량은 : %d\n\n", a);
                    if (a >= 100) {
                        break;
                    }
                }
            }
            else if (b >= 40) {
                printf("CPU 온도가 기준 온도보다 높습니다.\n");
                printf("일반 충전이 진행중입니다.\n\n");
                b--;
                a++;
                printf("현재 CPU 온도는 : %d\n", b);
                printf("현재 배터리량은 : %d\n\n", a);
                if (a >= 100) {
                    printf("완전 충전되었습니다.  현재 상태를 유지중입니다.\n\n");
                    break;
                }
            }
        }
        if (a >= 100) {
            printf("완전 충전되었습니다.  현재 상태를 유지중입니다.\n\n");
            break;
        }
    }
}

int main() {
    int i;
    int k = 20;
    int num = 5;
    int j[5] = { 34, 13, 55, 80, 3 };                  //5개 휴대폰의 잔여 배터리량
    int n[5];

    Init();

    for (i = 0; i < num; i++) {
        n[i] = cpu_degree(k);
        printf("%d번째 휴대폰의 사용자 이름은 : ", i + 1);
        insert_Phone(i, make_Phone(n[i]));
        printf("\n");
        printf("%d번째 휴대폰의 잔여 배터리량은 : %d\n", i + 1, j[i]);
        printf("%d번째 휴대폰의 현재 CPU 온도는 : %d\n\n", i + 1, n[i]);

        Charge_Degree(j[i], n[i]);
        printf("\n\n");
    }
}