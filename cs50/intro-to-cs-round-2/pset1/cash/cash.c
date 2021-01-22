#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main()
{
    int change;
    int quarters = 0;
    int dimes = 0;
    int nickels = 0;
    int pennies = 0;

    // Request change from user
    do
    {
        // Convert dollars to cents
        change = round(get_float("Changed owed: ") * 100);
    }
    while (change <= 0);

    // Calculate number of quarters
    quarters = change / 25;
    change = change % 25;

    // Calculate number of dimes
    if (change > 0)
    {
        dimes = change / 10;
        change = change % 10;
    }

    // Calculate number of nickels
    if (change > 0)
    {
        nickels = change / 5;
        change = change % 5;
    }

    // The remaining change is pennies
    pennies = change;

    // Print the number of coins to return
    printf("%d\n", quarters + dimes + nickels + pennies);
}
