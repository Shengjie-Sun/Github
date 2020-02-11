import copy

class Solution:
    def __init__(self):
        self.EXIST = False

    def exist(self, board, word):
        V = [1, 0, -1, 0]
        H = [0, -1, 0, 1]
        
        def move(v, h, word_left, BOARD):
            if not self.EXIST:
                if len(word_left)==1 and BOARD[v][h] == word_left[0]:
                    self.EXIST = True
                    # print("f")
                elif BOARD[v][h] == word_left[0]:
                    BOARD[v][h] = "*"
                    for i in range(4):
                        nex_v = v+V[i]
                        nex_h = h+H[i]
                        if 0<=nex_v<bh and 0<=nex_h<bw:
                            move(nex_v, nex_h, word_left[1:], BOARD)
                    BOARD[v][h] = word_left[0]

        if not board:
            return False
        else:
            bw = len(board[0])
            bh = len(board)
            for i in range(bh):
                for j in range(bw):
                    if board[i][j] == word[0]:
                        BOARD = copy.deepcopy(board)
                        move(i, j, word, BOARD)
        return self.EXIST

class SOLUTION:
    def exist(self, board, word):
        V = [1, 0, -1, 0]
        H = [0, -1, 0, 1]
        
        def move(v, h, word_left):
            
            result = False
            
            if len(word_left)==1 and board[v][h] == word_left[0]:
                result = True
            elif board[v][h] == word_left[0]:
                board[v][h] = "*"
                for i in range(4):
                    nex_v = v+V[i]
                    nex_h = h+H[i]
                    if 0<=nex_v<bh and 0<=nex_h<bw:
                        result = move(nex_v, nex_h, word_left[1:])
                        # 限制递归的数量
                        if result:
                            break
                # 记得把状态修改回去
                board[v][h] = word_left[0]
            # 注意递归的返还方式
            return result

        bw = len(board[0])
        bh = len(board)
        for i in range(bh):
            for j in range(bw):
                if move(i, j, word):
                    return True
        return False
    

if __name__ == "__main__":
    # Test Case
    board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    word = "ABCCED"

    sol = SOLUTION()
    print(sol.exist(board, word))
