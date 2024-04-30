from match_conditions.fuzzf import completely, partial_ratio, token_sort_ratio

match_conditions = {
    "rdfs:label": partial_ratio,
    "hasGenre": partial_ratio,
    "column": partial_ratio,
    "hasAuthor": completely,
    "hasDescribedTarget": partial_ratio,
    "hasInceptionDate": partial_ratio,
    "hasPublisher": partial_ratio,
    "hasReserved": token_sort_ratio,
    "hasEditor": token_sort_ratio,
    "hasBookIncription": token_sort_ratio,
    "hasBookPrefacer": token_sort_ratio,
    "hasBookTitle": token_sort_ratio,
    "hasContributor": token_sort_ratio,
    "hasTranslator": token_sort_ratio,
    "issue": completely,
    "penName": completely,
    "period": partial_ratio
}
