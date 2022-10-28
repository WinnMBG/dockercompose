from fastapi import FastAPI, Request;
from redis import Redis, RedisError;
import socket;
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Connect to Redis 
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def hello(request: Request):
	try:
		visites = redis.incr("compteur")
	except RedisError:
		visites = "Erreur de connection Redis, compteur desactive"
		   
	return templates.TemplateResponse("index.html",{"request": request, "nbVisites" : visites})
	
@app.get("/{id}/", response_class=HTMLResponse)
async def getpage(request: Request, id: int):
	if(id%2==0):
		return templates.TemplateResponse("index1.html",{"request": request})
	return templates.TemplateResponse("index2.html", {"request": request})

