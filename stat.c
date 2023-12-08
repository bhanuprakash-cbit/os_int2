#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/stat.h>
int main()
{
    struct stat file_stat;
    const char *filename="file1.txt";
    if(stat(filename,&file_stat)==0)
    {
        printf("FIle size is %ld bytes\n",file_stat.st_size);
        printf("File permissions is %o\n",file_stat.st_mode & 0777);
    }
    else
    {
        perror("Error getting information");
    }
}