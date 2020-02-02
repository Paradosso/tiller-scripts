import fire
import pandas as pd
import datetime as dt
from functools import partial


class AppleStatement:

    def __init__(self, *args):
        parse_apple_statement = partial(pd.read_csv,
                                        usecols=["Transaction Date", "Merchant", "Category", "Description",
                                                 "Amount (USD)"],
                                        dtype={"Transaction Date": "str", "Merchant": "str", "Category": "str",
                                               "Description": "str", "Amount (USD)": "float32"},
                                        parse_dates=["Transaction Date"])
        dfs = (parse_apple_statement(f) for f in args)
        self.input = pd.concat(dfs)

    def head(self):
        print(self.input.head())
        print(self.input.dtypes)

    def tillerize(self, output, last4="1234"):
        df = pd.DataFrame(
            columns="""Tiller Date Description Category Amount Account Account_Number Institution
            Month Week Transaction_ID Check_Number Full_Description	Date_Added""".split()
        )
        df["Tiller"] = ""
        df["Date"] = self.input["Transaction Date"]
        df["Description"] = self.input["Merchant"]
        df["Category"] = self.input["Category"]
        df["Amount"] = self.input["Amount (USD)"].apply(func=lambda x: round(x, 2) * -1)
        df["Account"] = "CREDIT CARD"
        df["Account_Number"] = "xxxx" + str(last4)
        df["Institution"] = "Apple"
        df["Month"] = df["Date"].apply(func=lambda d: d.replace(day=1))
        df["Week"] = df['Date'] - pd.to_timedelta(arg=df['Date'].dt.weekday, unit='D')
        df["Transaction_ID"] = ""
        df["Full_Description"] = self.input["Description"]
        df["Date_Added"] = pd.to_datetime(dt.date.today())

        print(df.head())
        df.to_csv(path_or_buf=output,
                  index=False,
                  date_format='%m/%d/%Y')


if __name__ == '__main__':
    fire.Fire(AppleStatement)
