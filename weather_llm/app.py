import streamlit as st
import requests

from chain import city_chain, summary_chain
from weather_tool import get_weather

# Page Configuration
st.set_page_config(
    page_title="🌤️ Weather AI Assistant",
    page_icon="🌤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for vibrant styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Header Styling */
    .header-title {
        text-align: center;
        font-size: 3.5em;
        margin-bottom: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: shine 3s ease-in-out infinite;
    }
    
    @keyframes shine {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    .subtitle {
        text-align: center;
        background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 1.2em;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    
    /* Metrics - Color coded by weather */
    .metric-temp {
        background: linear-gradient(135deg, #ff9a56 0%, #ff6b6b 100%) !important;
        padding: 1.5rem !important;
        border-radius: 15px !important;
        color: white !important;
        box-shadow: 0 8px 16px rgba(255, 107, 107, 0.3) !important;
        border: 2px solid #ff6b6b !important;
    }
    
    .metric-humidity {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%) !important;
        padding: 1.5rem !important;
        border-radius: 15px !important;
        color: white !important;
        box-shadow: 0 8px 16px rgba(79, 172, 254, 0.3) !important;
        border: 2px solid #00f2fe !important;
    }
    
    .metric-wind {
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%) !important;
        padding: 1.5rem !important;
        border-radius: 15px !important;
        color: white !important;
        box-shadow: 0 8px 16px rgba(67, 233, 123, 0.3) !important;
        border: 2px solid #38f9d7 !important;
    }
    
    .metric-condition {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%) !important;
        padding: 1.5rem !important;
        border-radius: 15px !important;
        color: white !important;
        box-shadow: 0 8px 16px rgba(250, 112, 154, 0.3) !important;
        border: 2px solid #fee140 !important;
    }
    
    /* Card styling */
    .weather-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    
    .input-section {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 1.5rem;
        box-shadow: 0 5px 15px rgba(252, 182, 159, 0.3);
    }
    
    .tips-section {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(168, 237, 234, 0.3);
    }
    
    .example-section {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
    }
    
    .report-section {
        background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%);
        padding: 2rem;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        box-shadow: 0 8px 20px rgba(142, 197, 252, 0.3);
        color: #333;
    }
    
    .success-badge {
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        margin: 1rem 0;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.8rem 1.5rem !important;
        font-weight: bold !important;
        font-size: 1.1em !important;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.6) !important;
    }
    
    /* Tab styling */
    .stTabs {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 1rem;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header-title">🌤️ Weather AI Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Get real-time weather insights powered by AI</div>', unsafe_allow_html=True)

# Create two columns for better layout
col1, col2 = st.columns([2, 1])

with col1:
    # Input Section
    st.markdown('<div class="input-section"><h3>🔍 Search Weather</h3></div>', unsafe_allow_html=True)
    
    query = st.text_input(
        "Enter your query",
        placeholder="e.g., What's the weather in London?",
        label_visibility="collapsed"
    )
    
    # Example queries in an expander
    with st.expander("📝 Example Queries"):
        st.markdown('<div class="example-section">', unsafe_allow_html=True)
        st.write("""
        🌍 **Global Examples:**
        - What's the weather in Chandigarh today?
        - How's the weather in New York?
        - Tell me about Tokyo's weather
        - Weather conditions in Paris?
        - What's it like in Sydney?
        """)
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="tips-section"><h3>💡 Tips</h3></div>', unsafe_allow_html=True)
    st.markdown("""
    ✅ **Be specific** with city names
    ✅ **Works worldwide** across all cities
    ✅ **Real-time data** from OpenWeatherMap
    ✅ **AI-powered** insights from Gemini
    """)

# Search button
if st.button("🔎 Get Weather", use_container_width=True, key="search_btn"):
    if query:
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Step 1: Extract City
            status_text.text("🔍 Analyzing your query...")
            progress_bar.progress(25)
            
            city = city_chain.invoke(
                {"query": query}
            ).strip()
            
            # Step 2: Fetch Weather
            status_text.text(f"📡 Fetching weather for {city}...")
            progress_bar.progress(50)
            
            weather = get_weather(city)
            
            if "error" in weather:
                st.error(f"❌ {weather['error']}. Please try another city name.")
                progress_bar.empty()
                status_text.empty()
            else:
                # Step 3: Generate Report
                status_text.text("🤖 Generating AI insights...")
                progress_bar.progress(75)
                
                report = summary_chain.invoke(
                    {
                        "city": weather["city"],
                        "temperature": weather["temperature"],
                        "feels_like": weather.get("feels_like", weather["temperature"]),
                        "humidity": weather["humidity"],
                        "condition": weather["condition"],
                        "wind_speed": weather["wind_speed"],
                        "pressure": weather.get("pressure", "N/A"),
                        "clouds": weather.get("clouds", "N/A"),
                        "visibility": weather.get("visibility", "N/A")
                    }
                )
                
                progress_bar.progress(100)
                status_text.empty()
                progress_bar.empty()
                
                # Success message
                st.markdown('<div class="success-badge">✅ Weather Retrieved Successfully!</div>', unsafe_allow_html=True)
                
                # Main Weather Display
                st.markdown(f'<div class="weather-card"><h2>🌍 Weather in {weather["city"]}</h2></div>', 
                           unsafe_allow_html=True)
                
                # Weather Metrics in a colorful grid
                metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
                
                with metric_col1:
                    st.markdown('<style>.metric-container { padding: 0 5px; }</style>', unsafe_allow_html=True)
                    st.markdown('<div class="metric-temp">', unsafe_allow_html=True)
                    st.metric(
                        "🌡️ Temperature",
                        f"{weather['temperature']}°C",
                        f"Feels like {weather.get('feels_like', weather['temperature'])}°C"
                    )
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with metric_col2:
                    st.markdown('<div class="metric-humidity">', unsafe_allow_html=True)
                    st.metric(
                        "💧 Humidity",
                        f"{weather['humidity']}%",
                        "Air Moisture"
                    )
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with metric_col3:
                    st.markdown('<div class="metric-wind">', unsafe_allow_html=True)
                    st.metric(
                        "💨 Wind Speed",
                        f"{weather['wind_speed']} m/s",
                        "Current Wind"
                    )
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with metric_col4:
                    st.markdown('<div class="metric-condition">', unsafe_allow_html=True)
                    st.metric(
                        "☁️ Condition",
                        weather['condition'],
                        weather.get('condition_main', 'Weather')
                    )
                    st.markdown('</div>', unsafe_allow_html=True)
                
                # Additional Weather Details
                st.markdown("### 📊 Detailed Weather Information")
                
                detail_col1, detail_col2, detail_col3 = st.columns(3)
                
                with detail_col1:
                    st.markdown(f"""
                    **🌍 Location:**
                    - City: {weather.get('city', 'N/A')}
                    - Country: {weather.get('country', 'N/A')}
                    
                    **🔍 Atmospheric:**
                    - Pressure: {weather.get('pressure', 'N/A')} hPa
                    - Clouds: {weather.get('clouds', 'N/A')}%
                    - Visibility: {weather.get('visibility', 'N/A')} m
                    """)
                
                with detail_col2:
                    st.markdown(f"""
                    **🌡️ Temperature Details:**
                    - Current: {weather['temperature']}°C
                    - Feels Like: {weather.get('feels_like', weather['temperature'])}°C
                    - Humidity: {weather['humidity']}%
                    """)
                
                with detail_col3:
                    st.markdown(f"""
                    **💨 Wind Details:**
                    - Speed: {weather['wind_speed']} m/s
                    - Direction: {weather.get('wind_deg', 'N/A')}°
                    
                    **☀️ Sun Times:**
                    - Sunrise: {weather.get('sunrise', 'N/A')}
                    - Sunset: {weather.get('sunset', 'N/A')}
                    """)
                
                # AI Report Section
                st.markdown("### 📋 AI Weather Report")
                
                with st.container():
                    st.markdown(f"""
                    <div class="report-section">
                    {report}
                    </div>
                    """, unsafe_allow_html=True)
                
                # Additional Info in Tabs
                tab1, tab2, tab3 = st.tabs(["📊 Details", "📝 Query Info", "🎨 Weather Summary"])
                
                with tab1:
                    st.markdown("**🌍 Full Weather Report:**")
                    st.json({
                        "Location": {"City": weather.get('city', 'N/A'), "Country": weather.get('country', 'N/A')},
                        "Temperature": {"Current": f"{weather['temperature']}°C", "Feels Like": f"{weather.get('feels_like', weather['temperature'])}°C"},
                        "Humidity": f"{weather['humidity']}%",
                        "Wind": {"Speed": f"{weather['wind_speed']} m/s", "Direction": f"{weather.get('wind_deg', 'N/A')}°"},
                        "Atmospheric": {"Pressure": f"{weather.get('pressure', 'N/A')} hPa", "Clouds": f"{weather.get('clouds', 'N/A')}%", "Visibility": f"{weather.get('visibility', 'N/A')} m"},
                        "Condition": weather['condition']
                    })
                
                with tab2:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("**🔤 Your Original Query:**")
                        st.info(query)
                    with col2:
                        st.markdown("**🏙️ Extracted City:**")
                        st.success(city)
                    
                    st.divider()
                    st.markdown("**📡 Data Source:**")
                    st.write("✅ Real-time data from **OpenWeatherMap API**")
                    st.write("✅ AI insights powered by **Google Gemini**")
                
                with tab3:
                    st.markdown("**🎯 Weather Assessment:**")
                    temp_status = "🔥 Hot" if weather['temperature'] > 25 else "❄️ Cold" if weather['temperature'] < 10 else "😊 Mild"
                    humidity_status = "💧 Humid" if weather['humidity'] > 70 else "🏜️ Dry"
                    wind_status = "🌪️ Windy" if weather['wind_speed'] > 10 else "🍃 Calm"
                    visibility_status = "👁️ Good" if weather.get('visibility', 10000) > 5000 else "🌫️ Poor"
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"""
                        **Current Conditions:**
                        - Temperature: {temp_status}
                        - Humidity: {humidity_status}
                        - Visibility: {visibility_status}
                        """)
                    with col2:
                        st.markdown(f"""
                        **Other Factors:**
                        - Wind: {wind_status}
                        - Condition: {weather['condition'].upper()}
                        - Cloud Cover: {weather.get('clouds', 'N/A')}%
                        """)
        
        
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            progress_bar.empty()
            status_text.empty()
    
    else:
        st.warning("⚠️ Please enter a query to get started!")