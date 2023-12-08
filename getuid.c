#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
int main()
{
    uid_t user_id;
    user_id=getuid();
    printf("User id: %d\n",user_id);
}
