import pytest
from pdf_task.pdf_comparator import compare_pdfs

def test_compare_pdfs():
    pdf_data_1 = {"pages": [{"text": "Hello World"}]}
    pdf_data_2 = {"pages": [{"text": "Hello World"}]}
    pdf_data_3 = {"pages": [{"text": "Different Text"}]}

    assert compare_pdfs(pdf_data_1, pdf_data_2) == True
    assert compare_pdfs(pdf_data_1, pdf_data_3) == False
