from ast import Str
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    patente: str
    id1: float

app = FastAPI()

patentes = {
  1: "AAAA000",
  2: "AAAA001",
  3: "AAAA002",
  4: "AAAA003",
  5: "AAAA004",
  6: "AAAA005",
  7: "AAAA006",
  8: "AAAA007",
  9: "AAAA008",
  10: "AAAA009",
  11: "AAAA010"
}

@app.get("/id/{pat_id}")
def read_id(pat_id: int, ): 
    p = patentes[pat_id] 
    return {"pat_id": pat_id, "patente": p}


@app.get("/patente/{patente}")
def read_pat(patente: str):
    pat = [k for k, v in patentes.items() if v == patente][0]
    return {"pat_id": pat, "patente": patente}


@app.put("/id/{pat_id}")
def read_pat(patente: str):
    pat = [k for k, v in patentes.items() if v == patente][0]
    return {"pat_id": pat, "patente": patente}