# COMP-001 - Ryzen 5 3400G con motherboards B550

| Campo | Valor |
|-------|-------|
| **Código** | COMP-001 |
| **Categoría** | Compatibilidad / Incompatibilidad |
| **Área** | Ventas, Taller de Armado, RMA y Soporte Técnico Virtual |
| **Estado** | <span class="kb-status kb-status--ok">Vigente</span> |
| **Versión** | 1.0 |
| **Fecha de creación** | 2026-08-15 |
| **Última actualización** | 2026-08-15 |

---

# Objetivo

Documentar la incompatibilidad entre el procesador **AMD Ryzen 5 3400G** y determinados motherboards con chipset **AMD B550**, y establecer cómo validar una combinación de CPU, motherboard y versión de BIOS antes de una venta o un armado.

---

# Componentes involucrados

## Procesador

| Característica | Detalle |
|----------------|---------|
| Modelo | AMD Ryzen 5 3400G con gráficos Radeon RX Vega 11 |
| Nombre en clave | Picasso |
| Arquitectura | Zen+ |
| Socket | AM4 |
| Gráficos integrados | Sí |

Aunque comercialmente pertenece a la serie Ryzen 3000, el Ryzen 5 3400G utiliza la arquitectura **Zen+** y el diseño **Picasso**. AMD no incluye al chipset B550 entre los chipsets admitidos en la ficha vigente de este procesador.

## Motherboards relevados

| Código interno | Modelo exacto | Resultado con Ryzen 5 3400G |
|----------------|---------------|------------------------------|
| 14138 | ASUS PRIME B550M-A AC | No compatible |
| 13151 | ASUS TUF GAMING B550-PLUS WIFI II | No compatible |
| 13421 | MSI B550M-A PRO | No compatible |

---

# Compatibilidad

## Resultado general

El socket AM4 compartido no garantiza que el procesador sea compatible con todos los chipsets ni con todos los modelos de motherboard. El procesador también debe aparecer en la **lista de CPU compatibles del modelo exacto**, junto con una versión de BIOS cuando corresponda.

En las tres motherboards relevadas, el Ryzen 5 3400G no debe ofrecerse ni instalarse como una combinación compatible:

| Motherboard | Evidencia del fabricante | Conclusión |
|-------------|--------------------------|------------|
| ASUS PRIME B550M-A AC | El Ryzen 5 3400G no figura en su lista oficial de CPU compatibles. | Incompatibilidad oficial; no se debe asumir que una actualización de BIOS agregará soporte. |
| ASUS TUF GAMING B550-PLUS WIFI II | El Ryzen 5 3400G no figura en su lista oficial de CPU compatibles. | Incompatibilidad oficial; no se debe utilizar esta combinación. |
| MSI B550M-A PRO | MSI indica expresamente que el modelo no es compatible con Ryzen 5 3400G ni Ryzen 3 3200G. | Incompatibilidad oficial. |

!!! warning "La ausencia de video es un síntoma, no la causa"

    Con esta combinación el sistema puede no completar el POST ni inicializar el procesador. Por eso no se obtiene imagen desde las salidas de video del motherboard. Instalar una placa de video dedicada no corrige la falta de soporte del CPU.

## Prueba interna documentada

Se verificó la combinación **Ryzen 5 3400G + ASUS PRIME B550M-A AC (código interno 14138)**. El equipo no entregó imagen y el comportamiento se mantuvo después de actualizar la motherboard a la última versión de BIOS disponible durante la prueba.

El resultado coincide con la lista oficial de ASUS, donde el Ryzen 5 3400G no aparece como procesador compatible para la variante `B550M-A AC`.

## Diferencia entre modelos similares

No se deben trasladar compatibilidades entre modelos con nombres parecidos:

- **ASUS PRIME B550M-A AC:** el Ryzen 5 3400G no figura en la lista oficial.
- **ASUS PRIME B550M-A**, sin `AC`: ASUS incorporó soporte para el Ryzen 5 3400G desde la BIOS 3636.

La presencia o ausencia del sufijo `AC`, `WiFi`, `II` u otra revisión puede identificar un producto con una lista de CPU y un firmware diferentes.

---

# Limitaciones

- Las listas de compatibilidad pueden cambiar si el fabricante publica una BIOS nueva.
- Una BIOS reciente no garantiza soporte para un procesador que no figura en la lista oficial.
- La expresión **Ryzen 3000 compatible** puede excluir modelos `G` como el Ryzen 5 3400G y el Ryzen 3 3200G.
- No se debe verificar sólo el chipset o el socket; es necesario consultar el modelo y la revisión exactos del motherboard.
- La compatibilidad con una motherboard no implica compatibilidad automática con otra variante de la misma familia.

---

# Verificación antes de una venta o un armado

1. Identificar el modelo y la revisión exactos del motherboard.
2. Ingresar a la sección de soporte oficial del fabricante.
3. Abrir la lista **CPU Support**, **CPU Compatibles** o equivalente.
4. Buscar el modelo exacto del procesador, incluyendo sufijos como `G`, `GE`, `X` o `PRO`.
5. Verificar la versión mínima de BIOS indicada.
6. Confirmar que el motherboard disponible tenga esa BIOS o pueda actualizarse de forma segura antes de instalar el CPU.
7. Si el procesador no figura en la lista, considerar la combinación como no compatible aunque comparta el mismo socket.

---

# Recomendaciones

## Para Ventas

- No ofrecer las tres motherboards relevadas junto con un Ryzen 5 3400G.
- Proponer una motherboard cuyo listado oficial incluya expresamente al Ryzen 5 3400G y comprobar la BIOS mínima requerida.
- Como alternativa, evaluar otro procesador que figure en la lista del motherboard B550 seleccionado.
- Volver a consultar las páginas oficiales al momento de la operación; esta entrada no reemplaza la validación del modelo disponible.

## Explicación sugerida para el cliente

> Aunque el procesador y la motherboard utilizan socket AM4, el fabricante no incluye esta combinación en su lista de compatibilidad. Una actualización de BIOS no garantiza que funcione. Para asegurar el arranque y la garantía de funcionamiento, es necesario elegir una motherboard que incluya expresamente al Ryzen 5 3400G en su lista de CPU compatibles, o seleccionar otro procesador compatible con la motherboard B550.

## Para Taller, RMA y Soporte

- Ante un equipo sin POST o sin imagen, comprobar la lista de CPU antes de reemplazar memoria, fuente o placa de video.
- No interpretar una actualización de BIOS exitosa como prueba de compatibilidad.
- Registrar el modelo completo, la revisión del PCB y la versión de BIOS utilizada durante la prueba.

---

# Referencias

- [AMD - Especificaciones del Ryzen 5 3400G](https://www.amd.com/en/support/downloads/drivers.html/processors/ryzen/ryzen-3000-series/amd-ryzen-5-3400g.html)
- [ASUS - CPU compatibles con PRIME B550M-A AC](https://www.asus.com/latin/supportonly/prime%20b550m-a%20ac/helpdesk_cpu/)
- [ASUS - CPU compatibles con TUF GAMING B550-PLUS WIFI II](https://www.asus.com/latin/motherboards-components/motherboards/tuf-gaming/tuf-gaming-b550-plus-wifi-ii/helpdesk_cpu?model2Name=TUF-GAMING-B550-PLUS-WIFI-II)
- [MSI - Especificaciones de B550M-A PRO](https://us.msi.com/Motherboard/B550M-A-PRO/Specification)
- [ASUS - CPU compatibles con PRIME B550M-A sin AC](https://www.asus.com/us/supportonly/prime%20b550m-a/helpdesk_cpu/)

Referencias consultadas el **2026-08-15**.

---

# Historial de cambios

| Versión | Fecha | Descripción |
|---------|-------|-------------|
| 1.0 | 2026-08-15 | Creación del documento con tres motherboards relevadas y una prueba interna. |
