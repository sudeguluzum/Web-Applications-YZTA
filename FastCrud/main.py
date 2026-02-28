from fastapi import FastAPI, Body

app = FastAPI()

courses_db = [
    {'id': 1, 'instructor': 'Sude', 'title': 'Python', 'category': 'Development'},
    {'id': 2, 'instructor': 'Aylin', 'title': 'Java', 'category': 'Backend'},
    {'id': 3, 'instructor': 'Sude', 'title': 'Deep Learning', 'category': 'AI'},
    {'id': 4, 'instructor': 'Edis', 'title': 'Machine Learning', 'category': 'AI'},
    {'id': 5, 'instructor': 'Zeynep', 'title': 'Javascript', 'category': 'Development'},
    {'id': 6, 'instructor': 'Ayşe', 'title': 'HTML', 'category': 'Frontend'}

]


# endpoint
@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


@app.get("/courses")
async def get_all_courses():
    return courses_db


# Path Parameter
@app.get("/courses/{course_title")
async def get_course(course_title: str):
    for course in courses_db:
        if course.get('title').casefold() == course_title.casefold():
            return course


@app.get("/courses/{course_id") #bu kod url'den dolayı çalışmaz
async def get_course_by_id(course_id: str):
    for course in courses_db:
        if course.get('id') == course_id:
            return course


@app.get("/courses/byid/{course_id") #url böyle yazılırsa çalışır
async def get_course_by_id(course_id: int):
    for course in courses_db:
        if course.get('id') == course_id:
            return course


#Query
@app.get("/courses/")
async def get_category_by_query(category: str):
    courses_to_return = []
    for course in courses_db:
        if course.get('category').casefold() == category.casefold():
            courses_to_return.append(course)
    return courses_to_return

# Path ve Query ile 2li sorgu
@app.get("/courses/{course_instructor}/")
async def get_instructor_category_by_query(course_instructor: str, category: str):
    courses_to_return = []
    for course in courses_db:
        if (course.get('instructor').casefold() == course_instructor.casefold()
                and course.get('category').casefold() == category.casefold()):
            courses_to_return.append(course)
    return courses_to_return


# POST
@app.post("/courses/create_course")
async def create_course(new_course=Body()):
    courses_db.append(new_course)


# PUT
@app.put("/courses/update_course")
async def update_course(updated_course=Body()):
    for index in range(len(courses_db)):
        if courses_db[index].get("id") == updated_course.get("id"):
            courses_db[index]= updated_course



# UPDATE
@app.delete("/courses/delete_course/{course_id}")
async def delete_course(course_id: int):
    for index in range(len(courses_db)):
        if courses_db[index].get("id") == course_id:
            courses_db.pop(index)
            break