#include <iostream>
#include <cmath>
#include <algorithm> // min 함수 사용을 위해 필요

using namespace std;

// === Global Variables (Data Section) ===
int N, M;
int map[51][51];

int house_y[100], house_x[100];
int house_cnt = 0;

int chicken_y[13], chicken_x[13];
int chicken_cnt = 0;

// [New Asset] 조합을 위한 선택 배열
// selected[i] == true 이면 i번째 치킨집이 선택된 것임
bool selected[13]; 
int min_ans = 21e8; // 충분히 큰 값으로 초기화 (약 21억)

// === Logic Section (Code Section) ===

// idx: 이번에 선택을 고려할 치킨집의 인덱스
// cnt: 현재까지 선택된 치킨집의 개수
void dfs(int idx, int cnt) {
    // 1. 종료 조건 (Base Case): M개를 모두 골랐을 때
    if (cnt == M) {
        int total_dist = 0;
        
        // 모든 집에 대하여 (Loop 1)
        for(int i = 0; i < house_cnt; i++) {
            int h_y = house_y[i];
            int h_x = house_x[i];
            int dist = 21e8; // 해당 집에서의 최소 치킨 거리

            // 선택된 치킨집들과의 거리 비교 (Loop 2)
            for(int j = 0; j < chicken_cnt; j++) {
                if(selected[j] == true) { // 선택된 치킨집만 계산
                     // TODO 1: 거리 계산 및 최소값 갱신 로직 (1~2줄)
                     // int d = abs(...) + abs(...);
                     // dist = min(dist, d);
                     int d = abs(h_y - chicken_y[j]) + abs(h_x - chicken_x[j]);
                     dist = min(dist, d);
                }
            }
            total_dist += dist;
        }

        // 도시의 치킨 거리 최솟값 갱신
        if (total_dist < min_ans) {
            min_ans = total_dist;
        }
        return;
    }

    // 2. 재귀 호출 (Recursive Step)
    // idx부터 시작해서 하나를 뽑고 다음 재귀로 넘김
    for(int i = idx; i < chicken_cnt; i++) {
        // TODO 2: Backtracking 패턴 구현 (3단계)
        // 1. i번째 치킨집 선택 마킹 (selected[i] = true)
        selected[i] = true;
        // 2. 재귀 호출 (dfs 호출, 파라미터 주의: i+1, cnt+1)
        dfs(i+1, cnt+1);
        // 3. i번째 치킨집 선택 해제 (Backtracking)
        selected[i] = false;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;
    // ... (입력부는 이전과 동일하므로 생략 가능, house_cnt/chicken_cnt 채워졌다고 가정) ...
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> map[i][j];
            if (map[i][j] == 1) {
                house_y[house_cnt] = i;
                house_x[house_cnt] = j;
                house_cnt++;
            } else if (map[i][j] == 2) {
                chicken_y[chicken_cnt] = i;
                chicken_x[chicken_cnt] = j;
                chicken_cnt++;
            }
        }
    }

    // DFS 시작
    dfs(0, 0);

    cout << min_ans << "\n";
    return 0;
}