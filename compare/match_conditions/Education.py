from match_conditions.fuzzf import completely, partial_ratio, token_sort_ratio

match_conditions = {
    "hasAcademicDegree": partial_ratio,
    "hasAcademicDiscipline": partial_ratio,
    "hasEducatedAt": partial_ratio,
    "hasStartDate": partial_ratio,
    "hasEndDate": partial_ratio,
    "hasPlace": partial_ratio,
}
