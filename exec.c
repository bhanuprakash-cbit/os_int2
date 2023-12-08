#include<stdlib.h>
#include<stdio.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<unistd.h>
#include<sys/wait.h>
int main()
{
    pid_t pid;
    printf("executing ls command\n");
    if ((pid=fork())==0)
    {
        execl("/bin/ls","ls","-l",(char*)NULL);
        exit(EXIT_FAILURE);
    }
    else
    {
        wait(NULL);
        
    }
    
    printf("Executing pwd command\n");
    if ((pid=fork())==0)
    {
        execl("/bin/pwd","pwd",(char*)NULL);
        exit(EXIT_FAILURE);
    }
    else
    {
        wait(NULL);
    }
    
    printf("executing date command\n");
    if ((pid=fork())==0)
    {
        execl("/bin/date","date",(char*)NULL);
        exit(EXIT_FAILURE);
    }
    else
    {
        wait(NULL);
    }
    
    printf("executing echo command\n");
    if((pid==fork())==0)
    {
        execl("/bin/echo","echo","helo",(char*)NULL);
        exit(EXIT_FAILURE);
    }
    else
    {
        wait(NULL);
    }
    return 0;
}