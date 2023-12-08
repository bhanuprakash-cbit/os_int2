#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>
#include<stdlib.h>
int main()
{
    const char *source_file="source.txt";
    const char *link_file="linked.txt";
    
    FILE *source_fp=fopen(source_file,"w");
    if (source_fp==NULL)
    {
        perror("error");
        return 1;
    }
    fclose(source_fp);
    
    if (link(source_file,link_file)==0)
    {
        printf("Link successful");
    }
    else
    {
        perror("error");
        return 1;
    }
    return 0;
}