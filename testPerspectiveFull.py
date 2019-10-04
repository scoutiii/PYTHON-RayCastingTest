import Perspective_Functions as PF
import turtle

window = turtle.Screen()
pen = turtle.Turtle()

window.bgcolor("black")
window.tracer(0, 1)


pen.color("white")
pen.pensize(1)
pen.shape("blank")
pen.speed(10)

pen.dot()

r1 = [[-4, 3, -1], [-4, 3, 1], [-4, 5, 1], [-4, 5, -1]]
r2 = [[-4, 5, -1], [-4, 5, 1], [-3, 6, 1], [-3, 6, -1]]
r3 = [[-3, 6, -1], [-3, 6, 1], [-1, 6, 1], [-1, 6, -1]]
r4 = [[-1, 6, -1], [-1, 6, 1], [1, 6, 1], [1, 6, -1]]
r5 = [[1, 6, -1], [1, 6, 1], [3, 6, 1], [3, 6, -1]]
r6 = [[3, 6, -1], [3, 6, 1], [4, 5, 1], [4, 5, -1]]
r7 = [[4, 5, -1], [4, 5, 1], [4, 3, 1], [4, 3, -1]]

ep = [-.1, -.1, -.1]
cp = [-.1, .9, -.1]

t = PF.PF(ep, cp)

scale = 500

r1p = [t.get_perspective_points(r1[0]), t.get_perspective_points(r1[1]), t.get_perspective_points(r1[2]), t.get_perspective_points(r1[3])]
r2p = [t.get_perspective_points(r2[0]), t.get_perspective_points(r2[1]), t.get_perspective_points(r2[2]), t.get_perspective_points(r2[3])]
r3p = [t.get_perspective_points(r3[0]), t.get_perspective_points(r3[1]), t.get_perspective_points(r3[2]), t.get_perspective_points(r3[3])]
r4p = [t.get_perspective_points(r4[0]), t.get_perspective_points(r4[1]), t.get_perspective_points(r4[2]), t.get_perspective_points(r4[3])]
r5p = [t.get_perspective_points(r5[0]), t.get_perspective_points(r5[1]), t.get_perspective_points(r5[2]), t.get_perspective_points(r5[3])]
r6p = [t.get_perspective_points(r6[0]), t.get_perspective_points(r6[1]), t.get_perspective_points(r6[2]), t.get_perspective_points(r6[3])]
r7p = [t.get_perspective_points(r7[0]), t.get_perspective_points(r7[1]), t.get_perspective_points(r7[2]), t.get_perspective_points(r7[3])]

rp = [r1p, r2p, r3p, r4p, r5p, r6p, r7p]

command = 'y'

while command != 'c':
    window.update()
    command = input()
    pen.clear()

    if command == 'w':
        ep[1] += 1
        cp[1] += 1
    elif command == 's':
        ep[1] -= 1
        cp[1] -= 1
    elif command == 'a':
        ep[0] -= 1
        cp[0] -= 1
    elif command == 'd':
        ep[0] += 1
        cp[0] += 1
    elif command == 'q':
        ep[2] += 1
        cp[2] += 1
    elif command == 'e':
        ep[2] -= 1
        cp[2] -= 1

    t.update_point(ep, cp)

    r1p = [t.get_perspective_points(r1[0]), t.get_perspective_points(r1[1]), t.get_perspective_points(r1[2]),
           t.get_perspective_points(r1[3])]
    r2p = [t.get_perspective_points(r2[0]), t.get_perspective_points(r2[1]), t.get_perspective_points(r2[2]),
           t.get_perspective_points(r2[3])]
    r3p = [t.get_perspective_points(r3[0]), t.get_perspective_points(r3[1]), t.get_perspective_points(r3[2]),
           t.get_perspective_points(r3[3])]
    r4p = [t.get_perspective_points(r4[0]), t.get_perspective_points(r4[1]), t.get_perspective_points(r4[2]),
           t.get_perspective_points(r4[3])]
    r5p = [t.get_perspective_points(r5[0]), t.get_perspective_points(r5[1]), t.get_perspective_points(r5[2]),
           t.get_perspective_points(r5[3])]
    r6p = [t.get_perspective_points(r6[0]), t.get_perspective_points(r6[1]), t.get_perspective_points(r6[2]),
           t.get_perspective_points(r6[3])]
    r7p = [t.get_perspective_points(r7[0]), t.get_perspective_points(r7[1]), t.get_perspective_points(r7[2]),
           t.get_perspective_points(r7[3])]

    rp = [r1p, r2p, r3p, r4p, r5p, r6p, r7p]

    for x in range(0, 7):
        pen.up()
        pen.goto(scale * rp[x][0][0], scale * rp[x][0][1])
        pen.down()
        pen.goto(scale * rp[x][1][0], scale * rp[x][1][1])
        pen.goto(scale * rp[x][2][0], scale * rp[x][2][1])
        pen.goto(scale * rp[x][3][0], scale * rp[x][3][1])
        pen.goto(scale * rp[x][0][0], scale * rp[x][0][1])

window.exitonclick()
