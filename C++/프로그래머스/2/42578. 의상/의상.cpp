#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    map<string,int> mapp;
    
    for(auto& str:clothes){
        mapp[str[1]]++;
    }
    
    int answer=1;
    
    for (const auto& pair : mapp) {
        answer *= (pair.second + 1);
    }
    
    return answer - 1;
}