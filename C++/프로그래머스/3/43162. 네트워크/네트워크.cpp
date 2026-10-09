#include <string>
#include <vector>
#include <stack>
using namespace std;

void dfs(int now, int n, vector<vector<int>>& computers,vector<bool>& visited){
    for(int i=0;i<n;i++){
        if(!visited[i]&&computers[now][i]){
            visited[i]=true;
            dfs(i,n,computers,visited);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<bool> visited(n,false);
    
    for(int i=0;i<n;i++){
        if(!visited[i]){
            answer++;
            visited[i]=true;
            dfs(i,n,computers,visited);
        }
    }
    return answer;
}