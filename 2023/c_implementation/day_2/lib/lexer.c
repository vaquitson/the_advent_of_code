#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define STRING_LITERAL 1
#define NUMERIC_LITERAL 2
#define NEW_LINE 3
#define SEMI_COL 4


typedef struct {
  int type;
  void *p_value;
} Token;


Token init_string_literal(){
  Token *new_token = (Token *)malloc(sizeof(Token));
  new_token->type = STRING_LITERAL;
  return *new_token;
}

Token init_numeric_literal(){
  Token *new_token = (Token *)malloc(sizeof(Token));
  new_token->type = NUMERIC_LITERAL;
  return *new_token;
}

Token init_new_line(){
  Token *new_token = (Token *)malloc(sizeof(Token));
  new_token->type = NEW_LINE;
  return *new_token;
}

Token init_eof(){
  Token *new_token = (Token *)malloc(sizeof(Token));
  new_token->type = EOF;
  return *new_token;
}

Token init_semi_col(){
  Token *new_token = (Token *)malloc(sizeof(Token));
  new_token->type = SEMI_COL;
  return *new_token;
}


Token get_token(FILE *file){
  Token new_token;
  void *p_value;
  char c = getc(file);
  // buffer 
  char *buffer = malloc(15);
  int i_buff = 0;
  if (c == EOF){
    new_token = init_eof(); 

  } else if (c == ';'){
    new_token = init_semi_col();
    char *semi_col =  (char *)malloc(1);
    *semi_col = ';';

  } else if (isdigit(c)){
    while (isdigit(c)){
      buffer[i_buff] = c;
      i_buff++;
      c = getc(file);
    }
    buffer[i_buff] = '\0';
    new_token = init_numeric_literal(); 

  } else if (isalpha(c)){
    while (isalpha(c)){
      buffer[i_buff] = c;
      i_buff++;
      c = getc(file);
    }
    buffer[i_buff] = '\0';
    new_token = init_string_literal(); 
  } 
}
