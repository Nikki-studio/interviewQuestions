#include <iostream>

/*
Find the result of multiplication of two numbers without using multiplications
 */
template<typename Type>


// Most accurate
Type easiest_way(Type a, Type b)
{
    return b / (1/a);
}

Type

Type int_using_addition(Type a,Type b) //only accurate while using integers
{
    //is your input negative? read keenly
    bool negative = false;
    if (a < 0)
    {
        a = -a;
        if (b < 0 ) {
            b = -b;
        }
        else
        {
            negative = ! negative;
        }
    }
    else
    {
        if (b < 0)
        {
            negative = !negative;
            b = -b;
        }
   }


}










int main(void)
{
    std::cout<<"Hello, world!\n";
    return 0;
}
