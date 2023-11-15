
# Fungsi pengurangan
def minus(a, b):
    return a - b

# Fungsi pertambahan
def add(a, b):
    return a + b

# Fungsi perkalian
def mult(a, b):
    return a * b

# Fungsi pembagian
def div(a, b):
    if b == 0:
        raise ValueError("Pembagian dengan nol tidak diperbolehkan.")
    return a / b

def tree(node):
    if isinstance(node, (int, float)):
        return node
    elif isinstance(node, tuple) and len(node) == 3:
        operator, a, b = node
        if operator == '+':
            return add(tree(a), tree(b))  # Menggunakan fungsi pertambahan
        elif operator == '-':
            return minus(tree(a), tree(b))  # Menggunakan fungsi pengurangan
        elif operator == '*':
            return mult(tree(a), tree(b))   # Menggunakan fungsi perkalian
        elif operator == '/':
            return div(tree(a), tree(b))    # Menggunakan fungsi pembagian

# Mendefinisikan expression_tree di luar fungsi
expression_tree = ('/', ('+', 5, 5), ('-', 3, 2))

# Memanggil fungsi tree untuk mengevaluasi expression_tree
result = tree(expression_tree)

# Mencetak hasil
print("Hasil evaluasi pohon ekspresi:", result)
