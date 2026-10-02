#include <stdio.h>
#include <errno.h>
#include <stdint.h>
#include <string.h>

#define BUFF_SIZE 100
#define INPUT_PATH "inputs/main_input_1.txt"
//#define INPUT_PATH "inputs/test_input_1.txt"

int main(){
  FILE *f;
  size_t read_s;
  int floor = 0; 
  char buf[BUFF_SIZE];

  f = fopen(INPUT_PATH, "r");
  if (f == NULL){
    printf("ERROR: fopen faild: %s\n", strerror(errno));
    return -1;
  }
  
  do {
    read_s = fread(buf, sizeof(char), BUFF_SIZE, f);
    if (read_s > 0){
      for (size_t i = 0; i < read_s; i++){
        if (buf[i] == '(' ){
          floor++; 
        } else if (buf[i] == ')'){
          floor--;
        }
      }
    }
  } while(read_s > 0);

  printf("Santas FLoor: %d\n", floor);
  return 0;
}
