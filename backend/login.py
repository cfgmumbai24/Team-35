# from fastapi import FastAPI, Form, HTTPException, Request
# from fastapi.responses import RedirectResponse
# from fastapi.templating import Jinja2Templates

# app = FastAPI()
# templates = Jinja2Templates(directory="templates")

# # Hardcoded user data
# users = {
#     "Sinjini": "cfg#35"
# }

# @app.get("/")
# async def read_root():
#     return {"message": "Welcome to the user authentication system"}

# @app.get("/login")
# async def login_form(request: Request):
#     return templates.TemplateResponse("login.html", {"request": request})

# @app.post("/login")
# async def login(username: str = Form(...), password: str = Form(...)):
#     if username in users and users[username] == password:
#         return {"message": "Login successful"}
#     else:
#         return RedirectResponse(url="/signup", status_code=302)

# @app.get("/signup")
# async def signup_form(request: Request):
#     return templates.TemplateResponse("signup.html", {"request": request})

# @app.post("/signup")
# async def signup(username: str = Form(...), password: str = Form(...)):
#     if username in users:
#         raise HTTPException(status_code=400, detail="User already exists")
#     users[username] = password
#     return {"message": "Signup successful"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
