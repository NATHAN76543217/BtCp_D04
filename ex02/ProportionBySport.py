from FileLoader import FileLoader
import pandas


def proportionBySport(df, year, sport, gender):
    percent = float()
    FilterSport = df["Sport"] == sport
    FilterYear = df["Year"] == year
    FilterGender = df["Sex"] == gender

    df = df.where(FilterYear & FilterGender)
    df = df.dropna(how="all")
    df = df.drop_duplicates(subset=["Name"])

    TOT = df["Year"].value_counts()[year]
    df = df.where(FilterSport)
    df = df.dropna(how="all")
    STOT = df["Year"].value_counts()[year]

    percent = STOT / TOT
    return percent


if __name__ == "__main__":
    FL = FileLoader()
    df = FL.load("../athlete_events.csv")
    prop = proportionBySport(df, 2004, "Tennis", 'F')
    print("prop = ", prop)
    print()
    prop = proportionBySport(df, 2004, "Basketball", 'M')
    print("prop = ", prop)
