#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <climits>

using namespace std;

int map[10][10];
int paper[6] = { 0, 5, 5, 5, 5, 5 };
int min_ans = INT_MAX;

bool check(int x, int y, int size)
{
	if (x + size > 10 || y + size > 10) return false;

	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			if (map[y + j][x + i] == 0) return false;
		}
	}

	return true;
}

void attach(int x, int y, int size, int val)
{
	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size; j++)
		{
			map[y + j][x + i] = val;
		}
	}
}

void dfs(int x, int y, int cnt)
{
	if (min_ans < cnt) return;

	if (x > 9)
	{
		dfs(0, y + 1, cnt);
		return;
	}

	if (map[y][x] == 0)
	{
		dfs(x + 1, y, cnt);
		return;
	}

	if (y > 9)
	{
		min_ans = min(min_ans, cnt);
		return;
	}

	for (int size = 5; size > 0; size--)
	{
		if (paper[size] > 0 && check(x, y, size))
		{
			paper[size] = paper[size] - 1;

			attach(x, y, size, 0);

			dfs(x + 1, y, cnt + 1);

			attach(x, y, size, 1);

			paper[size] = paper[size] + 1;
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int result;

	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			cin >> map[i][j];
		}
	}

	dfs(0, 0, 0);

	if (min_ans == INT_MAX) result = -1;
	else result = min_ans;

	cout << result;

	return 0;
}