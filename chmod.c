#include <stdio.h>
#include <sys/stat.h>

int main() {
    const char *file_path = "example.txt";
    mode_t new_permissions = S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH;  // Read and write for owner, read for group and others

    // Create a file (you can replace this with opening an existing file)
    FILE *file_fp = fopen(file_path, "w");
    if (file_fp == NULL) {
        perror("Error creating file");
        return 1;
    }
    fclose(file_fp);

    // Change the permissions of the file
    if (chmod(file_path, new_permissions) == 0) {
        printf("Permissions changed successfully.\n");
    } else {
        perror("Error changing permissions");
        return 1;
    }

    return 0;
}