#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>

using namespace std;

int T;
int map[50][50];
bool visited[50][50];
int dx[] = { 0, 1, 0, -1 };
int dy[] = { 1, 0, -1, 0 };

int M;
int N;
int K;

void dfs(int x, int y) {

	visited[y][x] = true;

	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx < 0 || nx >= M || ny < 0 || ny >= N) continue;
		if (visited[ny][nx] == 0 && map[ny][nx] == 1) {
			dfs(nx, ny);
		}
	}
}

int main() {
	freopen("sample_input.txt", "r", stdin);

	ios::sync_with_stdio(false);
	cin.tie(NULL);

	// ... 문제 풀이 로직 ...
	
	cin >> T;

	for (int tc = 0; tc < T; tc++) {
		memset(map, 0, sizeof(map));
		memset(visited, 0, sizeof(visited));

		int count = 0;

		cin >> M >> N >> K;

		int m;
		int n;

		for (int k = 0; k < K; k++) {
			cin >> m >> n;
			map[n][m] = 1;
		}

		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				if (map[j][i] == 1 && visited[j][i] == 0) {
					dfs(i, j);
					count++;
				}
			}
		}

		cout << count << "\n";
	}


	return 0;
}