### 为什么要用动态规划？

减少递归中的重复计算

### 什么问题适合用动态规划解决？

**多阶段决策最优解模型**

一般是优化问题，如：最短路径，最长公共子序列等等。整个问题可以拆分成**多个决策阶段**，每个阶段的决策结果可总结/保存为一个状态。需要寻找一组决策序列，通过这组决策序列可产生最终期望的最优值。

### 动态规划算法的特征？

1. **最优子结构**

   问题的最优解包含子问题的最优解。子问题的最优解，可推导出问题的最优解。

2. **无后效性**

   推导当前状态时只关心之前的状态值（递推关系式），因此需要边界条件。某个状态一旦确定，则不受之前阶段状态的决策影响。

3. **重复子问题**

   也就是子结构中的问题和问题本身相似/相同。

### 搭建动态规划算法的思路？

1. **从后往前，从简单到复杂，递归式的思考**

   一般能用动态规划解决的问题，都可以使用递归算法的暴力解决。先思考最后任务快完成的情况，寻求`递归关系`。再寻找递归算法中的`重复子问题`，并找到合适的`状态定义`，设计`递推关系`。递推关系需要起始值，一般递推关系的起始即为递归关系的终止条件。最后设计动态规划算法，考虑状态跟新的顺序，空间的优化等等。

2. **状态转移方程法**

   有些问题的数学特征比较明显，可以直接寻找特推关系式，如斐波那契数列。

3. 

### 动态规划代码实战

#### 路径问题

LeetCode 62-Medium-Unique Paths

- 状态定义：【二维目标的二维度稠密表示】

  $states(i, j)$ 表示到第$i$行第$j$列的路径有几条。

LeetCode 64-Medium-Minimum Path Sum

- 状态定义：【二维目标的二维度稠密表示】

  $states(i, j)$ 表示到第$i$行第$j$列的最小路径的和。



#### 0-1 Knapsack：0-1背包问题

0-1 Knapsack with weights and values

- 状态定义：【一维目标的二维度稀疏表示】

  $states(n, W)$ 表示前$n$个物品在重量为$W$的限制下，最多能达到的价值。

- 递归关系式：

  $$states(n, W) = max(states(n-1, W), states(n-1, W-w_n)+v_n)$$

- 思路总结：

  `连续决策`问题。状态与递归关系式的思考过程为当前的状态是如何得到的，分情况讨论，`分而治之`。写代码的时候注意递归基的定义，以及index越界的处理。

LeetCode 416-Medium-Partition Equal Subset Sum

- 思路总结：

  0-1 Knapsack的直接变体，若存在可以装满背包（所有数和的一半）的array的子集，则存在这样的partition。

LeetCode 494-Medium-Target Sum

- 状态定义：【一维目标的二维度稀疏表示】

  $states(n, s)$ 表示前$n$个物品通过或加或减的组合达到$s$的不同组合的个数。

- 思路总结：

  `连续决策`问题。是0-1 Knapsack的直接变体。这里由于$s$可以为负，导致若使用状态矩阵存贮状态会变得复杂且冗余，考虑到状态的稀疏性，可改为`defaultdict`来存储状态。

LeetCode 1049-Medium-Last Stone Weight II

- 思路总结：

  0-1 Knapsack的间接变体，LeetCode 494的现实应用，撞的石头为减去自身重量（-）， 被撞的石头为加上自身重要（+）。原来的背包问题中物体是可选可不选，这题的物体是加上或者是减去。相比LeetCode 494，这里只关心某个重量是否存在，而不关心出现次数。



#### 字符串问题

LeetCode 1143-Medium-Longest Common Subsequence

- 状态定义：

  $states(i, j)$ 表示第一了字符串的前$i$个与第二个字符串的前$j$的最长公共子串的长度。二维矩阵，逐行或者是逐列更新。

- 递归关系式：

  $$\begin{equation} states(i, j)= \left\{ \begin{aligned} & states(i-1, j-1) + 1 & text1[i] = text2[j] \\ & max\{states(i-1, j), states(i, j-1)\} & otherwise \end{aligned} \right. \end{equation}$$

- 思路总结：

  `双序列`问题。状态与递归关系式的思考过程为思考两个序列的最后一个元素的处理，处理完之后就不再考虑该元素，`剪而治之`， 同时对问题`分而治之`。写代码的时候注意递归基的定义。


LeetCode 647-Medium-Palindromic Substrings

- 状态定义：【一维目标的二维度稠密表示】

  $states(i, j)$ 表示字符串第$i$个到第$j$的字符是否组成回文数。

- 思路总结：

  `双序列`问题。状态与递归关系式的思考过程为思考两个序列的最后一个元素的处理，处理完之后就不再考虑该元素，`剪而治之`， 同时对问题`分而治之`。写代码的时候注意递归基的定义。



#### 数字序列问题

Segmented Least Squares

- 状态定义：

  $states(j)$ : minimum cost of a partition of the points $p_1, ..., p_j$.

- 递归关系式子

  $state(n) = min_{1 \leq i \leq n}\{state(i-1)+error\{L, p_i, ..., p_n\}+C\}$

- 思路总结：

  `单序列`问题。递归的状态易得，从后往前，将设前序状态已知，如何得到当前状态，和广义数学归纳法的思维类似。

Sequence Alignment

- 状态定义：

  $states(i, j)$ : minimum cost of an alignment between $x_1, ..., x_i$ and $y_1, ..., y_j$.

- 递归关系式子

  $$\begin{equation} states(i, j)= \left\{ \begin{aligned} & j\delta & if \quad i = 0 \\ & min\left\{\begin{aligned}\alpha_{x_ix_j}+states(i-1, j-1) \\ \delta+states(i-1, j) \\ \delta + states(i, j-1) \end{aligned}\right. & if \quad i, j \geq 1 \\ & i\delta & if \quad j = 0\end{aligned} \right. \end{equation}$$

- 思路总结

  `双序列`问题。和LeetCode 1143几乎一样的解法，只不过更新方式略有不同。



