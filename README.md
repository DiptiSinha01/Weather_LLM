# 🌤️ Weather LLM Assistant

An AI-powered weather assistant built with Streamlit, LangChain and Google Gemini.

---

### Weather LLM Interface

Search any city worldwide to get real-time weather data, with quick stats for temperature, humidity, wind speed, and current conditions displayed in a clean card layout.


<img width="1600" height="839" alt="image" src="https://github.com/user-attachments/assets/00981fe1-6f86-4836-a615-56e3d5c33068" />

---
### AI Weather Report

Gemini generates a detailed, human-readable travel and planning advisory based on the live weather data — covering current conditions, what to expect, and practical recommendations.

<img width="1600" height="783" alt="image" src="https://github.com/user-attachments/assets/8ade8c7a-a5ab-401b-94c2-d7685227a776" />

---
### Detailed Information

A complete breakdown of raw weather data including location, atmospheric conditions (pressure, cloud cover, visibility), temperature details, wind direction/speed, and sunrise/sunset times.

<img width="1362" height="313" alt="image" src="https://github.com/user-attachments/assets/f5519007-1042-45a7-9be1-c9160a762cee" />




## 🎯 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure your API keys in .env file
# (Already configured with sample keys)

# 3. Run the application
streamlit run weather_llm/app.py
```

The app will open at `http://localhost:8501`

## ✨ Features

- 🌍 **Natural Language Processing**: Extract city names from conversational queries
- 📊 **Real-time Weather Data**: Fetch current weather from OpenWeatherMap API
- 🤖 **AI-Powered Reports**: Generate professional weather insights using Google Gemini
- 💨 **Comprehensive Metrics**: Display temperature, humidity, wind speed, pressure, and cloud coverage
- 🌐 **Global Coverage**: Works with any city worldwide

## 🏗️ Architecture

### Technology Stack
- **[Streamlit](https://streamlit.io/)** - Interactive web UI framework
- **[LangChain](https://langchain.com/)** - LLM orchestration
- **[Google Gemini](https://ai.google.dev/)** - Generative AI model
- **[OpenWeatherMap API](https://openweathermap.org/api)** - Weather data source
- **[Python Requests](https://requests.readthedocs.io/)** - HTTP client

### Components

```
weather_llm/
├── app.py           # Main Streamlit UI and application flow
├── chain.py         # LangChain setup and LLM configuration
└── weather_tool.py  # OpenWeatherMap API integration
```

#### app.py
- Streamlit interface with input field for queries
- Button to trigger weather fetch and report generation
- Display of formatted weather data and AI insights

#### chain.py
- LangChain configuration for LLM operations
- City extraction from user queries
- Report generation pipeline

#### weather_tool.py
- OpenWeatherMap API client
- Weather data parsing and formatting
- Error handling and logging

## 📋 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- API Keys (see below)

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get API Keys

#### OpenWeatherMap API Key
1. Visit [https://openweathermap.org/api](https://openweathermap.org/api)
2. Sign up for a free account
3. Navigate to API keys section
4. Copy your API key

#### Google Gemini API Key
1. Go to [https://aistudio.google.com/app/apikeys](https://aistudio.google.com/app/apikeys)
2. Click "Create API Key"
3. Copy the generated key

### 3. Configure Environment Variables

Create or update `.env` file with:

```env
WEATHER_API_KEY=your_openweather_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

### 4. Run the Application

```bash
streamlit run weather_llm/app.py
```

Open your browser to: **http://localhost:8501**

## 🚀 Usage

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies:**
- `streamlit==1.36.0` - Web framework
- `langchain==0.2.0` - LLM orchestration
- `langchain-google-genai==1.0.0` - Google Gemini integration
- `python-dotenv==1.0.0` - Environment variable management
- `requests==2.31.0` - HTTP requests
- `google-generativeai==0.5.0` - Google AI SDK
- `pydantic==2.0.0` - Data validation

### 2. Get API Keys

#### OpenWeatherMap API Key
1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Navigate to API keys section
4. Copy your API key (free tier includes current weather)

#### Google Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikeys)
2. Click "Create API Key"
3. Copy the generated API key (free tier available)

### 3. Configure Environment Variables

Update the `.env` file:

```env
# OpenWeatherMap API Key
WEATHER_API_KEY=your_openweather_api_key_here

# Google Gemini API Key
GOOGLE_API_KEY=your_google_api_key_here
```

### 4. Run the Application

```bash
streamlit run weather_llm/app.py
```

Browser opens at: http://localhost:8501

## 🚀 Usage

### Basic Usage
1. **Enter Query**: Type a natural language question about weather
2. **Click Button**: Press "🔎 Get Weather" button
3. **View Results**: See real-time weather data and AI-generated insights

### Example Queries
```
✅ "What's the weather in London today?"
✅ "Tell me about the weather in Tokyo"
✅ "Is it going to rain in New York tomorrow?"
✅ "What's the temperature in Berlin right now?"
✅ "What's the weather like in Paris?"
✅ "Should I bring an umbrella in Sydney?"
```

### Output Includes
- 🌡️ Current temperature and "feels like" temperature
- 💧 Humidity percentage
- 💨 Wind speed and direction
- ☁️ Cloud coverage
- 🌅 Sunrise and sunset times
- 📝 AI-generated weather recommendations

## 🎨 Interface Features

### Search Section
- Natural language query input
- Example queries for quick reference
- One-click query application

### Tips Section
- ✅ Be specific with city names
- ✅ Works worldwide across all cities
- ✅ Real-time data from OpenWeatherMap
- ✅ AI-powered insights from Gemini

### Results Display
- Real-time weather metrics
- JSON-formatted weather data
- AI-generated report with recommendations
- Easy-to-read formatting

## 🔄 How It Works

```
User Query
    ↓
[LangChain] Extract City Name
    ↓
[OpenWeatherMap API] Fetch Real-time Data
    ↓
[Google Gemini] Generate Report
    ↓
[Streamlit] Display Results
```

## 📊 Weather Data Provided

- **Temperature**: Current, min, max, "feels like"
- **Conditions**: Weather status (Clear, Cloudy, Rainy, etc.)
- **Wind**: Speed, direction, gusts
- **Moisture**: Humidity, pressure, visibility
- **Sun**: Sunrise/sunset times
- **Coverage**: Cloud percentage

## 📸 Screenshots

To capture app screenshots:
1. Run the application
2. Take a screenshot using your OS screenshot tool
3. Save to `assets/` directory
4. Update README with image references

Example image reference:
```markdown
![App Interface](./assets/weather-assistant-ui.png)
```

## 🛠️ Troubleshooting

### Issue: "API Key not found"
- **Solution**: Ensure `.env` file exists in project root with valid API keys
- Check that `.env` file is not in `.gitignore`

### Issue: "Streamlit not found"
- **Solution**: Install requirements: `pip install -r requirements.txt`
- Ensure virtual environment is activated

### Issue: "Connection timeout"
- **Solution**: Check internet connection and API service availability
- Verify API keys are valid and haven't exceeded rate limits

### Issue: "City not recognized"
- **Solution**: Try a more specific city name with country code
- Example: "London, UK" instead of just "London"

### Issue: "Module not found"
- **Solution**: Reinstall dependencies: `pip install --upgrade -r requirements.txt`

## 📁 Project Structure

```
weather_llm/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (API keys)
├── .gitignore               # Git ignore rules
│
├── weather_llm/             # Main package
│   ├── __pycache__/        # Python cache
│   ├── app.py              # Streamlit UI application
│   ├── chain.py            # LangChain LLM configuration
│   └── weather_tool.py     # Weather API client
│
└── assets/                  # Static assets and screenshots
    └── README.md           # Assets documentation
```

## 🔐 Security Notes

- Never commit `.env` file to version control
- Keep API keys confidential
- Use free tier limits appropriately
- Monitor API usage for unexpected charges

## 🚀 Performance Tips

- Queries are cached by Streamlit for faster reruns
- API responses are logged for debugging
- Weather data updates reflect real-time conditions
- Consider rate limiting for production use

## 📚 Dependencies Details

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.36.0 | Web framework |
| langchain | 0.2.0 | LLM orchestration |
| langchain-google-genai | 1.0.0 | Google Gemini integration |
| google-generativeai | 0.5.0 | Google AI SDK |
| python-dotenv | 1.0.0 | Environment variables |
| requests | 2.31.0 | HTTP client |
| pydantic | 2.0.0 | Data validation |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/enhancement`)
3. Commit changes (`git commit -am 'Add enhancement'`)
4. Push to branch (`git push origin feature/enhancement`)
5. Create Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 🙋 Support & Feedback

For issues, questions, or suggestions:
- Check existing GitHub issues
- Review troubleshooting section
- Check API provider documentation

## 🔗 Useful Links

- [Streamlit Documentation](https://docs.streamlit.io/)
- [LangChain Documentation](https://python.langchain.com/)
- [Google Gemini API](https://ai.google.dev/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Python Documentation](https://docs.python.org/)

## 📊 API Rate Limits

- **OpenWeatherMap**: Free tier - 60 calls/minute
- **Google Gemini**: Free tier - 15 requests/minute
- Plan usage accordingly for production

---

**Last Updated**: 2026-06-20  
**Status**: Active & Maintained ✅

## File Structure
- `app.py` - Streamlit UI and main application
- `chain.py` - LangChain prompts and chains for AI processing
- `weather_tool.py` - OpenWeatherMap API integration
- `.env` - Environment variables (API keys) - **DO NOT COMMIT THIS**
- `requirements.txt` - Project dependencies
