# Write a function that provides change directory (cd) function for an abstract file system.
#
# Notes:
#
#     Root path is '/'.
#     Path separator is '/'.
#     Parent directory is addressable as '..'.
#     Directory names consist only of English alphabet letters (A-Z and a-z).
#     The function should support both relative and absolute paths.
#     The function will not be passed any invalid paths.
#     Do not use built-in path-related functions.
#
# For example:
#
# path = Path('/a/b/c/d')
# path.cd('../x')
# print(path.current_path)
#
# should display '/a/b/c/x'.
class Stack:
    def __init__(self):
        self.st = []

    def set(self, temp):
        self.st.append(temp)

    def pop(self):
        return self.st.pop()

    def sprint(self):
        return ('/'.join(self.st))

    def isEmpty(self):
        if self.st:
            return True
        return False

class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        stack=Stack()
        for temp in self.current_path.split('/'):
            stack.set(temp)
        print stack.sprint()
        for xx in new_path.split('/'):
            if xx == '..':
                if stack.isEmpty():
                    stack.pop()
                else:
                    raise Exception ("error")

            elif xx == '.':
                pass

            else:
                stack.set(xx)

        self.current_path = stack.sprint()

path = Path('/')
path.cd('/x')
print(path.current_path)