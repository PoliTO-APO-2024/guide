class Counter:
    def __init__(self, start_count=0, step=1):
        self._count = start_count
        self._step = step

    def get_count(self):
        return self._count

    def get_step(self):
        return self._step

    def set_step(self, step):
        self._step = step

    def reset(self, start_count=0, step=1):
        self._count = start_count
        self._step = step

    def increment(self):
        self._count += self._step

    def __str__(self):
        return str(self._count)

    def __lt__(self, other):
        return self._count < other._count




