#include "./headers.h"


void Call_Shapes()
{
    printf("Pick your shape from the list by number.\n");

    /*
    1. rectangle
    2. square
    3. x
    4. triangle bottom left
    5. triangle bottom right
    6. triangle top left
    7. triangle top right
    8. |x|
    */



    printf("\t1. rectangle\n\t2. square\n\t3. x\n\t4. triangle bottom left\n\t5. triangle bottom right\n\t6. triangle top left\n\t7. triangle top right\n\t8.|x|\n--( CHOISE )--$  ");
    char choise[2];
    int x,y;
    scanf("%s",choise);
    choise[1] = '\0';
    if (strcmp(choise,"1")==0)
    {
        printf("--( %s )--[ width: x  height: y ]$  ",choise);
        scanf("%i %i",&x,&y);
        printf("[ width: %i height: %i ]\n",x,y);
        rectangle(x,y);
    } else if (strcmp(choise,"2")==0)
    {
        printf("--( %s )--[ side: x ]$  ",choise);
        scanf("%i",&x);
        printf("[ side: %i ]\n",x);
        square(x);
    } else if (strcmp(choise,"3")==0)
    {
        printf("--( %s )--[ width: x  height: y ]$  ",choise);
        scanf("%i %i",&x,&y);
        printf("[ width: %i height: %i ]\n",x,y);
        letterX(x,y);
    } else if (strcmp(choise,"4")==0)
    {
        printf("--( %s )--[ width: x  height: y ]$  ",choise);
        scanf("%i %i",&x,&y);
        printf("[ width: %i height: %i ]\n",x,y);
        triangleBottomLeft(x,y);
    } else if (strcmp(choise,"5")==0)
    {
        printf("--( %s )--[ width: x  height: y ]$  ",choise);
        scanf("%i %i",&x,&y);
        printf("[ width: %i height: %i ]\n",x,y);
        triangleBottomRight(x,y);
    } else if (strcmp(choise,"6")==0)
    {
        printf("--( %s )--[ width: x  height: y ]$  ",choise);
        scanf("%i %i",&x,&y);
        printf("[ width: %i height: %i ]\n",x,y);
        triangleTopLeft(x,y);
    } else if (strcmp(choise,"7")==0)
    {
        printf("--( %s )--[ width: x  height: y ]$  ",choise);
        scanf("%i %i",&x,&y);
        printf("[ width: %i height: %i ]\n",x,y);
        triangleTopRight(x,y);
    } else if (strcmp(choise,"8")==0)
    {
        printf("--( %s )--[ width: x  height: y ]$  ",choise);
        scanf("%i %i",&x,&y);
        printf("[ width: %i height: %i ]\n",x,y);
        BorderedletterX(x,y);
    }

}




void rectangle(const int x, const int y)
{
    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
        {
            if (i == 0 || i == x-1 || j == 0 || j == y-1)
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
}


void square(const int x)
{
    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < x; j++)
        {
            if (i ==  0 || i == x-1 || j == 0 || j == x-1)
            {
                printf("*");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
}


void letterX(const int x, const int y)
{
    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
        {
            if ( j == i || j == x-i-1 )
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
}


void BorderedletterX(const int x, const int y)
{
    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
        {
            if ( j == i || j == x-i-1 || j == 0 || j == y-1 ||  i == 0 || i == x-1 )
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
}


void triangleBottomLeft(const int x, const int y)
{
    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
        {
            if ( j == i || j == 0 || i == x-1 )
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
}


void triangleBottomRight(const int x, const int y)
{
    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
        {
            if ( j == x-i-1 || j == y-1 || i == x-1 )
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
}

void triangleTopLeft(const int x, const int y)
{
    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
        {
            if ( j == x-i-1 || j == 0 || i == 0 )
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
}



void triangleTopRight(const int x, const int y)
{
    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
        {
            if ( j == i || j == x-1 || i == 0 )
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
}

















