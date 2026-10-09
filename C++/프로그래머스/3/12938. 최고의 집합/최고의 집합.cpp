#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(vector<int> a, vector<int>b){
    int result_a=1,result_b=1;
    
    for(auto i:a){
        result_a*=i;
    }
    for(auto j:b){
        result_b*=j;
    }
    return result_a>result_b;
}

vector<int> solution(int n, int s) {
    vector<int> answer;
    
    if(n>s){
        answer.push_back(-1);
        return answer;
    }
    
    int mox = s/n;
    int namj = s%n;
    
    for (int i=0;i<n;i++){
        answer.push_back(mox);
    }
    int idx = 0;
    while(namj>0){
        answer[idx]++;
        idx = (idx+1)%n;
        namj--;
    }
    sort(answer.begin(),answer.end());
    return answer;
}