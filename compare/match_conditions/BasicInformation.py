from match_conditions.fuzzf import completely, partial_ratio, token_sort_ratio

match_conditions = {
    "bestKnownName": completely,
    "deathAge": partial_ratio,
    "deathCause": partial_ratio,
    "disable": partial_ratio,
    "displayRetireDate": partial_ratio,
    "gender": completely,
    "hao": token_sort_ratio,
    "hasBirthDate": partial_ratio,
    "hasDeathDate": partial_ratio,
    "hasNationality": partial_ratio,
    "hasNativePlace": partial_ratio,
    "hasPlaceOfBirth": partial_ratio,
    "hasPlaceOfBuried": partial_ratio,
    "hasPlaceOfDeath": partial_ratio,
    "illness": token_sort_ratio,
    "joinPenName": token_sort_ratio,
    "occupation": token_sort_ratio,
    "originalName": completely,
    "penName": token_sort_ratio,
    "reputation": partial_ratio,
    "researchArea": partial_ratio,
    "zi": token_sort_ratio
}
