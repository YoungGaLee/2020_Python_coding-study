using namespace std;
#include <iostream>


int a;

scanf("%d, &a");

if (a<0)
printf("Age is not valid, setting age to 0.\n");

if (a<10)
printf("You are young.\nYou are young.\n");

if (a<16)
printf("You are young.\nYou are a teenager.\n");

if (a<18)
printf("You are a teenager.\nYou are old.\n");

else
printf("You are old.\nYou are old.\n");

/*
class Person{
    public:
        int age;
        Person(int initialAge);
        void amIOld();
        void yearPasses();
    };

    Person::Person(int initialAge){
        // Add some more code to run some checks on initialAge

    }

    void Person::amIOld(){
        // Do some computations in here and print out the correct statement to the console 

    }

    void Person::yearPasses(){
        // Increment the age of the person in here

    } */


int main(){
