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

Phone* head;                        // ���������

Phone* getNode(int pos) {
    Phone* p;

    p = head;
    for (int i = 0; i < pos; i++) {
        if (p == NULL) {      //��ġ ����(�ش� �Ǵ� ��ġ�� ��尡 ����
            return NULL;      //ȣ���Լ��� ���� ��ġ�̹Ƿ�, ���� ó���Ͽ��� ��
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

Phone make_Phone(int degree) {   // Phone ���� �Լ�
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
        printf("���� ��ġ ����\n");
    }
}

//a�� �츮�� �Է��� ���� �ܿ� ���͸���
//b�� �츮�� �Է��� ���� CPU �µ�
void Charge_Degree(int a, int b) {

    while (a <= 100) {                           // �ܿ� ���͸����� 100%���� ���� ��
        if (a < 100) {
            if (b < 20) {
                printf("CPU �µ��� ���� �µ����� �����ϴ�.\n");
                printf("��� ������ �������Դϴ�.\n\n");
                b++;
                a += 2;
                printf("���� CPU �µ��� : %d\n", b);
                printf("���� ���͸����� : %d\n\n", a);
            }
            else if (b >= 20 && b < 40) {
                while (b <= 50) {
                    printf("CPU �µ��� ���� �µ����� ������ ���� X.\n");
                    printf("��� ������ �������Դϴ�.\n");
                    b++;
                    a += 2;
                    printf("���� CPU �µ��� : %d\n", b);
                    printf("���� ���͸����� : %d\n\n", a);
                    if (a >= 100) {
                        break;
                    }
                }
            }
            else if (b >= 40) {
                printf("CPU �µ��� ���� �µ����� �����ϴ�.\n");
                printf("�Ϲ� ������ �������Դϴ�.\n\n");
                b--;
                a++;
                printf("���� CPU �µ��� : %d\n", b);
                printf("���� ���͸����� : %d\n\n", a);
                if (a >= 100) {
                    printf("���� �����Ǿ����ϴ�.  ���� ���¸� �������Դϴ�.\n\n");
                    break;
                }
            }
        }
        if (a >= 100) {
            printf("���� �����Ǿ����ϴ�.  ���� ���¸� �������Դϴ�.\n\n");
            break;
        }
    }
}

int main() {
    int i;
    int k = 20;
    int num = 5;
    int j[5] = { 34, 13, 55, 80, 3 };                  //5�� �޴����� �ܿ� ���͸���
    int n[5];

    Init();

    for (i = 0; i < num; i++) {
        n[i] = cpu_degree(k);
        printf("%d��° �޴����� ����� �̸��� : ", i + 1);
        insert_Phone(i, make_Phone(n[i]));
        printf("\n");
        printf("%d��° �޴����� �ܿ� ���͸����� : %d\n", i + 1, j[i]);
        printf("%d��° �޴����� ���� CPU �µ��� : %d\n\n", i + 1, n[i]);

        Charge_Degree(j[i], n[i]);
        printf("\n\n");
    }
}