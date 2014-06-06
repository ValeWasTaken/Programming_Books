/* 
Oh god, I am so sorry for whoever has to read this code. Please forgive me, it's half-assed, hahaha 

P.S. Exercise 1-9 was skipped because it wasn't a question rather than a coding problem.
*/

#define YES     1
#define NO      0

main() /* Prints words one at a time from input. */
{
  int c, inword;

        inword = NO;
        while((c = getchar()) != EOF) {
                if (c == '\n' || c == '\t')
                        inword = NO;
                else 
                        putchar(c);
                        if(c == ' ')
                                printf("\n");
        }
}
