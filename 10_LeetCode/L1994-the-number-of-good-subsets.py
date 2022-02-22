# https://leetcode-cn.com/problems/the-number-of-good-subsets/

from collections import Counter

def numberOfGoodSubsets(nums) -> int:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    mod = 10 ** 9 + 7

    freq = Counter(nums)
    f = [0] * (1 << len(primes))
    f[0] = pow(2, freq[1], mod)  # pow自带取余功能

    for i, occ in freq.items():
        if i == 1:
            continue
        
        # 检查 i 的每个质因数是否均不超过 1 个
        subset, x = 0, i
        check = True
        for j, prime in enumerate(primes):
            if x % (prime * prime) == 0:
                check = False
                break
            if x % prime == 0:
                subset |= (1 << j)
        
        if not check:
            continue

        # 动态规划
        for mask in range(0, (1 << len(primes))):  # 倒序和顺序更新都对，因为(1)只会更新含subset的mask，且(2)只依赖不含subset的mask。所以i和mask的更新顺序都无所谓
            if (mask & subset) == subset:  # &表示与运算符，即subset二进制数里为1的这几位，在mask二进制数里也为1
                f[mask] = (f[mask] + f[mask ^ subset] * occ) % mod
                # 本来mask已经有N个组合了，现在还可以从mark ^ subset来1 * occ个组合，所以更新一下mask的状态

    ans = sum(f[1:]) % mod
    return ans


cs = [
    # [1,2,3,4],
    # [4,2,3,15],
    [5,10,1,26,24,21,24,23,11,12,27,4,17,16,2,6,1,1,6,8,13,30,24,20,2,19],
    [10,11,5,1,10,1,3,1,26,11,6,1,1,15,1,7,22,1,1,1,1,1,23,1,29,5,6,1,1,29,1,1,21,19,1,1,1,2,1,11,1,15,1,22,14,1,1,1,1,6,7,1,14,3,5,1,22,1,1,1,17,1,29,2,1,15,10,1,5,7,1,1,1,30,1,30,1,21,10,1,1,1,1,1,2,6,5,7,3,1,1,19,29,1,7,13,14,1,5,26,19,11,1,1,1,1,1,1,1,1,22,15,1,1,13,1,17,1,1,1,13,6,1,10,1,1,17,1,1,3,14,7,17,1,13,1,1,1,1,1,11,1,1,6,1,1,1,1,1,2,1,30,2,26,1,1,14,1,26,29,30,1,13,21,1,1,14,21,1,23,1,15,23,21,1,30,19,19,1,10,23,3,3,17,22,2,26,1,11,1,23,1,1,1,15,1,1,13,1,1],
]

for nums in cs:
    print(numberOfGoodSubsets(nums))