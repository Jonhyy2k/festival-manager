import streamlit as st
import random
import json
import os
from datetime import datetime
import time

# ============================================
# PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="Festival Manager",
    page_icon="🎪",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================
# PROFESSIONAL DARK THEME CSS
# ============================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        font-family: 'Poppins', sans-serif;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Story Card */
    .story-card {
        background: linear-gradient(145deg, #1a1a3e, #2d2d5a);
        border: 2px solid #4a4a8a;
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        text-align: center;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
    }

    .story-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        display: block;
    }

    .story-title {
        color: #ffd700;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .story-text {
        color: #c9c9e3;
        font-size: 1.05rem;
        line-height: 1.7;
        margin-bottom: 1rem;
    }

    .story-highlight {
        color: #ff6b6b;
        font-weight: 600;
    }

    /* Main Title */
    .main-title {
        text-align: center;
        padding: 1.5rem 0;
        background: linear-gradient(90deg, #ff6b6b, #ffd700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.2rem;
        font-weight: 700;
    }

    .subtitle {
        text-align: center;
        color: #a2a8d3;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }

    /* Stats Display */
    .stats-container {
        display: flex;
        justify-content: center;
        gap: 0.8rem;
        margin: 1rem 0;
        flex-wrap: wrap;
    }

    .stat-card {
        background: linear-gradient(145deg, #1e1e4a, #2a2a5e);
        border: 1px solid #3a3a7a;
        border-radius: 12px;
        padding: 0.8rem 1.2rem;
        text-align: center;
        min-width: 90px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }

    .stat-value {
        font-size: 1.2rem;
        font-weight: 700;
        color: #ffffff;
    }

    .stat-value.budget { color: #4ade80; }
    .stat-value.budget.low { color: #fbbf24; }
    .stat-value.budget.critical { color: #ef4444; }
    .stat-value.hype { color: #f472b6; }
    .stat-value.capacity { color: #60a5fa; }
    .stat-value.risk { color: #fbbf24; }

    .stat-label {
        font-size: 0.7rem;
        color: #8888aa;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Phase Progress */
    .phase-progress {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 0.3rem;
        margin: 1rem 0;
    }

    .phase-step {
        width: 40px;
        height: 6px;
        border-radius: 3px;
        background: #2a2a5e;
    }

    .phase-step.completed { background: #4ade80; }
    .phase-step.active { background: linear-gradient(90deg, #ff6b6b, #ffd700); }

    /* Choice Cards */
    .choice-card {
        background: linear-gradient(145deg, #1e1e4a, #2a2a5e);
        border: 2px solid #3a3a7a;
        border-radius: 16px;
        padding: 1.2rem;
        margin: 0.6rem 0;
        transition: all 0.3s ease;
    }

    .choice-card:hover {
        border-color: #ff6b6b;
        transform: translateX(5px);
        box-shadow: 0 5px 20px rgba(255, 107, 107, 0.2);
    }

    .choice-title {
        font-size: 1.05rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 0.4rem;
    }

    .choice-description {
        font-size: 0.8rem;
        color: #9999bb;
        margin-bottom: 0.6rem;
        line-height: 1.4;
    }

    .choice-stats {
        display: flex;
        gap: 0.6rem;
        flex-wrap: wrap;
    }

    .choice-stat {
        background: rgba(0, 0, 0, 0.3);
        padding: 0.3rem 0.6rem;
        border-radius: 15px;
        font-size: 0.75rem;
        color: #ccccee;
    }

    .choice-stat.cost { color: #ef4444; }
    .choice-stat.hype { color: #f472b6; }
    .choice-stat.capacity { color: #60a5fa; }
    .choice-stat.risk { color: #fbbf24; }
    .choice-stat.bonus { color: #4ade80; }

    /* Buttons */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #ff6b6b, #ff8e53) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.7rem 1.2rem !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        font-family: 'Poppins', sans-serif !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3) !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 25px rgba(255, 107, 107, 0.5) !important;
    }

    .stButton > button:disabled {
        background: #3a3a5a !important;
        box-shadow: none !important;
    }

    /* Leaderboard */
    .leaderboard-container {
        background: linear-gradient(145deg, #1a1a3e, #252560);
        border: 2px solid #4a4a8a;
        border-radius: 16px;
        padding: 1.2rem;
        margin: 1rem 0;
    }

    .leaderboard-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }

    .leaderboard-title {
        color: #ffd700;
        font-size: 1.2rem;
        font-weight: 600;
    }

    .leaderboard-live {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        color: #4ade80;
        font-size: 0.8rem;
    }

    .live-dot {
        width: 8px;
        height: 8px;
        background: #4ade80;
        border-radius: 50%;
        animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(1.2); }
    }

    .leaderboard-entry {
        display: flex;
        align-items: center;
        padding: 0.7rem 1rem;
        margin: 0.3rem 0;
        background: rgba(0, 0, 0, 0.2);
        border-radius: 10px;
        transition: all 0.2s ease;
    }

    .leaderboard-entry.gold {
        background: linear-gradient(90deg, rgba(255, 215, 0, 0.2), rgba(255, 215, 0, 0.05));
        border: 1px solid #ffd700;
    }

    .leaderboard-entry.silver {
        background: linear-gradient(90deg, rgba(192, 192, 192, 0.2), rgba(192, 192, 192, 0.05));
        border: 1px solid #c0c0c0;
    }

    .leaderboard-entry.bronze {
        background: linear-gradient(90deg, rgba(205, 127, 50, 0.2), rgba(205, 127, 50, 0.05));
        border: 1px solid #cd7f32;
    }

    .leaderboard-entry.you {
        background: linear-gradient(90deg, rgba(255, 107, 107, 0.3), rgba(255, 107, 107, 0.1));
        border: 2px solid #ff6b6b;
    }

    .player-rank {
        font-size: 1.1rem;
        font-weight: 700;
        width: 35px;
        text-align: center;
    }

    .player-name {
        flex: 1;
        color: #ffffff;
        font-weight: 500;
        margin-left: 0.5rem;
    }

    .player-score {
        color: #4ade80;
        font-weight: 700;
        font-size: 1rem;
    }

    .player-score.negative { color: #ef4444; }

    .player-status {
        font-size: 0.7rem;
        padding: 0.2rem 0.5rem;
        border-radius: 10px;
        margin-left: 0.5rem;
    }

    .player-status.playing {
        background: rgba(251, 191, 36, 0.2);
        color: #fbbf24;
    }

    .player-status.finished {
        background: rgba(74, 222, 128, 0.2);
        color: #4ade80;
    }

    /* Event Card */
    .event-card {
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        text-align: center;
    }

    .event-card.disaster {
        background: linear-gradient(135deg, #7f1d1d, #991b1b);
        border: 2px solid #ef4444;
        box-shadow: 0 0 30px rgba(239, 68, 68, 0.3);
    }

    .event-card.problem {
        background: linear-gradient(135deg, #78350f, #92400e);
        border: 2px solid #f59e0b;
        box-shadow: 0 0 30px rgba(245, 158, 11, 0.3);
    }

    .event-card.lucky {
        background: linear-gradient(135deg, #065f46, #047857);
        border: 2px solid #10b981;
        box-shadow: 0 0 30px rgba(16, 185, 129, 0.3);
    }

    .event-icon {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }

    .event-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
    }

    .event-description {
        color: rgba(255, 255, 255, 0.8);
        font-size: 0.95rem;
    }

    .event-impact {
        margin-top: 1rem;
        padding: 0.5rem 1rem;
        background: rgba(0, 0, 0, 0.3);
        border-radius: 10px;
        display: inline-block;
        font-weight: 600;
    }

    /* Results */
    .result-card {
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
    }

    .result-card.success {
        background: linear-gradient(135deg, #065f46, #047857);
        border: 2px solid #10b981;
    }

    .result-card.failure {
        background: linear-gradient(135deg, #7f1d1d, #991b1b);
        border: 2px solid #ef4444;
    }

    .result-card.bankrupt {
        background: linear-gradient(135deg, #1f1f1f, #2d2d2d);
        border: 2px solid #525252;
    }

    .result-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: white;
    }

    .result-profit {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 1rem 0;
    }

    .result-profit.positive { color: #4ade80; }
    .result-profit.negative { color: #ef4444; }

    /* Metric Grid */
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 0.8rem;
        margin: 1rem 0;
    }

    .metric-card {
        background: linear-gradient(145deg, #1e1e4a, #2a2a5e);
        border: 1px solid #3a3a7a;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
    }

    .metric-value {
        font-size: 1.3rem;
        font-weight: 700;
        color: #ffffff;
    }

    .metric-label {
        font-size: 0.75rem;
        color: #8888aa;
        margin-top: 0.2rem;
    }

    /* Input styling */
    .stTextInput > div > div > input {
        background: #1e1e4a !important;
        border: 2px solid #3a3a7a !important;
        border-radius: 12px !important;
        color: white !important;
        font-size: 1rem !important;
        padding: 0.7rem 1rem !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #ff6b6b !important;
    }

    /* Slider */
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #4ade80, #fbbf24, #ef4444) !important;
    }

    /* Divider */
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #4a4a8a, transparent);
        margin: 1.5rem 0;
    }

    /* Warning box */
    .warning-box {
        background: rgba(251, 191, 36, 0.1);
        border: 1px solid #fbbf24;
        border-radius: 12px;
        padding: 1rem;
        color: #fcd34d;
        font-size: 0.9rem;
        margin: 1rem 0;
    }

    /* Info box */
    .info-box {
        background: rgba(96, 165, 250, 0.1);
        border: 1px solid #60a5fa;
        border-radius: 12px;
        padding: 1rem;
        color: #93c5fd;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# DATABASE - JSON FILE FOR REAL-TIME SYNC
# ============================================
LEADERBOARD_FILE = "leaderboard.json"
PLAYERS_FILE = "active_players.json"

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        try:
            with open(LEADERBOARD_FILE, "r") as f:
                data = json.load(f)
                cutoff = datetime.now().timestamp() - (2 * 60 * 60)  # 2 hours
                return [e for e in data if e.get("timestamp", 0) > cutoff]
        except:
            return []
    return []

def save_to_leaderboard(name, profit, status="finished"):
    leaderboard = load_leaderboard()
    # Remove existing entry for this player
    leaderboard = [e for e in leaderboard if e.get("name") != name]
    leaderboard.append({
        "name": name,
        "profit": profit,
        "status": status,
        "timestamp": datetime.now().timestamp()
    })
    leaderboard.sort(key=lambda x: x["profit"], reverse=True)
    leaderboard = leaderboard[:30]
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(leaderboard, f)

def register_player(name, phase=0):
    """Register player as active."""
    players = load_active_players()
    players[name] = {
        "phase": phase,
        "timestamp": datetime.now().timestamp()
    }
    with open(PLAYERS_FILE, "w") as f:
        json.dump(players, f)

def load_active_players():
    if os.path.exists(PLAYERS_FILE):
        try:
            with open(PLAYERS_FILE, "r") as f:
                data = json.load(f)
                cutoff = datetime.now().timestamp() - (10 * 60)  # 10 min timeout
                return {k: v for k, v in data.items() if v.get("timestamp", 0) > cutoff}
        except:
            return {}
    return {}

# ============================================
# STORY NARRATIVES
# ============================================
STORIES = {
    "intro": {
        "icon": "🎪",
        "title": "Your Dream Begins",
        "text": """You've always dreamed of running your own music festival.
        After years of saving, you finally have <span class="story-highlight">€50,000</span> to make it happen.

        But be warned: <span class="story-highlight">most festivals fail</span>.
        Bad weather, poor planning, or just bad luck can turn your dream into a nightmare.

        Every decision matters. Choose wisely."""
    },
    "location": {
        "icon": "📍",
        "title": "Chapter 1: Finding Your Stage",
        "text": """Your phone buzzes with messages from venue owners.

        The <span class="story-highlight">location you choose will define your festival</span>.
        A cheap warehouse might save money, but will anyone come?
        A beach resort sounds amazing, but what if it rains?

        Remember: bigger capacity means more potential tickets, but also <span class="story-highlight">higher risk</span> if people don't show up."""
    },
    "artists": {
        "icon": "🎤",
        "title": "Chapter 2: Booking the Talent",
        "text": """Your venue is secured. Now you need someone to perform.

        Famous artists <span class="story-highlight">guarantee crowds</span> but eat your budget alive.
        Unknown bands are cheap but might not attract anyone.

        The music industry is brutal: <span class="story-highlight">one wrong choice here can bankrupt you</span> before doors even open."""
    },
    "marketing": {
        "icon": "📢",
        "title": "Chapter 3: Spreading the Word",
        "text": """You have a venue. You have artists. But <span class="story-highlight">does anyone know about it?</span>

        Marketing is where festivals are won or lost.
        Too little, and you'll play to an empty field.
        Too much on a risky viral stunt, and you might <span class="story-highlight">waste everything</span>.

        Choose your strategy carefully."""
    },
    "extras": {
        "icon": "✨",
        "title": "Chapter 4: The Final Touches",
        "text": """The festival is taking shape. But the details matter.

        Security keeps everyone safe (and avoids <span class="story-highlight">lawsuits</span>).
        Food trucks can bring extra revenue—or extra problems.
        VIP areas attract big spenders, but cost money to set up.

        <span class="story-highlight">Every euro spent here is one less for emergencies.</span>"""
    },
    "pricing": {
        "icon": "🎟️",
        "title": "Chapter 5: The Moment of Truth",
        "text": """Everything is ready. Now comes the hardest decision: <span class="story-highlight">ticket price</span>.

        Price too high? People stay home. Price too low? You won't cover costs.

        And remember: you can't control the weather.
        A storm could <span class="story-highlight">destroy everything</span> you've built.

        Take a deep breath. Set your price. And hope for the best."""
    },
    "results": {
        "icon": "🎭",
        "title": "Festival Day",
        "text": """The gates are open. The music is playing.

        Now you can only watch and wait...

        <span class="story-highlight">Did you make the right choices?</span>"""
    }
}

# ============================================
# RANDOM EVENTS - GOOD AND BAD
# ============================================
RANDOM_EVENTS = {
    "disasters": [
        {
            "name": "Sound System Failure",
            "icon": "🔇",
            "description": "The main speakers exploded during setup. Emergency replacements cost a fortune.",
            "cost": 8000,
            "hype_loss": 10,
            "chance": 0.08
        },
        {
            "name": "Headliner Cancels",
            "icon": "😱",
            "description": "Your main artist just posted on Instagram: 'Not feeling it today.' Refunds demanded!",
            "attendance_multiplier": 0.5,
            "hype_loss": 30,
            "chance": 0.05
        },
        {
            "name": "Food Poisoning Outbreak",
            "icon": "🤢",
            "description": "A food truck served bad shrimp. Half the crowd is sick. Lawsuits incoming.",
            "cost": 15000,
            "attendance_multiplier": 0.7,
            "chance": 0.06
        },
        {
            "name": "Security Incident",
            "icon": "🚨",
            "description": "A fight broke out and went viral for the wrong reasons. People are leaving.",
            "attendance_multiplier": 0.6,
            "hype_loss": 20,
            "chance": 0.07
        },
        {
            "name": "Power Grid Failure",
            "icon": "⚡",
            "description": "The entire venue lost power. Generators cost extra and the delay killed the vibe.",
            "cost": 5000,
            "attendance_multiplier": 0.8,
            "chance": 0.06
        },
    ],
    "problems": [
        {
            "name": "Traffic Nightmare",
            "icon": "🚗",
            "description": "Massive traffic jam. Many ticket holders couldn't make it in time.",
            "attendance_multiplier": 0.85,
            "chance": 0.12
        },
        {
            "name": "Competing Event",
            "icon": "🎪",
            "description": "A rival festival announced a surprise free event nearby. Some people went there instead.",
            "attendance_multiplier": 0.8,
            "chance": 0.10
        },
        {
            "name": "Permit Issues",
            "icon": "📋",
            "description": "Last-minute permit problems. You had to pay 'express fees' to city officials.",
            "cost": 4000,
            "chance": 0.10
        },
        {
            "name": "Equipment Rental Overcharge",
            "icon": "💸",
            "description": "The equipment company hit you with hidden fees at the last minute.",
            "cost": 3000,
            "chance": 0.12
        },
        {
            "name": "Bad Review Goes Viral",
            "icon": "📱",
            "description": "An influencer posted a 1-star review before the festival even started.",
            "hype_loss": 15,
            "attendance_multiplier": 0.9,
            "chance": 0.08
        },
    ],
    "lucky": [
        {
            "name": "Celebrity Spotted!",
            "icon": "⭐",
            "description": "A famous celebrity showed up unexpectedly! Everyone's posting about it.",
            "hype_bonus": 20,
            "attendance_multiplier": 1.2,
            "chance": 0.05
        },
        {
            "name": "Viral TikTok Moment",
            "icon": "📱",
            "description": "A video from your festival is trending! Free marketing!",
            "hype_bonus": 15,
            "attendance_multiplier": 1.15,
            "chance": 0.08
        },
        {
            "name": "Local News Coverage",
            "icon": "📺",
            "description": "The local news did a positive feature about your festival!",
            "hype_bonus": 10,
            "attendance_multiplier": 1.1,
            "chance": 0.10
        },
    ]
}

WEATHER_EFFECTS = {
    "perfect": {"name": "Perfect Sunny Day", "icon": "☀️", "multiplier": 1.2, "message": "Beautiful weather! Extra people showed up!"},
    "good": {"name": "Partly Cloudy", "icon": "⛅", "multiplier": 1.05, "message": "Nice weather. Comfortable for everyone."},
    "okay": {"name": "Overcast", "icon": "☁️", "multiplier": 0.95, "message": "Gray skies. Some people decided to stay home."},
    "rain": {"name": "Rainy Day", "icon": "🌧️", "multiplier": 0.65, "message": "Rain is falling. Many stayed home."},
    "storm": {"name": "Severe Storm", "icon": "⛈️", "multiplier": 0.35, "message": "Dangerous storm! Most people stayed away!"},
}

# ============================================
# GAME DATA
# ============================================
LOCATIONS = {
    "warehouse": {
        "name": "Abandoned Warehouse",
        "icon": "🏚️",
        "cost": 3000,
        "capacity": 2000,
        "hype": 5,
        "risk": 20,
        "description": "Cheap and edgy. No AC, sketchy neighborhood, but authentic underground vibes."
    },
    "park": {
        "name": "City Park",
        "icon": "🌳",
        "cost": 8000,
        "capacity": 6000,
        "hype": 10,
        "risk": 10,
        "description": "Public park with permits. Family-friendly but noise restrictions apply."
    },
    "field": {
        "name": "Countryside Field",
        "icon": "🏞️",
        "cost": 12000,
        "capacity": 12000,
        "hype": 15,
        "risk": 25,
        "description": "Wide open space. Great for camping, but very weather-dependent."
    },
    "stadium": {
        "name": "City Stadium",
        "icon": "🏟️",
        "cost": 28000,
        "capacity": 20000,
        "hype": 25,
        "risk": 8,
        "description": "Professional venue with facilities. Expensive but reliable."
    },
    "beach": {
        "name": "Beach Resort",
        "icon": "🏖️",
        "cost": 38000,
        "capacity": 10000,
        "hype": 45,
        "risk": 30,
        "description": "Premium beachfront. Instagram paradise, but storms could ruin everything."
    },
    "castle": {
        "name": "Historic Castle",
        "icon": "🏰",
        "cost": 48000,
        "capacity": 6000,
        "hype": 55,
        "risk": 15,
        "description": "Unique medieval venue. Limited capacity but unforgettable atmosphere."
    },
}

ARTISTS = {
    "local": {
        "name": "Local Bands",
        "icon": "🎸",
        "cost": 2000,
        "hype": 5,
        "description": "5 eager local bands. Cheap, but will anyone come to see them?"
    },
    "tribute": {
        "name": "Tribute Acts",
        "icon": "🎭",
        "cost": 6000,
        "hype": 12,
        "description": "Cover bands playing hits. Familiar songs, but not the real thing."
    },
    "rising": {
        "name": "Rising Stars",
        "icon": "⭐",
        "cost": 15000,
        "hype": 25,
        "description": "Up-and-coming artists. Could be the next big thing, or flop entirely."
    },
    "dj": {
        "name": "Famous DJ",
        "icon": "🎧",
        "cost": 28000,
        "hype": 40,
        "description": "Well-known DJ with millions of streams. Guaranteed party vibes."
    },
    "legends": {
        "name": "Rock Legends",
        "icon": "🤘",
        "cost": 42000,
        "hype": 55,
        "description": "Legendary band reunion. Appeals to multiple generations."
    },
    "superstar": {
        "name": "Global Superstar",
        "icon": "👑",
        "cost": 55000,
        "hype": 70,
        "description": "A-list celebrity. Massive draw, but takes most of your budget."
    },
}

MARKETING = {
    "none": {
        "name": "Word of Mouth",
        "icon": "🗣️",
        "cost": 0,
        "hype": 2,
        "description": "Free but slow. Only friends and family might hear about it."
    },
    "social": {
        "name": "Social Media Ads",
        "icon": "📱",
        "cost": 4000,
        "hype": 15,
        "description": "Instagram and TikTok campaigns. Good for young audiences."
    },
    "radio": {
        "name": "Radio & Posters",
        "icon": "📻",
        "cost": 10000,
        "hype": 25,
        "description": "Traditional media mix. Reaches broader demographics."
    },
    "influencers": {
        "name": "Influencer Campaign",
        "icon": "🤳",
        "cost": 18000,
        "hype": 40,
        "risk_bonus": 10,
        "description": "Partner with influencers. High engagement but unpredictable."
    },
    "tv": {
        "name": "TV & Billboards",
        "icon": "📺",
        "cost": 28000,
        "hype": 50,
        "description": "Premium advertising. Maximum visibility and credibility."
    },
    "viral": {
        "name": "Viral Stunt",
        "icon": "🚀",
        "cost": 22000,
        "hype": 65,
        "risk_bonus": 25,
        "description": "High-risk creative stunt. Could explode or backfire spectacularly."
    },
}

EXTRAS = {
    "security_basic": {
        "name": "Basic Security",
        "icon": "👮",
        "cost": 3000,
        "risk_reduction": 8,
        "description": "Minimum legal requirement. Might not handle problems well."
    },
    "security_pro": {
        "name": "Professional Security",
        "icon": "🛡️",
        "cost": 10000,
        "risk_reduction": 20,
        "description": "Experienced team with medical staff. Peace of mind."
    },
    "food": {
        "name": "Food Court",
        "icon": "🍔",
        "cost": 6000,
        "hype": 5,
        "revenue_bonus": 4,
        "description": "Food vendors. Extra revenue and happy customers."
    },
    "vip": {
        "name": "VIP Section",
        "icon": "🥂",
        "cost": 12000,
        "hype": 8,
        "revenue_bonus": 10,
        "description": "Premium area with perks. Attracts big spenders."
    },
    "eco": {
        "name": "Eco-Friendly Setup",
        "icon": "♻️",
        "cost": 7000,
        "hype": 12,
        "description": "Sustainable practices. Great PR with younger crowds."
    },
    "stream": {
        "name": "Live Stream",
        "icon": "📡",
        "cost": 9000,
        "hype": 15,
        "description": "Professional streaming. Reach global audience online."
    },
}

# ============================================
# SESSION STATE
# ============================================
def init_game():
    st.session_state.phase = 0
    st.session_state.budget = 50000
    st.session_state.hype = 0
    st.session_state.capacity = 0
    st.session_state.risk = 0
    st.session_state.revenue_bonus = 0
    st.session_state.location = None
    st.session_state.artist = None
    st.session_state.marketing = None
    st.session_state.extras = []
    st.session_state.ticket_price = 40
    st.session_state.game_started = True
    st.session_state.result_saved = False
    st.session_state.events = []
    st.session_state.weather = None

if "game_started" not in st.session_state:
    init_game()

if "player_name" not in st.session_state:
    st.session_state.player_name = ""

# ============================================
# HELPER FUNCTIONS
# ============================================
def display_stats():
    budget = st.session_state.budget
    budget_class = "budget"
    if budget < 5000:
        budget_class = "budget critical"
    elif budget < 15000:
        budget_class = "budget low"

    st.markdown(f"""
    <div class="stats-container">
        <div class="stat-card">
            <div class="stat-value {budget_class}">€{budget:,}</div>
            <div class="stat-label">Budget</div>
        </div>
        <div class="stat-card">
            <div class="stat-value hype">{st.session_state.hype}</div>
            <div class="stat-label">Hype</div>
        </div>
        <div class="stat-card">
            <div class="stat-value capacity">{st.session_state.capacity:,}</div>
            <div class="stat-label">Capacity</div>
        </div>
        <div class="stat-card">
            <div class="stat-value risk">{st.session_state.risk}%</div>
            <div class="stat-label">Risk</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def display_phase_progress(current):
    steps = ""
    for i in range(1, 7):
        if i < current:
            steps += '<div class="phase-step completed"></div>'
        elif i == current:
            steps += '<div class="phase-step active"></div>'
        else:
            steps += '<div class="phase-step"></div>'
    st.markdown(f'<div class="phase-progress">{steps}</div>', unsafe_allow_html=True)

def display_story(story_key):
    story = STORIES[story_key]
    st.markdown(f"""
    <div class="story-card">
        <span class="story-icon">{story['icon']}</span>
        <div class="story-title">{story['title']}</div>
        <div class="story-text">{story['text']}</div>
    </div>
    """, unsafe_allow_html=True)

def display_leaderboard(highlight_player=None):
    leaderboard = load_leaderboard()
    active_players = load_active_players()

    entries_html = ""

    if not leaderboard and not active_players:
        entries_html = '<p style="text-align: center; color: #8888aa; padding: 1rem;">No players yet. Be the first!</p>'
    else:
        # Combine finished players and active players
        all_entries = []

        for entry in leaderboard:
            all_entries.append({
                "name": entry["name"],
                "profit": entry["profit"],
                "status": "finished"
            })

        for name, data in active_players.items():
            if not any(e["name"] == name for e in all_entries):
                all_entries.append({
                    "name": name,
                    "profit": None,
                    "status": "playing"
                })

        # Sort: finished players by profit, then playing players
        finished = sorted([e for e in all_entries if e["status"] == "finished"], key=lambda x: x["profit"], reverse=True)
        playing = [e for e in all_entries if e["status"] == "playing"]

        all_sorted = finished + playing

        for i, entry in enumerate(all_sorted[:15]):
            if entry["status"] == "finished":
                rank = i + 1
                if rank == 1:
                    rank_display = "🥇"
                    entry_class = "gold"
                elif rank == 2:
                    rank_display = "🥈"
                    entry_class = "silver"
                elif rank == 3:
                    rank_display = "🥉"
                    entry_class = "bronze"
                else:
                    rank_display = f"#{rank}"
                    entry_class = ""

                score_class = "negative" if entry["profit"] < 0 else ""
                score_display = f"€{entry['profit']:,}"

                if highlight_player and entry["name"] == highlight_player:
                    entry_class += " you"
            else:
                rank_display = "⏳"
                entry_class = ""
                score_class = ""
                score_display = "Playing..."

                if highlight_player and entry["name"] == highlight_player:
                    entry_class = "you"

            status_html = f'<span class="player-status {entry["status"]}">{entry["status"].upper()}</span>' if entry["status"] == "playing" else ""

            entries_html += f"""
            <div class="leaderboard-entry {entry_class}">
                <span class="player-rank">{rank_display}</span>
                <span class="player-name">{entry['name']}</span>
                {status_html}
                <span class="player-score {score_class}">{score_display}</span>
            </div>
            """

    st.markdown(f"""
    <div class="leaderboard-container">
        <div class="leaderboard-header">
            <span class="leaderboard-title">🏆 Live Leaderboard</span>
            <span class="leaderboard-live"><span class="live-dot"></span>LIVE</span>
        </div>
        {entries_html}
    </div>
    """, unsafe_allow_html=True)

def render_choice(key, data, choice_type):
    cost = data["cost"]
    can_afford = st.session_state.budget >= cost

    stats = [f'<span class="choice-stat cost">€{cost:,}</span>']
    if "hype" in data:
        stats.append(f'<span class="choice-stat hype">+{data["hype"]} Hype</span>')
    if "capacity" in data:
        stats.append(f'<span class="choice-stat capacity">{data["capacity"]:,} cap</span>')
    if "risk" in data:
        stats.append(f'<span class="choice-stat risk">+{data["risk"]}% risk</span>')
    if "risk_reduction" in data:
        stats.append(f'<span class="choice-stat bonus">-{data["risk_reduction"]}% risk</span>')
    if "revenue_bonus" in data:
        stats.append(f'<span class="choice-stat bonus">+€{data["revenue_bonus"]}/ticket</span>')
    if "risk_bonus" in data:
        stats.append(f'<span class="choice-stat risk">+{data["risk_bonus"]}% risk</span>')

    st.markdown(f"""
    <div class="choice-card">
        <div class="choice-title">{data['icon']} {data['name']}</div>
        <div class="choice-description">{data['description']}</div>
        <div class="choice-stats">{''.join(stats)}</div>
    </div>
    """, unsafe_allow_html=True)

    if can_afford:
        if st.button(f"Choose {data['name']}", key=f"{choice_type}_{key}", use_container_width=True):
            return True
    else:
        st.button(f"Can't afford (need €{cost:,})", key=f"{choice_type}_{key}", disabled=True, use_container_width=True)
    return False

# ============================================
# GAME PHASES
# ============================================
def show_start():
    st.markdown('<h1 class="main-title">🎪 Festival Manager</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Can you build a successful festival?</p>', unsafe_allow_html=True)

    display_leaderboard()

    display_story("intro")

    name = st.text_input("Enter your name:", placeholder="Your name...", max_chars=15)

    if st.button("🚀 Begin Your Journey", type="primary", use_container_width=True):
        if name.strip():
            st.session_state.player_name = name.strip()
            register_player(name.strip(), 1)
            st.session_state.phase = 1
            st.rerun()
        else:
            st.error("Please enter your name!")

def show_location():
    st.markdown('<h1 class="main-title">📍 Choose Location</h1>', unsafe_allow_html=True)
    display_phase_progress(1)
    display_stats()
    display_story("location")

    for key, data in LOCATIONS.items():
        if render_choice(key, data, "loc"):
            st.session_state.budget -= data["cost"]
            st.session_state.capacity = data["capacity"]
            st.session_state.hype += data["hype"]
            st.session_state.risk += data["risk"]
            st.session_state.location = data["name"]
            register_player(st.session_state.player_name, 2)
            st.session_state.phase = 2
            st.rerun()

def show_artists():
    st.markdown('<h1 class="main-title">🎤 Book Artists</h1>', unsafe_allow_html=True)
    display_phase_progress(2)
    display_stats()
    display_story("artists")

    for key, data in ARTISTS.items():
        if render_choice(key, data, "art"):
            st.session_state.budget -= data["cost"]
            st.session_state.hype += data["hype"]
            st.session_state.artist = data["name"]
            register_player(st.session_state.player_name, 3)
            st.session_state.phase = 3
            st.rerun()

def show_marketing():
    st.markdown('<h1 class="main-title">📢 Marketing</h1>', unsafe_allow_html=True)
    display_phase_progress(3)
    display_stats()
    display_story("marketing")

    for key, data in MARKETING.items():
        if render_choice(key, data, "mkt"):
            st.session_state.budget -= data["cost"]
            st.session_state.hype += data["hype"]
            st.session_state.risk += data.get("risk_bonus", 0)
            st.session_state.marketing = data["name"]
            register_player(st.session_state.player_name, 4)
            st.session_state.phase = 4
            st.rerun()

def show_extras():
    st.markdown('<h1 class="main-title">✨ Extras</h1>', unsafe_allow_html=True)
    display_phase_progress(4)
    display_stats()
    display_story("extras")

    for key, data in EXTRAS.items():
        cost = data["cost"]
        can_afford = st.session_state.budget >= cost
        selected = key in st.session_state.extras

        stats = [f'<span class="choice-stat cost">€{cost:,}</span>']
        if "hype" in data:
            stats.append(f'<span class="choice-stat hype">+{data["hype"]} Hype</span>')
        if "risk_reduction" in data:
            stats.append(f'<span class="choice-stat bonus">-{data["risk_reduction"]}% risk</span>')
        if "revenue_bonus" in data:
            stats.append(f'<span class="choice-stat bonus">+€{data["revenue_bonus"]}/ticket</span>')

        st.markdown(f"""
        <div class="choice-card">
            <div class="choice-title">{data['icon']} {data['name']}</div>
            <div class="choice-description">{data['description']}</div>
            <div class="choice-stats">{''.join(stats)}</div>
        </div>
        """, unsafe_allow_html=True)

        if selected:
            st.button(f"✅ Added!", key=f"ext_{key}", disabled=True, use_container_width=True)
        elif can_afford:
            if st.button(f"Add {data['name']}", key=f"ext_{key}", use_container_width=True):
                st.session_state.budget -= data["cost"]
                st.session_state.hype += data.get("hype", 0)
                st.session_state.risk -= data.get("risk_reduction", 0)
                st.session_state.revenue_bonus += data.get("revenue_bonus", 0)
                st.session_state.extras.append(key)
                st.rerun()
        else:
            st.button(f"Can't afford", key=f"ext_{key}", disabled=True, use_container_width=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    if st.button("➡️ Continue to Pricing", type="primary", use_container_width=True):
        register_player(st.session_state.player_name, 5)
        st.session_state.phase = 5
        st.rerun()

def show_pricing():
    st.markdown('<h1 class="main-title">🎟️ Set Price</h1>', unsafe_allow_html=True)
    display_phase_progress(5)
    display_stats()
    display_story("pricing")

    st.markdown(f"""
    **Your Festival:**
    - Location: {st.session_state.location}
    - Artist: {st.session_state.artist}
    - Marketing: {st.session_state.marketing}
    """)

    price = st.slider("Ticket Price (€)", 15, 200, 40, 5)
    st.session_state.ticket_price = price

    # Demand calculation preview
    base_demand = st.session_state.hype * 60
    price_penalty = max(0, (price - 25) * 1.8)
    demand = max(0, base_demand - price_penalty)
    expected = min(int(demand), st.session_state.capacity)

    costs = 50000 - st.session_state.budget
    revenue = expected * (price + st.session_state.revenue_bonus)
    expected_profit = revenue - costs

    color = "#4ade80" if expected_profit > 0 else "#ef4444"

    st.markdown(f"""
    <div class="info-box">
        <strong>Projection (before weather & events):</strong><br>
        Expected attendance: ~{expected:,}<br>
        Expected profit: <span style="color: {color}">€{expected_profit:,}</span>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.risk > 20:
        st.markdown(f"""
        <div class="warning-box">
            ⚠️ <strong>High Risk Alert!</strong> Your risk level is {st.session_state.risk}%.
            Bad things are more likely to happen!
        </div>
        """, unsafe_allow_html=True)

    if st.button("🎲 Launch Festival!", type="primary", use_container_width=True):
        register_player(st.session_state.player_name, 6)
        st.session_state.phase = 6
        st.rerun()

def show_results():
    st.markdown('<h1 class="main-title">🎪 Festival Day!</h1>', unsafe_allow_html=True)
    display_story("results")

    events_occurred = []
    total_cost_from_events = 0
    attendance_multiplier = 1.0
    hype_modifier = 0

    # Check for random events based on risk
    risk_factor = st.session_state.risk / 100

    # Disasters (more likely with high risk)
    for event in RANDOM_EVENTS["disasters"]:
        if random.random() < event["chance"] * (1 + risk_factor * 2):
            events_occurred.append(("disaster", event))
            total_cost_from_events += event.get("cost", 0)
            attendance_multiplier *= event.get("attendance_multiplier", 1.0)
            hype_modifier -= event.get("hype_loss", 0)
            break  # Only one disaster

    # Problems (common)
    for event in RANDOM_EVENTS["problems"]:
        if random.random() < event["chance"] * (1 + risk_factor):
            events_occurred.append(("problem", event))
            total_cost_from_events += event.get("cost", 0)
            attendance_multiplier *= event.get("attendance_multiplier", 1.0)
            hype_modifier -= event.get("hype_loss", 0)
            if len([e for e in events_occurred if e[0] == "problem"]) >= 2:
                break

    # Lucky events (less likely with high risk)
    if random.random() < 0.15 * (1 - risk_factor * 0.5):
        event = random.choice(RANDOM_EVENTS["lucky"])
        events_occurred.append(("lucky", event))
        attendance_multiplier *= event.get("attendance_multiplier", 1.0)
        hype_modifier += event.get("hype_bonus", 0)

    # Weather
    weather_weights = [10, 20, 30, 25, 15]
    weather_weights[3] += int(st.session_state.risk * 0.5)
    weather_weights[4] += int(st.session_state.risk * 0.3)

    weather_key = random.choices(list(WEATHER_EFFECTS.keys()), weights=weather_weights, k=1)[0]
    weather = WEATHER_EFFECTS[weather_key]

    # Display events
    for event_type, event in events_occurred:
        card_class = event_type
        impact_text = ""
        if event.get("cost"):
            impact_text += f"💸 -€{event['cost']:,} "
        if event.get("attendance_multiplier") and event["attendance_multiplier"] < 1:
            loss = int((1 - event["attendance_multiplier"]) * 100)
            impact_text += f"👥 -{loss}% attendance "
        if event.get("attendance_multiplier") and event["attendance_multiplier"] > 1:
            gain = int((event["attendance_multiplier"] - 1) * 100)
            impact_text += f"👥 +{gain}% attendance "

        st.markdown(f"""
        <div class="event-card {card_class}">
            <div class="event-icon">{event['icon']}</div>
            <div class="event-title">{event['name']}</div>
            <div class="event-description">{event['description']}</div>
            <div class="event-impact">{impact_text}</div>
        </div>
        """, unsafe_allow_html=True)

    # Weather display
    weather_class = "lucky" if weather["multiplier"] >= 1.0 else "problem" if weather["multiplier"] >= 0.6 else "disaster"
    st.markdown(f"""
    <div class="event-card {weather_class}">
        <div class="event-icon">{weather['icon']}</div>
        <div class="event-title">{weather['name']}</div>
        <div class="event-description">{weather['message']}</div>
    </div>
    """, unsafe_allow_html=True)

    # Final calculations
    effective_hype = max(0, st.session_state.hype + hype_modifier)
    base_demand = effective_hype * 60
    price_penalty = max(0, (st.session_state.ticket_price - 25) * 1.8)
    demand = max(0, base_demand - price_penalty)

    # Apply all multipliers
    demand *= attendance_multiplier
    demand *= weather["multiplier"]
    demand *= random.uniform(0.85, 1.15)  # Random variance

    actual_attendance = min(max(0, int(demand)), st.session_state.capacity)

    # Financials
    ticket_revenue = actual_attendance * st.session_state.ticket_price
    bonus_revenue = actual_attendance * st.session_state.revenue_bonus
    total_revenue = ticket_revenue + bonus_revenue

    base_costs = 50000 - st.session_state.budget
    total_costs = base_costs + total_cost_from_events

    profit = total_revenue - total_costs

    # Display metrics
    st.markdown(f"""
    <div class="metric-grid">
        <div class="metric-card">
            <div class="metric-value">👥 {actual_attendance:,}</div>
            <div class="metric-label">Attended</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">🏟️ {st.session_state.capacity:,}</div>
            <div class="metric-label">Capacity</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">💵 €{total_revenue:,}</div>
            <div class="metric-label">Revenue</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">💸 €{total_costs:,}</div>
            <div class="metric-label">Total Costs</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Result verdict
    if profit > 25000:
        result_class = "success"
        title = "🏆 LEGENDARY!"
        st.balloons()
    elif profit > 10000:
        result_class = "success"
        title = "🎉 SUCCESS!"
    elif profit > 0:
        result_class = "success"
        title = "✅ Profit!"
    elif profit > -10000:
        result_class = "failure"
        title = "😓 Small Loss"
    elif profit > -25000:
        result_class = "failure"
        title = "😰 Big Loss"
    else:
        result_class = "bankrupt"
        title = "💀 BANKRUPT"

    profit_class = "positive" if profit >= 0 else "negative"

    st.markdown(f"""
    <div class="result-card {result_class}">
        <div class="result-title">{title}</div>
        <div class="result-profit {profit_class}">€{profit:,}</div>
    </div>
    """, unsafe_allow_html=True)

    # Save to leaderboard
    if not st.session_state.result_saved:
        save_to_leaderboard(st.session_state.player_name, profit)
        st.session_state.result_saved = True

    display_leaderboard(st.session_state.player_name)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Play Again", use_container_width=True):
            init_game()
            st.session_state.result_saved = False
            st.rerun()
    with col2:
        if st.button("🔃 Refresh Board", use_container_width=True):
            st.rerun()

# ============================================
# MAIN
# ============================================
def main():
    phase = st.session_state.phase

    if phase == 0:
        show_start()
    elif phase == 1:
        show_location()
    elif phase == 2:
        show_artists()
    elif phase == 3:
        show_marketing()
    elif phase == 4:
        show_extras()
    elif phase == 5:
        show_pricing()
    elif phase == 6:
        show_results()

if __name__ == "__main__":
    main()
