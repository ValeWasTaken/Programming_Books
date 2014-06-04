/* Replaces two or more blank spaces with a single space. */
#include <stdio.h>

main()
{
  int c, extraSpace;

  extraSpace = 0;
  while((c = getchar()) != EOF)
  {
    if(c == ' ')
    {
      if(extraSpace == 0)
      {
        extraSpace = 1;
        putchar(c);
      }
    }
    
    else if(c != ' ')
    {
      extraSpace = 0;
      putchar(c);
    }
  }
}
