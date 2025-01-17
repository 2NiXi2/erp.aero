import fitz

def extract_text_and_structure(pdf_path):
    pdf_data = {"pages": []}
    with fitz.open(pdf_path) as pdf:
        for page_number in range(len(pdf)):
            page = pdf[page_number]
            page_dict = {
                "text": page.get_text(),
                "blocks": [],
                "images": [],
            }
            for block in page.get_text("dict")["blocks"]:
                page_dict["blocks"].append({
                    "type": block.get("type", 0),
                    "bbox": block.get("bbox", []),
                    "lines": [line["spans"] for line in block.get("lines", [])]
                })
            pdf_data["pages"].append(page_dict)
    return pdf_data

def extract_metadata(pdf_path):
    with fitz.open(pdf_path) as pdf:
        return pdf.metadata

def parse_pdf_to_dict(pdf_path):
    data = {
        "metadata": extract_metadata(pdf_path),
        "content": extract_text_and_structure(pdf_path)
    }
    return data
