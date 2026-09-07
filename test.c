#include <stdio.h>

double cube(double x)
{
    return x*x*x;
}




int main(void)
{
    double x[5] = {1.0, 2.0, 3.0, 4.0, 5.0};

    printf("The value of x[2] is: %f\n", x[2]);
    printf("The cube of x[2] is: %f\n", cube(x[2]));

}

