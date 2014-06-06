/* Counts blanks, tabs, and new lines. */
#include<stdio.h>

main() /* Copy input to output; Exercise 1-6, Chapter 1. */
{
        int c, blanks, tabs, newLines;
        blanks,tabs,newLines = 0;

        while ((c = getchar()) != EOF)
                if (c == '\n')
                        ++newLines;
                else if (c == '\t')
                        ++tabs;
                else if (c == ' ')
                        ++blanks;
        printf("Blanks: %d\n", blanks);
        printf("Tabs: %d\n", tabs);
        printf("New lines: %d\n", newLines);
}
