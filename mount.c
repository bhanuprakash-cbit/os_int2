#include<sys/mount.h>
#include<unistd.h>
#include<stdlib.h>
#include<stdio.h>
int main()
{
    const char *source_path="/dev/sdb1";
    const char *target_path="/mnt/external";
    const char *filesystem_type="ext4";
    const unsigned long mount_flag=0;
    
    if(mount(source_path,target_path,filesystem_type,mount_flag,NULL)==0)
    {
        printf("succesfful");
    }
    else
    {
        perror("error");
        return 1;
    }
    return 0;
}