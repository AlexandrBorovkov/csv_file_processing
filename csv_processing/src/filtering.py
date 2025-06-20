def condition_parsing(condition):
    try:
        operators = ['>=', '<=', '>', '<', '=']
        for op in operators:
            if op in condition:
                column, value = condition.split(op)
                return column.strip(), op, value.strip()
    except ValueError:
        return None

def filter_the_data(data, filter_condition):
    if not data:
        return None
    condition = condition_parsing(filter_condition)
    if not condition:
        return None
    column, operator, value = condition
    try:
        match operator:
            case '=':
                return [row for row in data if str(row[column]) == str(value)]
            case '>':
                return [row for row in data if float(row[column]) > float(value)]
            case '<':
                return [row for row in data if float(row[column]) < float(value)]
            case '>=':
                return [row for row in data if float(row[column]) >= float(value)]
            case '<=':
                return [row for row in data if float(row[column]) <= float(value)]
    except KeyError:
        return None
