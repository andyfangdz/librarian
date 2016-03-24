#include <iostream>
#include <string>
#include <fstream>
#include "Solution.cpp"

using namespace std;

int main(int argc, char *argv[]) {
	ifstream in(argv[1])
	ofstream out(argv[2]);

    string data;

    std::getline(in, data);
    int a = stoi(data);

    std::getline(in, data);
    int b = stoi(data);

    Solution solution;
    out <<  solution.aplusb(a, b) << std::endl;
    out.close();
    return 0;
}