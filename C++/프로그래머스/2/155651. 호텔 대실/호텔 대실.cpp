#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

bool cmp(vector<string> a, vector<string> b){
    return a[0]<b[0];
}

int timeToMinute(string time) {
    int hour = stoi(time.substr(0, 2));
    int min = stoi(time.substr(3, 2));
    return hour * 60 + min;
}

int solution(vector<vector<string>> book_time) {
    int answer = 0;
    sort(book_time.begin(), book_time.end(), cmp);
    vector<bool>check(book_time[0].size(),false);
    priority_queue<int, vector<int>, greater<int>> pq;
    for(auto book: book_time){
        int start = timeToMinute(book[0]);
    int end = timeToMinute(book[1]) + 10;

    if (pq.empty() || pq.top() > start) {
        answer++; 
        pq.push(end);
    } else {
        pq.pop();
        pq.push(end);
    }
    }
    return answer;
}