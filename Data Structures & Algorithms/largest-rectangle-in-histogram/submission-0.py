class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        answer = 0

        stack = []



        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                h,j= stack.pop()
                w= i-j
                a = h*w
                answer = max(answer, a)
                start = j
            stack.append((height, start))
                

        while stack:
            h,j = stack.pop()
            w = n-j
            answer = max(answer, h*w)

        return answer
    