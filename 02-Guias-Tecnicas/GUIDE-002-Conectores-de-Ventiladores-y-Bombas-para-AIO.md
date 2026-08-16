# GUIDE-002 - Conectores de ventiladores y bombas para refrigeración AIO

| Campo | Valor |
|-------|-------|
| **Código** | GUIDE-002 |
| **Categoría** | Guía Técnica |
| **Área** | Taller de Armado, RMA y Soporte Técnico Virtual |
| **Estado** | Vigente |
| **Versión** | 1.0 |
| **Fecha de creación** | 2026-08-15 |
| **Última actualización** | 2026-08-15 |

---

# Objetivo

Explicar la función de los principales headers de ventilación de una motherboard y establecer criterios para conectar correctamente la bomba y los ventiladores de un sistema de refrigeración líquida AIO.

---

# Introducción

Los sistemas de refrigeración líquida AIO, también llamados **water coolers**, combinan una bomba, un radiador y uno o más ventiladores. Las motherboards pueden incluir varios headers de tres o cuatro pines con nombres y comportamientos diferentes. Aunque algunos conectores permiten seleccionar control **PWM** o **DC** desde la BIOS/UEFI, no todos están destinados a la misma función ni entregan la misma corriente máxima.

Una conexión incorrecta o una configuración inadecuada puede provocar:

- Una advertencia de ventilador de CPU durante el arranque.
- Una bomba detenida o funcionando por debajo del régimen requerido.
- Temperaturas elevadas, pérdida de rendimiento o apagados por protección térmica.
- Sobrecarga eléctrica del header cuando se conectan más dispositivos de los admitidos.

!!! warning "El manual del fabricante tiene prioridad"

    La distribución siguiente es una referencia general. Siempre se deben consultar los manuales del AIO y de la motherboard, porque algunos equipos utilizan un hub o controlador propio, alimentación SATA/PCIe y un cable separado que sólo informa las RPM a `CPU_FAN`.

---

# Descripción de los headers

## CPU_FAN

Es el conector principal para el ventilador del disipador del procesador o para la señal de monitoreo indicada por el fabricante del AIO.

- La BIOS/UEFI suele supervisar sus RPM para comprobar que exista refrigeración sobre la CPU.
- Si no detecta una señal válida, la motherboard puede mostrar una advertencia como **CPU Fan Error** o solicitar intervención durante el arranque.
- En una instalación AIO convencional, los ventiladores del radiador suelen conectarse aquí mediante un splitter compatible.
- En AIO con controlador propio, puede recibir únicamente el cable tacométrico de la bomba o del controlador.

No se debe desactivar la supervisión de `CPU_FAN` para ocultar una advertencia sin comprobar antes que la bomba y los ventiladores funcionan correctamente.

## CPU_OPT

Es un conector auxiliar pensado principalmente para un segundo ventilador del disipador o para otro grupo de ventiladores asociado a la CPU.

- En muchas motherboards comparte o replica la curva de `CPU_FAN`.
- Puede utilizarse para un segundo ventilador del radiador cuando así lo permitan los manuales.
- No conviene asumir que posee control independiente ni que admite la corriente necesaria para una bomba.

Para ventiladores de gabinete es preferible utilizar `SYS_FAN` o `CHA_FAN`, salvo indicación diferente del fabricante.

## AIO_PUMP / PUMP_FAN / PUMP_SYS

Son nombres utilizados para headers destinados a bombas de refrigeración líquida. La denominación exacta depende del fabricante de la motherboard.

- Suelen disponer de un perfil predeterminado de velocidad completa o de parámetros específicos para bombas.
- Algunos admiten control PWM o DC; otros funcionan a velocidad completa de manera predeterminada.
- Pueden tener un límite de corriente diferente al de los headers de ventiladores.

Cuando el AIO alimenta la bomba directamente desde la motherboard y ambos manuales lo indican, éste es normalmente el header preferido. La bomba no debe forzarse siempre al 100 % si el fabricante del AIO especifica otra forma de control.

## SYS_FAN / CHA_FAN

Están destinados principalmente a los ventiladores del gabinete.

- Su curva puede configurarse desde la BIOS/UEFI o desde el software de la motherboard.
- Según el modelo, la fuente de temperatura utilizada por la curva puede ser seleccionable.
- No se debe conectar una bomba en estos headers sin verificar que el fabricante lo permita, que el modo de control sea correcto y que no se exceda la corriente máxima.

---

# Configuración recomendada para un AIO

## Esquema general

Para un AIO cuya bomba y ventiladores se conectan directamente a la motherboard:

| Componente | Conexión recomendada |
|------------|----------------------|
| Bomba | `AIO_PUMP`, `PUMP_FAN` o equivalente |
| Ventilador principal o splitter del radiador | `CPU_FAN` |
| Segundo grupo de ventiladores del radiador | `CPU_OPT`, si el manual lo admite |
| Ventiladores del gabinete | `SYS_FAN` o `CHA_FAN` |

Los ventiladores del radiador deben responder preferentemente a la temperatura de la CPU. Si se utiliza un splitter, sólo una de sus ramas suele devolver la señal de RPM; esto es normal y evita que se superpongan varias señales tacométricas.

## Si la motherboard no posee un header para bomba

1. Consultar qué conexión indica el fabricante del AIO: puede ser `CPU_FAN`, `CPU_OPT`, otro header compatible o un controlador externo.
2. Configurar el header en modo PWM o DC según el tipo de conector y la especificación de la bomba.
3. Aplicar velocidad completa únicamente cuando el fabricante de la bomba lo recomiende.
4. Conectar los ventiladores del radiador a otro header asociado a la CPU o a un splitter/controlador compatible.
5. Confirmar que la BIOS/UEFI reciba una señal de RPM de la refrigeración de CPU o configurar su monitoreo exactamente como indique el fabricante.

## AIO con alimentación o controlador propio

Algunos AIO modernos alimentan la bomba y los ventiladores mediante SATA, PCIe o un hub propietario. En esos modelos:

- No se debe trasladar la alimentación al header `AIO_PUMP` si el manual no lo indica.
- El cable conectado a `CPU_FAN` puede transportar únicamente la señal tacométrica.
- También pueden ser necesarias conexiones internas USB 2.0 y ARGB/RGB para control y monitoreo.

---

# Verificación después del armado

1. Confirmar físicamente que la bomba, los ventiladores del radiador y los ventiladores del gabinete estén conectados según sus manuales.
2. Verificar que ningún splitter o conjunto de dispositivos exceda la corriente máxima indicada para el header.
3. Ingresar a la BIOS/UEFI y comprobar que se informen RPM en los conectores relevantes.
4. Revisar el modo de control del header: **PWM** para dispositivos PWM de cuatro pines o **DC** para dispositivos de tres pines, salvo indicación diferente del fabricante.
5. Comprobar que la bomba mantenga el régimen especificado y que los ventiladores aumenten su velocidad con la temperatura.
6. Controlar la temperatura de la CPU bajo carga y confirmar que no existan ruidos anormales, alertas o apagados.

!!! danger "Detener la prueba ante temperatura anormal"

    Si la temperatura de la CPU aumenta rápidamente o no se detectan RPM donde deberían existir, apagar el equipo y revisar la alimentación, el header utilizado, el montaje del bloque y la configuración de control.

---

# Casos de uso

## Taller de Armado

- Identificar todos los cables del AIO antes de energizar el equipo.
- Evitar asignar los conectores sólo por similitud física.
- Incorporar la comprobación de RPM y temperaturas al control final.

## RMA y Soporte Técnico

- Revisar la conexión y el modo PWM/DC ante alertas de `CPU_FAN` o temperatura elevada.
- Comprobar si el AIO utiliza un controlador propio antes de interpretar un header sin RPM como una bomba detenida.
- Verificar límites de corriente, splitters y curvas cuando los ventiladores no responden como se espera.

---

# Consideraciones

- Los nombres, límites eléctricos y opciones de control varían entre motherboards.
- Un conector de cuatro pines no garantiza por sí solo que el dispositivo o el header estén configurados en modo PWM.
- No se deben confundir los headers de ventilación con conectores RGB de 12 V o ARGB de 5 V.
- La cantidad de dispositivos conectados mediante splitters debe respetar la corriente máxima total del header.
- La ausencia de RPM puede deberse a que el cable sólo alimenta el dispositivo o a que el sistema utiliza otro canal de monitoreo; se debe validar el diseño específico.

---

# Referencias

- [ASUS - Solución para el mensaje CPU FAN Error durante el arranque](https://www.asus.com/us/support/faq/1006064/)
- [MSI - Funciones de los puertos y headers de una motherboard](https://us.msi.com/blog/what-are-the-functions-of-motherboard-ports-and-headers)
- [Corsair - Manual de los AIO iCUE LINK H100i, H115i, H150i y H170i](https://www.corsair.com/us/en/explorer/diy-builder/cpu-coolers/icue-link-h100i-h115i-h150i-h170i-rgb-aio/)
- Manuales del sistema AIO y de la motherboard utilizados en cada equipo.

---

# Historial de cambios

| Versión | Fecha | Descripción |
|---------|-------|-------------|
| 1.0 | 2026-08-15 | Creación del documento. |
