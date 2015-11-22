from __future__ import division # for Python 2.x compatibility
import numpy

class EuclidField(object):
    p = 5.0
    r = 30.0
    @staticmethod
    def dist(x, y):
        return numpy.hypot(x[0]-y[0], x[1]-y[1])
    def __init__(self, size, dst, obstacles):
        w, h = size
        self.shape = (h, w)
        self.dst = dst
        self.obstacles = obstacles
    def __getitem__(self, q):
        i, j = q
        h, w = self.shape
        if not (i in range(h) and j in range(w)):
            raise IndexError
        base = self.dist(q, self.dst)
        k = 0.0
        p = self.p
        for obj in self.obstacles:
            dist_to_obj = self.dist(q, obj)
            if dist_to_obj <= p:
                k += (1/dist_to_obj - 1/p)**2
        return (1.0 + k) * base**2 + self.r*k
    def __array__(self):
        h, w = self.shape
        return numpy.array([[self[i, j] for j in range(w)] for i in range(h)])

f = EuclidField((3, 3), (0, 0), [(1,1)])
