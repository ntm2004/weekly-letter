# Embeds logo.jpg into template.html -> index.html (self-contained, works offline-from-disk for PDF export)
import base64, pathlib
here = pathlib.Path(__file__).parent
logo = base64.b64encode((here / "logo.jpg").read_bytes()).decode()
html = (here / "template.html").read_text(encoding="utf-8").replace("__LOGO__", "data:image/jpeg;base64," + logo)
(here / "index.html").write_text(html, encoding="utf-8")
print("wrote index.html")
