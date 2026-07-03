import numpy as np
def macro_average_accuracy(subtask_results: dict) -> float:
    """
    Compute the unweighted macro-average accuracy across benchmark subtasks.
    Each value in subtask_results is a list of (prediction, label) tuples.
    Return the macro-average accuracy rounded to 4 decimals.
    """
    result = []
    if not subtask_results:
        return 0.0
    for x in subtask_results.keys():
        count = 0
        len_ = len(subtask_results[x])
        if len_ == 0:
            result.append(0.0)
            continue
        for i in subtask_results[x]:
            if i[0]==i[1]:
                count = count + 1
        result.append(float(count/len_))
    return (float(sum(result)/len(result)))