#include <iostream>
#define max 10

using namespace std;

class queue
{
    int data[max];
    int front, rear;
    public:
    queue(){
        front = rear = -1;
    }
    bool isfull();
    bool isempty();
    void enqueue(int);
    int dequeue();
    void display();
};

bool queue :: isfull()
{
    if(rear==max-1)
        return true;
    else
        return false;
}

bool queue :: isempty()
{
    if(front == -1 && rear == -1)
        return true;
    else
        return false;
}

void queue :: enqueue(int x)
{
    if(isfull())
        cout<<"Queue is full";
    else
        if(rear == -1)
            front++;
            data[++rear] = x;
            cout<<"Job added";
}

int queue :: dequeue()
{
    int x;
    if(isempty())
        cout<<"queue is empty";
    else
        x = data[front];
        front++;
        cout<<"Job removed";
        return x; 
    return -1;
}

void queue :: display()
{
    if(isempty())
        cout<<"queue empty";
    else
        for(int i = 0; i<=rear; i++)
            cout<<data[i];
}

int main()
{
    queue q;
    int ch, id;
    cout<<"1.add 2. remove 3. display 4. exit";
    do{
        cout<<"\nEnter your choice:";
        cin>>ch;
        switch(ch){
            case 1 : "Enter job id:";
                    cin>>id;
                    q.enqueue(id);
                    break;
            case 2 : q.dequeue();
                    break;
            case 3 : q.display();
                    break;

        }
    }
    while(ch != 4);
}












