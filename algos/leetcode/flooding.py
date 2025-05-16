#https://leetcode.com/problems/flood-fill/
class Solution:
    def dfs(self, row, column, image, color, original_color):
        # Check if the current position is out of bounds
        if not (0 <= row < len(image) and 0 <= column < len(image[0])):
            return
        # Check if the current pixel is already the target color or not the original color
        if image[row][column] != original_color:
            return
        # Change the color of the current pixel
        image[row][column] = color

        # Recursively call dfs in four directions
        self.dfs(row + 1, column, image, color, original_color)
        self.dfs(row - 1, column, image, color, original_color)
        self.dfs(row, column + 1, image, color, original_color)
        self.dfs(row, column - 1, image, color, original_color)

    def floodFill(self, image, start_row, start_column, new_color):
        original_color = image[start_row][start_column]
        if original_color != new_color:  # Only proceed if there's an actual color change
            self.dfs(start_row, start_column, image, new_color, original_color)
        return image
