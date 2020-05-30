from FileLoader import FileLoader
import pandas


def YoungestFellah(df, year):
    """
    The function returns a dictionary containing
    the age of the youngest woman and man who took
    part in the Olympics on that year.
    The name of the dictionary’s keys is up to you,
    but it must be self-explanatory.
    """
    if not isinstance(year, int):
        return None
    if not isinstance(df, pandas.core.frame.DataFrame):
        return None
    dico = {}
    Filter = df["Year"] == year
    FilterM = df['Sex'] == "M"
    FilterF = df['Sex'] == "F"
    dico["M"] = df['Age'].where(FilterM & Filter).min()
    dico["F"] = df['Age'].where(FilterF & Filter).min()
    return dico


if __name__ == "__main__":
    FL = FileLoader()
    df = FL.load("../athlete_events.csv")
    dico = YoungestFellah(df, 1920)
    print(dico)
