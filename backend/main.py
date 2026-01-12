from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas


models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Invoice Recovery Case Tracker")


def get_db():
db = SessionLocal()
try:
yield db
finally:
db.close()

@app.post("/clients", status_code=201)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
db_client = models.Client(**client.dict())
db.add(db_client)
db.commit()
db.refresh(db_client)
return db_client


@app.get("/clients")
def list_clients(db: Session = Depends(get_db)):
return db.query(models.Client).all()


@app.post("/cases", status_code=201)
def create_case(case: schemas.CaseCreate, db: Session = Depends(get_db)):
client = db.query(models.Client).filter(models.Client.id == case.client_id).first()
if not client:
raise HTTPException(status_code=400, detail="Invalid client ID")
db_case = models.Case(**case.dict())
db.add(db_case)
db.commit()
db.refresh(db_case)
return db_case

@app.get("/cases")
def list_cases(status: str | None = None, sort: str | None = None, db: Session = Depends(get_db)):
query = db.query(models.Case)
if status:
query = query.filter(models.Case.status == status)
if sort == "asc":
query = query.order_by(models.Case.due_date.asc())
elif sort == "desc":
query = query.order_by(models.Case.due_date.desc())
return query.all()


@app.get("/cases/{case_id}")
def get_case(case_id: int, db: Session = Depends(get_db)):
case = db.query(models.Case).filter(models.Case.id == case_id).first()
if not case:
raise HTTPException(status_code=404, detail="Case not found")
return case

@app.patch("/cases/{case_id}")
def update_case(case_id: int, update: schemas.CaseUpdate, db: Session = Depends(get_db)):
case = db.query(models.Case).filter(models.Case.id == case_id).first()
if not case:
raise HTTPException(status_code=404, detail="Case not found")
for key, value in update.dict(exclude_unset=True).items():
setattr(case, key, value)
db.commit()
db.refresh(case)
return case