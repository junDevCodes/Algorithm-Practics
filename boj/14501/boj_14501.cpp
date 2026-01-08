#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

int N;
int T[20];
int P[20];

int max_profit = 0;

void dfs(int day, int sum){
    if (day >= N) {
        max_profit = max(max_profit, sum);
        return;
    }

    dfs(day + 1, sum);
    if (day + T[day] <= N) dfs(day + T[day], sum + P[day]);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> T[i] >> P[i];
    }

    dfs(0, 0);

    cout << max_profit;
}