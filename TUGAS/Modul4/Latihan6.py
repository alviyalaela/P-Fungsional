def point(x, y):
    return x, y

def line_equation_of(p1, M):
    x1, y1 = p1

    # Inner function untuk menghitung nilai C
    def calculate_c(x, y, m):
        return y - m * x

    # Hitung nilai C dengan inner function
    C = calculate_c(x1, y1, M)
    
    return f"y = {M:.2f}x + {C:.2f}"

# Titik (6, -2) dengan gradien 2
titik_P = point(6, -2)
gradien_M = 2

print("Persamaan garis yang melalui titik (6, -2) dan bergradien 2:")
print(line_equation_of(titik_P, gradien_M))
