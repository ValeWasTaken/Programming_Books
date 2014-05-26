/* Print Fahrenheit-Celsius table
        for f = 0, 20, ..., 300 */
#include<stdio.h>

main()
{
        int lower, upper, step;
        float fahr, celsius;

        lower = 0; /* Lower limit of the table. */
        upper = 300; /* Upper limit of the table. */
        step = 20; /* Step size */

        fahr = lower;
        while (fahr <= upper) {
                celsius = (5.0/9.0) * (fahr-32.0);
                printf("%4.0f %6.1f\n", fahr, celsius);
                fahr = fahr + step;
        }
}

/* Notes:
        - %4.0f says that a floating point number is to be printed in a space at
          least four characters wide, with no digits after the decimal point.
          
        - %6.1f describes another number to occupy at least six spaces, 
          with 1 digit after the decimal point.
*/
      
