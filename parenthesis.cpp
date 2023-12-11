#include <iostream>
#define size 10

using namespace std;

class stack
{
    int top;
    char st[size];
    public:
    stack()
    {
        top = -1;
    }
    int isfull();
    int isempty();
    void push(char);
    char pop();

};

int stack :: isfull()
{
    if(top == size)
        return 1;
    else
        return 0;
}

int stack :: isempty()
{
    if(top == -1)
        return 1;
    else
        return 0;
}

void stack :: push(char x)
{
    top++;
    st[top] = x;
}

char stack :: pop()
{
    char s = st[top];
    top--;
    return s;
}

int main()
{
    stack s1;
    char exp[20],ch ; 
    int i = 0;
    cout<<"ENTER EXP";
    cin>>exp;
    if((exp[0]==')')||(exp[0]=='}')||(exp[0]==']'))
    {
        cout<<"invalid";
        return 0;
    }
    else
    {
        while(exp[i]!='\0')
        {
            ch = exp[i];
            switch(ch)
            {
                case '(': s1.push(ch); break;
                case '[': s1.push(ch); break;
                case '{': s1.push(ch); break;
                case ')': s1.pop(); break;
                case '}': s1.pop(); break;
                case ']': s1.pop(); break;

            }
        }
        
    }
        if(s1.isempty())
        {
            cout<<"well parenthesized";
        }
        else{
            cout<<"not parenthesized";
        }
    return 0;
}