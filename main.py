#!/usr/bin/python3

from PIL import Image, ImageDraw

import snake as mod

size = (800, 800)

initial = [(35, 400), (764, 400)]
depth = 6

# fractal = [
# 	[(0    , 0     ), (1 / 3, 0     ), (0    , 1 / 9)],
# 	[(1 / 3, 0     ), (2 / 3, 0     ), (1 / 9, 2 / 9)],
# 	[(2 / 3, 0     ), (2 / 3, -1 / 3), (2 / 9, 3 / 9)],
# 	[(2 / 3, -1 / 3), (1 / 3, -1 / 3), (3 / 9, 4 / 9)],
# 	[(1 / 3, -1 / 3), (1 / 3, 0     ), (4 / 9, 5 / 9)],
# 	[(1 / 3, 0     ), (1 / 3, 1 / 3 ), (5 / 9, 6 / 9)],
# 	[(1 / 3, 1 / 3 ), (2 / 3, 1 / 3 ), (6 / 9, 7 / 9)],
# 	[(2 / 3, 1 / 3 ), (2 / 3, 0     ), (7 / 9, 8 / 9)],
# 	[(2 / 3, 0     ), (1    , 0     ), (8 / 9, 9 / 9)]
# ]

# fractal = [
# 	[(0    , 0     ), (1 / 3, 0     ), (0    , 1 / 9)],
# 	[(1 / 3, 0     ), (1 / 3, -1 / 3), (1 / 9, 2 / 9)],
# 	[(2 / 3, -1 / 3), (2 / 3, 0     ), (3 / 9, 4 / 9)],
# 	[(2 / 3, 0     ), (1 / 3, 0     ), (4 / 9, 5 / 9)],
# 	[(1 / 3, 0     ), (1 / 3, 1 / 3 ), (5 / 9, 6 / 9)],
# 	[(2 / 3, 1 / 3 ), (2 / 3, 0     ), (7 / 9, 8 / 9)],
# 	[(2 / 3, 0     ), (1    , 0     ), (8 / 9, 9 / 9)]
# ]

output = Image.new("HSV", size)
doutput = ImageDraw.Draw(output)

def lerp (m, n, t):
	return m + (n - m) * t

def vlerp (m, n, t):
	return (m[0] + (n[0] - m[0]) * t[0] - (n[1] - m[1]) * t[1],
	        m[1] + (n[0] - m[0]) * t[1] + (n[1] - m[1]) * t[0])

def fracline (m = (0, 0), n = (0, 0), d = 0, col = 0):
	if d == 0:
		if col != 0:
			doutput.line([m, n], (int(col[0]), 255, 255))
		else:
			doutput.line([m, n], (0, 0, 255))
		return

	for f in mod.fractal:
		c = 0
		if col != 0:
			c = (lerp(col[0], col[1], f[2][0]), lerp(col[0], col[1], f[2][1]))
		fracline(vlerp(m, n, f[0]), vlerp(m, n, f[1]), d - 1, c)

fracline(initial[0], initial[1], depth, (0, 255))

output.show("Output image")
