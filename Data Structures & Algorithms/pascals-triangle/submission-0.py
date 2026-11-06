class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            rowList = [1]
            pTriangle = []
            pTriangle.append(rowList)
            for i in range(1,numRows):
                rowList = [1]
                if i > 1:
                    j = 0
                    while len(rowList) != i:
                        rowList.append(pTriangle[i-1][j] + pTriangle[i-1][j+1])
                        j += 1

                rowList.append(1)
                pTriangle.append(rowList)
        return pTriangle