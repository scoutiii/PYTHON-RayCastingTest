# https://www.math.utah.edu/~treiberg/Perspect/Perspect.htm
# This is where I got the math from, under Perspective Projections.

import math


class PF:

    def __t__(self, x, y, z):
        return [x - self.ep[0], y - self.ep[1], z - self.ep[2]]

    def __r__(self, x, y, z):
        return [self.c1*x - self.s1*y, self.s1*x + self.c1*y, z]

    def __s__(self, x, y, z):
        return [x, self.c2*y + self.s2*z, -self.s2*y + self.c2*z]

    def __srt__(self, x, y, z):
        t = self.__t__(x, y, z)
        r = self.__r__(t[0], t[1], t[2])
        s = self.__s__(r[0], r[1], r[2])
        return s

    def __gppp__(self, x, y, z):
        return self.s1*self.c2*(x - self.ep[0]) + self.c1*self.c2*(y - self.ep[1]) + self.s2*(z - self.ep[2])

    def __init__(self, eye_point, center_point):
        self.ep = eye_point
        self.cp = center_point
        self.dp = self.__t__(self.cp[0], self.cp[1], self.cp[2])
        self.r1 = math.sqrt(self.dp[0]**2 + self.dp[1]**2)
        self.s1 = self.dp[0] / self.r1
        self.c1 = self.dp[1] / self.r1
        self.rdp = self.__r__(self.dp[0], self.dp[1], self.dp[2])
        self.r2 = math.sqrt(self.rdp[1]**2 + self.rdp[2]**2)
        self.c2 = self.rdp[1] / self.r2
        self.s2 = self.rdp[2] / self.r2

    def get_perspective_points(self, point):
        depth = self.__gppp__(point[0], point[1], point[2])
        u_v = self.__srt__(point[0], point[1], point[2])
        return [u_v[0] / depth, u_v[2] / depth]

    def update_point(self, eye_point, center_point):
        self.ep = eye_point
        self.cp = center_point
        self.dp = self.__t__(self.cp[0], self.cp[1], self.cp[2])
        self.r1 = math.sqrt(self.dp[0] ** 2 + self.dp[1] ** 2)
        self.s1 = self.dp[0] / self.r1
        self.c1 = self.dp[1] / self.r1
        self.rdp = self.__r__(self.dp[0], self.dp[1], self.dp[2])
        self.r2 = math.sqrt(self.rdp[1] ** 2 + self.rdp[2] ** 2)
        self.c2 = self.rdp[1] / self.r2
        self.s2 = self.rdp[2] / self.r2
