
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> A, vector<int> B) {
    int answer = 0;
    
    // 1. A와 B 배열을 오름차순으로 정렬합니다.
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    
    int a_idx = 0; // A팀 선수를 가리키는 포인터
    
    // 2. B팀 선수를 기준으로 순회합니다.
    for (int b_idx = 0; b_idx < B.size(); b_idx++) {
        // 3. A팀 선수가 B팀 선수보다 약하면 승리합니다.
        if (A[a_idx] < B[b_idx]) {
            answer++;    // 승점 획득
            a_idx++;     // 이긴 A팀 선수는 다음 경기에 나올 필요가 없으므로 다음 선수로 넘어갑니다.
        }
        // B팀 선수는 이기든 지든 다음 선수로 넘어갑니다. (for문이 b_idx를 자동으로 증가시킴)
    }
    
    return answer;
}