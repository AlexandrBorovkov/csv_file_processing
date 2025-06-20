def aggregate_data(data, aggregate_condition):
    if not data:
        return None
    try:
        column, func = aggregate_condition.split('=')
        column = column.strip()
        func = func.strip()

        numbers = [float(row[column]) for row in data]

        match func:
            case 'avg':
                return sum(numbers) / len(numbers)
            case 'min':
                return min(numbers)
            case 'max':
                return max(numbers)
    except Exception:
        return None
