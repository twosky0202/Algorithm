import sys
input = sys.stdin.readline

n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))

nums.sort()

# 산술평균
print(round(sum(nums) / len(nums)))

# 중앙값
print(nums[len(nums)//2])

# 최빈값
cnt = dict()
for i in nums:
    if i in cnt:
        cnt[i]+= 1
    else:
        cnt[i] = 1

mx = max(cnt.values())
mx_list = []

for i in cnt:
    if cnt[i] == mx:
        mx_list.append(i)

if len(mx_list) > 1:
    print(mx_list[1])
else:
    print(mx_list[0])

# 범위
print(max(nums) - min(nums))
