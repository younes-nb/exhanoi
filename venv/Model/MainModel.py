class Model:
    def hanoi(self, count, start, mid, end, result=list):
        if count == 1:
            result.append((start, end))
        else:
            self.hanoi(count - 1, start, end, mid, result)
            result.append((start, end))
            self.hanoi(count - 1, mid, start, end, result)

        return result

    def exhanoi(self, count, start, mid, end, result=list):
        if count == 1:
            result.append((end, mid))
            result.append((start, end))
            result.append((mid, start))
            result.append((mid, end))
            result.append((start, end))
        else:
            self.exhanoi(count - 1, start, mid, end, result)
            result = self.hanoi((3 * count) - 2, end, start, mid, result)
            result.append((start, end))
            result = self.hanoi((3 * count) - 1, mid, start, end, result)

        return result
