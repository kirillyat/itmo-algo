def total_time(x, a, Vp, Vf):
    return ( ((x**2 + (1 - a)**2)**0.5) / Vp ) + \
           ( ((1 - x)**2 + a**2)**0.5 / Vf )

def golden_section_search(a, Vp, Vf, l, r, eps):
    alfa = (5**0.5 - 1) / 2
    while abs(r - l) > eps:
        x1 = r - alfa * (r - l)
        x2 = l + alfa * (r - l)
        if total_time(x1, a, Vp, Vf) < total_time(x2, a, Vp, Vf):
            r = x2
        else:
            l = x1
    return (l + r) / 2

Vp, Vf = map(int, input().split())
a = float(input())

l = 0
r = 1
eps = 1e-5 

x = golden_section_search(a, Vp, Vf, l, r, eps)

print("{:.4f}".format(x))
