from FileLoader import FileLoader
import pandas


def howManyMedals(df, name):
    if not isinstance(name, str):
        return None
    dico = {}

    FilterName = df["Name"] == name
    df = df.where(FilterName)
    df = df.dropna(how="all")
    df = df.dropna(subset=["Medal"])
    df = df.drop_duplicates()
    cross = pandas.crosstab(df['Medal'], df["Year"])
    for year in cross:
        dico[int(year)] = {
            "G": cross[year][1], "S": cross[year][2], "B": cross[year][0]}
    return dico


if __name__ == "__main__":
    FL = FileLoader()
    df = FL.load("../athlete_events.csv")
    print(howManyMedals(df, 'Kjetil Andr Aamodt'))
