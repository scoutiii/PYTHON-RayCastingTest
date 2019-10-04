import InitPen


class RotationMoveDraw:

    def __init__(self, world_array):
        self.map = world_array
        self.win_pen = InitPen.InitPen()
        self.window = self.win_pen.get_window()
        self.pen = self.win_pen.get_pen()
        self.ep = [self.map[0].__len__() - 1 + .001, self.map.__len__() - 1 + .001, 0]
        self.cp = [self.ep[0], self.ep[1] + 1, 0]
        self.rotation = 0

    def __draw_floor__(self):
        self.pen.up()
        self.pen.goto(-5000, 0)
        self.pen.color("saddle brown", "saddle brown")
        self.pen.begin_fill()
        self.pen.down()
        self.pen.goto(-5000, -5000)
        self.pen.goto(5000, -5000)
        self.pen.goto(5000, 0)
        self.pen.up()
        self.pen.end_fill()

    def __draw_sky__(self):
        self.pen.up()
        self.pen.goto(-5000, 0)
        self.pen.color("deep sky blue", "deep sky blue")
        self.pen.begin_fill()
        self.pen.down()
        self.pen.goto(-5000, 5000)
        self.pen.goto(5000, 5000)
        self.pen.goto(5000, 0)
        self.pen.up()
        self.pen.end_fill()

    def __draw_cross_hair__(self):
        self.pen.goto(0, 0)
        self.pen.dot(10, "yellow")

    def __rotation_0__(self, command):
        if command == 'w':
            self.ep[1] += 2
            self.cp[1] += 2
        elif command == 's':
            self.ep[1] -= 2
            self.cp[1] -= 2
        elif command == 'a':
            self.ep[0] -= 2
            self.cp[0] -= 2
        elif command == 'd':
            self.ep[0] += 2
            self.cp[0] += 2
        elif command == 'c':
            self.window.bye()

        self.cp = [self.ep[0], self.ep[1] + 2, self.ep[2]]

        level = 1
        count = 1
        art_alg_res = []

        for y in range(int((self.ep[1] / 2) + 1), self.map.__len__() + 1, 1):
            for x in range(int(self.ep[0] / 2) - 2 * level, int(self.ep[0] / 2) + 2 * level + 1, 1):
                if y < 0 or x < 0 or x >= self.map[0].__len__() or y >= self.map.__len__():
                    continue
                if self.map[y][x] is not None:
                    art_alg_res += [(self.map[y][x], count)]
                    count += 1
            level += 1

        return art_alg_res

    def __rotation_1__(self, command):
        if command == 'w':
            self.ep[1] += 2
            self.ep[0] += 2
            self.cp[0] += 2
            self.cp[1] += 2
        elif command == 's':
            self.ep[1] -= 2
            self.ep[0] -= 2
            self.cp[0] -= 2
            self.cp[1] -= 2
        elif command == 'a':
            self.ep[0] -= 2
            self.ep[1] += 2
            self.cp[1] += 2
            self.cp[0] -= 2
        elif command == 'd':
            self.ep[0] += 2
            self.ep[1] -= 2
            self.cp[1] -= 2
            self.cp[0] += 2
        elif command == 'c':
            self.window.bye()

        count = 1
        art_alg_res = []

        self.cp = [self.ep[0] + 2, self.ep[1] + 2, self.ep[2]]

        for l in range(1, (self.map.__len__() - 1 - int(self.ep[1] / 2)) + (
                self.map[0].__len__() - 1 - int(self.ep[0] / 2)) + 1, 1):
            tic = 0
            while tic <= l:
                y = int(self.ep[1] / 2) + l - tic
                x = int(self.ep[0] / 2) + tic
                if 0 <= y < self.map.__len__() and 0 <= x < self.map[0].__len__():
                    if self.map[y][x] is not None:
                        art_alg_res += [(self.map[y][x], count)]
                        count += 1
                tic += 1

        return art_alg_res

    def __rotation_2__(self, command):
        if command == 'w':
            self.ep[0] += 2
            self.cp[0] += 2
        elif command == 's':
            self.ep[0] -= 2
            self.cp[0] -= 2
        elif command == 'a':
            self.ep[1] += 2
            self.cp[1] += 2
        elif command == 'd':
            self.ep[1] -= 2
            self.cp[1] -= 2
        elif command == 'c':
            self.window.bye()

        level = 1
        count = 1
        art_alg_res = []

        self.cp = [self.ep[0] + 2, self.ep[1], self.ep[2]]

        for x in range(int((self.ep[0] / 2) + 1), self.map[0].__len__() + 1, 1):
            for y in range(int(self.ep[1] / 2) - 2 * level, int(self.ep[1] / 2) + 2 * level + 1, 1):
                if y < 0 or x < 0 or x >= self.map[0].__len__() or y >= self.map.__len__():
                    continue
                if self.map[y][x] is not None:
                    art_alg_res += [(self.map[y][x], count)]
                    count += 1
            level += 1

        return art_alg_res

    def __rotation_3__(self, command):
        if command == 'w':
            self.ep[0] += 2
            self.ep[1] -= 2
            self.cp[0] += 2
            self.cp[1] -= 2
        elif command == 's':
            self.ep[0] -= 2
            self.ep[1] += 2
            self.cp[0] -= 2
            self.cp[1] += 2
        elif command == 'a':
            self.ep[0] += 2
            self.ep[1] += 2
            self.cp[0] += 2
            self.cp[1] += 2
        elif command == 'd':
            self.ep[0] -= 2
            self.ep[1] -= 2
            self.cp[0] -= 2
            self.cp[1] -= 2
        elif command == 'c':
            self.window.bye()

        count = 1
        art_alg_res = []

        self.cp = [self.ep[0] + 2, self.ep[1] - 2, self.ep[2]]

        for l in range(1, int(self.ep[1] / 2) + (self.map[0].__len__() - int(self.ep[0] / 2)) + 1, 1):
            tic = 0
            while tic <= l:
                x = int(self.ep[0] / 2) + l - tic
                y = int(self.ep[1] / 2) - tic

                if 0 <= x < self.map[0].__len__() and 0 <= y < self.map.__len__():
                    if self.map[y][x] is not None:
                        art_alg_res += [(self.map[y][x], count)]
                        count += 1
                tic += 1

        return art_alg_res

    def __rotation_4__(self, command):
        if command == 'w':
            self.ep[1] -= 2
            self.cp[1] -= 2
        elif command == 's':
            self.ep[1] += 2
            self.cp[1] += 2
        elif command == 'a':
            self.ep[0] += 2
            self.cp[0] += 2
        elif command == 'd':
            self.ep[0] -= 2
            self.cp[0] -= 2
        elif command == 'c':
            self.window.bye()

        level = 1
        count = 1
        art_alg_res = []

        self.cp = [self.ep[0], self.ep[1] - 2, self.ep[2]]

        for y in range(int(self.ep[1] / 2) - 1, -1, -1):
            for x in range(int(self.ep[0] / 2) - 2 * level, int(self.ep[0] / 2) + 2 * level + 1, 1):
                if y < 0 or x < 0 or x >= self.map[0].__len__() or y >= self.map.__len__():
                    continue
                if self.map[y][x] is not None:
                    art_alg_res += [(self.map[y][x], count)]
                    count += 1
            level += 1

        return art_alg_res

    def __rotation_5__(self, command):
        if command == 'w':
            self.ep[0] -= 2
            self.ep[1] -= 2
            self.cp[0] -= 2
            self.cp[1] -= 2
        elif command == 's':
            self.ep[0] += 2
            self.ep[1] += 2
            self.cp[0] += 2
            self.cp[1] += 2
        elif command == 'a':
            self.ep[0] += 2
            self.ep[1] -= 2
            self.cp[0] += 2
            self.cp[1] -= 2
        elif command == 'd':
            self.ep[0] -= 2
            self.ep[1] += 2
            self.cp[0] -= 2
            self.cp[1] += 2
        elif command == 'c':
            self.window.bye()

        count = 1
        art_alg_res = []

        self.cp = [self.ep[0] - 2, self.ep[1] - 2, self.ep[2]]

        for l in range(1, int(self.ep[0] / 2) + int(self.ep[1] / 2) + 1, 1):
            tic = 0
            while tic <= l:
                x = int(self.ep[0] / 2) - l + tic
                y = int(self.ep[1] / 2) - tic

                if 0 <= x < self.map[0].__len__() and 0 <= y < self.map.__len__():
                    if self.map[y][x] is not None:
                        art_alg_res += [(self.map[y][x], count)]
                        count += 1
                tic += 1

        return art_alg_res

    def __rotation_6__(self, command):
        if command == 'w':
            self.ep[0] -= 2
            self.cp[0] -= 2
        elif command == 's':
            self.ep[0] += 2
            self.cp[0] += 2
        elif command == 'a':
            self.ep[1] -= 2
            self.cp[1] -= 2
        elif command == 'd':
            self.ep[1] += 2
            self.cp[1] += 2
        elif command == 'c':
            self.window.bye()

        level = 1
        count = 1
        art_alg_res = []

        self.cp = [self.ep[0] - 2, self.ep[1], self.ep[2]]

        for x in range(int(self.ep[0] / 2) - 1, -1, -1):
            for y in range(int(self.ep[1] / 2) - 2 * level, int(self.ep[1] / 2) + 2 * level + 1, 1):
                if y < 0 or x < 0 or x >= self.map[0].__len__() or y >= self.map.__len__():
                    continue
                if self.map[y][x] is not None:
                    art_alg_res += [(self.map[y][x], count)]
                    count += 1
            level += 1

        return art_alg_res

    def __rotation_7__(self, command):
        if command == 'w':
            self.ep[0] -= 2
            self.ep[1] += 2
            self.cp[0] -= 2
            self.cp[1] += 2
        elif command == 's':
            self.ep[0] += 2
            self.ep[1] -= 2
            self.cp[0] += 2
            self.cp[1] -= 2
        elif command == 'a':
            self.ep[0] -= 2
            self.ep[1] -= 2
            self.cp[0] -= 2
            self.cp[1] -= 2
        elif command == 'd':
            self.ep[0] += 2
            self.ep[1] += 2
            self.cp[0] += 2
            self.cp[1] += 2
        elif command == 'c':
            self.window.bye()

        count = 1
        art_alg_res = []

        self.cp = [self.ep[0] - 2, self.ep[1] + 2, self.ep[2]]

        for l in range(1, int(self.ep[0] / 2) + (self.map.__len__() - int(self.ep[1] / 2)) + 1, 1):
            tic = 0
            while tic <= l:
                x = int(self.ep[0] / 2) - l + tic
                y = int(self.ep[1] / 2) + tic
                if 0 <= x < self.map[0].__len__() and 0 <= y < self.map.__len__():
                    if self.map[y][x] is not None:
                        art_alg_res += [(self.map[y][x], count)]
                        count += 1
                tic += 1

        return art_alg_res

    def draw_input(self, command):
        global artist_algorithm_results

        if command == 'e':
            self.rotation += 1
        elif command == 'q':
            self.rotation -= 1

        rotation_switch = self.rotation % 8

        orig_x = self.ep[0]
        orig_y = self.ep[1]
        orig_cx = self.cp[0]
        orig_cy = self.cp[1]

        if rotation_switch == 0:
            artist_algorithm_results = self.__rotation_0__(command)
        elif rotation_switch == 1:
            artist_algorithm_results = self.__rotation_1__(command)
        elif rotation_switch == 2:
            artist_algorithm_results = self.__rotation_2__(command)
        elif rotation_switch == 3:
            artist_algorithm_results = self.__rotation_3__(command)
        elif rotation_switch == 4:
            artist_algorithm_results = self.__rotation_4__(command)
        elif rotation_switch == 5:
            artist_algorithm_results = self.__rotation_5__(command)
        elif rotation_switch == 6:
            artist_algorithm_results = self.__rotation_6__(command)
        elif rotation_switch == 7:
            artist_algorithm_results = self.__rotation_7__(command)

        x = int(self.ep[0]/2)
        y = int(self.ep[1]/2)

        if 0 <= x < self.map[0].__len__() and 0 <= y < self.map.__len__():
            if self.map[int(self.ep[0]/2)][int(self.ep[1]/2)] is not None:
                self.ep[0] = orig_x
                self.ep[1] = orig_y
                self.cp[0] = orig_cx
                self.cp[1] = orig_cy
                return

        artist_algorithm_results = sorted(artist_algorithm_results, key=lambda s: s[1], reverse=True)

        # So that you don't draw when there isn't a screen anymore
        if command == 'c':
            return

        self.pen.clear()

        # Draw the floor and sky
        self.__draw_floor__()
        self.__draw_sky__()

        # Draw the walls
        for index in range(0, artist_algorithm_results.__len__()):
            artist_algorithm_results[index][0].draw(self.pen, self.ep, self.cp, 500)

        # Draw the cross hair
        self.__draw_cross_hair__()
        self.window.update()

    def i_w(self):
        self.draw_input('w')

    def i_s(self):
        self.draw_input('s')

    def i_a(self):
        self.draw_input('a')

    def i_d(self):
        self.draw_input('d')

    def i_q(self):
        self.draw_input('q')

    def i_e(self):
        self.draw_input('e')

    def i_c(self):
        self.draw_input('c')

    def start_loop(self):
        self.window.listen()
        self.window.onkey(self.i_w, "w")
        self.window.onkey(self.i_a, "a")
        self.window.onkey(self.i_s, "s")
        self.window.onkey(self.i_d, "d")
        self.window.onkey(self.i_e, "e")
        self.window.onkey(self.i_q, "q")
        self.window.onkey(self.i_c, "c")
        self.window.mainloop()
