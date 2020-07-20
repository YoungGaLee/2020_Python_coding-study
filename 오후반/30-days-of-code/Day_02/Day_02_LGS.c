#include <bits/stdc++.h>

using namespace std;

// Complete the solve function below.
void solve(double meal_cost, int tip_percent, int tax_percent) {



{
    double i;
    double tip = i*20/100;
    double tax = i*8/100;
    
    double mealCost = 12*tip_percent + 20*tax_percent
    double totalCost = mealCost + tip + tax;
    int round(totalCost);

    printf("the value is %d/n", round(totalCost));

    /*double meal_cost;
    cin >> meal_cost;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int tip_percent;
    cin >> tip_percent;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int tax_percent;
    cin >> tax_percent;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    solve(meal_cost, tip_percent, tax_percent);
    */
    return 0;
}
