def balance_undersample(data: list) -> list:
    """
    Undersample the majority classes so all classes have the same number of
    samples equal to the minority class count.

    data: list of (sample, label) tuples
    Returns: list of (sample, label) tuples, order-preserving
    """
    dict_ = {}
    result = []
    if len(data) == 0:
        return []
    for i in data:
        if i[1] in dict_:
            dict_[i[1]].append(i)
        else:
            dict_[i[1]] = [i]
    min_value = min(len(val) for val in dict_.values())
    for key in dict_:
        dict_[key] = dict_[key][:min_value]

    for i in data:
        label = i[1]

        if i in dict_[label]:
            result.append(i)

    return result
