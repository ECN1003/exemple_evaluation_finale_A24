from nbconvert.exporters import HTMLExporter
import os

class CustomHTMLExporter(HTMLExporter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Get the path to custom.css
        custom_css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'custom/custom.css')
        # Read the custom CSS
        with open(custom_css_path, 'r') as f:
            custom_css = f.read()
        
        # Add the custom CSS to the existing CSS
        self.extra_css = custom_css