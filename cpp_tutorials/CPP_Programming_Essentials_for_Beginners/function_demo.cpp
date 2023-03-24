//
// Created by Hui Shi on 24/03/2023.
//
#include<iostream>
using namespace std;

void playMusic() {
    cout <<"Play Music"<<endl;
}

void sayHi(string name) {
    cout <<"Hi "+name<<endl;
}

int areaOfCircle(int radius){
    return 3.14 * radius * radius;
}

int main() {
    playMusic();
    playMusic();
    playMusic();
    int area = areaOfCircle(5);
    cout<<"The area is "<< area <<endl;
    sayHi("Amalie");
    sayHi("Kate");
    return 0;
}