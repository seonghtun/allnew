#include <stdio.h>

int main() {
  int i;

  printf("Input your age : ");
  scanf("%d", &i);// address of i call by adderess method
  printf("Your age is %d \n", i);// call by value method

  return 0;// 프로그램 꺼지니까 0 을 리턴
}
