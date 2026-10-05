from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to swiggy Order service", "status": "healthy"}

# Whatever we are doing in terminal for running the server with uvicorn, we can do in programmitical way also.
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    
