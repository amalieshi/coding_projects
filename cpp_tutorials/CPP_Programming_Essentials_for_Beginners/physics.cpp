#include<iostream>
using namespace std;

int main(){
	
	//User Input Data
	int physics, chem, math;
	cout << "What is the physics score :";
	cin >> physics;
	cout << "What is the chemistry score :";
	cin >> chem;
	cout << "What is the math score :";
	cin >> math;

	//Processing
	float avg = (physics + chem + math)/3.;

	//Output
	cout <<"Average marks: "<< avg<<endl;
	return 0;
}