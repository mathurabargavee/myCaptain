#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
int main()
{
    FILE *fp,*fptr1;
    char ch, fname[30], newch[500],filename[20],c;
    int i=0, j, COUNT=0;
    printf("Enter the filename with extension: ");
    gets(fname);
    fp = fopen(fname, "r");
    if(!fp)
    {
        printf("Error in opening the file...\nExiting...");
        getch();
        return 0;
    }
    printf("\nThe original content is:\n");
    ch = getc(fp);
    while(ch != EOF)
    {
        COUNT++;
        putchar(ch);
        newch[i] = ch;
        i++;
        ch = getc(fp);
    }
    printf("\n\n\n");
    printf("The content in reverse order is:\n");
    for(j=(COUNT-1); j>=0; j--)
    {
        ch = newch[j];
        printf("%c", ch);
        fprintf(fp,"%c",ch);
    }
    printf("\n");
    // Open another file for writing
    printf("\n\nEnter filename with extension where the contents should be copied: ");
    gets(filename);
    fptr1 = fopen(filename, "w");
    if (fptr1 == NULL)
    {
        printf("Cannot open file %s \n", filename);
        exit(0);
    }
  
    
    printf("\nContents copied to the new file!\n");
    
    c = fgetc(fp);
    while (c != EOF)
    {
        fputc(c, fptr1);
        c = fgetc(fp);
        printf("%c",c);
        
    }
     fclose(fp);
    fclose(fptr1);
  
    
  
    getch();
    return 0;
}
