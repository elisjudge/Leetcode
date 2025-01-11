class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m_l, m_r = 0, len(matrix) - 1

        if target < matrix[m_l][0] or target > matrix[m_r][-1]:
            return False

        while m_l <= m_r:
            m_mid = (m_l + m_r) // 2

            if matrix[m_mid][0] <= target <= matrix[m_mid][-1]:
                n_l, n_r = 0, len(matrix[m_l]) - 1

                while n_l <= n_r:
                    n_mid = (n_l + n_r) // 2

                    if target == matrix[m_mid][n_mid]:
                        return True
                    elif target > matrix[m_mid][n_mid]:
                        n_l = n_mid + 1
                    elif target < matrix[m_mid][n_mid]:
                        n_r = n_mid - 1
                return False

            elif target > matrix[m_mid][-1]:
                m_l = m_mid + 1
                
            elif target < matrix[m_mid][0]:
                m_r = m_mid - 1
        return False

s = Solution()

testcases = [
    {"matrix": [[1],[3]], "target": 3, "expected": True},
    {"matrix": [[1]], "target": 1, "expected": True},
    {"matrix": [[1,3,5,7],[10,11,16,20],[23,30,34,60]], "target": 3, "expected": True},
    {"matrix": [[1,3,5,7],[10,11,16,20],[23,30,34,60]], "target": 13, "expected": False}
]

for i, testcase in enumerate(testcases):
    output = s.searchMatrix(testcase["matrix"], testcase["target"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")