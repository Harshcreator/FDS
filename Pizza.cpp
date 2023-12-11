#include <iostream>
#define max 5

using namespace std;

class pizza
{
    int front, rear;
    int order[max];
    public:
    pizza()
    {
        front = rear = -1;
    }
    bool add(int x);
    void serve();
    void display();
};

bool pizza :: add(int x)
{
    if(rear == -1){
        front = rear = 0;
        order[rear] = x;
        return true;
    }
    else{
        int pos = (rear+1)%max;
        if(pos == front){
            cout<<"queue is full";
            return false;
        }
        else{
            rear = pos;
            order[rear] = x;
            return true;
        }
    }
}
void pizza :: serve()
{
    if(front == -1){
        cout<<"No orders";
        return;
    }
    else{
        cout<<"order number"<<order[front];
        if(front == rear){
            front = rear = -1;
        }
        else{
            front = (front+1)%max;
        }
    }
}

void pizza :: display()
{
    int i = 0;
    if(front == -1){
        cout<<"No orders";
    }
    else{
        cout<<"Order list: ";
        while(i != rear){
            cout<<order[i]<<" ";
        }
        i++;
    }
}

int main(){
    int ch,x;
    pizza q;
    do{
        cout<<"1. add 2. remove 3. display";
        cout<<"Enter choice";
        cin>> ch;
        switch(ch){
            case 1: x++;
            if(q.add(x)){
                cout<<"Order added";
            }
            else{
                x--;
            }
            break;
            case 2 : q.serve();
            break;
            case 3 : q.display();
            break;
            
        }
    }
    while(ch!=4);
}