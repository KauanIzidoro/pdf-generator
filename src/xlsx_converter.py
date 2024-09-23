import pandas as pd
import pdfkit

# Solicita o nome do arquivo e o nome de destino
filename = input("Excel filename (without extension): ")
target_filename = input("Target filename (without extension): ")

# Carregar o arquivo Excel
excel_data = pd.read_excel(f"{filename}.xlsx").dropna()

# Converter o conteúdo do Excel em uma tabela HTML
table_html = excel_data.to_html(index=False)

# Definir a estrutura HTML com a tabela convertida e CSS
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: Arial, sans-serif; /* Define Arial como a fonte padrão */
            font-size: 12pt;  /* Tamanho da fonte padrão */
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        table, th, td {{
            border: 1px solid black;
        }}
        th, td {{
            padding: 8px;
            text-align: left;
        }}
    </style>
</head>
<body>
    <h2>Excel Data</h2>
    {table_html}
</body>
</html>
"""

# Gerar o PDF a partir do HTML
pdfkit.from_string(html_content, f"{target_filename}.pdf")

print("Excel to PDF.")
