import Wall as W
import RotationMoveDraw as RMD

map = [[W.Wall([0, 0, 0], "white", "blue", 5), W.Wall([2, 0, 0], "white", "blue", 0),
        W.Wall([4, 0, 0], "white", "blue", 0), W.Wall([6, 0, 0], "white", "blue", 0),
        W.Wall([8, 0, 0], "white", "blue", 0), W.Wall([10, 0, 0], "white", "blue", 0),
        W.Wall([12, 0, 0], "white", "blue", 4)],
       [W.Wall([0, 2, 0], "white", "green", 1), None, None, None, None, None, W.Wall([12, 2, 0], "white", "red", 1)],
       [W.Wall([0, 4, 0], "white", "green", 1), None, W.Wall([4, 4, 0], "white", "purple", 0), None, None, None, W.Wall([12, 4, 0], "white", "red", 1)],
       [W.Wall([0, 6, 0], "white", "green", 1), None, None, None, None, None, W.Wall([12, 6, 0], "white", "red", 1)],
       [W.Wall([0, 8, 0], "white", "green", 1), None, None, None, None, None, W.Wall([12, 8, 0], "white", "red", 1)],
       [W.Wall([0, 10, 0], "white", "green", 1), None, None, None, None, None, W.Wall([12, 10, 0], "white", "red", 1)],
       [W.Wall([0, 12, 0], "white", "orange", 2), W.Wall([2, 12, 0], "white", "orange", 0),
        W.Wall([4, 12, 0], "white", "orange", 0), W.Wall([6, 12, 0], "white", "orange", 0),
        W.Wall([8, 12, 0], "white", "orange", 0), W.Wall([10, 12, 0], "white", "orange", 0),
        W.Wall([12, 12, 0], "white", "orange", 3)]]

roMoDr = RMD.RotationMoveDraw(map)
roMoDr.draw_input('y')
roMoDr.start_loop()
