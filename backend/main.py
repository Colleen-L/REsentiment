from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from scraper import scrape
from sentiment import analyze_sentiment

app = FastAPI()

# allows CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
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
  headlines = scrape(company)

  #analyze sentiment of scraped data
  results = []
  total_score = 0

  for item in headlines:
      sentiment = analyze_sentiment(item["title"])
      total_score += sentiment["score"]
      results.append({
          "title": item["title"],
          "url": item["url"],
          "sentiment": sentiment
        })
      
  average_score = total_score / len(results) if results else 0
  overall_label = (
      "positive" if average_score >= 0.05 else
      "negative" if average_score <= -0.05 else
      "neutral"
  )

  return {
    "company": company,
    "headlines": results,
    "sentiment": {
        "label": overall_label,
        "score": round(average_score, 3)
    }
  }