"""
https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c
再帰関数でよさそう
これnC4とかになるから、n^4とかになるか。

なるほどー2本ずつで考えるのね
bisect_leftで[3, 4]のときに3.5がきたら返り値は1になるんだ...0だと思ってた
[1, 2, 3, 4, 4, 4, 5]
left = 3 (4のとこ)
right = 6 (5のとこ)
つまり、同じ値がきたらleftだと同じ値の中の最左のindex、rightだと同じ値の最右の次のindexになる。
間の値がきたら右側のindexになる
"""
# 再帰関数 O(N^4)
import sys
sys.setrecursionlimit(10 ** 5)
num_points, point_limit = map(int, input().split())
points = []
for _ in range(num_points):
    points.append(int(input()))
NUM_CAN_USE = 4

max_point = 0
def compute_max_point(num_use, got_point, index):
    if got_point > point_limit:
        return
    if num_use == NUM_CAN_USE or index == num_points:
        global max_point
        max_point = max(max_point, got_point)
        return
    
    compute_max_point(num_use + 1, got_point + points[index], index)
    compute_max_point(num_use, got_point, index + 1)

compute_max_point(0, 0, 0)
print(max_point)

# 半分全列挙 + 二分探索
from bisect import bisect_right
num_points, point_limit = map(int, input().split())
points = []
for _ in range(num_points):
    points.append(int(input()))

points_with_max_two_arrows  = [0]
for i in range(num_points):
    points_with_max_two_arrows.append(points[i])
    for j in range(i, num_points):
        points_with_max_two_arrows.append(points[i] + points[j])
points_with_max_two_arrows.sort()

max_point = 0
for i in range(len(points_with_max_two_arrows)):
    j = bisect_right(points_with_max_two_arrows, point_limit - points_with_max_two_arrows[i])
    if j != 0:
        j -= 1
    got_point = points_with_max_two_arrows[i] + points_with_max_two_arrows[j]
    if got_point > point_limit:
        continue
    max_point = max(max_point, got_point)
print(max_point)
