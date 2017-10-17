from enum import Enum


class ValueLimiter:
    class Direction(Enum):
        Stable = 0,
        Increasing = 1,
        Decreasing = -1

    def __init__(self, initial, min_val, max_val, delta, incr_func=None):
        self.max_val = max_val
        self.delta = delta
        self.min_val = min_val
        self.position = initial
        self.final_val = initial
        self.direction = ValueLimiter.Direction.Stable

        # In case of using anything other than linear interpolation
        if incr_func is None:
            self._internal_step = delta / 10

    def increment(self):
        if self.final_val is not None and self.final_val + self.delta > self.max_val:
            return

        self.final_val += self.delta
        self.direction = ValueLimiter.Direction.Increasing

    def _update(self):
        if self.direction == ValueLimiter.Direction.Increasing and self.position < self.final_val:
            self.position += self._internal_step
        elif self.direction == ValueLimiter.Direction.Decreasing and self.position > self.final_val:
            self.position -= self._internal_step
        else:
            self.position = self.final_val
            self.direction = ValueLimiter.Direction.Stable

    def get_value(self):
        if self.direction != ValueLimiter.Direction.Stable:
            self._update()

        return self.position


def main():
    limiter = ValueLimiter(0, -1, 1, 0.05)
    limiter.increment()

    while True:
        current_val = limiter.get_value()
        print(current_val)
        if limiter.get_value() == current_val:
            break


if __name__ == "__main__":
    main()
