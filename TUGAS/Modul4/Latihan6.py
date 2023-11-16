def point(x, y):
    return x, y

def line_equation_of(p1, M):
    x1, y1 = p1

    def calc_constanta(x, y, m):
        return y - m * x
    
    def result():
        C = calc_constanta(x1, y1, M)
        print(f"y = {M:.2f}x + {C:.2f}") 

    return result

print("Persamaan garis yang melalui titik (4, 0) dan bergradien 9:")
hasil = line_equation_of(point(4, 0), 9)
# del line_equation_of
hasil()
