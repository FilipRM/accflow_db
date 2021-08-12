
from fastapi import FastAPI, File, UploadFile, Path, Query
from typing import Optional
import io
import pandas as pd

app = FastAPI()


@app.post("/csv/")
async def create_upload_file(csv_file: UploadFile = File(...)):
    if csv_file.filename[-4:] == ".csv":
        raw_data = csv_file.file.read().decode("utf-8")
        temp_data = io.StringIO(raw_data)
        data = pd.read_csv(temp_data, sep = ",",
                           names=["Amount", "Balance"])
        return {"filename": csv_file.filename}
    else:
        return "Error, invalid file"

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    item_id: int, base_2_4: Optional[float] = None, lower_1_3: Optional[float] = None, upper_1_3: Optional[float] = None
):
    #henter de riktige tallene gjennom rules-modulen
    return