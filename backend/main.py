from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Hardcoded user data
users = {
    "Sinjini": "cfg#35"
}


@app.get("/")
async def read_root():
    return {"message": "Welcome to the user authentication system"}

@app.get("/login")
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if username in users and users[username] == password:
        return {"message": "Login successful"}
    else:
        return RedirectResponse(url="/signup", status_code=302)

@app.get("/signup")
async def signup_form(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/signup")
async def signup(username: str = Form(...), password: str = Form(...)):
    if username in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[username] = password
    return {"message": "Signup successful"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# from fastapi import FastAPI, Form, HTTPException, Request
# from fastapi.responses import RedirectResponse
# from fastapi.templating import Jinja2Templates
# from pymongo import MongoClient
# from pymongo.errors import DuplicateKeyError

# app = FastAPI()
# templates = Jinja2Templates(directory="templates")

# # MongoDB connection URI (replace with your actual MongoDB URI)
# MONGO_URI = "mongodb+srv://sinjini:cfg35@cfgt35.u03jomy.mongodb.net/?retryWrites=true&w=majority"
# DATABASE = "cfg35_test"
# COLLECTION = "cfg"

# # MongoDB client
# client = MongoClient(MONGO_URI)
# db = client[DATABASE]
# collection = db[COLLECTION]

# @app.get("/")
# async def read_root():
#     return {"message": "Welcome to the user authentication system"}

# @app.get("/login")
# async def login_form(request: Request):
#     return templates.TemplateResponse("login.html", {"request": request})

# @app.post("/login")
# async def login(username: str = Form(...), password: str = Form(...)):
#     user = collection.find_one({"username": username, "password": password})
#     if user:
#         return {"message": "Login successful"}
#     else:
#         return RedirectResponse(url="/signup", status_code=302)

# @app.get("/signup")
# async def signup_form(request: Request):
#     return templates.TemplateResponse("signup.html", {"request": request})

# @app.post("/signup")
# async def signup(username: str = Form(...), password: str = Form(...)):
#     try:
#         # Insert new user into MongoDB
#         result = collection.insert_one({"username": username, "password": password})
#         return {"message": "Signup successful"}
#     except DuplicateKeyError:
#         raise HTTPException(status_code=400, detail="Username already exists")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)

