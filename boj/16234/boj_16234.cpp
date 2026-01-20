#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>

using namespace std;

int N, L, R;

int map[50][50];
int visited[50][50];

int val_total = 0;

int val_cal = 0;


bool is_changed = true;

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

bool bfs(int x, int y)
{
	queue<pair<int, int>>q;
	vector<pair<int, int>>union_members;

	q.push({ x, y });
	visited[y][x] = true;
	union_members.push_back({ x, y });

	while (!q.empty())
	{
		pair<int, int> cur = q.front();
		q.pop();

		int cx = cur.first;
		int cy = cur.second;

		for (int i = 0; i < 4; i++)
		{
			int nx = cx + dx[i];
			int ny = cy + dy[i];

			if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
			if ((abs(map[cy][cx] - map[ny][nx]) < L) || (abs(map[cy][cx] - map[ny][nx]) > R)) continue;
			if (visited[ny][nx]) continue;

			q.push({ nx, ny });
			union_members.push_back({ nx, ny });
			val_total = val_total + map[ny][nx];
			visited[ny][nx] = true;
		}
	}

	int mem_size = union_members.size();

	if (mem_size > 1)
	{
		val_cal = val_total / mem_size;
		for (int i = 0; i < mem_size; i++)
		{
			pair<int, int> cur = union_members[i];
			int cx = cur.first;
			int cy = cur.second;

			map[cy][cx] = val_cal;
		}

		return true;
	}
	else if(!is_changed)
	{
		return false;
	}

	return true;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	//freopen("input.txt", "r", stdin);

	cin >> N >> L >> R;

	int day = 0;
	
	memset(map, 0, sizeof(map));

	for (int y = 0; y < N; y++)
	{
		for (int x = 0; x < N; x++)
		{
			cin >> map[y][x];
		}
	}

	while (is_changed)
	{
		day++;
		memset(visited, 0, sizeof(visited));

		is_changed = false;
		val_total = 0;

		for (int y = 0; y < N; y++)
		{
			for (int x = 0; x < N; x++)
			{
				if (visited[y][x]) continue;
				visited[y][x] = true;
				val_total = map[y][x];
				is_changed = bfs(x, y);
			}
		}
	}

	cout << day-1;

	return 0;
}