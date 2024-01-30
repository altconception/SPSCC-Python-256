#include <stdio.h>

void onePointOne(int grade)
{
    printf("I hope you get over %d grade in CNA 256!", grade);
    return 0;
}

void onePointTwo()
{
    printf("The difference between these values are as follows: \nThe first value is a string, and is not able to be used for mathematical operations. \nThe second value is a basic integer. This cannot store large values (in terms of memory allocation), or non-whole numbers. \nThe third value is a float, as denoted by the decimal point. These can store larger (in memory terms) numbers. \nThe last value is a boolean, which can either be True or False, or 1 or 0. ");
    return 0;
    /*how funny would it be if I described them based on syntax errors by incorrectly using them*/
}

void onePointThree(int grade)
{
    printf("If you study hard you might even get over %d percent!", grade+10);
    return 0;
}

void onePointFour()
{
    float first = 1.0;
    int second = -3;
    float third = 343.0;
    int fourth = 0;
    float fith = -21.0;
    float sixth = 2.3333333333333334;

    char placement1[24];
    char placement2[24];
    
    printf("Let's play a game! Josh is lazy and doesn't want to do math, so let's make the\nuser figure out how to get the values needed!\n\nThe values needed are: \n%f, %d, %f, %d, %f, %f\n\n", first, second, third, fourth, fith, sixth);

    printf("Using only 3, 3.0, -3, -3.0, 7, 7.0, -7, and -7.0, how can get multiply or divide to get the above values?\nChoose your first number: ");
    scanf("%s\n", &placement1);
    printf("Choose your next number: ");
    scanf("%s", &placement2);

    char nums[] = {placement1, placement2};
    int i;
    for (i = 0; i < 2; i++)
    {
    int counter = 0;
    float placementFloat = 0.0;
    float placementFloat2 = 0.0;
    int placementInt = 0;
    int placementInt2 = 0;

    if(strchr(nums[counter], '.') != NULL )
    {
        
        if(placementFloat != 0.0)
        {
            placementFloat2 = nums[counter];
        }
        else
        {
            placementFloat = nums[counter];
        }

        counter++;

    }
    else
    {
       
        if(placementInt != 0)
        {
            placementInt2 = nums[counter];
        }
        else
        {
            placementInt = nums[counter];
        }
        
        counter++;
    }
    }

    char operator[1];

    printf("Are you multiplying or dividing? M for multiplying and D for dividing: ");
    scanf("%c" &operator[1]);

    if(placementFloat = 0.0)
    {
        int op1 = placementInt;
        int op2 = placementInt2;
    }
    else if(placementInt = 0)
    {
        float op1 = placementFloat;
        float op2 = placementFloat2;
    }
    else if(placementFloat2 = 0)
    {
        float op1 = placementFloat;
        int op2 = placementInt;       
    }
    else
    {
        int op1 = placementInt;
        float op2 = placementFloat;
    }

    if(operator = ("M" || "m"))
    {
        printf("%d", op1 * op2);
    }else if(operator = ("D" || "d"))
    {
        printf("%d", op1 / op2);
    }



    return 0;
}

void onePointFive()
{
    printf("The difference between these outputs is that when multiplying a string, it repeats it X many times, \nwhile for an integer or float, it does the mathmatical evaulation.");
    return 0;
}