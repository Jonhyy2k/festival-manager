import streamlit as st
import random
import json
import os
from datetime import datetime

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
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        font-family: 'Poppins', sans-serif;
    }

    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Main Title */
    .main-title {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #e94560, #ff6b6b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.5rem;
        font-weight: 700;
        text-shadow: 0 0 30px rgba(233, 69, 96, 0.3);
    }

    .subtitle {
        text-align: center;
        color: #a2a8d3;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* Stats Display */
    .stats-container {
        display: flex;
        justify-content: space-around;
        gap: 1rem;
        margin: 1.5rem 0;
        flex-wrap: wrap;
    }

    .stat-card {
        background: linear-gradient(145deg, #1e2a4a, #253a5e);
        border: 1px solid #3a4a6e;
        border-radius: 16px;
        padding: 1.2rem;
        text-align: center;
        min-width: 100px;
        flex: 1;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }

    .stat-icon {
        font-size: 1.5rem;
        margin-bottom: 0.3rem;
    }

    .stat-value {
        font-size: 1.4rem;
        font-weight: 700;
        color: #ffffff;
    }

    .stat-value.budget { color: #4ade80; }
    .stat-value.hype { color: #f472b6; }
    .stat-value.capacity { color: #60a5fa; }

    .stat-label {
        font-size: 0.75rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Phase Header */
    .phase-header {
        background: linear-gradient(90deg, #e94560, #ff6b6b);
        padding: 1rem 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 4px 20px rgba(233, 69, 96, 0.4);
    }

    .phase-header h2 {
        color: white;
        margin: 0;
        font-size: 1.3rem;
        font-weight: 600;
    }

    .phase-indicator {
        display: flex;
        justify-content: center;
        gap: 0.5rem;
        margin: 1rem 0;
    }

    .phase-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: #3a4a6e;
    }

    .phase-dot.active {
        background: linear-gradient(90deg, #e94560, #ff6b6b);
        box-shadow: 0 0 10px rgba(233, 69, 96, 0.6);
    }

    .phase-dot.completed {
        background: #4ade80;
    }

    /* Choice Cards */
    .choice-card {
        background: linear-gradient(145deg, #1e2a4a, #253a5e);
        border: 2px solid #3a4a6e;
        border-radius: 16px;
        padding: 1.2rem;
        margin: 0.8rem 0;
        transition: all 0.3s ease;
        cursor: pointer;
    }

    .choice-card:hover {
        border-color: #e94560;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(233, 69, 96, 0.2);
    }

    .choice-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .choice-description {
        font-size: 0.85rem;
        color: #94a3b8;
        margin-bottom: 0.8rem;
        line-height: 1.4;
    }

    .choice-stats {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
    }

    .choice-stat {
        background: rgba(0, 0, 0, 0.2);
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        color: #e2e8f0;
    }

    .choice-stat.cost { border-left: 3px solid #ef4444; }
    .choice-stat.hype { border-left: 3px solid #f472b6; }
    .choice-stat.capacity { border-left: 3px solid #60a5fa; }
    .choice-stat.risk { border-left: 3px solid #fbbf24; }

    /* Buttons */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #e94560, #ff6b6b) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.8rem 1.5rem !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        font-family: 'Poppins', sans-serif !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(233, 69, 96, 0.4) !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(233, 69, 96, 0.6) !important;
    }

    /* Leaderboard */
    .leaderboard-container {
        background: linear-gradient(145deg, #1e2a4a, #253a5e);
        border: 1px solid #3a4a6e;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
    }

    .leaderboard-title {
        text-align: center;
        color: #fbbf24;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    .leaderboard-entry {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.8rem 1rem;
        margin: 0.4rem 0;
        background: rgba(0, 0, 0, 0.2);
        border-radius: 10px;
        transition: all 0.2s ease;
    }

    .leaderboard-entry:hover {
        background: rgba(233, 69, 96, 0.1);
    }

    .leaderboard-entry.gold {
        background: linear-gradient(90deg, rgba(251, 191, 36, 0.2), rgba(251, 191, 36, 0.1));
        border: 1px solid #fbbf24;
    }

    .leaderboard-entry.silver {
        background: linear-gradient(90deg, rgba(192, 192, 192, 0.2), rgba(192, 192, 192, 0.1));
        border: 1px solid #c0c0c0;
    }

    .leaderboard-entry.bronze {
        background: linear-gradient(90deg, rgba(205, 127, 50, 0.2), rgba(205, 127, 50, 0.1));
        border: 1px solid #cd7f32;
    }

    .player-rank {
        font-size: 1.2rem;
        font-weight: 700;
        width: 40px;
    }

    .player-name {
        flex: 1;
        color: #ffffff;
        font-weight: 500;
    }

    .player-score {
        color: #4ade80;
        font-weight: 700;
        font-size: 1.1rem;
    }

    .player-score.negative {
        color: #ef4444;
    }

    /* Results */
    .result-card {
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        margin: 1.5rem 0;
    }

    .result-card.success {
        background: linear-gradient(135deg, #065f46, #047857);
        border: 2px solid #10b981;
        box-shadow: 0 8px 30px rgba(16, 185, 129, 0.3);
    }

    .result-card.failure {
        background: linear-gradient(135deg, #7f1d1d, #991b1b);
        border: 2px solid #ef4444;
        box-shadow: 0 8px 30px rgba(239, 68, 68, 0.3);
    }

    .result-title {
        font-size: 2rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
    }

    .result-subtitle {
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.8);
    }

    /* Input styling */
    .stTextInput > div > div > input {
        background: #1e2a4a !important;
        border: 2px solid #3a4a6e !important;
        border-radius: 12px !important;
        color: white !important;
        font-size: 1.1rem !important;
        padding: 0.8rem 1rem !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #e94560 !important;
        box-shadow: 0 0 10px rgba(233, 69, 96, 0.3) !important;
    }

    .stSlider > div > div > div > div {
        background: #e94560 !important;
    }

    /* Section divider */
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #3a4a6e, transparent);
        margin: 1.5rem 0;
    }

    /* Info boxes */
    .info-box {
        background: rgba(59, 130, 246, 0.1);
        border: 1px solid #3b82f6;
        border-radius: 12px;
        padding: 1rem;
        color: #93c5fd;
        font-size: 0.9rem;
    }

    /* Metric cards for results */
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
        margin: 1rem 0;
    }

    .metric-card {
        background: linear-gradient(145deg, #1e2a4a, #253a5e);
        border: 1px solid #3a4a6e;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
    }

    .metric-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #ffffff;
    }

    .metric-label {
        font-size: 0.8rem;
        color: #94a3b8;
        margin-top: 0.3rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# LEADERBOARD FILE MANAGEMENT
# ============================================
LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    """Load leaderboard from file."""
    if os.path.exists(LEADERBOARD_FILE):
        try:
            with open(LEADERBOARD_FILE, "r") as f:
                data = json.load(f)
                # Filter entries from last 24 hours only
                cutoff = datetime.now().timestamp() - (24 * 60 * 60)
                return [e for e in data if e.get("timestamp", 0) > cutoff]
        except:
            return []
    return []

def save_to_leaderboard(name, score, profit):
    """Save a player's score to the leaderboard."""
    leaderboard = load_leaderboard()
    leaderboard.append({
        "name": name,
        "score": score,
        "profit": profit,
        "timestamp": datetime.now().timestamp()
    })
    # Sort by score descending
    leaderboard.sort(key=lambda x: x["score"], reverse=True)
    # Keep top 50
    leaderboard = leaderboard[:50]
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(leaderboard, f)

# ============================================
# GAME DATA - EXPANDED OPTIONS
# ============================================
LOCATIONS = {
    "abandoned_warehouse": {
        "name": "Abandoned Warehouse",
        "icon": "🏚️",
        "cost": 3000,
        "capacity": 2000,
        "hype": 5,
        "risk": 10,
        "description": "Cheap and edgy, but limited space and might have safety issues. Popular with underground music fans."
    },
    "public_park": {
        "name": "Public Park",
        "icon": "🌳",
        "cost": 8000,
        "capacity": 8000,
        "hype": 10,
        "risk": 5,
        "description": "Affordable city park with good access. Requires permits but family-friendly atmosphere."
    },
    "open_field": {
        "name": "Countryside Field",
        "icon": "🏞️",
        "cost": 12000,
        "capacity": 15000,
        "hype": 15,
        "risk": 15,
        "description": "Large open space outside the city. Great for camping festivals but weather-dependent."
    },
    "city_stadium": {
        "name": "City Stadium",
        "icon": "🏟️",
        "cost": 25000,
        "capacity": 25000,
        "hype": 25,
        "risk": 5,
        "description": "Professional venue with excellent facilities. High cost but reliable infrastructure."
    },
    "beach_resort": {
        "name": "Beach Resort",
        "icon": "🏖️",
        "cost": 35000,
        "capacity": 12000,
        "hype": 40,
        "risk": 20,
        "description": "Premium beachfront location. Instagram-worthy but vulnerable to weather and limited parking."
    },
    "historic_castle": {
        "name": "Historic Castle",
        "icon": "🏰",
        "cost": 45000,
        "capacity": 8000,
        "hype": 50,
        "risk": 10,
        "description": "Unique medieval venue with incredible atmosphere. Limited capacity but unforgettable experience."
    },
}

ARTISTS = {
    "local_bands": {
        "name": "Local Bands Package",
        "icon": "🎸",
        "cost": 2000,
        "hype": 8,
        "description": "5 local bands eager to perform. Low cost, supports community, but limited draw power."
    },
    "tribute_acts": {
        "name": "Tribute Acts",
        "icon": "🎭",
        "cost": 5000,
        "hype": 15,
        "description": "Popular tribute bands covering famous artists. Crowd-pleasers at a reasonable price."
    },
    "rising_stars": {
        "name": "Rising Stars",
        "icon": "⭐",
        "cost": 12000,
        "hype": 25,
        "description": "Up-and-coming artists with growing fanbases. Good value with viral potential."
    },
    "famous_dj": {
        "name": "Famous DJ",
        "icon": "🎧",
        "cost": 25000,
        "hype": 40,
        "description": "Well-known DJ with millions of streams. Guarantees a party atmosphere."
    },
    "rock_legends": {
        "name": "Rock Legends",
        "icon": "🤘",
        "cost": 40000,
        "hype": 55,
        "description": "Legendary rock band reunion. Appeals to multiple generations of fans."
    },
    "global_superstar": {
        "name": "Global Superstar",
        "icon": "👑",
        "cost": 60000,
        "hype": 75,
        "description": "A-list celebrity performer. Massive draw but takes most of your budget."
    },
}

MARKETING = {
    "word_of_mouth": {
        "name": "Word of Mouth Only",
        "icon": "🗣️",
        "cost": 500,
        "hype": 5,
        "description": "Free marketing through friends and community. Slow but authentic growth."
    },
    "social_media": {
        "name": "Social Media Campaign",
        "icon": "📱",
        "cost": 3000,
        "hype": 15,
        "description": "Targeted ads on Instagram, TikTok, and Facebook. Good reach for young audiences."
    },
    "radio_posters": {
        "name": "Radio + Street Posters",
        "icon": "📻",
        "cost": 8000,
        "hype": 22,
        "description": "Traditional media mix. Reaches broader demographics including older audiences."
    },
    "influencer_package": {
        "name": "Influencer Partnership",
        "icon": "🤳",
        "cost": 15000,
        "hype": 35,
        "description": "Partner with 10 influencers for promotion. High engagement but unpredictable results."
    },
    "tv_billboard": {
        "name": "TV + Billboard Campaign",
        "icon": "📺",
        "cost": 25000,
        "hype": 45,
        "description": "Premium advertising on TV and city billboards. Maximum visibility and credibility."
    },
    "viral_stunt": {
        "name": "Viral Marketing Stunt",
        "icon": "🚀",
        "cost": 20000,
        "hype": 55,
        "risk_bonus": 15,
        "description": "High-risk creative stunt for viral attention. Could explode or flop completely."
    },
}

EXTRAS = {
    "basic_security": {
        "name": "Basic Security",
        "icon": "👮",
        "cost": 2000,
        "risk_reduction": 5,
        "description": "Minimum required security staff. Meets legal requirements but stretched thin."
    },
    "premium_security": {
        "name": "Premium Security",
        "icon": "🛡️",
        "cost": 8000,
        "risk_reduction": 15,
        "description": "Professional security team with medical staff. Peace of mind for everyone."
    },
    "food_trucks": {
        "name": "Food Truck Village",
        "icon": "🍔",
        "cost": 5000,
        "hype": 8,
        "revenue_bonus": 3,
        "description": "10 diverse food trucks. Additional revenue stream and keeps crowd happy."
    },
    "vip_area": {
        "name": "VIP Experience Zone",
        "icon": "🥂",
        "cost": 10000,
        "hype": 10,
        "revenue_bonus": 8,
        "description": "Exclusive VIP area with premium viewing. Attracts high-spending customers."
    },
    "eco_friendly": {
        "name": "Eco-Friendly Package",
        "icon": "♻️",
        "cost": 6000,
        "hype": 12,
        "description": "Sustainable practices, recycling, solar power. Great PR and attracts conscious consumers."
    },
    "live_streaming": {
        "name": "Live Stream Setup",
        "icon": "📡",
        "cost": 8000,
        "hype": 15,
        "description": "Professional live stream to reach global audience. Builds brand for future events."
    },
}

WEATHER_EFFECTS = {
    "perfect": {"name": "Perfect Sunny Day", "icon": "☀️", "multiplier": 1.25, "message": "Beautiful weather brings extra crowds!"},
    "good": {"name": "Partly Cloudy", "icon": "⛅", "multiplier": 1.1, "message": "Pleasant weather, comfortable for everyone."},
    "okay": {"name": "Overcast", "icon": "☁️", "multiplier": 1.0, "message": "Gray skies but no rain. Standard turnout."},
    "rain": {"name": "Light Rain", "icon": "🌧️", "multiplier": 0.75, "message": "Rain keeps some people home..."},
    "storm": {"name": "Thunderstorm", "icon": "⛈️", "multiplier": 0.5, "message": "Storm warning! Many stay home for safety."},
}

# ============================================
# INITIALIZE SESSION STATE
# ============================================
def init_game():
    """Initialize or reset the game state."""
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
    st.session_state.ticket_price = 45
    st.session_state.game_started = True
    st.session_state.result_saved = False

if "game_started" not in st.session_state:
    init_game()

if "player_name" not in st.session_state:
    st.session_state.player_name = ""

# ============================================
# HELPER FUNCTIONS
# ============================================
def display_stats():
    """Display current game statistics."""
    st.markdown(f"""
    <div class="stats-container">
        <div class="stat-card">
            <div class="stat-icon">💰</div>
            <div class="stat-value budget">€{st.session_state.budget:,}</div>
            <div class="stat-label">Budget</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">🔥</div>
            <div class="stat-value hype">{st.session_state.hype}</div>
            <div class="stat-label">Hype</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">👥</div>
            <div class="stat-value capacity">{st.session_state.capacity:,}</div>
            <div class="stat-label">Capacity</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def display_phase_indicator(current_phase):
    """Display progress through phases."""
    phases = ["Location", "Artists", "Marketing", "Extras", "Price"]
    dots_html = ""
    for i, phase in enumerate(phases):
        if i + 1 < current_phase:
            dots_html += '<div class="phase-dot completed"></div>'
        elif i + 1 == current_phase:
            dots_html += '<div class="phase-dot active"></div>'
        else:
            dots_html += '<div class="phase-dot"></div>'

    st.markdown(f'<div class="phase-indicator">{dots_html}</div>', unsafe_allow_html=True)

def display_leaderboard():
    """Display the current leaderboard."""
    leaderboard = load_leaderboard()

    if not leaderboard:
        st.markdown("""
        <div class="leaderboard-container">
            <div class="leaderboard-title">🏆 Leaderboard</div>
            <p style="text-align: center; color: #94a3b8;">No players yet. Be the first!</p>
        </div>
        """, unsafe_allow_html=True)
        return

    entries_html = ""
    for i, entry in enumerate(leaderboard[:10]):
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

        entries_html += f"""
        <div class="leaderboard-entry {entry_class}">
            <span class="player-rank">{rank_display}</span>
            <span class="player-name">{entry['name']}</span>
            <span class="player-score {score_class}">€{entry['profit']:,}</span>
        </div>
        """

    st.markdown(f"""
    <div class="leaderboard-container">
        <div class="leaderboard-title">🏆 Live Leaderboard</div>
        {entries_html}
    </div>
    """, unsafe_allow_html=True)

def render_choice_card(key, data, choice_type):
    """Render a choice card and handle selection."""
    cost = data["cost"]
    can_afford = st.session_state.budget >= cost

    stats_html = f'<span class="choice-stat cost">💰 €{cost:,}</span>'

    if "hype" in data:
        stats_html += f'<span class="choice-stat hype">🔥 +{data["hype"]} Hype</span>'
    if "capacity" in data:
        stats_html += f'<span class="choice-stat capacity">👥 {data["capacity"]:,}</span>'
    if "risk" in data:
        stats_html += f'<span class="choice-stat risk">⚠️ +{data["risk"]}% Risk</span>'
    if "risk_reduction" in data:
        stats_html += f'<span class="choice-stat capacity">🛡️ -{data["risk_reduction"]}% Risk</span>'
    if "revenue_bonus" in data:
        stats_html += f'<span class="choice-stat hype">💵 +€{data["revenue_bonus"]}/ticket</span>'

    st.markdown(f"""
    <div class="choice-card">
        <div class="choice-title">{data['icon']} {data['name']}</div>
        <div class="choice-description">{data['description']}</div>
        <div class="choice-stats">{stats_html}</div>
    </div>
    """, unsafe_allow_html=True)

    if can_afford:
        if st.button(f"Select {data['name']}", key=f"{choice_type}_{key}", use_container_width=True):
            return True
    else:
        st.button(f"❌ Can't afford (need €{cost:,})", key=f"{choice_type}_{key}", disabled=True, use_container_width=True)

    return False

# ============================================
# GAME PHASES
# ============================================
def show_start_screen():
    """Display the welcome screen with name entry."""
    st.markdown('<h1 class="main-title">🎪 Festival Manager</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Compete to build the most profitable music festival!</p>', unsafe_allow_html=True)

    display_leaderboard()

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <strong>How to Play:</strong><br>
        You have <strong>€50,000</strong> to organize a music festival.<br>
        Make strategic choices through 5 phases, set your ticket price, and hope for good weather!<br>
        <strong>Goal:</strong> Make the highest profit to top the leaderboard! 🏆
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    name = st.text_input("Enter your name to compete:", placeholder="Your name...", max_chars=20)

    if st.button("🚀 Start Game", type="primary", use_container_width=True):
        if name.strip():
            st.session_state.player_name = name.strip()
            st.session_state.phase = 1
            st.rerun()
        else:
            st.error("Please enter your name to play!")

def show_location_phase():
    """Phase 1: Choose location."""
    st.markdown('<h1 class="main-title">📍 Choose Location</h1>', unsafe_allow_html=True)
    display_phase_indicator(1)
    display_stats()
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown("**Where will you host your festival?** Each venue has different capacity, hype appeal, and risks.")

    for key, data in LOCATIONS.items():
        if render_choice_card(key, data, "location"):
            st.session_state.budget -= data["cost"]
            st.session_state.capacity = data["capacity"]
            st.session_state.hype += data["hype"]
            st.session_state.risk += data.get("risk", 0)
            st.session_state.location = data["name"]
            st.session_state.phase = 2
            st.rerun()

def show_artists_phase():
    """Phase 2: Choose artists."""
    st.markdown('<h1 class="main-title">🎵 Book Artists</h1>', unsafe_allow_html=True)
    display_phase_indicator(2)
    display_stats()
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown(f"**Location:** {st.session_state.location}")
    st.markdown("**Who will headline your festival?** Better artists = more hype, but higher costs.")

    for key, data in ARTISTS.items():
        if render_choice_card(key, data, "artist"):
            st.session_state.budget -= data["cost"]
            st.session_state.hype += data["hype"]
            st.session_state.artist = data["name"]
            st.session_state.phase = 3
            st.rerun()

def show_marketing_phase():
    """Phase 3: Choose marketing."""
    st.markdown('<h1 class="main-title">📢 Marketing Strategy</h1>', unsafe_allow_html=True)
    display_phase_indicator(3)
    display_stats()
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown(f"**Location:** {st.session_state.location} | **Artist:** {st.session_state.artist}")
    st.markdown("**How will you spread the word?** Marketing builds hype and drives ticket sales.")

    for key, data in MARKETING.items():
        if render_choice_card(key, data, "marketing"):
            st.session_state.budget -= data["cost"]
            st.session_state.hype += data["hype"]
            if "risk_bonus" in data:
                st.session_state.risk += data["risk_bonus"]
            st.session_state.marketing = data["name"]
            st.session_state.phase = 4
            st.rerun()

def show_extras_phase():
    """Phase 4: Choose extras."""
    st.markdown('<h1 class="main-title">✨ Extra Features</h1>', unsafe_allow_html=True)
    display_phase_indicator(4)
    display_stats()
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown("**Optional upgrades** to enhance your festival. Select any you can afford, then continue.")

    selected_extras = []

    for key, data in EXTRAS.items():
        cost = data["cost"]
        can_afford = st.session_state.budget >= cost
        already_selected = key in st.session_state.extras

        stats_html = f'<span class="choice-stat cost">💰 €{cost:,}</span>'
        if "hype" in data:
            stats_html += f'<span class="choice-stat hype">🔥 +{data["hype"]} Hype</span>'
        if "risk_reduction" in data:
            stats_html += f'<span class="choice-stat capacity">🛡️ -{data["risk_reduction"]}% Risk</span>'
        if "revenue_bonus" in data:
            stats_html += f'<span class="choice-stat hype">💵 +€{data["revenue_bonus"]}/ticket</span>'

        st.markdown(f"""
        <div class="choice-card">
            <div class="choice-title">{data['icon']} {data['name']}</div>
            <div class="choice-description">{data['description']}</div>
            <div class="choice-stats">{stats_html}</div>
        </div>
        """, unsafe_allow_html=True)

        if already_selected:
            st.button(f"✅ {data['name']} Added!", key=f"extra_{key}", disabled=True, use_container_width=True)
        elif can_afford:
            if st.button(f"Add {data['name']}", key=f"extra_{key}", use_container_width=True):
                st.session_state.budget -= data["cost"]
                st.session_state.hype += data.get("hype", 0)
                st.session_state.risk -= data.get("risk_reduction", 0)
                st.session_state.revenue_bonus += data.get("revenue_bonus", 0)
                st.session_state.extras.append(key)
                st.rerun()
        else:
            st.button(f"❌ Can't afford", key=f"extra_{key}", disabled=True, use_container_width=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    if st.button("➡️ Continue to Pricing", type="primary", use_container_width=True):
        st.session_state.phase = 5
        st.rerun()

def show_pricing_phase():
    """Phase 5: Set ticket price."""
    st.markdown('<h1 class="main-title">🎟️ Set Ticket Price</h1>', unsafe_allow_html=True)
    display_phase_indicator(5)
    display_stats()
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown("### Your Festival Summary")
    st.markdown(f"""
    - **Location:** {st.session_state.location}
    - **Headliner:** {st.session_state.artist}
    - **Marketing:** {st.session_state.marketing}
    - **Extras:** {', '.join([EXTRAS[e]['name'] for e in st.session_state.extras]) or 'None'}
    """)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown("**Set your ticket price carefully!**")
    st.markdown("Higher prices = more revenue per ticket, but fewer people will buy.")

    ticket_price = st.slider(
        "Ticket Price (€)",
        min_value=15,
        max_value=200,
        value=45,
        step=5,
        key="price_slider"
    )
    st.session_state.ticket_price = ticket_price

    # Calculate estimated demand
    base_demand = st.session_state.hype * 80
    price_factor = max(0.15, 1.2 - (ticket_price / 120))
    expected_demand = int(base_demand * price_factor)
    expected_attendance = min(expected_demand, st.session_state.capacity)

    total_ticket_revenue = expected_attendance * (ticket_price + st.session_state.revenue_bonus)
    total_spent = 50000 - st.session_state.budget
    expected_profit = total_ticket_revenue - total_spent

    st.markdown(f"""
    <div class="info-box">
        <strong>📊 Projected Results (before weather):</strong><br>
        Estimated attendance: ~{expected_attendance:,} people<br>
        Expected revenue: ~€{total_ticket_revenue:,}<br>
        Expected profit: ~€{expected_profit:,}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🎲 Launch Festival!", type="primary", use_container_width=True):
        st.session_state.phase = 6
        st.rerun()

def show_results():
    """Phase 6: Show final results."""
    st.markdown('<h1 class="main-title">🎪 Festival Day!</h1>', unsafe_allow_html=True)

    # Determine weather (with risk factor affecting bad weather chance)
    weather_weights = [15, 25, 30, 20, 10]  # Base weights
    risk_penalty = st.session_state.risk
    weather_weights[3] += risk_penalty  # More chance of rain
    weather_weights[4] += risk_penalty // 2  # More chance of storm

    weather_keys = list(WEATHER_EFFECTS.keys())
    weather_key = random.choices(weather_keys, weights=weather_weights, k=1)[0]
    weather = WEATHER_EFFECTS[weather_key]

    # Calculate attendance
    base_demand = st.session_state.hype * 80
    price_factor = max(0.15, 1.2 - (st.session_state.ticket_price / 120))
    demand = int(base_demand * price_factor * weather["multiplier"])

    # Add some randomness (+/- 15%)
    demand = int(demand * random.uniform(0.85, 1.15))

    actual_attendance = min(max(0, demand), st.session_state.capacity)

    # Calculate financials
    ticket_revenue = actual_attendance * st.session_state.ticket_price
    bonus_revenue = actual_attendance * st.session_state.revenue_bonus
    total_revenue = ticket_revenue + bonus_revenue
    total_spent = 50000 - st.session_state.budget
    profit = total_revenue - total_spent

    # Calculate score (profit + bonuses)
    score = profit

    # Weather display
    st.markdown(f"""
    <div style="text-align: center; font-size: 3rem; margin: 1rem 0;">
        {weather['icon']}
    </div>
    <div style="text-align: center; color: #e2e8f0; font-size: 1.2rem; margin-bottom: 0.5rem;">
        <strong>{weather['name']}</strong>
    </div>
    <div style="text-align: center; color: #94a3b8; margin-bottom: 1.5rem;">
        {weather['message']}
    </div>
    """, unsafe_allow_html=True)

    # Results metrics
    st.markdown(f"""
    <div class="metric-grid">
        <div class="metric-card">
            <div class="metric-value">👥 {actual_attendance:,}</div>
            <div class="metric-label">Attendance</div>
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
            <div class="metric-value">💸 €{total_spent:,}</div>
            <div class="metric-label">Costs</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Final result
    if profit > 30000:
        result_class = "success"
        result_title = "🏆 LEGENDARY SUCCESS!"
        result_subtitle = "You're a festival mogul!"
        st.balloons()
    elif profit > 10000:
        result_class = "success"
        result_title = "🎉 GREAT SUCCESS!"
        result_subtitle = "Solid profit! Well managed!"
    elif profit > 0:
        result_class = "success"
        result_title = "✅ PROFIT!"
        result_subtitle = "You made money! Not bad!"
    elif profit > -10000:
        result_class = "failure"
        result_title = "😅 SMALL LOSS"
        result_subtitle = "Close, but not quite..."
    else:
        result_class = "failure"
        result_title = "💸 BANKRUPT!"
        result_subtitle = "Your festival was a disaster!"

    st.markdown(f"""
    <div class="result-card {result_class}">
        <div class="result-title">{result_title}</div>
        <div class="result-subtitle">{result_subtitle}</div>
        <div style="font-size: 2.5rem; font-weight: 700; margin-top: 1rem;">
            €{profit:,}
        </div>
        <div style="opacity: 0.8;">Final Profit/Loss</div>
    </div>
    """, unsafe_allow_html=True)

    # Save to leaderboard (only once)
    if not st.session_state.result_saved:
        save_to_leaderboard(st.session_state.player_name, score, profit)
        st.session_state.result_saved = True

    # Show leaderboard
    st.markdown("<br>", unsafe_allow_html=True)
    display_leaderboard()

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🔄 Play Again", type="primary", use_container_width=True):
        init_game()
        st.session_state.result_saved = False
        st.rerun()

# ============================================
# MAIN GAME LOOP
# ============================================
def main():
    """Main function to run the game."""
    phase = st.session_state.phase

    if phase == 0:
        show_start_screen()
    elif phase == 1:
        show_location_phase()
    elif phase == 2:
        show_artists_phase()
    elif phase == 3:
        show_marketing_phase()
    elif phase == 4:
        show_extras_phase()
    elif phase == 5:
        show_pricing_phase()
    elif phase == 6:
        show_results()

if __name__ == "__main__":
    main()
