from custom_exporter import CustomHTMLExporter

# Create an instance of the custom exporter
exporter = CustomHTMLExporter()

# Export the notebook to HTML with custom CSS
output_html, resources = exporter.from_filename('binder_test.ipynb')

# Write the exported HTML to a file
with open('binder_test_custom.html', 'w', encoding='utf-8') as f:
    f.write(output_html)

print("Notebook exported with custom CSS to binder_test_custom.html")