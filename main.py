# Every index represent the queen and value in it represent the column in which the queen is placed

import numpy as np

currentsolution = np.zeros(8)
solution = list()


def isSafe(testrow, testcol):
    if testrow==0:
        return True
    for row in range(testrow):
        if testcol==currentsolution[row]:
            return False
        if abs(testrow-row)==abs(testcol-currentsolution[row]):
            return False
    return True


if __name__ == '__main__':
    for col0 in range(8):
        if not isSafe(0, col0):
            continue
        else:
            currentsolution[0] = col0
        for col1 in range(8):
            if not isSafe(1, col1):
                continue
            else:
                currentsolution[1] = col1
            for col2 in range(8):
                if not isSafe(2, col2):
                    continue
                else:
                    currentsolution[2] = col2
                for col3 in range(8):
                    if not isSafe(3, col3):
                        continue
                    else:
                        currentsolution[3] = col3
                    for col4 in range(8):
                        if not isSafe(4, col4):
                            continue
                        else:
                            currentsolution[4] = col4
                        for col5 in range(8):
                            if not isSafe(5, col5):
                                continue
                            else:
                                currentsolution[5] = col5
                            for col6 in range(8):
                                if not isSafe(6, col6):
                                    continue
                                else:
                                    currentsolution[6] = col6
                                for col7 in range(8):
                                    if not isSafe(7, col7):
                                        continue
                                    else:
                                        currentsolution[7] = col7
                                        solution.append(currentsolution.copy())
    print(len(solution))
    for i in solution:
        print(i)