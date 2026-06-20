from dotenv import load_dotenv
import os

try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ImportError:
    from langchain.chat_models.google_palm import ChatGooglePalm as ChatGoogleGenerativeAI

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Get API key
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY not set in .env file")

# Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
    google_api_key=google_api_key
)

# =========================
# Chain 1: Extract City
# =========================

city_prompt = PromptTemplate(
    input_variables=["query"],
    template="""
You are a city extraction assistant.

Extract only the city name from the user query.

User Query:
{query}

Return only city name.
"""
)

city_chain = (
    city_prompt
    | llm
    | StrOutputParser()
)

# =========================
# Chain 2: Weather Summary
# =========================

summary_prompt = PromptTemplate(
    input_variables=[
        "city",
        "temperature",
        "feels_like",
        "humidity",
        "condition",
        "wind_speed",
        "pressure",
        "clouds",
        "visibility"
    ],
    template="""
Create a comprehensive and professional weather report for travel/planning purposes.

**Location:** {city}

**Temperature Details:**
- Current: {temperature}°C
- Feels Like: {feels_like}°C

**Atmospheric Conditions:**
- Humidity: {humidity}%
- Condition: {condition}
- Wind Speed: {wind_speed} m/s
- Pressure: {pressure} hPa
- Cloud Cover: {clouds}%
- Visibility: {visibility} m

Based on this data, provide:
1. **Weather Summary:** Brief overview of current conditions
2. **What to Expect:** How the weather will feel and any warnings
3. **Outdoor Activities:** Best activities for this weather
4. **Clothing Recommendation:** What to wear based on temperature and conditions
5. **Health Tips:** Any health-related recommendations (allergies, hydration, etc.)
6. **Travel Advisory:** Any travel recommendations based on conditions

Make the report engaging, informative, and practical.
""")

summary_chain = (summary_prompt | llm | StrOutputParser())