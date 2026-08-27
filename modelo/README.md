# Modelo

```bash
pip install pulp
python -c "from modelo import *; print(resolver(INV)[0])"
```

`modelo.py` contiene los parámetros nutricionales, los requerimientos Esfera, los topes de aceptabilidad y el inventario de ejemplo. `resolver(inv)` devuelve `(D*, asignación, duales, asignación_etapa2)`.

Los precios sombra calculados por dualidad coinciden con la perturbación directa del inventario en todos los casos probados. Ver el anexo de verificación en [`../docs/modelo-ensamblaje-alimentario.md`](../docs/modelo-ensamblaje-alimentario.md).

**Advertencia:** el inventario es de ejemplo. Los topes de aceptabilidad `a_i` no están calibrados en campo — es el parámetro más débil del modelo.
