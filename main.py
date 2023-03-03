#!/usr/bin/python3

from PIL import Image, ImageDraw

import demo as mod

size = (600, 600)

initial = [(44, 300), (556, 300)]
depth = 9

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
