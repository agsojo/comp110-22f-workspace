from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Docstring."""
    result: dict[str, list[str]] = {}
    first_row: list[str] = column_table.keys()
    for column in first_row:
        col_vals: list[str] = []
        i: int = 0
        while i < n:
            col_vals.append(column_table[column][i])
            i += 1
        result[column] = col_vals
    return result


def select(column_table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Docstring."""
    result: dict[str, list[str]] = {}
    for key in column_table:
        if key in columns:
            result[key] = column_table[key]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Docstring."""
    result: dict[str, list[str]] = {}
    for key in table_1:
        result[key] = table_1[key]
    for key in table_2:
        if key in result:
            result[key] += table_2[key]
        else:
            result[key] = table_2[key]
    return result