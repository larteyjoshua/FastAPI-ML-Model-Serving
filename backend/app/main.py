from fastapi import FastAPI,HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

from app.schemas.schema import GenerateMLImage
from app.modelServices.imageModelService import generateImage

app = FastAPI(title= 'ML Model Serving API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/image/generate")
async def generate_synthetic_image(request:GenerateMLImage):
    if request.textPrompt is None:
         raise HTTPException(status_code=418, detail="No Empty Message")
         
    # generating = generateImage(request.textPrompt)
    # return StreamingResponse(generating, media_type="image/png")
    return {"Hello": "World"}