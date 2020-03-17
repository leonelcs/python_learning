import sys
import collections as c
import ast

def main():
    print(sys.argv)

    file = None

    for arg in sys.argv:
        if ".txt" in arg:
            file = open(arg, 'r')
    treasure_map = ast.literal_eval(file.read())

    print(find_treasure(treasure_map))

def find_treasure(m):
    if len(m) == 0 or len(m[0]) == 0:
        return -1 #impossible
    
    matrix = [row[:] for row in m]
    nrow, ncol = len(matrix), len(matrix[0])

    q = c.deque([((0, 0), 0)])  # ((x, y), step)
    matrix[0][0] = "D"
    while q:
        (x, y), step = q.popleft()

        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if 0 <= x+dx < nrow and 0 <= y+dy < ncol:
                if matrix[x+dx][y+dy] == "X":
                    return step+1
                elif matrix[x+dx][y+dy] == "O":
                    # mark visited
                    matrix[x + dx][y + dy] = "D"
                    q.append(((x+dx, y+dy), step+1))

    return -1


if __name__ == "__main__":
    # execute only if run as a script
    main()