"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

 

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]
"""
def floodFill(image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        if not image:
            return image 
        if image[sr][sc] == color:
            return image 
        
        previous_color = image[sr][sc]

        def dfs(sr, sc):
            if (sr < 0  or sr >= len(image) or
                sc < 0 or sc >= len(image[0]) or
                image[sr][sc] != previous_color
            ):
                 return 

            image[sr][sc] = color

            dfs(sr + 1, sc)
            dfs(sr - 1, sc)
            dfs(sr, sc + 1)
            dfs(sr, sc - 1)
        
        dfs(sr, sc)
        return image 


image = [[1,1,1],[1,1,0],[1,0,1]]
print(floodFill(image, 1, 1, 2))

                
