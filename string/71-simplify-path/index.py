class Solution:

    def simplifyPath(self, path: str) -> str:
        i, firstSlash, stack = 0, 0, []
        path += '/'

        while i < len(path):
            if path[i] == '/':

                if firstSlash != i and path[firstSlash:i] == '..' and stack:
                    stack.pop()  # remove '/'
                    if stack:
                        stack.pop()  # remove dir
                elif firstSlash != i and path[firstSlash:i] != '.':
                    stack.append(path[firstSlash:i])

                while i < len(path) and path[i] == '/':
                    i += 1

                firstSlash = i

                if not stack or stack[-1] != '/':
                    stack.append('/')

            i += 1

        if len(stack) > 1 and stack[-1] == '/':
            stack.pop()

        return "".join(stack)