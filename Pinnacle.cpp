#include <iostream>
#include <cstring>
using namespace std;

struct node
{
	void addatbeg();
	void display();
	void del();
	char info[10];
	int prn;
	struct node *next,*start=NULL,*end=NULL;
};

void node::addatbeg()
{
struct node *ptr;
ptr=new node;
struct node *temp;


if(start==NULL)
{
	
	cout<<"Enter Name and then PRN of President.  \n";
	cin>>ptr->info;
	cin>>ptr->prn;
	ptr->next=NULL;
	start=ptr;
	end=start;
}
else
{
if(start->next==NULL)
{
	temp=start;
	cout<<"Enter Name and then PRN of Secretary.  \n";
	cin>>ptr->info;
	cin>>ptr->prn;

	end->next=ptr;
	end=end->next;

}
else
{
	struct node *ptr1;
	ptr1=new node;
	temp=start;
	cout<<"Enter Name and then PRN of Member.  \n";
	cin>>ptr1->info;
	cin>>ptr1->prn;
	while(temp->next->next!=NULL)
	{
		temp=temp->next;
	}
	temp->next=ptr1;
	ptr1->next=end;

}

}

}

void node::display()
{
cout<<"\n";
struct node *ptr;
ptr=new node;
ptr=start;
if(start==NULL)
	cout<<"\nList is Empty\n";
else
{
while(ptr!=NULL){

	cout<<"Name: "<<ptr->info<<"\n";
	cout<<"PRN : "<<ptr->prn<<"\n";
	cout<<"\n";
	ptr=ptr->next;
	}


}
	cout<<"\n";
}



void node::del()
{
int prn_no,deleted=0;
cout<<"\n\nEnter PRN to delete ";
cin>>prn_no;
struct node * temp=new node;
struct node * free=new node;
temp=start;
if(temp->next!=NULL)
	{
		while(temp->prn!=prn_no)
		{
			temp=temp->next;
		}
	free=temp->next;
	temp->next=temp->next->next;
	delete free;
	cout<<"\n\nDeleted Successfully\n\n";
	deleted=1;
	}
if(start->next==NULL && start->prn==prn_no)
	{
		start=NULL;
	cout<<"\n\nDeleted Successfully\n\n";
	deleted=1;
	}
if(deleted==0)
if(start->prn!=prn_no && start->next!=NULL)
{
	cout<<"\n\nNo Record Found\n\n";
}


}

int main()
{
node a,b;


int choice,c;
while(1)
{
cout<<"1.Display both lists\n2.Add for first linked list\n3.Add for second linked list\n4.concatenate both lists\n5.Delete Record\n6.exit\n";
cin>>choice;
switch(choice)
{
case 1: a.display();
cout<<"\nSecond list is below\n";
b.display();
break;
case 2:
a.addatbeg();
break;
case 3:
b.addatbeg();
break;
case 4:
a.end->next=b.start;
break;
case 5:
cout<<"Enter 1. for first list \n 2. for Second list\n\n";
cin>>c;
if(c==1)
a.del();
if(c==2)
b.del();
break;
case 6: return 0;
break;

}
}


return 0;
}