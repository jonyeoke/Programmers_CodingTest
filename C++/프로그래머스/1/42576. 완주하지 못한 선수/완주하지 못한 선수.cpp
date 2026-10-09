#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    for (int i = 0; i < completion.size(); ++i) {
        // 만약 같은 인덱스에서 이름이 다르다면, 그 참가자가 완주하지 못한 선수입니다.
        if (participant[i] != completion[i]) {
            return participant[i];
        }
    }
    
    return participant.back();
}