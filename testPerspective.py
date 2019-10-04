import turtle
import Perspective_Functions as PF

window = turtle.Screen()
pen = turtle.Turtle()

window.bgcolor("black")
window.tracer(0, 1)


pen.color("white")
pen.pensize(1)
pen.shape("blank")
pen.speed(10)

pen.dot()

rp = [[-1, 0, -1], [-1, 0, 1], [1, 0, 1], [1, 0, -1]]


x_y = [0, -1, 0]

test = PF.PF(x_y, [0, 0, 0])

scale = 100

rpp = [test.get_perspective_points(rp[0]), test.get_perspective_points(rp[1]),
       test.get_perspective_points(rp[2]), test.get_perspective_points(rp[3])]

pen.up()
pen.goto(scale * rpp[0][0], scale * rpp[0][1])
pen.down()
pen.goto(scale * rpp[1][0], scale * rpp[1][1])
pen.goto(scale * rpp[2][0], scale * rpp[2][1])
pen.goto(scale * rpp[3][0], scale * rpp[3][1])
pen.goto(scale * rpp[0][0], scale * rpp[0][1])

window.update()

window.exitonclick()
