#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> sequence, int k) {
    vector<int> answer;
    int start = 0, end=0;
    int min_length=10000001;
    int now = sequence[start];
    while(start<=end){
        if (now == k) {
    if (end - start < min_length) {
        min_length = end - start;
        answer = {start, end};
    }
    now -= sequence[start++];
} else if (now < k) {
    end++;
    if (end < sequence.size()) {
        now += sequence[end];
    } else {
        break;
    }
} else {
    now -= sequence[start++];
}
    }
    return answer;
}