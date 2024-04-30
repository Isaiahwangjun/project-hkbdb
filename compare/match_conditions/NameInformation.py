from match_conditions.fuzzf import completely, partial_ratio, token_sort_ratio

match_conditions = {
    "nnBestKnownName": completely,
    "hao": token_sort_ratio,
    "joinPenName": token_sort_ratio,
    "originalName": completely,
    "penName": token_sort_ratio,
    "zi": token_sort_ratio
}
