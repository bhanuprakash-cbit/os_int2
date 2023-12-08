#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
int main()
{
    const char *fp="example.txt";
    uid_t new_user=1000;
    gid_t new_group=1000;
    
    FILE *file_fp=fopen(fp,"w");
    if(file_fp==NULL)
    {
        perror("error");
        return 1;
    }
    
    fclose(file_fp);
    if(chown(fp,new_user,new_group)==0)
    {
        printf("Successul");
    }
    else
    {
        perror("error");
        return 1;
    }
    return 0;
    
}
