import math

# Higher-order function untuk translasi
def translasi(tx, ty):
    return lambda x, y: (x + tx, y + ty)

# Higher-order function untuk dilatasi
def dilatasi(sx, sy):
    return lambda x, y: (sx * x, sy * y)

# Higher-order function untuk rotasi
def rotasi(sudut):
    radian = math.radians(sudut)
    return lambda x, y: (x * math.cos(radian) - y * math.sin(radian),
                        x * math.sin(radian) + y * math.cos(radian))

titik_awal = (3, 5)

# Gunakan higher-order functions
translasi_function = translasi(2, -1)
dilatasi_function = dilatasi(2, -1)
rotasi_function = rotasi(30)

# Terapkan fungsi-fungsi tersebut pada titik_awal
after_translation = translasi_function(*titik_awal)
after_dilation = dilatasi_function(*titik_awal)
after_rotation = rotasi_function(*titik_awal)

print("Setelah translasi:", after_translation)
print("Setelah dilatasi:", after_dilation)
print("Setelah rotasi:", after_rotation)
