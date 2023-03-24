#include <iostream>
using namespace std;

int main() {
	cout << "What is the consumption of a household in units: ";
	int fuel_units;
	cin >> fuel_units;
	int charge;
	if (fuel_units>=1 && fuel_units<=100){
		charge = 0;
	}
	else if (fuel_units>=100 && fuel_units<=200){
		charge = 5 * fuel_units;
	}
	else if (fuel_units>=200 && fuel_units<=300){
		charge = 10 * fuel_units;
	}
	else if (fuel_units>=300){
		charge = 12 * fuel_units;
	}
	cout << "charge is: "<<charge<<endl;
}