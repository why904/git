from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/users")
def get_users():
    return [
        {"id":1,"name":"张三"},
        {"id":2,"name":"李四"},
        {"id":3,"name":"王五"},
    ]
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)