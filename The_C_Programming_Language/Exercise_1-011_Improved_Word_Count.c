#include <stdio.h>
#include <ctype.h>

/*
ctype.h is for 'isalpha' I used this to detect letters instead of numbers when looking for words.
*/

#define true    0
#define false   1

main() /* Count words */
{
        int c, wordCount, isWord;
        isWord = false;
        c = wordCount = 0;
        while ((c = getchar()) != EOF) {
                if (c == ' ' || c == '\n' || c == '\t')
                        isWord = false;
                else if (isWord == false && isalpha(c))
                        isWord = true;
                        ++wordCount;
                }
        }
        printf("Word count: %d", wordCount);
}
