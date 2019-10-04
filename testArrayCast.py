import Wall as W
import InitPen as IP

win_pen = IP.InitPen()
window = win_pen.get_window()
pen = win_pen.get_pen()

map = [[W.Wall([0, 0, 0], "white", "blue", 5), W.Wall([2, 0, 0], "white", "blue", 0),
        W.Wall([4, 0, 0], "white", "blue", 0), W.Wall([6, 0, 0], "white", "blue", 0),
        W.Wall([8, 0, 0], "white", "blue", 0), W.Wall([10, 0, 0], "white", "blue", 0),
        W.Wall([12, 0, 0], "white", "blue", 4)],
       [W.Wall([0, 2, 0], "white", "green", 1), None, None, None, None, None, W.Wall([12, 2, 0], "white", "red", 1)],
       [W.Wall([0, 4, 0], "white", "green", 1), None, W.Wall([4, 4, 0], "white", "purple", 0), None, W.Wall([8, 4, 0], "white", "purple", 1), None, W.Wall([12, 4, 0], "white", "red", 1)],
       [W.Wall([0, 6, 0], "white", "green", 1), None, None, None, None, None, W.Wall([12, 6, 0], "white", "red", 1)],
       [W.Wall([0, 8, 0], "white", "green", 1), None, None, None, None, None, W.Wall([12, 8, 0], "white", "red", 1)],
       [W.Wall([0, 10, 0], "white", "green", 1), None, None, None, None, None, W.Wall([12, 10, 0], "white", "red", 1)],
       [W.Wall([0, 12, 0], "white", "orange", 2), W.Wall([2, 12, 0], "white", "orange", 0),
        W.Wall([4, 12, 0], "white", "orange", 0), W.Wall([6, 12, 0], "white", "orange", 0),
        W.Wall([8, 12, 0], "white", "orange", 0), W.Wall([10, 12, 0], "white", "orange", 0),
        W.Wall([12, 12, 0], "white", "orange", 3)]]

ep = [6.001, 6.001, 0]
cp = [6.001, 4.001, 0]

command = 'y'

while command != 'c':
    level = 1
    count = 1
    rp = []

    for y in range(int(ep[1]/2) - 1, -1, -1):
        for x in range(int(ep[0]/2) - level, int(ep[0]/2) + level + 1, 1):
            if y < 0 or x < 0 or x >= map[0].__len__() or y >= map[0].__len__():
                continue
            if map[y][x] is not None:
                rp += [(map[y][x], count)]
                count += 1
        level += 1
    rp = sorted(rp, key=lambda s: s[1], reverse=True)
    # Draw the floor
    pen.up()
    pen.goto(-5000, 0)
    pen.color("brown", "brown")
    pen.begin_fill()
    pen.down()
    pen.goto(-5000, -5000)
    pen.goto(5000, -5000)
    pen.goto(5000, 0)
    pen.up()
    pen.end_fill()
    # Draw the walls
    for r in range(0, rp.__len__()):
        rp[r][0].draw(pen, ep, cp, 500)
    # Draw the cross hair
    pen.goto(0, 0)
    pen.dot(10, "yellow")

    window.update()
    command = input()
    pen.clear()

    if command == 'w':
        ep[1] -= 2
        cp[1] -= 2
    elif command == 's':
        ep[1] += 2
        cp[1] += 2
    elif command == 'a':
        ep[0] += 2
        cp[0] += 2
    elif command == 'd':
        ep[0] -= 2
        cp[0] -= 2
    elif command == 'c':
        window.bye()

# window.exitonclick()
