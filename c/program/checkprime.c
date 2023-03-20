int checkprime(int n){
  for(int i = 2; i <= n; i++){
    if (n % i == 0){
      if (i == n)
        return 0;
      else
        return 1;
    }
  }
}
