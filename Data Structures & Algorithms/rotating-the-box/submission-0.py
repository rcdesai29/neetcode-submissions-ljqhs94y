class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows = len(box)
        cols = len(box[0])

        for r in range(rows):
            empty = cols - 1
            for c in reversed(range(cols)):
                if box[r][c] == '#':
                    box[r][c], box[r][empty] = box[r][empty], box[r][c]
                    empty -= 1
                elif box[r][c] == '*':
                    empty = c - 1
        
        res = [ ['' for r in range(rows)] for c in range(cols) ]

        for r in range(rows):
            for c in range(cols):
                res[c][rows - 1 - r] = box[r][c]
        return res
        