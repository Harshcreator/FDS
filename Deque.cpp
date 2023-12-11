#include <iostream>
using namespace std;
#define max 5

class deque
{
    int a[10], front, rear, count;
    public:
    deque()
    {
        front = rear = -1;
        count = 0;
    }
        void addf(int);
        void addl(int);
        void delf();
        void dell();
        void display();
};

void deque :: addf(int x)
{
    int i;
    if(front == -1)
    {
        front++;
        a[rear++] = x;
        count++;
    }
    else if(rear>=max-1)
    {
        cout<<"overflow";
    }
    else
    {
        for( i = count; i>=0; i--)
        {
            a[i] = a[i-1];
        }
        a[i] = x;
        count++;
        rear++;
    }
}

void deque::addl(int x)
{
	if(front==-1)
	{
		front++;
		rear++;
		a[rear]=x;
		count++;
	}
	else if(rear>=max-1)
	{
		cout<<"\nInsertion is not possible,overflow!!!";
		return;
	}
	else
	{
		a[++rear]=x;
	}
}
void deque::display()
{

	for(int i=front;i<=rear;i++)
	{
		cout<<a[i]<<" ";	
    }
}

void deque::delf()
{
	if(front==-1)
	{
		cout<<"Deletion is not possible:: Dequeue is empty";
		return;
	}
	else
	{
		if(front==rear)
		{
			front=rear=-1;
			return;
		}
		cout<<"The deleted element is "<<a[front];
		front=front+1;
	}
}
void deque::dell()
{
	if(front==-1)
	{
		cout<<"Deletion is not possible:Dequeue is empty";
		return;
	}
	else
	{
		if(front==rear)
		{
			front=rear=-1;
		}
		cout<<"The deleted element is "<< a[rear];
		rear=rear-1;
	}
}
int main()
{
	int c,item;
	deque d1;

	do
	{
		cout<<"\n\n****DEQUE OPERATION****\n";
		cout<<"\n1-Insert at beginning";
		cout<<"\n2-Insert at end";
		cout<<"\n3_Display";
		cout<<"\n4_Deletion from front";
		cout<<"\n5-Deletion from rear";
		cout<<"\n6_Exit";
		cout<<"\nEnter your choice<1-4>:";
		cin>>c;

		switch(c)
		{
		case 1:
			cout<<"Enter the element to be inserted:";
			cin>>item;
			d1.addf(item);
			break;

		case 2:
			cout<<"Enter the element to be inserted:";
			cin>>item;
			d1.addl(item);
			break;

		case 3:
			d1.display();
			break;

		case 4:
			d1.delf();
			break;
		case 5:
			d1.dell();
			break;

		case 6:
			exit(1);
			break;

		default:
			cout<<"Invalid choice";
			break;
		}

	}while(c!=7);
	return 0;

}
