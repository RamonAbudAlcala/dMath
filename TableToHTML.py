# script to turn dictionaries whose values are lists of the same length into html tables.

def table_to_HTML(table):
    html_table = ""
    html_table += "<table>\n"
    html_table += "<thead>\n"
    html_table += "<tr>\n"
    for key in table:
        html_table += f"""<th scope="col">{key}</th>\n"""
    html_table += "</tr>\n"
    html_table += "</thead>\n"
    html_table += "<tbody>\n"
    for i in range(len(list(table.values())[0])):
        html_table += "<tr>\n"
        for key in table:
            html_table += f"<td>{table[key][i]}</td>\n"
        html_table += "</tr>\n"
    html_table += "</tbody>\n"
    html_table += "</table>\n"
    return html_table