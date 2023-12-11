#include <iostream>
#include <string.h>
#define max 10

using namespace std;

class stack
{
    char a[max];
    int top;
    public:
    stack()
    {
        top = -1;
    }
    void push(char);
    void reverse();
    void convert(char[]);
    void palindrome();
};

void stack :: push(char c)
{
    top ++;
    a[top] = c;
    a[top+1] = '\0';
    cout<<"Element pushed";
}

void stack :: reverse()
{
    char str[max];
    cout<<"reverse string";
    for(int i = top, j=0; i>=0; i--, j++)
    {
        cout<<a[i];
        str[j] = a[i];
    }
    cout<<endl;
}

void stack :: convert(char str[])
{
    int j,k, len = strlen(str);
    for(j=0, k=0; j<len; j++)
    {
        if((int)str[j] >=97 && (int)str[j] <=122 || ((int)str[j]>=65) && ((int)str[j]<=90))
        {
            if((int)str[j]<=90)
            {
                str[k] = (char)((int)str[j]+32);
            }
            else
            {
                str[k] = str[j];
            }
            k++;
        }
    }
    str[k] = '\0';
    cout<<endl<<"converted string:"<<str<<"\n";
}

void stack :: palindrome()
{
	char str[max];
	int i,j;		

	for(i=top,j=0; i>=0; i--,j++)
	{
		str[j]=a[i];
	}
	str[j]='\0';
	
	
	if(strcmp(str,a) == 0)
		cout<<"\n\nString is palindrome...";
	else
		cout<<"\n\nString is not palindrome...";
}

int main()
{
    stack st;
    char str[max];
    int i = 0;
    cout<<"Enter string";
    cin.getline(str,50);
    st.convert(str);
    while(str[i]!='\0')
    {
        st.push(str[i]);
        i++;
    }
    st.palindrome();
    st.reverse();
}