from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# allows CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
  return {"message": "Welcome to REsentiment!"}

class Company(BaseModel):
  company_name: str

@app.post("/analysis")
async def analyze_company(request: Company):
  print("here")
  company = request.company_name

  #scrap web data about company's rebranding

  #analyze sentiment of scraped data
  sentiment = {"label": "awful", "score": 0.1}

  return {"company": company, "sentiment": sentiment}