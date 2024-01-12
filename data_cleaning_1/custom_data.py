# extract required columns and load table into postgresql database

import pandas as pd
import json
from sqlalchemy import create_engine


def custom_data(custom_list, file):
    print("Extracting custom data ...")
    df = pd.read_csv(file)
    field = df.columns[2]

    df_custom_data = []
    for text in custom_list:
        # filtered_df = df[df[field].str.contains(text, case=False, na=False)]
        filtered_df = df[df[field].str.contains(text, na=False)]
        df_custom_data.append(filtered_df)

    df_custom_data = pd.concat(df_custom_data)
    print("Custom data successfully extracted.")
    df_custom_data.to_csv('my_custom_data.csv', index=False)
    return df_custom_data


def extract_json(df):
    print("Creating json file ...")
    df_groups = df.groupby("SystemId")
    custom_data = []
    for key, sub_df in df_groups:
        df_subgroups = sub_df.groupby("INDEX")
        try:
            for index, req_df in df_subgroups:
                pd.set_option("display.max_columns", None)

                req_df.set_index('FIELD', inplace=True)
                data = {
                    "SystemId": key,
                    "Index": index
                }
                for text in custom_list:
                    value = req_df.loc[text]['VALUE']
                    data[text] = value

                custom_data.append(data)
        except:
            pass

    with open('custom_data.json', "w", encoding='utf-8') as file:
        json.dump(custom_data, file)

    print("Json file successfully created.")


def load_to_database(file, db_url):
    print("Creating Table ...")
    df = pd.read_json(file)
    engine = create_engine(db_url)

    with engine.connect() as conn:
        df.to_sql('my_table', con=engine, if_exists='replace')
        conn.commit()

    print("Table successfully created.")


if __name__ == "__main__":
    custom_list = ["Organic_Title", "Organic_LandingLink", "Organic_ReviewCount",
                   "Organic_Price", "Organic_Rating"]
    
    # postgresql://user:password@host:port/database
    db_url = "postgresql://postgres:1234@localhost:5432/task"

    df_custom_data = custom_data(custom_list, "my_custom_data.csv")
    extract_json(df_custom_data)
    load_to_database('custom_data.json', db_url)
