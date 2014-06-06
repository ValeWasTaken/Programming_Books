/* Print Fahrenheit to Celsius table
        for f = 300, 280, 260, ..., 0 
*/
#include<stdio.h>

main()
{
        int lower, upper, step;
        float fahr, celsius;

        lower = 0; /* Lower limit of the table. */
        upper = 300; /* Upper limit of the table. */
        step = 20; /* Step size */

        fahr = upper;

        printf("Temperature converter\n");
        printf("---------------------\n");
        printf("Fahr.  Cel.\n");
        while (fahr >= lower) {
                celsius = (5.0/9.0) * (fahr-32.0);
                printf("%4.0f %6.1f\n", fahr, celsius);
                fahr = fahr - step;
        }
}
