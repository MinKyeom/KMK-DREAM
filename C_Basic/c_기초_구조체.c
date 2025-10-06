#include <stdio.h>

struct Node {
    int value;
    struct Node* next;
};

void printValue(struct Node* node) {
    printf("Value: %d\n", node->value);  //node가 NULL이면 터짐
}

int main() {
    struct Node* p = NULL;
    printValue(p);  // 에러 발생 가능!
    return 0;
}
