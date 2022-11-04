class Heap:
    def __init__(self, data):
        self.data = []
        self.size = 0
        for x in data:
            self.push(x)

    def push(self, x):
        self.data.append(x)
        i = self.size
        while i > 0:
            p = (i-1) // 2
            if self.data[p] <= x:
                break
            self.data[i] = self.data[p]
            i = p
        self.data[i] = x
        self.size += 1

    def pop(self) -> int:
        ret = self.data[0]
        self.data[0] = self.data[self.size-1]
        i = 0
        while i*2+1 < self.size-1:
            l = i*2+1
            r = i*2+2
            if r < self.size-1 and self.data[r] < self.data[l]:
                l = r
            if self.data[l] >= self.data[i]:
                break
            self.data[i], self.data[l] = self.data[l], self.data[i]
            i = l
        
        self.size -= 1
        self.data = self.data[:self.size]
        return ret

if __name__ == '__main__':
    h = Heap([1, 2, 4, 7, 8, 5])
    print(h.data)
    h.push(3)
    print(h.data)
    print(h.pop())
    print(h.data)

