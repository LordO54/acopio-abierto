import pulp, json

# ---- Parametros nutricionales por GRAMO de insumo ----
# (kcal, proteina g, grasa g)
NUT = {
 'arroz':            (3.60, 0.066, 0.006),
 'pasta':            (3.60, 0.120, 0.015),
 'harina_maiz':      (3.60, 0.070, 0.010),
 'panela':           (3.50, 0.005, 0.000),
 'frijol':           (3.40, 0.210, 0.012),
 'lenteja':          (3.50, 0.250, 0.010),
 'atun_lata':        (1.10, 0.250, 0.010),
 'leche_polvo':      (5.00, 0.250, 0.270),
 'aceite':           (9.00, 0.000, 1.000),
}
NUTRIENTES = ['energia','proteina','grasa']
def n(i,k): return NUT[i][NUTRIENTES.index(k)]

# Esfera: 2100 kcal; >=10% energia de proteina; >=17% energia de grasa
REQ = {'energia':2100.0, 'proteina':52.5, 'grasa':40.0}

# Tope de aceptabilidad: gramos maximos por persona-dia
ACEPT = {'arroz':400,'pasta':200,'harina_maiz':300,'panela':60,'frijol':120,
         'lenteja':120,'atun_lata':120,'leche_polvo':60,'aceite':40}

# Inventario tipico de acopio ciudadano (gramos) - sesgado a cereales
INV = {'arroz':2_000_000,'pasta':400_000,'harina_maiz':300_000,'panela':250_000,
       'frijol':120_000,'lenteja':80_000,'atun_lata':60_000,'leche_polvo':30_000,
       'aceite':25_000}

def resolver(inv, etapa2=True):
    I=list(inv); K=NUTRIENTES
    m=pulp.LpProblem("acopio",pulp.LpMaximize)
    x={i:pulp.LpVariable(f"x_{i}",0,None) for i in I}
    D=pulp.LpVariable("D",0)
    m += D
    for k in K:
        m += pulp.lpSum(n(i,k)*x[i] for i in I) - REQ[k]*D >= 0, f"nut_{k}"
    for i in I:
        m += x[i] <= inv[i], f"inv_{i}"
        m += x[i] - ACEPT[i]*D <= 0, f"acep_{i}"
    m.solve(pulp.PULP_CBC_CMD(msg=0))
    Dstar=D.varValue
    duales={c:m.constraints[c].pi for c in m.constraints}
    xs={i:x[i].varValue for i in I}
    if etapa2:
        m2=pulp.LpProblem("acopio2",pulp.LpMaximize)
        x2={i:pulp.LpVariable(f"x_{i}",0,None) for i in I}
        m2 += pulp.lpSum(x2[i] for i in I)
        for k in K: m2 += pulp.lpSum(n(i,k)*x2[i] for i in I) >= REQ[k]*Dstar
        for i in I:
            m2 += x2[i] <= inv[i]
            m2 += x2[i] <= ACEPT[i]*Dstar
        m2.solve(pulp.PULP_CBC_CMD(msg=0))
        xs2={i:x2[i].varValue for i in I}
    else: xs2=None
    return Dstar, xs, duales, xs2
