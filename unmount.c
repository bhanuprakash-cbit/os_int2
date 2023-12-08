#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
int main()
{
    const char *target="/mnt/external";
    if(system("umount/mnt/external")==0)

{
    printf("unmount successful");
}    
else
{
    perror("error");
    return 1;
}
return 0;
    
}