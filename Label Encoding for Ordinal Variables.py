def label_encode_ordinal(values: list, order: list) -> list:
    """
    Encode ordinal categorical values to integers based on specified order.
    
    Args:
        values: List of categorical values to encode
        order: List specifying the order of categories from lowest (0) to highest
    
    Returns:
        List of integers representing the encoded values
    """
    dict_ = {}
    result = []
    if len(values)==0:
        return []
    for i in range(len(order)):
        dict_[order[i]]=i
    for i in values:
        if i in dict_:
            result.append(dict_[i])
        else:
            result.append(-1)
    return result