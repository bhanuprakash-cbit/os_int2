#include<stdio.h>
#include<unistd.h>
int main()
{
    int current_priority=nice(0);
    printf("Current process priority value:%d\n",current_priority);
    int new_priority=nice(10);
    if (new_priority==-1){
        perror("nice");
        return 1;
    }
    else
    {
        printf("New process priority value:%d\n",new_priority);
    }
}