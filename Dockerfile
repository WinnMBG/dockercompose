FROM python:3.8

WORKDIR app

COPY . .

RUN pip install cmake
RUN pip install -r requirements.txt
RUN pip install "uvicorn[all]"

EXPOSE 8000

ENTRYPOINT ["uvicorn","app:app","--host","0.0.0.0","--port","8000","--reload"]
