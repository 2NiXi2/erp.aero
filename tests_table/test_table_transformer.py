from table_task.table_transformer import transform_table_to_json


def test_transform_table_to_json():
    table = [
        {"Columns View": "SO Number", "Sort By": "", "Highlight By": "equals=S110=rgba(172,86,86,1),equals=S111",
         "Condition": "equals=S110,equals=S111", "Row Height": "60", "Lines per page": "25"},
        {"Columns View": "Client PO", "Sort By": "", "Highlight By": "equals=P110,equals=P111",
         "Condition": "equals=P110", "Row Height": "", "Lines per page": ""},
        {"Columns View": "Terms of Sale", "Sort By": "asc", "Highlight By": "equals=S110=rgba(172,86,86,1)",
         "Condition": "", "Row Height": "", "Lines per page": ""}
    ]

    websocket_response = {
        "Client PO": {"index": "so_list_client_po", "filter": "client_po"},
        "SO Number": {"index": "so_list_so_number", "filter": "so_no"},
        "Terms of Sale": {"index": "so_list_terms_of_sale", "filter": "term_sale"}
    }

    base_ws = {
        "Columns View": "columns",
        "Sort By": "order_by",
        "Condition": "conditions_data",
        "Lines per page": "page_size",
        "Row Height": "row_height",
        "Highlight By": "color_conditions"
    }

    result = transform_table_to_json(table, websocket_response, base_ws)

    assert "columns" in result
    assert "order_by" in result
    assert "conditions_data" in result
    assert "color_conditions" in result
