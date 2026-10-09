#include <string>
#include <vector>
#include <queue>

using namespace std;
void createPerimeterMap(vector<vector<int>>& rectangle, vector<vector<int>>& map) {
    // 1단계: 모든 직사각형의 내부를 1로 채우기
    // 좌표를 2배로 확장하면서 채웁니다.
    for (const auto& rect : rectangle) {
        int x1 = rect[0] * 2;
        int y1 = rect[1] * 2;
        int x2 = rect[2] * 2;
        int y2 = rect[3] * 2;
        
        for (int i = y1; i <= y2; ++i) {
            for (int j = x1; j <= x2; ++j) {
                map[i][j] = 1;
            }
        }
    }

    // 2단계: 채워진 직사각형의 내부를 다시 0으로 파내기 (테두리만 남기기)
    for (const auto& rect : rectangle) {
        int x1 = rect[0] * 2;
        int y1 = rect[1] * 2;
        int x2 = rect[2] * 2;
        int y2 = rect[3] * 2;
        
        for (int i = y1 + 1; i < y2; ++i) {
            for (int j = x1 + 1; j < x2; ++j) {
                map[i][j] = 0;
            }
        }
    }
}
int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    int answer = 0;
    vector<vector<int>> map(120,vector<int>(120,0));
    vector<vector<bool>> visited(120,vector<bool>(120,false));
    queue<pair<pair<int,int>,int>> que;
    
    que.push({{characterY*2,characterX*2},0});
    visited[characterY*2][characterX*2]=true;
    
    createPerimeterMap(rectangle, map);
    
    int dy[4]={-1,1,0,0};
    int dx[4]={0,0,-1,1};
    
    while(!que.empty()){
        int nowY = que.front().first.first;
        int nowX = que.front().first.second;
        int distance = que.front().second;
        if(nowY==itemY*2&&nowX==2*itemX){
            return distance/2;
        }
        que.pop();
        for(int i=0;i<4;i++){
            int nextX = nowX+dx[i];
            int nextY = nowY+dy[i];
            if(nextX<0||nextY<0||nextX>=120||nextY>=120) continue;
            if(!visited[nextY][nextX]&&map[nextY][nextX]==1){
                que.push({{nextY,nextX},distance+1});
                visited[nextY][nextX]=true;
            }
        }
        
    }
    
    return answer;
}