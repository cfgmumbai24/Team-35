from language import transcribe, translation, text_to_speech
import json

async def update_json_values(data, language):
    try:
        print(f"\n\nData:\n{data}\n\nLanguage:{language}\n\n")
        if isinstance(data, dict):
            return {key: await update_json_values(value, language) for key, value in data.items()}
        elif isinstance(data, list):
            return [await update_json_values(item, language) for item in data]
        elif isinstance(data, str):
            text = await translation("English", language, data)
            print(f"\n\ntext: {text}\n\n")
            return text['translated_content']
        else:
            print(f"\n\nInside Else Data:\n{data}")
            return data
    except Exception as e:
        print(f"\n\nError:{e}\n\n")
        return e