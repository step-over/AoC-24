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

    
    for (int i=0; i < left_list.size(); i++){
        sum += abs(right_list[i] - left_list[i]);
    }

    cout << sum << endl;

    return 0;
}