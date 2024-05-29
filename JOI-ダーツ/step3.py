from bisect import bisect_right
num_points, point_limit = map(int, input().split())
points = []
for _ in range(num_points):
    points.append(int(input()))

points_with_max_two_arrows = [0]
for i in range(num_points):
    points_with_max_two_arrows.append(points[i])
    for j in range(i, num_points):
        points_with_max_two_arrows.append(points[i] + points[j])
points_with_max_two_arrows.sort()

max_point = 0
for already_got_point in points_with_max_two_arrows:
    index = bisect_right(points_with_max_two_arrows, point_limit - already_got_point) - 1
    if index == -1:
        index = 0
    got_point = already_got_point + points_with_max_two_arrows[index]
    if got_point > point_limit:
        continue
    max_point = max(max_point, got_point)
print(max_point)
