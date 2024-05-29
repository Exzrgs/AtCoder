from collections import defaultdict

nums_length = int(input())
nums = list(map(int, input().split()))

calculations_results = [defaultdict(int) for _ in range(nums_length - 1)]
calculations_results[0][nums[0]] = 1

for i in range(1, nums_length - 1):
    for current_num, num_paterns in calculations_results[i - 1].items():
        plus_result = current_num + nums[i]
        if plus_result <= 20:
            calculations_results[i][plus_result] += num_paterns
        minus_result = current_num - nums[i]
        if minus_result >= 0:
            calculations_results[i][minus_result] += num_paterns

print(calculations_results[nums_length - 2][nums[-1]])
