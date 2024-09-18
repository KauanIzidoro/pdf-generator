import markdown
import pdfkit

filename = input("filename: ")
target_filename = input("target filename: ")

# Open markdown file
with open(f"{filename}" + ".md", "r", encoding="utf-8") as md_file:
    markdown_content = md_file.read()

# Convert Markdown to HTML and add CSS styling and meta charset to UTF-8
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
    </style>
</head>
<body>
    {markdown.markdown(markdown_content)}
</body>
</html>
"""

# # Save the generated HTML to a file
# with open("template_format.html", "w", encoding="utf-8") as html_file:
#     html_file.write(html_content)

# Generate PDF from HTML with standard font and UTF-8 encoding
pdfkit.from_string(html_content, f"{target_filename}" + ".pdf")

print("Generate PDF and HTML")