#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    long sum = 0;
    vector<int> left_list, right_list;

    ifstream file("input.txt");
    string left_number, right_number;

    //save list numbers
    if (file.is_open()){
        
        while (file >> left_number) {
            file >> right_number;

            left_list.push_back(stoi(left_number));
            right_list.push_back(stoi(right_number));
        }

        file.close();
    }

    //pair and calculate distances
    sort(left_list.begin(), left_list.end());
    sort(right_list.begin(), right_list.end());

    
    //calculate similarity score for each number of left_list
    int idx_left = 0, idx_right = 0;

    while (idx_left < left_list.size()){
        int val_left = left_list[idx_left];
        int times = 0;

        while(val_left > right_list[idx_right]) { idx_right ++; }

        while (val_left == right_list[idx_right]) { 
            times ++ ;
            idx_right ++; }

        while (val_left == left_list[idx_left]) { 
            sum += times * val_left;
            idx_left ++; }
    }

    cout << sum << endl;

    return 0;
}