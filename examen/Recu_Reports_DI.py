from itertools import product

from PIL.ImageQt import align8to32
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Image, Spacer, SimpleDocTemplate, Table
from reportlab.lib.pagesizes import A4

from xeradorDatosAlbara import XeradorAlbaran

guion = []

x = XeradorAlbaran("modelosClasicos.dat")

datos_cabeceira = XeradorAlbaran.obter_cabeceira_albara(x,1)
datos_tabla = XeradorAlbaran.obter_detalle_albara(x,1)

print([fila[2] for fila in datos_tabla])
print([fila[3] for fila in datos_tabla])
nuevo_coso = [fila[2] for fila in datos_tabla]
new_datos = []

total_final_sin_deci = 0

for fila in datos_tabla:
    total = fila[2]*fila[3]
    total_final_sin_deci += total
    total = '%0.2f' % total
    fila3_2decimales = '%0.2f' % fila[3]
    fila3nueva = str(fila3_2decimales) + ' €'
    fila = (fila[0],fila[1],fila[2],fila3nueva,str(total)+' €')
    new_datos += [fila]

total_final = '%0.2f' % total_final_sin_deci

print(new_datos)
print(datos_cabeceira)
print(datos_tabla)
producto = '                                     Produto                                     '
datos_para_tabla = [['Código', producto, 'Cantidade', 'Prezo Unit.','    Total    ']] + new_datos

tabla = Table(datos_para_tabla)

tabla.setStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.darkgrey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('BACKGROUND', (0, 2), (-1, 2), colors.lightgrey),
    ('ALIGN', (1, 1), (1, -1), 'LEFT'),
    ('FONT', (0, 0), (-1, 0), "Helvetica-Bold")
])

espacio = '                                                                                        '
tit = [espacio, '', 'EMPRESA DISTRIBUIDORA GALEGA S.L', '']
cab = ['', '', '', 'poligono Industrial As Gándaras']
dic = ['', '', '','15708 Santiago de Compostela']
NIF = ['', '', '', 'NIF: B15888777']
tel = ['', '', '', 'Tel: 981 100 200']

tabla2 = Table ([tit, cab, dic, NIF, tel])

tabla2.setStyle([
    ('FONT', (0, 0), (-1, 0), "Helvetica-Bold"),
    ('TEXTCOLOR', (0,0), (-1,0), colors.darkgrey),
    ('ALIGN', (0,0), (-1,-1), 'RIGHT'),
    ('SPAN', (2, 0), (3, 0)),
    ('SIZE', (0, 0), (-1, 0), 11)
])

tit1 = ['CLIENTE:', datos_cabeceira[2]+''+datos_cabeceira[3], '','','                                                                                                    ']
cab1 = ['Nº CLIENTE:', datos_cabeceira[1], '', '','']
dic1 = ['', '', '','','']
NIF1 = ['DATA ALBARAN:', datos_cabeceira[4], '', '','']
tel1 = ['DATA ENTREGA:', datos_cabeceira[5], '', '','']

tabla3 = Table ([tit1, cab1, dic1, NIF1, tel1])

tabla3.setStyle([
    ('FONT', (0, 0), (0, -1), "Helvetica-Bold"),
    ('SIZE', (0, 0), (0, -1), 10)
])


estilos = getSampleStyleSheet()

estilo_titulo = estilos['Title']
estilo_titulo.textColor = colors.black
estilo_titulo.fontSize = 24
texto_titulo = Paragraph("ALBARÁN Nº 1", estilo_titulo)


prueba = [espacio, '      ', 'TOTAL:  '+str(total_final)+'€', '']
tablaprueba = Table([prueba])
tablaprueba.setStyle([
    ('TEXTCOLOR', (0,0), (-1,0), colors.black),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('LINEABOVE', (2,0), (-1, 0), 1.5, colors.black),
    ('SPAN', (2, 0), (3, 0)),
    ('SIZE', (0, 0), (-1, 0), 13),
    ('FONT', (0, 0), (-1, 8), "Helvetica-Bold")

])
texto_total_gracias = estilos['Normal']
texto_total_gracias.textColor = colors.black
texto_total_gracias.fontSize = 7

texto_gracias = Paragraph("Grazas pola súa compra. Conserve este albarán como xustificante da entrega", texto_total_gracias)

esp = Spacer(100, 20)


guion.append(tabla2)
guion.append(esp)
guion.append(texto_titulo)
guion.append(esp)
guion.append(tabla3)
guion.append(esp)
guion.append(tabla)
guion.append(esp)
guion.append(tablaprueba)
guion.append(esp)
guion.append(texto_gracias)


doc = SimpleDocTemplate("Proyecto_Variable.pdf", pagesize=A4)
doc.build(guion)
