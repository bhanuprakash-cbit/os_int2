#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
int main()
{
    const char *unlink_file="linked.txt";
    
    FILE *unlink_fp=fopen(unlink_file,"w");
    if(unlink_fp==NULL)
    {
        perror("error");
        return 1;
    }
    
    if (unlink(unlink_file)==0)
    {
        printf("unlink successful");
        
    }
    else
    {
        perror("error");
        return 1;
    }
    return 0;
}