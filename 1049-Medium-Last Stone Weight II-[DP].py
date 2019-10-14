class Solution:
    # 这个是只能相邻的石头相互碰撞
    def lastStoneWeightII_neighbor(self, stones):
        N = len(stones)
        # states = [[0]*N]*N This is totally wrong!
        states = [[0]*N for _ in range(N)]
        for dif in range(N):
            for i in range(N-dif):
                j = i + dif
                if dif == 0:
                    states[i][j] = stones[i]
                else:
                    states[i][j] = min(abs(states[i][k]-states[k+1][j]) for k in range(i, j))
        return states

    def lastStoneWeightII(self, stones):
        '''
        Think of the final answer as a sum of weights with + or - sign symbols infront of each weight. 
        Actually, all sums with 1 of each sign symbol are possible.

        Use dynamic programming: for every possible sum with N stones, those sums +x or -x is possible with N+1 stones, where x is the value of the newest stone. 
        (This overcounts sums that are all positive or all negative, but those don't matter.)
        '''
        N = len(stones)
        S = sum(stones)
        states = [[0]*(S+1) for _ in range(N+1)]
        states[0][0] = 1
        for i in range(1, N+1):
            for j in range(S+1):
                if states[i-1][j]:
                    states[i][abs(j+stones[i-1])] = 1
                    states[i][abs(j-stones[i-1])] = 1
        return states

if __name__ == "__main__":
    stones = [6,6,3,6,3,2,5,1]
    sol = Solution()
    states = sol.lastStoneWeightII(stones)
    for line in states:
        print(" ".join(format(state, '3') for state in line))

        