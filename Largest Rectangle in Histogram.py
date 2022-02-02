class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		st,mx=[],0
		for i,ht in enumerate(heights+[0]):
			while st and heights[st[-1]]>=ht:
				h=heights[st.pop()] 
				w=i if not st else i-st[-1]-1
				mx=max(mx,w*h)
			st.append(i)
		return mx
