from fastapi import APIRouter
from models import Plan
from sqlmodel import select
from db import SessionDep
router = APIRouter()

@router.post("/plans", tags=["plans"])
def create_plan(plan_data: Plan, session: SessionDep):
  plan_db = Plan.model_validate(plan_data.model_dump())
  session.add(plan_db)
  session.commit()
  session.refresh(plan_db)
  return plan_db 


@router.get("/plans", response_model=list[Plan], tags=["plans"])
def list_plan(session: SessionDep):
 plan = session.exec(select(Plan)).all()
 return plan
