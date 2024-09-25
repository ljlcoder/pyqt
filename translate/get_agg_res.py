import re
import pandas as pd

def get_agg_res(text):
    words=re.split(r"^[A-Za-z0-9\s!,?\(\)\|]+$",text)
    words=[w.lower() for w in words if len(w)>2]
    df=pd.DataFrame({"word":words})
    df_agg=df["word"].value_counts()
    return df_agg


if __name__=="__main__":
    res=get_agg_res("Hello, world! This is a sample text. What's your name? (Optional question) | Another segment | Or this one.")
    print(res)