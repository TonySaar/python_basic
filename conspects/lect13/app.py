from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {'message': "Hello World!"}

@app.get('/{user_id}/friends')
def get_friends(user_id: int)
    return {
        "id":user_id
    }