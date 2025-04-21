#include <stdio.h>

int main() {
    char str[] = "education";
    int count = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        char ch = str[i];
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
            count++;
    }
    printf("Number of vowels: %d\n", count);
    return 0;
}
