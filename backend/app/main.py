from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    """handler for home route

    Returns:
    -------
        greetings
    """
    return {
        "message": "Hello World"
    }
