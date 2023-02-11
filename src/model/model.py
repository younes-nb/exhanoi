class Model:
    def hanoi(self, n, source, auxiliary, destination):
        if n == 1:
            yield source, destination
        else:
            yield from self.hanoi(n - 1, source, destination, auxiliary)
            yield source, destination
            yield from self.hanoi(n - 1, auxiliary, source, destination)

    def exhanoi(self, n, source, auxiliary, destination):
        if n == 1:
            yield destination, auxiliary
            yield source, destination
            yield auxiliary, source
            yield auxiliary, destination
            yield source, destination
        else:
            yield from self.exhanoi(n - 1, source, auxiliary, destination)
            yield from self.hanoi((3 * n) - 2, destination, source, auxiliary)
            yield source, destination
            yield from self.hanoi((3 * n) - 1, auxiliary, source, destination)
