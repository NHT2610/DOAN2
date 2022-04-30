import math

# Tích vô hướng của 2 vector u và v
def ScalarProduct(u, v):
    return sum(a * b for a, b in zip(u, v))

# Bình phương của chuẩn của vector u
def SquareOfNorm(u):
    return sum(a * a for a in u)

# Nhân vector v với hằng số a
def MultiplyWithScalar(a, v):
    return [a * element for element in v]

# Hiệu của 2 vector u và v
def Subtract(u, v):
    return [a - b for a, b in zip(u, v)]

# Kiểm tra vector u có bằng 0
def IsZero(u):
    for a in u:
        if a != 0:
            return False
    return True

# Lấy ma trận chuyển vị của ma trận A
def Transposition(A):
    B = []
    for i in range(len(A[0])):
        row = []
        for j in range(len(A)):
            row.append(A[j][i])
        B.append(row)
    return B

# Trực giao, trực chuẩn hệ vector U = {u1, u2, ..., un} 
def GramSchmidt(U, tc = True):
    flag = True
    # Trực giao
    V = []
    for u in U:
        vi = u
        for vj in V:
            vi = Subtract(vi, MultiplyWithScalar(ScalarProduct(u, vj) / SquareOfNorm(vj), vj))
            if IsZero(vi):
                flag = False
        V.append(vi)
    # Trực chuẩn
    Q = []
    if flag:
        if tc:
            for vi in V:
                qi = MultiplyWithScalar(1 / math.sqrt(SquareOfNorm(vi)), vi)
                Q.append(qi)
    return [V, Q]

# Phân tích QR từ hệ U và hệ trực chuẩn P
def QR_Decomposition(U, P):
    Q = []
    R = [[0] * len(V) for _ in range(len(V))]
    if P != []:
        # Lấy ma trận Q
        Q = Transposition(P)
        # Lấy ma trận R
        for i in range(len(R)):
            for j in range(i, len(R)):
                R[i][j] = ScalarProduct(P[i], U[j])
    return [Q, R]

# 1
u1 = [1, 0, 1]
u2 = [1, 1, 1]
u3 = [-1, 2, 1]

# 2
u1 = [1, 2, 1]
u2 = [1, -2, 1]
u3 = [1, 2, -1]

# 3
u1 = [1, 2, -2]
u2 = [1, -1, 4]
u3 = [2, 1, 1]

# 4
u1 = [1, 2, 3, 0]
u2 = [1, 2, 0, 0]
u3 = [1, 0, 0, 1]

# 5
u1 = [1, -1, 0, 1]
u2 = [1, 0, 1, -1]
u3 = [0, 1, 1, 0]

# 6
u1 = [-1, 1, -1, 1]
u2 = [-1, 3, -1, 3]
u3 = [1, 3, 5, 7]

U = [u1, u2, u3]

result1 = GramSchmidt(U)
print("Hệ trực giao:")
V = result1[0]
print(V)
print("Hệ trực chuẩn:")
P = result1[1]
print(P)

result2 = QR_Decomposition(U, P)
print("Phân rã QR")
print("Ma trận Q:")
Q = result2[0]
print(Q)
print("Ma trận R:")
R = result2[1]
print(R)