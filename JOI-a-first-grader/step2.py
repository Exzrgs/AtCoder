"""
plus → add
minus → sub
"""

from collections import defaultdict

nums_length = int(input())
nums = list(map(int, input().split()))

calculation_results = [defaultdict(int) for _ in range(nums_length - 1)]
calculation_results[0][nums[0]] = 1

for i in range(1, nums_length - 1):
    for current_num, num_paterns in calculation_results[i - 1].items():
        add_result = current_num + nums[i]
        if add_result <= 20:
            calculation_results[i][add_result] += num_paterns
        sub_result = current_num - nums[i]
        if sub_result >= 0:
            calculation_results[i][sub_result] += num_paterns

print(calculation_results[nums_length - 2][nums[-1]])
