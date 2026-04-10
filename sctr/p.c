#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char *str = "Hello, World!";
    char buffer[50];

    // Copy the string to the buffer
    strncpy(buffer, str, sizeof(buffer) - 1);
    buffer[sizeof(buffer) - 1] = '\0'; // Ensure null-termination

    printf("Copied string: %s\n", buffer);

    return 0;
}
