from fastapi import FastAPI

app = FastAPI()

patentes = {
  1: "AAAA000",
  2: "AAAA001",
  3: "AAAA002",
}

@app.get("/id/{pat_id}")
def read_id(pat_id: int, ): 
    p = patentes[pat_id] 
    return {"pat_id": pat_id, "patente": p}


@app.get("/patente/{patente}")
def read_pat(patente: str):
    pat = [k for k, v in patentes.items() if v == patente][0]
    return {"pat_id": pat, "patente": patente}