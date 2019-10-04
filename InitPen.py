import turtle


class InitPen:
    @staticmethod
    def get_window():
        window = turtle.Screen()
        window.bgcolor("black")
        window.tracer(0, 1)
        window.setup(1100, 700)
        return window

    @staticmethod
    def get_pen():
        pen = turtle.Turtle()
        pen.color("white")
        pen.pensize(1)
        pen.shape("blank")
        pen.speed(10)
        return pen
