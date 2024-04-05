class Solution:
    def makeGood(self, s: str) -> str:
        stack = []  # Use a stack to keep track of characters

        for char in s:
            # Check if the stack is not empty and the current character cancels the top character
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()  # Remove the top character
            else:
                stack.append(char)  # Otherwise, add the current character to the stack

        return ''.join(stack)  # Convert the stack to a string


