#include <stdio.h>

int main() {
    int a = 10, b = 25, c = 15;
    int largest;

    if (a >= b && a >= c)
        largest = a;
    else if (b >= a && b >= c)
        largest = b;
    else
        largest = c;

    printf("Largest number is %d\n", largest);
    return 0;
}
