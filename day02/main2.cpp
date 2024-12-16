#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

bool increasing_comp(int b, int a){
    return !(b > a && b - a < 4);
}


bool decreasing_comp(int b, int a){
    return !(a > b && a - b < 4);
}

bool is_safe(vector<int> &report) {
    return is_sorted(report.begin(), report.end(), increasing_comp) || 
    is_sorted(report.begin(), report.end(), decreasing_comp);
}



bool is_safe_problem_dampener(vector<int> &report){
    return is_safe(report) || is_safe_removing_one(report);
}

int main(){
    ifstream file("input.txt");
    long safes_number = 0;

    if (file.is_open()) {
        string line;

        while (getline(file, line)) {
            istringstream report_line(line);
            string level;

            vector<int> report;

            while (report_line >> level) {
                report.push_back(stoi(level));
            }

            safes_number += is_safe_problem_dampener(report);

        }

        file.close();
    }

    cout << safes_number << endl;

    return 0;
}