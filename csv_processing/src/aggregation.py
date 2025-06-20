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
                result = sum(numbers) / len(numbers)
            case 'min':
                result = min(numbers)
            case 'max':
                result = max(numbers)
        return {func: result}
    except Exception:
        return None
