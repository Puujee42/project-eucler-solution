#include <iostream>
#include <unordered_map>
#include <utility>

void calculate(int limit) {
    std::unordered_map<int, std::pair<int, int>> collect;
    for (int i = 1; i < limit; ++i) {
        for (int j = i; j < limit; ++j) {
            int sum = i * i * i + j * j * j;
            auto it = collect.find(sum);
            if (it != collect.end()) {
                auto pair1 = it->second;
                std::pair<int, int> pair2 = {i, j};
                if (pair1.first != pair2.first && pair1.second != pair2.second) {
                    std::cout << pair1.first << "^3 + " << pair1.second << "^3 = "
                              << pair2.first << "^3 + " << pair2.second << "^3 = " << sum << "\n";
                }
            } else {
                collect[sum] = {i, j};
            }
        }
    }
}

int main() {
    calculate(1000);
    return 0;
}