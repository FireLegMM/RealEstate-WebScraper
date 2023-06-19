import pandas as pd
import json
from sqlalchemy import create_engine
import os
import pathlib

engine = create_engine("postgresql://airflow:airflow@localhost:5432/realestate")
path = pathlib.Path(str(pathlib.Path(__file__).parent.resolve()) + "/data/")
df_lst = []

for file in os.listdir(path):
    with open(pathlib.Path(str(path) + "/" + file), mode="r", encoding="utf-8") as data:
        data = data.read()
    lst = json.loads(data)

    for i in lst:
        id = i["id"]
        city = i["location"]["address"]["city"]["name"]
        area = i["areaInSquareMeters"]
        transaction = i["transaction"]
        estate_type = i["estate"]
        import_date = file[5:13]

        if i["totalPrice"] == None:
            value = None
            curr = None
        else:
            value = i["totalPrice"]["value"]
            curr = i["totalPrice"]["currency"]
        if ((i["rentPrice"] == None), (i["rentPrice"] == i["totalPrice"])):
            rent_value = None
        else:
            rent_value = i["totalPrice"]["value"]
        df_lst.append(
            [
                id,
                city,
                area,
                value,
                curr,
                rent_value,
                transaction,
                estate_type,
                import_date,
            ]
        )

df = pd.DataFrame(df_lst)
df.columns = [
    "id",
    "city",
    "area",
    "value",
    "currency",
    "rent_value",
    "transaction",
    "estate_type",
    "import_date",
]
df["import_date"] = df["import_date"].astype("datetime64[ns]")

df.to_sql("data", con=engine, if_exists="replace")
