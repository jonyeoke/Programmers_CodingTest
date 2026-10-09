#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <algorithm>


using namespace std;

long long solution(int n, vector<int> works) {
    long long answer = 0;
    
    priority_queue<int> pq(works.begin(), works.end());
    while(n>0){
        if(pq.top()==0){
            return 0;
        }
        int max_work = pq.top();
        pq.pop();
        pq.push(max_work-1);
        n--;
    }
    
    while(!pq.empty()){
        long long top = pq.top();
        pq.pop();
        answer+=top*top;
    }
    return answer;
}