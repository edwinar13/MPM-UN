# -*- coding: utf-8 -*-
"""Solución analítica de Terzaghi (1925) para consolidación unidimensional.

Es la referencia del caso de validación 7.1 de Caro González (2024):
columna de altura H, drenada arriba e impermeable abajo (Hdr = H), carga q0
constante y presión de poros inicial p0 = q0.

    p(z, t) = Σ (2 p0 / M) sen(M z / Hdr) exp(−M² Tv),   M = (2m + 1) π / 2
    U(Tv)   = 1 − Σ (2 / M²) exp(−M² Tv)
    Tv      = cv t / Hdr²,   cv = k E' (1 − ν') / (γw (1 − 2ν') (1 + ν'))

z es la profundidad medida desde la frontera drenante (z = 0 arriba). En la
columna, con y medido desde el fondo, z = H − y.

USO
    python tools/experimentos/terzaghi.py [<figura.png>]

Sin argumentos verifica la serie contra valores de tabla; con una ruta además
dibuja las isócronas de la Figura 7-2 de la referencia.
"""
import math
import sys

import numpy as np

N_TERMINOS = 200


def cv(k, E, nu, gamma_w=9.81):
    """Coeficiente de consolidación (m²/s) con k en m/s, E en kPa, γw en kN/m³."""
    return k * E * (1 - nu) / (gamma_w * (1 - 2 * nu) * (1 + nu))


def presion(z_rel, Tv, n=N_TERMINOS):
    """p/p0 a la profundidad relativa z/Hdr (0 = borde drenante) y factor Tv."""
    z_rel = np.asarray(z_rel, dtype=float)
    if Tv <= 0:
        return np.where(z_rel > 0, 1.0, 0.0)
    p = np.zeros_like(z_rel)
    for m in range(n):
        M = (2 * m + 1) * math.pi / 2
        p += 2 / M * np.sin(M * z_rel) * math.exp(-M * M * Tv)
    return p


def grado_consolidacion(Tv, n=N_TERMINOS):
    """Grado de consolidación promedio U (0–1)."""
    if Tv <= 0:
        return 0.0
    return 1 - sum(2 / M ** 2 * math.exp(-M * M * Tv)
                   for M in ((2 * m + 1) * math.pi / 2 for m in range(n)))


def _verificar():
    # Valores clásicos de U(Tv) (p. ej. Das, tabla de consolidación)
    tabla = [(0.05, 0.252), (0.1, 0.357), (0.2, 0.504), (0.5, 0.764), (1.0, 0.931)]
    ok = True
    for Tv, U_ref in tabla:
        U = grado_consolidacion(Tv)
        bien = abs(U - U_ref) < 2e-3
        ok &= bien
        print(f"Tv = {Tv:4.2f}   U = {U:.4f}   tabla {U_ref:.3f}   {'ok' if bien else 'MAL'}")
    # En el fondo impermeable (z = Hdr) con Tv = 0.2: p/p0 ≈ 0.77 (ábacos de isócronas)
    p_fondo = float(presion(1.0, 0.2))
    print(f"p/p0 en el fondo, Tv = 0.2: {p_fondo:.3f}")
    # Caso 7.1 de la referencia: cv ≈ 1.01 m²/s
    print(f"cv (Tabla 7-1: k = 1e-3, E' = 1e4, ν' = 0) = {cv(1e-3, 1e4, 0.0):.3f} m²/s")
    return ok


def dibujar(ruta, Tvs=(0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0)):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    y = np.linspace(0, 1, 201)          # y/H desde el fondo
    fig, ax = plt.subplots(figsize=(5, 6))
    for Tv in Tvs:
        ax.plot(presion(1 - y, Tv), y, lw=1, label=f"Tv = {Tv:g}")
    ax.set_xlabel("p / p0")
    ax.set_ylabel("y / H")
    ax.set_xlim(0, 1.05)
    ax.set_ylim(0, 1)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=7, loc="lower left")
    ax.set_title("Isócronas de Terzaghi")
    fig.tight_layout()
    fig.savefig(ruta, dpi=150)
    print(f"figura: {ruta}")


if __name__ == "__main__":
    ok = _verificar()
    if len(sys.argv) > 1:
        dibujar(sys.argv[1])
    sys.exit(0 if ok else 1)
