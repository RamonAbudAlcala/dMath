# script to turn dictionaries whose values are lists of the same length into html tables with each list is a column.

def colDict_to_HTML(colDict):
    html_table = ""
    html_table += "<table>\n"
    html_table += "<thead>\n"
    html_table += "<tr>\n"
    for key in colDict:
        html_table += f"""<th scope="col">{key}</th>\n"""
    html_table += "</tr>\n"
    html_table += "</thead>\n"
    html_table += "<tbody>\n"
    for i in range(len(list(colDict.values())[0])):
        html_table += "<tr>\n"
        for key in colDict:
            html_table += f"<td>{colDict[key][i]}</td>\n"
        html_table += "</tr>\n"
    html_table += "</tbody>\n"
    html_table += "</table>\n"
    return html_table

# script to turn a list of pairs into a html table with two columns.

def rowList_to_HTML(rowList):
    html_table = ""
    html_table += "<table>\n"
    html_table += "<thead>\n"
    html_table += "<tr>\n"
    for key in rowList[0]:
        html_table += f"""<th scope="col">{key}</th>\n"""
    html_table += "</tr>\n"
    html_table += "</thead>\n"
    html_table += "<tbody>\n"
    for row in rowList[1:]:
        html_table += "<tr>\n"
        for i in range(len(row)):
            html_table += f"<td>{row[i]}</td>\n"
        html_table += "</tr>\n"
    html_table += "</tbody>\n"
    html_table += "</table>\n"
    return html_table