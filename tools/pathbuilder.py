class PathBuilder:
    def __init__(self, root='./'):
        self.root = root
    
    def build(self, bits):
        if self.root[0] == '.':
            return '/'.join(bits)
        else:
            return self.root + '/'.join(bits)

path = PathBuilder()