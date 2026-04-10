#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char input[100];
    printf("Enter a string: ");
    fgets(input, sizeof(input), stdin);
    
    // Remove newline character if present
    input[strcspn(input, "\n")] = '\0';
    
    printf("You entered: %s\n", input);
    return 0;
}