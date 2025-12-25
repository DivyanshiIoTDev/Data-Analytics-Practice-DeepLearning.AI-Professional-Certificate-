def normalize(series):
    """
    Normalize a pandas Series to the range [0, 1].
    Args:
        series (pd.Series): The series to normalize.
    Returns:
        pd.Series: The normalized series.
    """
    return (series - series.min()) / (series.max() - series.min())