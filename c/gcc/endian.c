#include <stdio.h>

int main() {
  int x=1;

  if(*(char *)&x == 1) {
    printf(" Result : %d \n", *(char *)&x);// x 가 있는 주소에 한바이트 값을 가져와줘라 포인터로 보니까
    printf(" This system is Little-Endian \n");
  } else {
    printf(" Result : %d \n", *(char *)&x);
    printf(" This system is Big-Endian-Endian \n");
  }
}
