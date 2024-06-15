from fastapi import FastAPI,File,UploadFile,Form, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from language import translation, transcribe, text_to_speech
from chatbot import ask_llm
from update_lang import update_json_values

import json

app = FastAPI()

@app.post('/chat_text')
async def chat_text(message: str = Form(...), language: str = Form(...)):
    try: 
        language = language
        message = message
        message_english = await translation(language, "English", message)
        message_english_text = message_english['translated_content']
        print(f"Message:\n{message_english_text}")
        answer = await ask_llm(message_english_text)
        answer_translate = await translation("English", language, answer)
        answer_translate_text = answer_translate['translated_content']
        return JSONResponse(content={"message": answer_translate_text, "success": True}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"message": "Error in running chat_text", "success": False}, status_code=500)
    

@app.post('/prefetch_login')
async def prefetch_login(language: str = Form(...)):
    try:
        f = open('static_data.json')
        print(f)
        data = json.load(f)
        lang_data = await update_json_values(data, language)
        print(data)
        return JSONResponse(content={"message": lang_data, "success": True}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"message": "Failed during trying prefetch_login", "success": False}, status_code=500)

# /fetch_pre_login
# /post_login