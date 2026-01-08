#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

int N;
int nums[12];
int operators[4];

int max_res = INT_MIN;
int min_res = INT_MAX;

void dfs(int idx, int sum){
    if (idx == N) {
        max_res = max(max_res, sum);
        min_res = min(min_res, sum);
        return;
    }

    for (int i = 0; i < 4; i++) {
        if (operators[i] > 0) {
            operators[i]--;

            if (i == 0) dfs(idx + 1, sum + nums[idx]);
            else if (i == 1) dfs(idx + 1, sum - nums[idx]);
            else if (i == 2) dfs(idx + 1, sum * nums[idx]);
            else if (i == 3) dfs(idx + 1, sum / nums[idx]);

            operators[i]++;
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> nums[i];
    }
    for (int i = 0; i < 4; i++){
        cin >> operators[i];
    }

    dfs(1, nums[0]);

    cout << max_res << "\n";
    cout << min_res << "\n";
}