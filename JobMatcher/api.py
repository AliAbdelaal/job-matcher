from typing import Optional
from JobMatcher.nlp import Matcher

from fastapi import FastAPI

app = FastAPI()
matcher = Matcher()

@app.get("/")
def check():
    return {"status": "Working !"}


@app.get("/jobs/")
def get_jobs(query: str):
    jobs = matcher.get_top_similar(query)
    return {
        "query": query,
        "similar_jobs": jobs,
        "most_similar" : jobs[0]
    }