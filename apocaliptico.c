#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main()
{
    int num;
    double result;
    char output[500];
    char *ret;
    for(num=970;num<=970;num++)
    {
        scanf("%d", &num);
        result=pow(2,num);
        snprintf(output, 500, "%.500g", result);
        printf("DIGITOS: %d\n\n ",(int) strlen(output));

        if((ret=strstr(output,"666"))!=NULL)
        {
            printf("NUMERO: %s\n\n\n", output);
            printf("LOCAL: %s\n\n\n", ret);
            printf("NUM: %d\n", num);
        }
        else
            printf("Nao apocalipitico\n");
    }

    return 0;
}
