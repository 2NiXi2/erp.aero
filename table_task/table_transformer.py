def transform_table_to_json(table, websocket_response, base_ws):
    result = {"columns": [], "order_by": {}, "conditions_data": {}, "page_size": None, "row_height": None,
              "color_conditions": {}, "module": "SO"}

    for row in table:
        columns_view = row.get("Columns View")
        if columns_view in websocket_response:
            response_data = websocket_response[columns_view]
            result["columns"].append({"index": response_data["index"], "sort": len(result["columns"])})

            condition = row.get("Condition", "")
            if condition:
                for cond in condition.split(","):
                    cond_type, value = cond.split("=")
                    result["conditions_data"].setdefault(response_data["filter"], []).append(
                        {"type": cond_type, "value": value})

            highlight_by = row.get("Highlight By", "")
            if highlight_by:
                for highlight in highlight_by.split(","):
                    parts = highlight.split("=")
                    if len(parts) == 3:
                        cond_type, value, color = parts
                        result["color_conditions"].setdefault(response_data["filter"], []).append(
                            {"type": cond_type, "value": value, "color": color})
                    elif len(parts) == 2:
                        cond_type, value = parts
                        result["color_conditions"].setdefault(response_data["filter"], []).append(
                            {"type": cond_type, "value": value, "color": ""})

        if row.get("Sort By"):
            result["order_by"] = {"direction": row["Sort By"], "index": websocket_response[columns_view]["index"]}
        if row.get("Lines per page"):
            result["page_size"] = row["Lines per page"]
        if row.get("Row Height"):
            result["row_height"] = row["Row Height"]

    return result
