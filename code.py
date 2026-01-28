
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes

# 1. Load environment variables
load_dotenv()
api_key = os.getenv(API_KEY)

# Safety Check: This will print in your terminal so you can see if the key exists
if not api_key:
    print("ERROR: GOOGLE_API_KEY not found in .env file!")
else:
    print("API Key detected. Starting server...")


# 2. Define the model and prompt
# Passing google_api_key=api_key directly fixes the Pydantic ValidationError
model = ChatGoogleGenerativeAI(
    model="<LLM_Model>,
    api_key1=api_key
)

chain = model

# 3. App definition
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LLM",
)

# 4. Add the route
add_routes(
    app,
    chain,
)

# 5. Run the server
if __name__ == "__main__":
    import uvicorn
    # Changed host to 127.0.0.1 for better Windows compatibility
    uvicorn.run(app, host="0.0.0.0", port=8000)

