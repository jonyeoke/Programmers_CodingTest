#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

string solution(string s) {
    string answer = "";
    stringstream ss(s);
    vector<int> arr;
    int num=0;
    while(ss>>num){
        arr.push_back(num);
    }
    sort(arr.begin(),arr.end());
    
    answer += to_string(arr.front());
    answer += " ";
    answer += to_string(arr.back());
    
    return answer;
}