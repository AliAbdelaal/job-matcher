# Job Matcher

A simple, quick yet powerful text based search engine to give you the most semantically similar job to your query.

The basic idea is to convert the input query to a vector using word2vec via spaCy, and then find the most similar job description vectors, rank them and pick the top jobs that are close to the input vector.

The data used in this project can be found on [Kaggle](https://www.kaggle.com/madhab/jobposts)

## Installation and usage

You can use the repo by creating a python virtual environment.

```bash
$python -m venv venv
```

Install the dependencies.

```bash
$pip install -r requirements.txt
```

You can then use the application.

```bash
$./run
```

## Notebook

The experiment notebook is available under [notebooks/](notebooks/) dir.

## example

Search for a `machine learning engineer` job, via requesting the url

`http://127.0.0.1:8000/jobs/?query=machine%20learning%20engineer`

you got the response

```json
{
query: "machine learning engineer",
similar_jobs: [
{
date: "Dec 29, 2011",
Title: "Data Scientist",
Company: "BigBek LLC",
.
.
.
},
{
date: "Mar 19, 2014",
Title: "Robotics Workshop Leader",
Company: "Tumo Center for Creative Technologies",
.
.
.
},
{
date: "Mar 28, 2008",
Title: "Software Performance Engineer",
Company: "Varnita Ltd",
.
.
.
},
{
date: "Aug 3, 2007",
Title: "Senior Mechanical Engineer/ Designer",
Company: "HT Euro, Inc.",
.
.
.
},
{
date: "Apr 28, 2004",
Title: "Mechanical Design Engineer",
Company: "ARQELL CJSC",
.
.
.
}
],
most_similar: {
date: "Dec 29, 2011",
Title: "Data Scientist",
Company: "BigBek LLC",
.
.
.
}
}
```
