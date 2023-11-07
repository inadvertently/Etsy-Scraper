from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from translation import translation


def make_pdf(listing_name, translated_text):
    pdf_filename = f"{listing_name}.pdf"
    doc = SimpleDocTemplate(f"{listing_name}.pdf",pagesize=letter,
                rightMargin=72,leftMargin=72,
                topMargin=72,bottomMargin=18)
    Story = []
    styles = getSampleStyleSheet()
    title_style = styles['Heading1']
    title_style.alignment = 1
    title = Paragraph("Aroma Depot", title_style)
    translated_description = translation(translated_text)
    text = Paragraph(translated_description, styles['Normal'])
    Story.append(title)
    Story.append(text)
    doc.build(Story)