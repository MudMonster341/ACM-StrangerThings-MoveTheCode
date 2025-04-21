#include <stdio.h>

int main() {
    int fact = 1;
    for (int i = 1; i <= 5; i++) {
        fact *= i;
    }
    printf("Factorial of 5 = %d\n", fact);
    return 0;
}
