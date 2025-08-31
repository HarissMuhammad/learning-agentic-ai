from fastapi import FastAPI

mcp_app = FastAPI()


@mcp_app.get("/")
async def root():
    return {"message": "Hello World"}

