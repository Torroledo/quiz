#include <math.h>
#include <stdlib.h>
#include <stdio.h>

float f(float c);
int main (int argc, char **argv){
  float a=  atof(argv[1]),    b= atof(argv[2]),  h= atof(argv[3]);
  float c;
  float x=a;
  float function=0.0;
  do{
    x+= h;
    function+= f(x)*h;
  }while(x<(b-h));
  printf("El valor de la integral es: %f \n", function);
}
float f(float c){
  return 1.0/sqrt(1.0+ (cos(c) * sin(c))); 
}
