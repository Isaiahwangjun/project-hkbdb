from match_conditions.fuzzf import completely, partial_ratio, token_sort_ratio

match_conditions = {
    "label_event": partial_ratio,
    "hasEventPlace": token_sort_ratio,
    "hasRelatedPerson": token_sort_ratio,
    "hasStartDate": partial_ratio,
    "hasEndDate": partial_ratio,
    "period": partial_ratio,
    "work": partial_ratio
}
