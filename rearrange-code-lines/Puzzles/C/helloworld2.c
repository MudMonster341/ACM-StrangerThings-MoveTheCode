#include <stdio.h>

int main() {
    int arr[] = {4, 7, 2, 9, 5};
    int max = arr[0];
    for (int i = 1; i < 5; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    printf("Maximum value is %d\n", max);
    return 0;
}
