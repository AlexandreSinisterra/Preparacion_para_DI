from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, Spacer
from reportlab.lib.pagesizes import A4

# ==========================================
# 1. DEFINIMOS LAS DOS LISTAS DE DATOS
# ==========================================
# Lista A: 3 elementos (ej. Frutas)
lista_3_elementos = [
    ['Manzanas', 45],
    ['Peras', 30],
    ['Naranjas', 25]
]

# Lista B: 5 elementos (ej. Dispositivos)
lista_5_elementos = [
    ['Oppo', 10],
    ['Pixel', 20],
    ['Galaxy', 30],
    ['Iphone', 15],
    ['Xiaomi', 25]
]

# ==========================================
# 2. ¡EL SELECTOR! (Cambia esto para probar)
# ==========================================
# Simplemente igualamos 'datos_elegidos' a la lista que queramos usar.
# Prueba a cambiar 'lista_3_elementos' por 'lista_5_elementos' y ejecuta.
datos_elegidos = lista_3_elementos

# ==========================================
# 3. PREPARAMOS EL GRÁFICO DE TARTA
# ==========================================
d = Drawing(400, 200)
tarta = Pie()
tarta.x = 100
tarta.y = 20
tarta.width = 150
tarta.height = 150

# Aquí está la magia dinámica para la tarta:
# Extraemos solo los nombres (posición 0) y solo los valores (posición 1)
tarta.labels = [fila[0] for fila in datos_elegidos]
tarta.data = [fila[1] for fila in datos_elegidos]

# Lista de colores suficientemente grande para aguantar hasta 5 elementos
paleta_colores = [colors.red, colors.blue, colors.green, colors.orange, colors.purple]

# Asignamos colores de forma variable según cuántos datos haya
for i in range(len(datos_elegidos)):
    tarta.slices[i].fillColor = paleta_colores[i]

d.add(tarta)

# ==========================================
# 4. PREPARAMOS LA TABLA DINÁMICA
# ==========================================
# Creamos una fila de cabecera y le sumamos los datos que hayamos elegido
datos_para_tabla = [['Categoría', 'Cantidad']] + datos_elegidos

tabla = Table(datos_para_tabla)

# Un estilo muy básico pero resultón
tabla.setStyle([
    ('BACKGROUND', (0,0), (1,0), colors.black),    # Fondo negro para la cabecera
    ('TEXTCOLOR', (0,0), (1,0), colors.white),     # Texto blanco para la cabecera
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),           # Todo centrado
    ('GRID', (0,0), (-1,-1), 1, colors.grey)       # Cuadrícula para todo
])

# ==========================================
# 5. CONSTRUIMOS EL PDF
# ==========================================
guion = []
guion.append(d)           # Añadimos el gráfico
guion.append(Spacer(1, 30)) # Un espacio
guion.append(tabla)       # Añadimos la tabla

doc = SimpleDocTemplate("Proyecto_Variable.pdf", pagesize=A4)
doc.build(guion)

print(f"PDF generado con éxito usando {len(datos_elegidos)} elementos.")