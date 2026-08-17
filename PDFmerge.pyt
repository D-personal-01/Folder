from pypdf import PdfReader, PdfWriter
writer = PdfWriter()

for pdf in ["a.pdf", "b.pdf"]:
    reader = PdfReader(pdf)
    for page in reader.pages:
        writer.add_page(page)

with open("merged.pdf", "wb") as f:
    writer.write(f)