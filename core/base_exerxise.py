import math
from abc import ABC, abstractmethod
import numpy as np

class BaseExercise(ABC):
    def __init__(self):
        self.reps = 0
        self.stage = None

    def calc_angle(self, a, b, c):
        bax, bay = b[0] - a[0], b[1] - a[1]
        cbx, cby = c[0] - b[0], c[1] - b[1]

        dot_prod = bax * cbx + bay * cby

        ba_mag = math.sqrt(bax ** 2 + bay ** 2)
        cb_mag = math.sqrt(cbx ** 2 + cby ** 2)

        if ba_mag * cb_mag == 0:
            return 0.0

        cos_theta = max(-1.0, min(1.0, dot_prod / (ba_mag * cb_mag)))

        return math.degrees(math.acos(cos_theta))

    def get_point(self, landmarks, idx):
        p = landmarks[idx]

        return (p.x, p.y)


    @abstractmethod
    def process(self, landmarks):
        pass

    @abstractmethod
    def reset(self):
        pass