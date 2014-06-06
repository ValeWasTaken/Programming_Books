/* Replaces tabs and backspaces with arrows. */
#include <stdio.h>

main()
{
  int c;
  
  while((c = getchar()) != EOF)
  {
    if(c == '\t')
    {
      putchar('-');
      putchar('>');
      /* You were supposed to write putchar('>') then '\b' then '-' for this program
        However this is the 1st edition of an extremely old book so doing so no longer
        makes sense. Thus I chose to leave it out.
      */
    }
    else if(c == '\b')
    {
      putchar('<');
      putchar('-');
    }
    else 
    { 
      putchar(c);
    }
  }
}
