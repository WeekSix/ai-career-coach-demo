import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

print("正在列出可用模型...")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"可用模型名称: {m.name}")