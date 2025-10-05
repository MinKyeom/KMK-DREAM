#include <stdio.h>

struct Node {
    int data;
    struct Node* next;
};

int main() {
    struct Node n2 = {20, NULL};
    struct Node n1 = {10, &n2};

    printf("n1.data = %d\n", n1.data);           // 10
    printf("n1.next->data = %d\n", n1.next->data); // 20

    return 0;
}