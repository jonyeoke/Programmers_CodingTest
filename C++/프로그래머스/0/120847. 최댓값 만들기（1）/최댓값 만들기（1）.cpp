#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> numbers) {
    int answer = 0;
    
    auto max_idx = max_element(numbers.begin(),numbers.end());
    answer+=*max_idx;
    numbers.erase(max_idx);
    max_idx = max_element(numbers.begin(),numbers.end());
    answer*=*max_idx;
    return answer;
}