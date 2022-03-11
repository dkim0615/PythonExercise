
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long long credit_card, e, o;
    int i, osum, even, esum, sum;
    do
    {
        credit_card = get_long_long("Enter credit card number: ");
    }
    while (credit_card < 0);

// multiplying digits

    for (o = credit_card, osum = 0; o > 0; o /= 100)
    {
        osum += o % 10;
    }

    for (e = credit_card/10, esum = 0; e > 0; e /= 100)
    {

            esum += (2 * (e % 10)) / 10;
            esum += (2 * (e % 10)) % 10;
    }

// adding products' digits

    sum = osum + esum;

// validate the card company
    if (sum % 10 == 0)
    {

        if ((credit_card >= 34000000000000000 && credit_card < 35000000000000000) || (credit_card >= 370000000000000 && credit_card < 380000000000000))
        {
            printf("AMEX\n");
        }

        else if (credit_card >= 5100000000000000 && credit_card < 5600000000000000)
        {
            printf("MASTERCARD\n");
        }

        else if ((credit_card >= 4000000000000 && credit_card < 5000000000000) || (credit_card >= 4000000000000000 && credit_card < 5000000000000000))
        {
            printf("VISA\n");
        }

        else
        {
            printf("INVALID\n");
        }
    }

    else{
        printf("INVALID\n");
    }

}
