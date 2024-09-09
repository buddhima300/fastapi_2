from typing import Optional
from pydantic import BaseModel
import joblib

# Load the pre-trained model
joblib_in = open("courses_recommender.joblib", "rb")
model = joblib.load(joblib_in)

class CourseData(BaseModel):
  course_name: str
  university: Optional[str] = None