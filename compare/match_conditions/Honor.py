from match_conditions.fuzzf import completely, partial_ratio, token_sort_ratio

match_conditions = {
    "awardTitle": partial_ratio,
    "hasAwardedForWork": partial_ratio,
    "hasPlace": partial_ratio,
    "hasStartDate": partial_ratio,
    "wasConferredBy": partial_ratio
}
