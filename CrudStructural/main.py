from fastapi import FastAPI, Body, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


class Course:
    id: int
    title: str
    instructor: str
    rating: int
    published_date: int

    def __init__(self, id: int, title: str, instructor: str, rating: int, published_date: int):
        self.id = id
        self.title = title
        self.instructor = instructor
        self.rating = rating
        self.published_date = published_date

#Kendi body'imizi oluşturmak için
class CourseRequest(BaseModel):
    id: Optional[int]= Field(description="The id of the course", default=None)
    title: str = Field(min_length=3, max_length=100)
    instructor: str = Field(min_length=3)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gte=2014, lte=2030)

    model_config = {  #opsiyonel
        "json_schema_extra": {
            "example": {
                "title": "Akademesi",
                "instructor": "sude",
                "rating": 5,
                "published_date": 2020,
            }
        }
    }

courses_db = [
    Course(1, "Python", "Sude", 5, 2025),
    Course( 2, "Machine Learning", "Emine", 3, 2024),
    Course(3, "Python", "Atıl",  4,  2025),
    Course(4, "Deep Learning","Emine",  4,  2025),
    Course(5, "Vue",  "Sude", 5,  2024),
    Course(6, "Jira",  "Gökçe",  5,  2022),
]

# endpoints
@app.get("/courses", status_code=status.HTTP_200_OK)
async def get_all_courses():
    return courses_db


# Path İşlemleri
@app.get("/courses/{course_id}", status_code=status.HTTP_200_OK)
async def get_course(course_id: int = Path(gt=0)):  #greater than 0'dan büyük, lt=3 less than 3'den küçük
    for course in courses_db:
        if course.id == course_id:
            return course
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")


# Query İşlemleri
@app.get("/courses/", status_code=status.HTTP_200_OK)
async def get_courses_by_rating(course_rating: int = Query(gt=0, lt=6)):
    courses_to_return=[]
    for course in courses_db:
        if course.rating == course_rating:
            courses_to_return.append(course)
    return courses_to_return


@app.get("/courses/publish/", status_code=status.HTTP_200_OK)
async def get_courses_by_publish_date(published_date: int = Query(gt=2016, lt=2030)):
    courses_to_return=[]
    for course in courses_db:
        if course.published_date == published_date:
            courses_to_return.append(course)
    return courses_to_return



#Pydantic İstekler

# Yeni kurs oluşturma
@app.post("/create-course", status_code=status.HTTP_201_CREATED)
async def create_course(course_request: CourseRequest):
    new_course = Course(**course_request.model_dump())
    courses_db.append(find_course_id(new_course))

def find_course_id(course: Course):
    course.id = 1 if len(courses_db) == 0 else courses_db[-1].id + 1
    return course


# Güncelleme
@app.put("/courses/update_course", status_code=status.HTTP_204_NO_CONTENT)
async def update_course(course_request: CourseRequest):
    course_updated = False
    for i in range(len(courses_db)):
        if courses_db[i].id == course_request.id:
            courses_db[i] = course_request
            course_updated=True
    if not course_updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")



# Sil
@app.delete("/courses/delete/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int= Path(gt=0)):
    course_deleted= False
    for i in range(len(courses_db)):
        if courses_db[i].id == course_id:
            courses_db.pop(i)
            course_deleted=True
            break
    if not course_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")