#include<iostream>
using namespace std;

int main() {
	cout << "Enter your mark: ";
	int marks;
	cin >> marks;

	if(marks>80){
		cout<<"let's party: grade A"<<endl;
	}
	else if (marks>70){
		cout <<"Good job: grade B"<<endl;
	}
	else if (marks>60){
		cout<<"keep it up: grade C"<<endl;
	}
	else{
		cout<< "work hard next time. You've failed this time."<<endl;
	}

	cout<<"This program is over."<<endl;
}