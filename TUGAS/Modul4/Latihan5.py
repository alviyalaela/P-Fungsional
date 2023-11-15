def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    m = (y2 - y1) / (x2 - x1)
    
    c = y1 - m * x1
    
    return f"y = {m:.2f}x + {c:.2f}"

print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(1, 4), point(0, 0)))
