int main() {
    string data;
    std::getline(std::cin, data);
    vector<int> params = Utility::parseIntVector(data);
    Solution solution;
    std::cout <<  solution.aplusb(params[0], params[1]) << std::endl;
    return 0;
}