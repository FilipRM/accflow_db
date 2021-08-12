
def amount_inbetween(data, lower, upper):
    y = data.where(lower <= data.Amount <= upper)
    return y


def amount_over_under(data, limit):
    y = []
    if capitalize(choice)[0] == "O":
        y[0] = data.where(data.Amount >= limit)
        y[1] = data.where(data.Amount >= limit)
        return y

    elif capitalize(choice)[0] == "U":
        y[0] = data.where(data.Amount <= limit)
        y[1] = data.where(data.Amount <= limit)
        return y
    else:
        return SyntaxError


def balance_inbetween(data, lower, upper):
    y = data.where(lower <= data.Balance <= upper)
    return y


def amount_over_under(data, limit):
    y = []
    if capitalize(choice)[0] == "O":
        y[0] = data.where(data.Balance >= limit)
        y[1] = data.where(data.Balance >= limit)
        return y

    elif capitalize(choice)[0] == "U":
        y[0] = data.where(data.Balance <= limit)
        y[1] = data.where(data.Balance <= limit)
        return y
