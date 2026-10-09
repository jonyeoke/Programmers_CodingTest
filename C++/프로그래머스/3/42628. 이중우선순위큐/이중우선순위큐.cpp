#include <string>
#include <vector>
#include <set>
#include <sstream>
using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    multiset<int> pq;
    
    int idx=0;
    for (const string now:operations){
        stringstream ss(now);
        char command;
        int number=0;
        ss>>command>>number;
        
        if(command=='I'){
            pq.insert(number);
        }
        else {
            if(!pq.empty()){
                if(number==1){
                    pq.erase(prev(pq.end()));
                }
                else{
                    pq.erase(pq.begin());
                }
            }
        }
    }
    
    if(pq.empty()){
        answer.push_back(0);
        answer.push_back(0);
    }
    else{
        answer.push_back(*pq.rbegin());
        answer.push_back(*pq.begin());
    }
    
    return answer;
}