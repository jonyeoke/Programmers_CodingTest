#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(vector<int> a, vector<int> b){
    return a[1]<=b[1];
}

int solution(vector<vector<int>> routes) {
    int answer = 0;
    vector<bool> check(routes.size(),false);
    int now = -30001; 
    
    sort(routes.begin(), routes.end(), cmp);
    for(auto route:routes){
        if(route[0]>now){
            answer++;
            now = route[1];
        }
    }
    
    return answer;
}