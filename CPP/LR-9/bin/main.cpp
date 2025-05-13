#include <iostream>
#include <vector>
#include <map>
#include "adapters.h"

int main() {
    std::vector<int> v = { 1,2,3,4,5,6 };

    std::cout << "\nVector: ";
    for (int x : v) std::cout << x << " ";

    std::cout << "\nFilter + Transform: ";
    auto pipeline = v | filter([](int x) { return x % 2 == 1; })
        | transform([](int x) { return x * x; });

    for(int x : pipeline) {
        std::cout << x << " "; // 1 9 25
    }

    std::map<int, std::string> m = {{1, "one"}, {2, "two"}};
    std::cout << "\nKeys: ";
    for(auto k : m | keys()) {
        std::cout << k << " "; // 1 2
    }

    std::cout << "\nValues: ";
    for(auto v : m | values()) {
        std::cout << v << " "; // one two
    }


    std::cout << "\nDrop: ";
    auto dropped  = v | drop(2);
    for (int x : dropped) std::cout << x << " ";


    std::cout << "\nTake: ";
    auto taken = v | take(2);
    for (int x : taken) std::cout << x << " ";
    
    std::cout << "\nReverse: ";
    auto reversed = v | reverse();
    for (int x : reversed) std::cout << x << " ";
    std::cout << "\n";


    return 0;
}