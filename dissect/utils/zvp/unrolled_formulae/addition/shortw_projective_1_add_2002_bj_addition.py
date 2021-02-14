from sage.all import *

pr = PolynomialRing(ZZ, ('a', 'b', 'X1', 'X2', 'Y1', 'Y2'), 6)
a, b, X1, X2, Y1, Y2 = pr.gens()
Z1, Z2 = 1, 1
formula = {}
U1 = X1 * Z2
formula['U1'] = U1
U2 = X2 * Z1
formula['U2'] = U2
S1 = Y1 * Z2
formula['S1'] = S1
S2 = Y2 * Z1
formula['S2'] = S2
ZZ = Z1 * Z2
formula['ZZ'] = ZZ
T = U1 + U2
formula['T'] = T
M = S1 + S2
formula['M'] = M
t0 = T ** 2
formula['t0'] = t0
t1 = ZZ ** 2
formula['t1'] = t1
t2 = a * t1
formula['t2'] = t2
t3 = U1 * U2
formula['t3'] = t3
t4 = t0 - t3
formula['t4'] = t4
R = t4 + t2
formula['R'] = R
F = ZZ * M
formula['F'] = F
L = M * F
formula['L'] = L
G = T * L
formula['G'] = G
t5 = R ** 2
formula['t5'] = t5
W = t5 - G
formula['W'] = W
t6 = F * W
formula['t6'] = t6
X3 = 2 * t6
formula['X3'] = X3
t7 = 2 * W
formula['t7'] = t7
t8 = G - t7
formula['t8'] = t8
t9 = L ** 2
formula['t9'] = t9
t10 = R * t8
formula['t10'] = t10
Y3 = t10 - t9
formula['Y3'] = Y3
t11 = F ** 2
formula['t11'] = t11
t12 = F * t11
formula['t12'] = t12
Z3 = 2 * t12
formula['Z3'] = Z3
for key, value in formula.items():
    print(f'{key} = {value}')