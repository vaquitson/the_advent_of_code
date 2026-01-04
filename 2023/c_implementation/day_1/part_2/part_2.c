# include <stdio.h>

# define NUM_IN_WORDS 9
# define MAX_LEN_WORD_NUM 6
# define MAX_INPUT_LINE 100

# define True 1

char string_number_arr[NUM_IN_WORDS][MAX_LEN_WORD_NUM] = {
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
};


int compare_strings(char *a, char *b){
    // return 1 if the strings are match and 0 if not
    while (True){
        if (*a != *b){
            return 0;
        } else if (*a == '\0' && *b == '\0'){
            return 1;
        }
        a++;
        b++;
    }
}


int slen(char *a){
    int len = 0;
    while (*a != '\0'){
        a++;
        len++;
    }
    return len;
}


int check_in_stirng(char *a, char *b){
    // return 1 if the strings a is in string b, and 0 if not
    
    // find the len of the first string
    int a_len = slen(a);
    int b_len = slen(b);

    char test_string[MAX_INPUT_LINE];
    char *P_head;

    if (a_len > b_len){
        return 0;
    }

    for (int i = 0; i < b_len; i++){
        P_head = b;
        for (int j = 0; j < a_len; j++){
            test_string[j] = *(P_head+j);
        }
        test_string[a_len] = '\0';
        printf("%s\n", test_string);
        if (compare_strings(test_string, a)){
            return 1;
        }
        b++;
    }
    return 0;
}


void get_line(FILE *file, char buffer[]){
    // puts the first line into the buffer
    // return 0 if it gets to the end of the file
    char c;
    int i = 0;
    while ((c = getc(file)) != EOF && c != '\n'){
        buffer[i] = c;
        i++;
    }
    buffer[i] = '\0';
}

int main(int argc, char *argv[]){
    char line_buffer[MAX_INPUT_LINE];
    FILE *p_file = fopen("./test.txt", "r");

    while (True){
        get_line(p_file, line_buffer);
        if (*line_buffer == '\0'){
            break;
        }

        char *head;
        char *tail;
    }
    

    fclose(p_file);
}
