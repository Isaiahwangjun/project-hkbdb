def diffDF(diff_df, key, GPT, HKBDB, score, source=None):

    row = {
        'key': key,
        'GPT': str(GPT),
        'HKBDB': str(HKBDB),
        'score': str(score)
    }
    if source is not None:
        row['source'] = source

    diff_df = diff_df._append(row, ignore_index=True)
    return diff_df


def onlyGPTorHKBDBhasDF(df, key, value, source=None):

    row = {'key': key, 'value': str(value)}

    if source is not None:
        row['source'] = source

    df = df._append(row, ignore_index=True)
    return df
