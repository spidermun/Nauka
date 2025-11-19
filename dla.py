from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import os

# Ścieżka zapisu PDF na pulpit
pdf_path = r"C:\Users\user\Desktop\tabelka_kierowcy.pdf"

# Tworzymy dokument PDF (małe marginesy, żeby tabela zajęła całą stronę)
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=A4,
    topMargin=10,
    bottomMargin=10,
    leftMargin=20,
    rightMargin=20,
)
styles = getSampleStyleSheet()
styleN = styles["Normal"]

# Nagłówek z miejscem na podpis
header_data = [
    [
        Paragraph("DATA:", styleN),
        Paragraph("nr Rejestracji:", styleN),
        Paragraph("podpis kierowcy:            ", styleN),
    ]
]

# Tabela główna (30 wierszy = pełna kartka A4)
table_data = [["Lp.", "", ""]]
for i in range(40):
    table_data.append(["", "", ""])

# Tworzenie tabeli nagłówka
header_table = Table(header_data, colWidths=[200, 200, 140])
header_table.setStyle(
    TableStyle(
        [
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.black),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]
    )
)

# Tabela główna
main_table = Table(table_data, colWidths=[50, 400, 90])
main_table.setStyle(
    TableStyle(
        [
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.black),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]
    )
)

# Składamy całość
elements = [header_table, Spacer(1, 6), main_table]
doc.build(elements)

print("✅ Utworzono plik:", pdf_path)

# (opcjonalnie) automatycznie otworzy PDF po zapisaniu
os.startfile(pdf_path)
