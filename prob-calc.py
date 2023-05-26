import copy
import random
from typing import Dict,List

# Consider using the modules imported above.
# I added what's in the third line 

class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = [ball for ball, count in kwargs.items() for x in range(count)]

    def draw(self, count: int) -> List[str]:
        if count > len(self.contents):
            return self.contents
        output = []
        for _ in range(count):
            pos = random.randrange(0, len(self.contents))
            output.append(self.contents.pop(pos))
        return output


def experiment(
    hat: Hat, expected_balls: Dict[str, int], num_balls_drawn: int, num_experiments: int
):
    count = 0
    for _ in range(num_experiments):
        expected = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        output = hat_copy.draw(num_balls_drawn)
        for color in output:
            if color in expected:
                expected[color] -= 1

        if all(x <= 0 for x in expected.values()):
            count += 1
    return count / num_experiments


