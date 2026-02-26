from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Image, Spacer, SimpleDocTemplate, Table
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

#lista que almacena todos los elementos
guion = []

# tabla
titulo = ['Horario','','','','','','','']
cab = ['', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
actM = ['Mañana', 'Cole', 'Correr', '-', '-', '-', 'Estudiar', 'Trabajar']
actT = ['Tarde', 'Trabajar', 'Clases', 'Clases', 'Trabajar', 'Trabajar', 'Leer', '-']
actN = ['Noche', '-', 'Trabajar', 'Trabajar', 'Trabajar', '-', '-', '-']

tabla = Table ([titulo, cab, actM, actT, actN])
tabla.setStyle([('TEXTCOLOR', (1,1), (7,1), colors.red),
                ('TEXTCOLOR', (0,0), (0,3), colors.blue),
                ('BACKGROUND', (1,1), (7,1), colors.cyan),
                ('INNERGRID', (0,0), (7,4), 1, colors.lightgrey),
                ('LINEABOVE', (1,2), (7, 2), 1.5, colors.red),
                ('LINEAFTER', (0,0), (0,0), 1.5, colors.violet),
                ('LINEBEFORE', (1,2), (1,4), 1.5, colors.red),
                ("BOX", (0,0), (7,4), 10, colors.blue),
                ('SPAN', (0, 0), (7, 0)),
                ('ALIGN', (0,0), (0,0), 'CENTER'),
                ('SPAN', (1, 1), (-2, 1)),
                ('ALIGN', (1, 1), (1, 1), 'CENTER'),
                ])
# el spacer
esp = Spacer(100, 100)

# para texto
estilos = getSampleStyleSheet()
texto_subtitulo = Paragraph("Organización de actividades de mañana, tarde y noche", estilos['Heading2'])

estilo_titulo = estilos['Title']
estilo_titulo.textColor = colors.green
estilo_titulo.fontSize = 24
texto_titulo = Paragraph("Mi Horario Semanal", estilo_titulo)

texto_normal = Paragraph("Este es mi texto de prueba", estilos['Normal'])

# para graficos
d3 = Drawing(400,200)

graficoTarta = Pie()

graficoTarta.x = 65 #dimensiones dentro del dibujo d3
graficoTarta.y = 15
graficoTarta.width = 170
graficoTarta.height = 170
graficoTarta.data = [10,20,30,40,50]
graficoTarta.labels = ['Oppo','Pixel','Galaxy','Iphone','Xiaomi']
graficoTarta.slices.strokeWidth = 0.5 #son las "porciones" de la tarta, el ancho de la linea
graficoTarta.slices[3].popout = 10 #la porción "3" se va a destacar
graficoTarta.slices[3].strokeDashArray = [5,2] #a la porción 3 tiene una linea de contorno especial intermitente
graficoTarta.slices[3].labelRadius = 3
graficoTarta.slices[3].fontColor = colors.red #le damos color a la descripción de la porción
graficoTarta.sideLabels = 1 #crea una linea indicativa de sección de gráfico y su definición

colores = [colors.blue, colors.red, colors.green, colors.yellow, colors.orange]

for i, color in enumerate(colores):
    graficoTarta.slices[i].fillColor = color

d3.add(graficoTarta)

# para hacer una leyenda

leyenda = Legend()

#hay que pasar una lista con el nombre de los valores de los colores, primero color luego la leyenda
#primero el color de relleno
#segundo se metería los nombres de moviles y el porcentaje que tiene el nombre en la tarta
leyenda.colorNamePairs = [(graficoTarta.slices[i].fillColor,
                           (graficoTarta.labels[i][0:20],'%0.2f' % graficoTarta.data[i] ))
                            for i in range (len(graficoTarta.data))]

#coordenadas de la leyenda
leyenda.x = 370
leyenda.y = 5
#fuente de la leyenda
leyenda.fontName = 'Helvetica'
#tamaño de la letra en la leyenda
leyenda.fontSize = 7
#posición a donde esta anclada la leyenda
leyenda.boxAnchor = 'n'
#delimita el máximo de columnas
leyenda.columnMaximum = 3
#
leyenda.strokeWidth = 1
#
leyenda.strokeColor = colors.black
#
leyenda.deltax = 20
#separa los elementos entre sí con el deltay
leyenda.deltay = 10
#separación entre las columnas
leyenda.autoXPadding = 20
#seperación entre los valores
leyenda.yGap = 0
# espaciado del texto dentro de su celda (el espaciado es del color)
leyenda.dxTextSpace = 10
#alinea el color a la izquierda de la palabra que lo relaciona
leyenda.alignment = 'right'
# son lineas divisoras en binario (no se como usar esta monda)
leyenda.dividerLines = 7
#esto mueve a la linea divisora
leyenda.dividerOffsY = 5.5
#subCols separa las columnas dentro de la leyenda
leyenda.subCols.rpad = 15

d3.add(leyenda)

# Insertar una imagen (asegúrate de que la foto exista en la misma carpeta)
# foto = Image("ruta_de_tu_logo.png", width=100, height=100)
# guion.append(foto)

guion.append(texto_titulo)
guion.append(d3)
guion.append(esp)
guion.append(texto_normal)
guion.append(esp)
guion.append(texto_subtitulo)
guion.append(esp)
guion.append(tabla)

doc = SimpleDocTemplate("EjemploPlaypus_Tabla.pdf", pagesize=A4, showBoundary=0)
doc.build (guion)