import streamlit as st
import random

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
# CUSTOM CSS FOR MOBILE-FRIENDLY UI
# ============================================
st.markdown("""
<style>
    /* Mobile-friendly styling */
    .stButton > button {
        width: 100%;
        padding: 0.75rem;
        font-size: 1.1rem;
        border-radius: 10px;
        margin: 0.25rem 0;
    }

    .stat-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin: 0.5rem 0;
    }

    .stat-value {
        font-size: 1.8rem;
        font-weight: bold;
    }

    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }

    .phase-header {
        background: linear-gradient(90deg, #11998e, #38ef7d);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 1rem;
    }

    .choice-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 0.5rem 0;
    }

    .result-success {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
    }

    .result-failure {
        background: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# GAME DATA - CHOICES FOR EACH PHASE
# ============================================
LOCATIONS = {
    "Open Field (Cheap)": {"cost": 5000, "capacity": 5000, "hype": 5, "icon": "🏞️"},
    "City Stadium": {"cost": 15000, "capacity": 15000, "hype": 15, "icon": "🏟️"},
    "Beach Paradise": {"cost": 25000, "capacity": 10000, "hype": 30, "icon": "🏖️"},
    "Historic Castle": {"cost": 35000, "capacity": 8000, "hype": 40, "icon": "🏰"},
}

ARTISTS = {
    "Local Bands": {"cost": 3000, "hype": 10, "icon": "🎸"},
    "Rising Stars": {"cost": 10000, "hype": 25, "icon": "🎤"},
    "Famous DJ": {"cost": 20000, "hype": 40, "icon": "⭐"},
    "Superstar Headliner": {"cost": 40000, "hype": 60, "icon": "👑"},
}

MARKETING = {
    "Social Media Only": {"cost": 1000, "hype": 10, "icon": "📱"},
    "Radio + Posters": {"cost": 5000, "hype": 20, "icon": "📻"},
    "TV Commercial": {"cost": 15000, "hype": 35, "icon": "📺"},
    "Viral Campaign + Influencers": {"cost": 25000, "hype": 50, "icon": "🚀"},
}

WEATHER_EFFECTS = {
    "Perfect Sunny Day ☀️": 1.2,
    "Partly Cloudy ⛅": 1.0,
    "Light Rain 🌧️": 0.7,
    "Thunderstorm ⛈️": 0.4,
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
    st.session_state.location = None
    st.session_state.artist = None
    st.session_state.marketing = None
    st.session_state.ticket_price = 50
    st.session_state.game_started = True

if "game_started" not in st.session_state:
    init_game()

# ============================================
# HELPER FUNCTIONS
# ============================================
def display_stats():
    """Display current game statistics."""
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-label">💰 Budget</div>
            <div class="stat-value">€{st.session_state.budget:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-label">🔥 Hype</div>
            <div class="stat-value">{st.session_state.hype}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-label">👥 Capacity</div>
            <div class="stat-value">{st.session_state.capacity:,}</div>
        </div>
        """, unsafe_allow_html=True)

def make_choice(choice_name, choice_data, choice_type):
    """Process a player's choice."""
    cost = choice_data["cost"]

    if st.session_state.budget >= cost:
        st.session_state.budget -= cost
        st.session_state.hype += choice_data.get("hype", 0)

        if "capacity" in choice_data:
            st.session_state.capacity = choice_data["capacity"]

        if choice_type == "location":
            st.session_state.location = choice_name
        elif choice_type == "artist":
            st.session_state.artist = choice_name
        elif choice_type == "marketing":
            st.session_state.marketing = choice_name

        st.session_state.phase += 1
        st.rerun()
    else:
        st.error("❌ Not enough budget! Choose a cheaper option.")

# ============================================
# GAME PHASES
# ============================================
def show_start_screen():
    """Display the welcome screen."""
    st.markdown("# 🎪 Festival Manager")
    st.markdown("### Can you run a successful music festival?")

    st.markdown("""
    ---
    **Welcome, Festival Director!**

    You have **€50,000** to organize the ultimate music festival.

    Make smart choices through 3 phases:
    1. 📍 **Choose your Location**
    2. 🎵 **Book your Artists**
    3. 📢 **Plan your Marketing**

    Then set your ticket price and hope for good weather!

    **Goal:** Sell tickets, cover costs, and make a profit!

    ---
    """)

    if st.button("🚀 Start Game", type="primary", use_container_width=True):
        st.session_state.phase = 1
        st.rerun()

def show_location_phase():
    """Phase 1: Choose location."""
    st.markdown('<div class="phase-header"><h2>📍 Phase 1: Choose Location</h2></div>', unsafe_allow_html=True)

    display_stats()

    st.markdown("---")
    st.markdown("**Where will you host your festival?**")

    for name, data in LOCATIONS.items():
        with st.container():
            st.markdown(f"""
            <div class="choice-card">
                <strong>{data['icon']} {name}</strong><br>
                💰 Cost: €{data['cost']:,} | 👥 Capacity: {data['capacity']:,} | 🔥 Hype: +{data['hype']}
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Select {name}", key=f"loc_{name}"):
                make_choice(name, data, "location")

def show_artists_phase():
    """Phase 2: Choose artists."""
    st.markdown('<div class="phase-header"><h2>🎵 Phase 2: Book Artists</h2></div>', unsafe_allow_html=True)

    display_stats()

    st.markdown("---")
    st.markdown(f"**Location:** {st.session_state.location}")
    st.markdown("**Who will perform at your festival?**")

    for name, data in ARTISTS.items():
        with st.container():
            st.markdown(f"""
            <div class="choice-card">
                <strong>{data['icon']} {name}</strong><br>
                💰 Cost: €{data['cost']:,} | 🔥 Hype: +{data['hype']}
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Book {name}", key=f"art_{name}"):
                make_choice(name, data, "artist")

def show_marketing_phase():
    """Phase 3: Choose marketing."""
    st.markdown('<div class="phase-header"><h2>📢 Phase 3: Marketing Campaign</h2></div>', unsafe_allow_html=True)

    display_stats()

    st.markdown("---")
    st.markdown(f"**Location:** {st.session_state.location}")
    st.markdown(f"**Artist:** {st.session_state.artist}")
    st.markdown("**How will you promote your festival?**")

    for name, data in MARKETING.items():
        with st.container():
            st.markdown(f"""
            <div class="choice-card">
                <strong>{data['icon']} {name}</strong><br>
                💰 Cost: €{data['cost']:,} | 🔥 Hype: +{data['hype']}
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Choose {name}", key=f"mkt_{name}"):
                make_choice(name, data, "marketing")

def show_pricing_phase():
    """Phase 4: Set ticket price."""
    st.markdown('<div class="phase-header"><h2>🎟️ Final Step: Set Ticket Price</h2></div>', unsafe_allow_html=True)

    display_stats()

    st.markdown("---")
    st.markdown("### Your Festival Setup:")
    st.markdown(f"- **Location:** {st.session_state.location}")
    st.markdown(f"- **Artist:** {st.session_state.artist}")
    st.markdown(f"- **Marketing:** {st.session_state.marketing}")

    st.markdown("---")
    st.markdown("**Set your ticket price:**")
    st.markdown("*Higher price = more revenue per ticket, but fewer people will come!*")

    ticket_price = st.slider(
        "Ticket Price (€)",
        min_value=10,
        max_value=150,
        value=50,
        step=5,
        key="price_slider"
    )
    st.session_state.ticket_price = ticket_price

    # Show demand preview
    base_demand = st.session_state.hype * 100
    price_factor = max(0.1, 1 - (ticket_price - 30) / 150)
    expected_demand = int(base_demand * price_factor)

    st.info(f"📊 With {st.session_state.hype} Hype and €{ticket_price} tickets, estimated demand: ~{expected_demand:,} people")

    if st.button("🎲 Launch Festival!", type="primary", use_container_width=True):
        st.session_state.phase = 5
        st.rerun()

def show_results():
    """Phase 5: Show final results."""
    st.markdown("# 🎪 Festival Day!")
    st.markdown("---")

    # Random weather
    weather, weather_multiplier = random.choice(list(WEATHER_EFFECTS.items()))

    # Calculate attendance
    base_demand = st.session_state.hype * 100
    price_factor = max(0.1, 1 - (st.session_state.ticket_price - 30) / 150)
    demand = int(base_demand * price_factor * weather_multiplier)

    # Cap at capacity
    actual_attendance = min(demand, st.session_state.capacity)

    # Calculate revenue
    revenue = actual_attendance * st.session_state.ticket_price
    total_spent = 50000 - st.session_state.budget
    profit = revenue - total_spent

    # Display weather
    st.markdown(f"### Weather Report: {weather}")
    if weather_multiplier >= 1.0:
        st.success("Great weather boosts attendance!")
    else:
        st.warning("Bad weather reduces attendance...")

    st.markdown("---")

    # Display breakdown
    st.markdown("### 📊 Financial Report")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("👥 Attendance", f"{actual_attendance:,}")
        st.metric("🎟️ Ticket Price", f"€{st.session_state.ticket_price}")
        st.metric("💵 Revenue", f"€{revenue:,}")

    with col2:
        st.metric("📍 Capacity", f"{st.session_state.capacity:,}")
        st.metric("💸 Total Costs", f"€{total_spent:,}")
        st.metric("📈 Profit/Loss", f"€{profit:,}", delta=f"€{profit:,}")

    st.markdown("---")

    # Final verdict
    if profit > 20000:
        st.markdown("""
        <div class="result-success">
            <h1>🏆 LEGENDARY SUCCESS!</h1>
            <p>You're the next big festival mogul!</p>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
    elif profit > 0:
        st.markdown("""
        <div class="result-success">
            <h1>✅ SUCCESS!</h1>
            <p>You made a profit! Well done!</p>
        </div>
        """, unsafe_allow_html=True)
    elif profit > -10000:
        st.markdown("""
        <div class="result-failure">
            <h1>😅 SMALL LOSS</h1>
            <p>You lost some money, but you'll survive!</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="result-failure">
            <h1>💸 BANKRUPT!</h1>
            <p>Your festival was a financial disaster!</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    if st.button("🔄 Play Again", type="primary", use_container_width=True):
        init_game()
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
        show_pricing_phase()
    elif phase == 5:
        show_results()

if __name__ == "__main__":
    main()
