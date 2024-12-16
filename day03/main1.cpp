#include <fstream>
#include <iostream>
#include <algorithm>
#include <ctype.h>

using namespace std;

long is_valid_mul(string line, size_t init, size_t end) {
    size_t comma = line.find(",", init+4);

    bool res = true;

    if (comma != string::npos && comma - init - 4 < 4 && end - comma - 1 < 4){
        
        string first_digit = line.substr(init+4, comma-init-4);
        string second_digit = line.substr(comma+1, end-comma-1);

        for (char c : first_digit+second_digit) {
            res &= isdigit(c);
        }

        if (res) {
            return stoi(first_digit) * stoi(second_digit);
        }
    }
    
    return 0;
}

int main(){
    ifstream file("input.txt");
    long sum = 0;

    if (file.is_open()) {
        string line;

        while (getline(file, line)) {
            
            // iterate through "mul("
            for (size_t init = line.find("mul("); init != string::npos ; init = line.find("mul(", init+1)) {
                size_t end = line.find(")", init);

                if (end != string::npos) {
                    sum += is_valid_mul(line, init, end);
                }
            }

        }

        file.close();
    }

    cout << sum << endl;
    return 0;
}