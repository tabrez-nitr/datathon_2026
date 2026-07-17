FROM python:3.12-slim 
# base environment lightweight python image 
WORKDIR /app 
#set working directory insside container to /app here evrythign will be coppied 

COPY requirements.txt .
# Copy the dependencies file first to leverage Docker's layer caching

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 
# copy the rest of the application code here 

CMD ["uvicorn","main:app" , "--host","0.0.0.0", "--port","8000", "--reload"]

