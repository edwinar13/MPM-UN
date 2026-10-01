# Experimentos de validación

Los dos scripts que sustentan el hallazgo documentado en
[docs/validacion_motor_vs_referencia.md](../../docs/validacion_motor_vs_referencia.md)
§5: por qué la app y el motor original no coinciden dígito a dígito en
capacidad portante.

Son autocontenidos — montan la configuración desde cero y no dependen de ninguna
corrida previa. Se ejecutan con el intérprete del repo:

```bash
python tools/experimentos/dos_motores.py
python tools/experimentos/orden_particulas.py
```

## `dos_motores.py`

Corre el mismo paso MPM con el motor original (`1 Referencia/Codigo MPM-UN
Original_V1/mpm_un/`) y con el de la app (`app/motorMPM/`), desde un estado
inicial idéntico, y compara salida por salida durante 6 iteraciones.

Configuración: capacidad portante, malla 1.0, 800 partículas.

**Resultado:** diferencia exactamente `0.000e+00` en `nmass`, `niforce`,
`neforce`, `nvel`, `sig` y `xp`, y `dtime` igual hasta el último bit. Los dos
motores son bit a bit idénticos en la ruta gaussiana.

Requiere que exista la carpeta de referencia; las rutas están al principio del
archivo (`V1` y `APP`).

## `orden_particulas.py`

Corre el **mismo** motor con los **mismos** datos, cambiando únicamente el orden
en que se recorren las partículas: el de `setup_MP` (el del script original)
contra el del proyecto de la app.

**Resultado:** el orden de la app reproduce los números de la app dígito por
dígito — mismo número de iteraciones (5453 / 4012 / 3292) y mismo `ff` a 16
cifras. Las diferencias que genera solo permutar (2.012e-03, 2.819e-03,
3.951e-03 en SIGYY) coinciden exactamente con las medidas entre app y script.

Lee el orden de partículas de
`test/6 archivos_mpm 2609/2_capacidad_portante_malla1.json` (constante `PROY`).

Cubre los incrementos 1–3, todos elásticos. Para cerrar también el rango
plástico basta subir el `range(3)` del bucle de `corrida()`.

## Doble fase: `terzaghi.py` y `consolidacion_1d.py`

Validación del MPM de doble fase (`app/motorMPM/dos_fases.py`) con el caso de
consolidación 1D de Caro González (2024), §7.1. Resultados y figuras en
[docs/Importantes_para_tesis/evaluacion_motor_dos_fases.md](../../docs/Importantes_para_tesis/evaluacion_motor_dos_fases.md) §9.

```bash
python tools/experimentos/terzaghi.py                        # verifica la serie contra U(Tv) tabulado
python tools/experimentos/consolidacion_1d.py <salida>       # caso completo, α = 0, 49 part./elem (~35 s)
python tools/experimentos/consolidacion_1d.py <salida> --alpha 0.025 [--amort ec531]
for n in 4 9 16 25 36 49; do python tools/experimentos/consolidacion_1d.py <salida> --nmpe $n; done
python tools/experimentos/consolidacion_1d.py <salida> --figura-nmpe   # sensibilidad con los .npz guardados
```

**Resultado (α = 0):** U difiere menos de 2 % de Terzaghi; el error de p/p0 es
máximo al inicio (≈ 0.06 en la partícula media) y < 0.005 para Tv ≥ 1.5. El
amortiguamiento local no mejora el ajuste.
