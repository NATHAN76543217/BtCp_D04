import pandas


class FileLoader():
    def __init__(self):
        pass

    def load(self, path):
        """
        takes as an argument the file path of
        the dataset to load, displays a message specifying the
        dimensions of the dataset (e.g. 340 x 500)
        and returns the dataset loaded as a pandas.DataFrame.
        """
        df = pandas.read_csv(path)
        print(
            "Loading dataset of dimensions {} x {}\n"
            .format(df.shape[0], df.shape[1]))
        return df

    def display(self, df, n):
        """
        takes a pandas.DataFrame and an integer as arguments,
        displays the first n rows of the dataset if n is positive,
        or the last n rows if n is negative.
        """
        if n > 0:
            print(df.head(n))
        else:
            print(df.tail(n))


if __name__ == "__main__":
    FL = FileLoader()
    df = FL.load("../athlete_events.csv")
    FL.display(df, 10)
