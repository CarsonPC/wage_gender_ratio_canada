import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('wage_edu_data.csv')

    cols_to_remove = ["Age group", "Type of work", "Both Sexes", "Wages", "Education level"]
    df.drop(cols_to_remove, axis=1, inplace=True)

    # remove whitespace
    df.columns = df.columns.str.strip()
    df["Geography"] = df["Geography"].str.strip()
    # remove rows where either male or female are 0.0
    df = df[df["Geography"] != "Manitoba"]
    df = df[df["Geography"] != "New Brunswick"]
    df = df[df["Geography"] != "Newfoundland and Labrador"]
    df = df[df["Geography"] != "Nova Scotia"]
    df = df[df["Male"] != 0.0]
    df = df[df["Female"] != 0.0]
    df['Ratio'] = df['Male'] / df['Female']

    gp = df.groupby(["YEAR", "Geography"], as_index = False).mean()
    # pyplot stuff
    gp.set_index(gp["YEAR"], inplace = True)
    gp.groupby("Geography")["Ratio"].plot(legend=True)
    plt.xticks(gp.index, gp["YEAR"], rotation = 90)
    plt.title("Ratio of Men's Wage to Women's Wage")
    plt.show()


