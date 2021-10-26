class MainModel:
    def hanoi(self, n, sourse, auxiliary, destination):
        if n == 1:
            yield (sourse, destination)
        else:
            yield from self.hanoi(n - 1, sourse, destination, auxiliary)
            yield (sourse, destination)
            yield from self.hanoi(n - 1, auxiliary, sourse, destination)

    def exhanoi(self, n, source, auxiliary, destination):
        if n == 1:
            yield (destination, auxiliary)
            yield (source, destination)
            yield (auxiliary, source)
            yield (auxiliary, destination)
            yield (source, destination)
        else:
            yield from self.exhanoi(n - 1, source, auxiliary, destination)
            yield from self.hanoi((3 * n) - 2, destination, source, auxiliary)
            yield (source, destination)
            yield from self.hanoi((3 * n) - 1, auxiliary, source, destination)
