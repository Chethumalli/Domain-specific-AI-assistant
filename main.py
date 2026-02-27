from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from llm_layer import generate_response
from prompt_router import build_prompt

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# ✅ HOME ROUTE
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ✅ ASK ROUTE
@app.post("/ask", response_class=HTMLResponse)
async def ask(request: Request, domain: str = Form(...), user_input: str = Form(...)):
    try:
        prompt = build_prompt(domain, user_input)
        response = generate_response(prompt)
    except Exception as e:
        response = f"Server Error: {str(e)}"

    return templates.TemplateResponse("index.html", {
        "request": request,
        "response": response
    })