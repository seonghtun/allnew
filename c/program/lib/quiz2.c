#include <stdio.h>
#include "libcheckprime.h"

void main(){
  int x;
  while (true){
    printf("Input integer (exit:0)=>");
    scanf("%d", &x);
    if (x == 0)
      return;
    if (checkprime(x))
      printf("%d is not prime ~~", x);
    else
      printf("%d is prime number!!",x);
  }
}
