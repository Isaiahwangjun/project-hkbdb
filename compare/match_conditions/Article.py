from match_conditions.fuzzf import completely, partial_ratio, token_sort_ratio

match_conditions = {
    "label_article": partial_ratio,
    "hasAuthor": completely,
    "hasDescribedTarget": partial_ratio,
    "hasGenre": partial_ratio,
    "hasInceptionDate": partial_ratio,
    "hasPublishedIn": partial_ratio,
    "hasTranslator": completely,
    "owner": partial_ratio,
    "penName": completely,
    "publishYear": partial_ratio
}
