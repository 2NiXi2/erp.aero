import pytest
from pdf_task.pdf_parser import extract_text_and_structure, parse_pdf_to_dict

def test_extract_text_and_structure():
    pdf_path = "test_task.pdf"
    result = extract_text_and_structure(pdf_path)
    assert "pages" in result
    assert len(result["pages"]) > 0
    assert "text" in result["pages"][0]
    assert "blocks" in result["pages"][0]

def test_parse_pdf_to_dict():
    pdf_path = "test_task.pdf"
    result = parse_pdf_to_dict(pdf_path)
    assert "metadata" in result
    assert "content" in result
    assert "pages" in result["content"]
