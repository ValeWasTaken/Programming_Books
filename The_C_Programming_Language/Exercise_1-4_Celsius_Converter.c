/* Print Celsius to Fahrenheit table
        for c = -50, 20, ..., 150 */
#include<stdio.h>

main()
{
        float lower, upper, step;
        float fahr, celsius;

        lower = -50.00; /* Lower limit of the table. */
        upper = 150.00; /* Upper limit of the table. */
        step = 5; /* Step size */

        celsius = lower;

        printf("Temperature converter\n");
        printf("---------------------\n");
        printf(" Cels.  Fahr.\n");
        while (celsius <= upper) {
                fahr = (celsius * (9.0/5.0) + 32);
                printf("%6.1f %4.0f\n", celsius, fahr);
                celsius = celsius + step;
        }
}
