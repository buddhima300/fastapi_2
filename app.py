from http.client import HTTPException
import uvicorn
from fastapi import FastAPI
import joblib
# import the coursesdata class to get the schema
from CourseData import CourseData
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('coursera.csv')

app = FastAPI()

# Load the pre-trained model
joblib_in = open("courses_recommender.joblib", "rb")
model = joblib.load(joblib_in)



@app.get('/')
def index():
    # return {print(df)}
    return {'message': 'Best university courses recommendation machine learning API'}

# @app.post("/university/predict")
# def predict_university(request: CourseData):
#     if not request.course_name or not request.university:
#         raise HTTPException(status_code=400, detail="Course name and university must be provided")
    
#     if request.course_name == "Finance for Managers" and request.university == "University D":
#         return {"prediction": "Top 10% university for this course"}
#     else:
#         return {"prediction": "Not in top 10%"}
    
@app.post("/university/predict")
def predict_university(request: CourseData):
    if not request.course_name:
        raise HTTPException(status_code=400, detail="Course name must be provided")
    
    if request.course_name == "Finance":
        return {"prediction": "Michigan University Top 10% university for this course"}
    elif request.course_name == "Accounting":
        return {"prediction": "Standford University is Top 10% university for this course"}
    elif request.course_name == "Programming":
        return {"prediction": "University of California is Top 10% university for this course"}
    else:
        return {"prediction": "Not in top 10%"}
    

    
courses_universities = {
    "Finance for Managers": "Michigan University",
    "Data Science": "Standford University",
    "Machine Learning": "University of California"
    "Hacking and Patching:""University of Colorado System"
    "Python Programming:""Rice University"
}

@app.get("/university")
def top_university(course_name: str):
    # Check if the course_name exists in the dictionary
    
    if course_name in courses_universities:
        return {
            "course_name": course_name,
            "top_university": courses_universities[course_name]
            }
    else:
        # Return an error if the course is not found
        raise HTTPException(status_code=404, detail="Course not found")
  


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
