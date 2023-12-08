#include<stdio.h>
#include<unistd.h>
int main()
{
    uid_t user_id;
    user_id=getuid();
    printf("Before setuid() user id: %d\n",user_id);
    if (setuid(0)==0)
    {
        printf("After setuid() user id: %d\n",getuid());
    }
    else
    {
        perror("setuid");
        return 1;
    }
}