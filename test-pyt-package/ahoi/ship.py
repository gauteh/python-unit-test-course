import numpy as np


class Field:
    x = None
    y = None
    xx = None
    yy = None

    def __init__(self, x, y):
        self.xx, self.yy = np.meshgrid(x, y)
        self.x = x
        self.y = y

    def grid(self):
        return self.xx, self.yy


def test_field():
    f = Field(np.linspace(0, 100), np.linspace(0, 100))
    assert f.xx.shape == (50, 50)
