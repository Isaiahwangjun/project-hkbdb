from match_conditions.fuzzf import completely, partial_ratio, token_sort_ratio

match_conditions = {
    "rdfs:label": partial_ratio,
    "employmentType": partial_ratio,
    "jobTitle": partial_ratio,
    "hasEmployedAt": partial_ratio,
    "hasAlumni": partial_ratio,
    "hasStartDate": partial_ratio,
    "hasEndDate": partial_ratio,
    "column": partial_ratio,
    "hasGenre": partial_ratio,
    "hasColumnist": partial_ratio,
    "penName": partial_ratio,
    "period": partial_ratio,
    "activity": partial_ratio,
    "workingArea": partial_ratio
}
