from match_conditions.fuzzf import completely, partial_ratio, token_sort_ratio

match_conditions = {
    "rdfs:label": partial_ratio,
    "hasFounded": partial_ratio,
    "hasLocationOfFormation": partial_ratio,
    "hasParticipant": partial_ratio,
    "hasPlace": partial_ratio,
    "organizationType": partial_ratio,
    "activity": partial_ratio,
    "hasStartDate": partial_ratio,
    "hasEndDate": partial_ratio,
    "jobTitle": partial_ratio,
    "period": partial_ratio
}
