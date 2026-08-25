from fastapi import FastAPI


app = FastAPI(
    title="ShopIt",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "ShopIt API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}