# Python 3.4

table_data = [['apples', 'oranges', 'cherries', 'bannana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(data):
    col_widths = [0] * len(data)
    tab_cols = len(col_widths)
    max_rows = 0

    for i in range(len(data)):
        if max_rows <= len(data[i]):
            max_rows = len(data[i])

        for n in range(len(data[i])):
            item_len = len(data[i][n])

            if col_widths[i] <= item_len:
                col_widths[i] = item_len

    for n in range(max_rows):
        text_row = ''
        for i in range(tab_cols):
            if not data[i][n]:
                text_row += '-'.rjust(col_widths[i] + 1)
            else:
                text_row += data[i][n].rjust(col_widths[i] + 1)
        print(text_row)

print_table(table_data)
