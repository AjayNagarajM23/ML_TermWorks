# dictionary = ["START", "NOTE", "SAND", "STONED"]
dictionary = ["MSA", "MSB", "MASBB", "MBS","PRANAV"]
n = len(dictionary)
M = 2
N = 2


def isWord(Str):
    for i in range(n):
        if Str == dictionary[i]:
            return True
    return False


def findWordsUtil(boggle, visited, i, j, Str):
    visited[i][j] = True
    Str = Str + boggle[i][j]

    if (isWord(Str)):
        print(Str)

    row = i - 1
    while row <= i + 1 and row < M:
        col = j - 1
        while col <= j + 1 and col < N:
            if row >= 0 and col >= 0 and not visited[row][col]:
                findWordsUtil(boggle, visited, row, col, Str)
            col += 1
        row += 1

    Str = "" + Str[-1]
    visited[i][j] = False


def findWords(boggle):
    visited = [[False for i in range(N)] for j in range(M)]

    Str = ""

    for i in range(M):
        for j in range(N):
            findWordsUtil(boggle, visited, i, j, Str)


# boggle = [["M", "S", "E", "F"], ["R", "A", "T", "D"], ["L", "O", "N", "E"], ["K", "A", "F", "B"]]
boggle = [["M", "S"], ["A", "B"]]
print("Following words of", "dictionary are present")
findWords(boggle)
