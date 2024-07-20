import os, shutil
from get_pix import get_image
from fastapi import FastAPI, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
app = FastAPI()

# Access the form at 'http://127.0.0.1:8000/' from your browser
@app.get('/')
async def main():
    content = '''
    <body>
    <form action='/uploadfile/' enctype='multipart/form-data' method='post'>
    <input name='file' type='file'>
    <input type='submit'>
    </form>
    </body>
    '''
    return HTMLResponse(content=content)

@app.post("/uploadfile/")
async def create_upload_file(file:UploadFile):
    upload_dir = os.path.join(os.getcwd(), "uploads")
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    dest = os.path.join(upload_dir, file.filename)
    with open(dest, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    white_pix_count, black_pix_count = get_image(dest)
    if white_pix_count > black_pix_count:
        winner = "Больше белых"
    elif black_pix_count > white_pix_count:
        winner = "Больше черных"
    else:
        winner = "Равны"


    content = f"""
        <p>Белые пиксели {white_pix_count}</p>
        <p>Черные пиксели {black_pix_count}</p>
        <p>{winner}</p>"""

    return HTMLResponse(content=content)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1",port=8000, log_level="info", reload=True)