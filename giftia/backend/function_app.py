# function_app.py — Azure Functions の入口
#
# 今ある FastAPI のアプリ（main.py の app）を、Azure Functions の HTTP の入口につなぐだけのファイル。
# main.py は変えない。ローカルの動かし方（uvicorn main:app --reload）もこれまでどおり。
import azure.functions as func

from main import app as fastapi_app

app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)
