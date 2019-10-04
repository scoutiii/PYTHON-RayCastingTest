import Perspective_Functions as PerFun


class Wall:

    def draw(self, pen, eye, center, scale):
        t = PerFun.PF(eye, center)
        p = []
        for r in self.corners:
            p += [t.get_perspective_points(r)]

        pen.color(self.edge_color, self.fill_color)
        pen.up()
        pen.goto(scale * p[0][0], scale * p[0][1])
        pen.down()
        pen.begin_fill()
        for x in range(0, p.__len__()):
            pen.goto(scale * p[x][0], scale * p[x][1])
        pen.goto(scale * p[0][0], scale * p[0][1])
        pen.up()
        pen.end_fill()

    def __init__(self, point, edge_color, fill_color, style=0):
        self.point = point
        self.edge_color = edge_color
        self.fill_color = fill_color
        self.style = style
        # facing parallel to camera (just changes in x)
        if style == 0:
            self.corners = [[point[0] - 1, point[1], point[2] - 1],
                            [point[0] - 1, point[1], point[2] + 1],
                            [point[0] + 1, point[1], point[2] + 1],
                            [point[0] + 1, point[1], point[2] - 1]]
        # facing normal to camera (just changes in y)
        elif style == 1:
            self.corners = [[point[0], point[1] - 1, point[2] - 1],
                            [point[0], point[1] - 1, point[2] + 1],
                            [point[0], point[1] + 1, point[2] + 1],
                            [point[0], point[1] + 1, point[2] - 1]]
        # top left corner
        elif style == 2:
            self.corners = [[point[0], point[1] - 1, point[2] - 1],
                            [point[0], point[1] - 1, point[2] + 1],
                            [point[0] + 1, point[1], point[2] + 1],
                            [point[0] + 1, point[1], point[2] - 1]]
        # top right corner
        elif style == 3:
            self.corners = [[point[0] - 1, point[1], point[2] - 1],
                            [point[0] - 1, point[1], point[2] + 1],
                            [point[0], point[1] - 1, point[2] + 1],
                            [point[0], point[1] - 1, point[2] - 1]]
        # bottom right corner
        elif style == 4:
            self.corners = [[point[0] - 1, point[1], point[2] - 1],
                            [point[0] - 1, point[1], point[2] + 1],
                            [point[0], point[1] + 1, point[2] + 1],
                            [point[0], point[1] + 1, point[2] - 1]]
        # bottom left corner
        elif style == 5:
            self.corners = [[point[0], point[1] + 1, point[2] - 1],
                            [point[0], point[1] + 1, point[2] + 1],
                            [point[0] + 1, point[1], point[2] + 1],
                            [point[0] + 1, point[1], point[2] - 1]]
