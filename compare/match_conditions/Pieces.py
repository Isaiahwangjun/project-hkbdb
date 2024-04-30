from match_conditions.fuzzf import completely, partial_ratio, token_sort_ratio

match_conditions = {
    "rdfs:label": partial_ratio,
    "hasRelatedPerson": partial_ratio,
    "hasStartDate": partial_ratio,
    "otherWorkType": partial_ratio,
    "hasRelatedOrganization": partial_ratio
}
