# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <stdbool.h>

char numbers[10] = "0123456789";

bool is_num(char character){
    // return true if the char is a number
    for (int j=0; j < strlen(numbers); j++){
        if (character == numbers[j]){
            return true;
        }
    }
    return false;
}

int main(){
    // se define un array de cracteres
    // para tener el path
    int tot = 0;

    char path[50] = "input.txt";
    FILE *pInput = fopen(path, "r");
    char buffer[255];

    char line_num[3];
    strcpy(line_num, "");

    // make a loop to iterate thought lines
    while (fgets(buffer, 255, pInput) != NULL){
        // make a loop to iterate thorugh letters
        int i = 0;
        while (true){
            if (is_num(buffer[i])){
                strncat(line_num, &buffer[i], 1);
                break;
            }
            i++;
        }

        size_t j = strlen(buffer) - 1;
        while (true){
            if (is_num(buffer[j])){
                strncat(line_num, &buffer[j], 1);
                break;
            }
            j--;
        }

        printf("%s\n", line_num);
        tot = tot + atoi(line_num);
        strcpy(line_num, "");
    }

    fclose(pInput);
    printf("\n%d", tot);
    return 0;
}