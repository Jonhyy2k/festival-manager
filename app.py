import streamlit as st
import random

# ============================================
# PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="Gestor de Festivais",
    page_icon="🎪",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================
# CLEAN MODERN CSS — MOBILE-FIRST, BIG TEXT
# ============================================
st.markdown("""
<style>
    .stApp {
        background: #0f172a;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #cbd5e1;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Story Card */
    .story-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-left: 4px solid #6366f1;
        border-radius: 8px;
        padding: 1.75rem;
        margin: 1.25rem 0;
    }

    .story-icon {
        font-size: 3rem;
        margin-bottom: 0.75rem;
        display: block;
        text-align: center;
    }

    .story-title {
        color: #f1f5f9;
        font-size: 1.35rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
        text-align: center;
    }

    .story-text {
        color: #94a3b8;
        font-size: 1.05rem;
        line-height: 1.7;
        text-align: center;
    }

    /* Main Title */
    .main-title {
        text-align: center;
        padding: 1.25rem 0;
        color: #f1f5f9;
        font-size: 2.2rem;
        font-weight: 800;
    }

    .subtitle {
        text-align: center;
        color: #64748b;
        font-size: 1.05rem;
        margin-bottom: 1.25rem;
    }

    /* Stats Display */
    .stats-container {
        display: flex;
        justify-content: center;
        gap: 0.5rem;
        margin: 0.5rem 0;
        flex-wrap: wrap;
    }

    .stat-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 0.6rem 1rem;
        text-align: center;
        min-width: 85px;
        flex: 1;
        max-width: 120px;
    }

    .stat-value {
        font-size: 1.15rem;
        font-weight: 700;
        color: #f1f5f9;
    }

    .stat-value.budget { color: #10b981; }
    .stat-value.budget.low { color: #f59e0b; }
    .stat-value.budget.critical { color: #ef4444; }
    .stat-value.hype { color: #a78bfa; }
    .stat-value.capacity { color: #60a5fa; }
    .stat-value.risk { color: #fb923c; }
    .stat-value.reputation { color: #c084fc; }
    .stat-value.morale { color: #fbbf24; }
    .stat-value.safety { color: #38bdf8; }
    .stat-value.sustainability { color: #34d399; }
    .stat-value.satisfaction { color: #f472b6; }

    .stat-label {
        font-size: 0.7rem;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 0.15rem;
    }

    /* Phase Progress */
    .phase-progress {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 0.4rem;
        margin: 1rem 0;
    }

    .phase-step {
        width: 44px;
        height: 6px;
        border-radius: 3px;
        background: #334155;
    }

    .phase-step.completed { background: #10b981; }
    .phase-step.active { background: #6366f1; }

    /* Choice Cards */
    .choice-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 1.25rem;
        margin: 0.75rem 0;
    }

    .choice-card:hover {
        border-color: #6366f1;
    }

    .choice-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #f1f5f9;
        margin-bottom: 0.4rem;
    }

    .choice-description {
        font-size: 0.95rem;
        color: #94a3b8;
        margin-bottom: 0.6rem;
        line-height: 1.5;
    }

    .choice-stats {
        display: flex;
        gap: 0.4rem;
        flex-wrap: wrap;
    }

    .choice-stat {
        background: #0f172a;
        padding: 0.3rem 0.6rem;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 600;
        color: #94a3b8;
    }

    .choice-stat.cost { color: #ef4444; }
    .choice-stat.hype { color: #a78bfa; }
    .choice-stat.capacity { color: #60a5fa; }
    .choice-stat.risk { color: #fb923c; }
    .choice-stat.bonus { color: #10b981; }

    /* Buttons */
    .stButton > button {
        width: 100%;
        background: #6366f1 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.85rem 1.25rem !important;
        font-size: 1.05rem !important;
        font-weight: 700 !important;
        min-height: 48px !important;
    }

    .stButton > button:hover {
        background: #4f46e5 !important;
    }

    .stButton > button:disabled {
        background: #334155 !important;
        color: #64748b !important;
    }

    /* Event Card */
    .event-card {
        border-radius: 8px;
        padding: 1.25rem;
        margin: 0.75rem 0;
        text-align: center;
    }

    .event-card.disaster {
        background: #1c0a0f;
        border: 1px solid #ef4444;
    }

    .event-card.problem {
        background: #1c150a;
        border: 1px solid #f59e0b;
    }

    .event-card.lucky {
        background: #0a1c12;
        border: 1px solid #10b981;
    }

    .event-icon {
        font-size: 2.5rem;
        margin-bottom: 0.4rem;
    }

    .event-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #f1f5f9;
        margin-bottom: 0.4rem;
    }

    .event-description {
        color: #94a3b8;
        font-size: 1rem;
        line-height: 1.5;
    }

    .event-impact {
        margin-top: 0.6rem;
        padding: 0.4rem 0.8rem;
        background: rgba(255, 255, 255, 0.06);
        border-radius: 6px;
        display: inline-block;
        font-weight: 700;
        font-size: 1rem;
        color: #e2e8f0;
    }

    /* Results */
    .result-card {
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        margin: 1.25rem 0;
    }

    .result-card.success {
        background: #0a1c12;
        border: 2px solid #10b981;
    }

    .result-card.failure {
        background: #1c0a0f;
        border: 2px solid #ef4444;
    }

    .result-card.bankrupt {
        background: #1a1a1a;
        border: 2px solid #475569;
    }

    .result-card.legendary {
        background: #150a1c;
        border: 2px solid #a78bfa;
    }

    .result-title {
        font-size: 1.7rem;
        font-weight: 800;
        color: #f1f5f9;
    }

    .result-profit {
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0.75rem 0;
    }

    .result-profit.positive { color: #10b981; }
    .result-profit.negative { color: #ef4444; }

    /* Metric Grid */
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 0.6rem;
        margin: 1rem 0;
    }

    .metric-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
    }

    .metric-value {
        font-size: 1.3rem;
        font-weight: 700;
        color: #f1f5f9;
    }

    .metric-label {
        font-size: 0.8rem;
        color: #64748b;
        margin-top: 0.2rem;
    }

    /* Divider */
    .divider {
        height: 1px;
        background: #334155;
        margin: 1.5rem 0;
    }

    /* Warning box */
    .warning-box {
        background: #1c150a;
        border: 1px solid #f59e0b;
        border-radius: 8px;
        padding: 1rem;
        color: #fbbf24;
        font-size: 1rem;
        font-weight: 600;
        margin: 0.75rem 0;
    }

    /* Info box */
    .info-box {
        background: #0c1a2e;
        border: 1px solid #3b82f6;
        border-radius: 8px;
        padding: 1rem;
        color: #93c5fd;
        font-size: 1rem;
        line-height: 1.6;
    }

    /* Financial Breakdown */
    .breakdown-container {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 1.25rem;
        margin: 1rem 0;
    }

    .breakdown-header {
        color: #f1f5f9;
        font-size: 1.1rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .financial-line {
        display: flex;
        justify-content: space-between;
        padding: 0.45rem 0.6rem;
        margin: 0.15rem 0;
        border-radius: 4px;
    }

    .financial-line:nth-child(even) {
        background: rgba(255, 255, 255, 0.03);
    }

    .financial-line .fl-label {
        color: #94a3b8;
        font-size: 1rem;
    }

    .financial-line .fl-value {
        font-weight: 700;
        font-size: 1rem;
    }

    .financial-line .fl-value.positive { color: #10b981; }
    .financial-line .fl-value.negative { color: #ef4444; }

    .breakdown-total {
        display: flex;
        justify-content: space-between;
        padding: 0.7rem 0.6rem;
        margin-top: 0.6rem;
        border-top: 2px solid #334155;
        font-weight: 700;
        font-size: 1.1rem;
    }

    .breakdown-total .fl-label { color: #f1f5f9; }

    /* Aftermath Cards */
    .aftermath-card {
        border-radius: 8px;
        padding: 1.25rem;
        margin: 0.75rem 0;
        text-align: center;
    }

    .aftermath-card.positive {
        background: #0a1c12;
        border: 1px solid #10b981;
    }

    .aftermath-card.negative {
        background: #1c0a0f;
        border: 1px solid #ef4444;
    }

    .aftermath-card.neutral {
        background: #1e293b;
        border: 1px solid #334155;
    }

    .aftermath-card.severe {
        background: #1c0a0f;
        border: 2px solid #ef4444;
    }

    .aftermath-card.great {
        background: #0a1c12;
        border: 2px solid #10b981;
    }

    .aftermath-category {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #64748b;
        margin-bottom: 0.3rem;
    }

    .aftermath-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #f1f5f9;
        margin-bottom: 0.5rem;
    }

    .aftermath-text {
        color: #94a3b8;
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 0.75rem;
    }

    .aftermath-impact {
        display: inline-block;
        padding: 0.4rem 1rem;
        border-radius: 6px;
        font-weight: 700;
        font-size: 1.05rem;
    }

    .aftermath-impact.gain {
        background: #0a1c12;
        color: #10b981;
    }

    .aftermath-impact.loss {
        background: #1c0a0f;
        color: #ef4444;
    }

    .aftermath-impact.none {
        background: #1e293b;
        color: #64748b;
    }

    /* Section Header */
    .section-header {
        text-align: center;
        padding: 1.5rem 0 0.5rem;
        color: #f1f5f9;
        font-size: 1.5rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Adjustment Summary */
    .adjustment-summary {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 1.25rem;
        margin: 1rem 0;
        text-align: center;
    }

    .adjustment-line {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 0;
        font-size: 1.05rem;
        color: #94a3b8;
    }

    .adjustment-line .value {
        font-weight: 700;
        font-size: 1.15rem;
    }

    .adjustment-line .value.positive { color: #10b981; }
    .adjustment-line .value.negative { color: #ef4444; }

    /* Streamlit slider label */
    .stSlider label {
        font-size: 1.05rem !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# STORY NARRATIVES
# ============================================
STORIES = {
    "intro": {
        "icon": "🎪",
        "title": "O Teu Sonho Começa",
        "text": "Sempre sonhaste em gerir o teu próprio festival de música. Depois de anos a poupar, finalmente tens 50.000€ para o tornar realidade.\n\nMas fica avisado: a maioria dos festivais falha. Mau tempo, planeamento fraco ou simplesmente azar podem transformar o teu sonho num pesadelo. E mesmo que o festival corra bem, as consequências podem destruir-te.\n\nCada decisão conta. Escolhe com cuidado."
    },
    "location": {
        "icon": "📍",
        "title": "Capítulo 1: Encontrar o Palco",
        "text": "O teu telemóvel não para com mensagens de donos de recintos.\n\nO local que escolheres vai definir o teu festival. Um armazém barato pode poupar dinheiro, mas alguém vai aparecer? Um resort de praia soa incrível, mas e se chover?\n\nLembra-te: maior capacidade significa mais bilhetes potenciais, mas também mais risco se as pessoas não aparecerem."
    },
    "artists": {
        "icon": "🎤",
        "title": "Capítulo 2: Contratar o Talento",
        "text": "O teu recinto está garantido. Agora precisas de alguém para atuar.\n\nArtistas famosos garantem multidões mas devoram o teu orçamento. Bandas desconhecidas são baratas mas podem não atrair ninguém.\n\nA indústria musical é brutal: uma escolha errada aqui pode levar-te à falência antes sequer de abrir portas."
    },
    "marketing": {
        "icon": "📢",
        "title": "Capítulo 3: Espalhar a Palavra",
        "text": "Tens um recinto. Tens artistas. Mas alguém sabe do festival?\n\nO marketing é onde os festivais se ganham ou perdem. Pouco, e vais tocar para um campo vazio. Demasiado numa acção viral arriscada, e podes desperdiçar tudo.\n\nEscolhe a tua estratégia com cuidado."
    },
    "extras": {
        "icon": "✨",
        "title": "Capítulo 4: Os Toques Finais",
        "text": "O festival está a ganhar forma. Mas os detalhes importam.\n\nSegurança mantém todos seguros (e evita processos). Food trucks podem trazer receita extra — ou problemas extra. Zonas VIP atraem grandes gastadores, mas custam dinheiro a montar.\n\nCada euro gasto aqui é um euro a menos para emergências."
    },
    "pricing": {
        "icon": "🎟️",
        "title": "Capítulo 5: O Momento da Verdade",
        "text": "Está tudo pronto. Agora vem a decisão mais difícil: o preço do bilhete.\n\nPreço demasiado alto? As pessoas ficam em casa. Preço demasiado baixo? Não cobres os custos.\n\nE lembra-te: não podes controlar o tempo. Uma tempestade pode destruir tudo o que construíste.\n\nRespira fundo. Define o preço. E espera pelo melhor."
    },
    "results": {
        "icon": "🎭",
        "title": "Dia do Festival",
        "text": "Os portões estão abertos. A música está a tocar.\n\nAgora só podes observar e esperar...\n\nFizeste as escolhas certas?"
    }
}

# ============================================
# RANDOM EVENTS - GOOD AND BAD
# ============================================
RANDOM_EVENTS = {
    "disasters": [
        {
            "name": "Falha do Sistema de Som",
            "icon": "🔇",
            "description": "As colunas principais explodiram durante a montagem. Substituições de emergência custam uma fortuna.",
            "cost": 8000,
            "hype_loss": 10,
            "fan_satisfaction_mod": -20,
            "staff_morale_mod": -10,
            "chance": 0.08
        },
        {
            "name": "Cabeça de Cartaz Cancela",
            "icon": "😱",
            "description": "O teu artista principal publicou no Instagram: 'Não me estou a sentir bem hoje.' Reembolsos exigidos!",
            "attendance_multiplier": 0.5,
            "hype_loss": 30,
            "fan_satisfaction_mod": -25,
            "reputation_mod": -15,
            "chance": 0.05
        },
        {
            "name": "Surto de Intoxicação Alimentar",
            "icon": "🤢",
            "description": "Um food truck serviu camarão estragado. Metade do público está doente. Processos judiciais a caminho.",
            "cost": 15000,
            "attendance_multiplier": 0.7,
            "safety_mod": -20,
            "fan_satisfaction_mod": -25,
            "reputation_mod": -15,
            "chance": 0.06
        },
        {
            "name": "Incidente de Segurança",
            "icon": "🚨",
            "description": "Uma briga rebentou e tornou-se viral pelas piores razões. As pessoas estão a ir embora.",
            "attendance_multiplier": 0.6,
            "hype_loss": 20,
            "safety_mod": -15,
            "staff_morale_mod": -10,
            "fan_satisfaction_mod": -15,
            "chance": 0.07
        },
        {
            "name": "Falha na Rede Elétrica",
            "icon": "⚡",
            "description": "Todo o recinto ficou sem energia. Os geradores custam extra e o atraso matou a vibe.",
            "cost": 5000,
            "attendance_multiplier": 0.8,
            "fan_satisfaction_mod": -15,
            "staff_morale_mod": -10,
            "chance": 0.06
        },
        {
            "name": "Colapso do Palco",
            "icon": "💥",
            "description": "A estrutura do palco principal colapsa durante a montagem. Feridos reportados. O festival pode não continuar.",
            "cost": 25000,
            "attendance_multiplier": 0.3,
            "hype_loss": 40,
            "safety_mod": -30,
            "reputation_mod": -25,
            "fan_satisfaction_mod": -30,
            "staff_morale_mod": -25,
            "chance": 0.03
        },
        {
            "name": "Escândalo de Drogas do Artista",
            "icon": "🚔",
            "description": "O teu cabeça de cartaz foi detido nos bastidores. A imprensa desce sobre o festival. Os pais estão furiosos.",
            "cost": 10000,
            "attendance_multiplier": 0.6,
            "hype_loss": 25,
            "reputation_mod": -30,
            "fan_satisfaction_mod": -20,
            "chance": 0.04
        },
        {
            "name": "Pânico de Debandada",
            "icon": "🏃",
            "description": "Um falso alarme causa uma debandada no portão principal. Múltiplos feridos. Serviços de emergência chamados.",
            "cost": 20000,
            "attendance_multiplier": 0.4,
            "safety_mod": -35,
            "staff_morale_mod": -20,
            "fan_satisfaction_mod": -30,
            "reputation_mod": -20,
            "chance": 0.02
        },
    ],
    "problems": [
        {
            "name": "Pesadelo de Trânsito",
            "icon": "🚗",
            "description": "Engarrafamento massivo. Muitos portadores de bilhetes não conseguiram chegar a tempo.",
            "attendance_multiplier": 0.85,
            "fan_satisfaction_mod": -10,
            "chance": 0.12
        },
        {
            "name": "Evento Concorrente",
            "icon": "🎪",
            "description": "Um festival rival anunciou um evento gratuito surpresa nas proximidades. Algumas pessoas foram para lá.",
            "attendance_multiplier": 0.8,
            "reputation_mod": -5,
            "chance": 0.10
        },
        {
            "name": "Problemas com Licenças",
            "icon": "📋",
            "description": "Problemas de última hora com licenças. Tiveste de pagar 'taxas expresso' aos funcionários da câmara.",
            "cost": 4000,
            "staff_morale_mod": -5,
            "chance": 0.10
        },
        {
            "name": "Sobretaxa de Equipamento",
            "icon": "💸",
            "description": "A empresa de equipamento cobrou-te taxas escondidas à última hora.",
            "cost": 3000,
            "staff_morale_mod": -5,
            "chance": 0.12
        },
        {
            "name": "Crítica Negativa Viral",
            "icon": "📱",
            "description": "Um influencer publicou uma avaliação de 1 estrela antes do festival sequer começar.",
            "hype_loss": 15,
            "attendance_multiplier": 0.9,
            "reputation_mod": -10,
            "fan_satisfaction_mod": -5,
            "chance": 0.08
        },
        {
            "name": "Greve de Vendedores",
            "icon": "✊",
            "description": "Os vendedores de comida recusam-se a abrir devido a uma disputa de pagamento. Multidões com fome são multidões zangadas.",
            "fan_satisfaction_mod": -15,
            "staff_morale_mod": -10,
            "attendance_multiplier": 0.9,
            "chance": 0.08
        },
        {
            "name": "Queixas de Ruído",
            "icon": "🔊",
            "description": "Os vizinhos apresentam queixas de ruído. A polícia obriga-te a baixar o volume. A música mal se ouve.",
            "fan_satisfaction_mod": -10,
            "hype_loss": 5,
            "reputation_mod": -5,
            "chance": 0.10
        },
    ],
    "lucky": [
        {
            "name": "Celebridade Avistada!",
            "icon": "⭐",
            "description": "Uma celebridade famosa apareceu inesperadamente! Toda a gente está a publicar sobre isso.",
            "hype_bonus": 20,
            "attendance_multiplier": 1.2,
            "reputation_mod": 15,
            "fan_satisfaction_mod": 10,
            "chance": 0.05
        },
        {
            "name": "Momento Viral no TikTok",
            "icon": "📱",
            "description": "Um vídeo do teu festival está em tendência! Marketing gratuito!",
            "hype_bonus": 15,
            "attendance_multiplier": 1.15,
            "reputation_mod": 10,
            "chance": 0.08
        },
        {
            "name": "Cobertura nos Noticiários",
            "icon": "📺",
            "description": "Os noticiários locais fizeram uma reportagem positiva sobre o teu festival!",
            "hype_bonus": 10,
            "attendance_multiplier": 1.1,
            "reputation_mod": 5,
            "chance": 0.10
        },
        {
            "name": "Artista Convidado Surpresa",
            "icon": "🎤",
            "description": "Um artista de renome na zona passa para um set surpresa! O público enlouquece.",
            "hype_bonus": 25,
            "attendance_multiplier": 1.25,
            "reputation_mod": 20,
            "fan_satisfaction_mod": 15,
            "chance": 0.03
        },
        {
            "name": "Logística Perfeita",
            "icon": "✅",
            "description": "Tudo corre como um relógio. A equipa está adiantada. Os participantes estão impressionados.",
            "staff_morale_mod": 15,
            "fan_satisfaction_mod": 10,
            "safety_mod": 10,
            "chance": 0.07
        },
    ]
}

WEATHER_EFFECTS = {
    "perfect": {
        "name": "Dia de Sol Perfeito", "icon": "☀️", "multiplier": 1.2,
        "message": "Tempo maravilhoso! Apareceram pessoas extra!",
        "fan_satisfaction_mod": 10, "staff_morale_mod": 5
    },
    "good": {
        "name": "Parcialmente Nublado", "icon": "⛅", "multiplier": 1.05,
        "message": "Tempo agradável. Confortável para todos.",
        "fan_satisfaction_mod": 5, "staff_morale_mod": 5
    },
    "okay": {
        "name": "Encoberto", "icon": "☁️", "multiplier": 0.95,
        "message": "Céu cinzento. Algumas pessoas decidiram ficar em casa.",
        "fan_satisfaction_mod": -5
    },
    "rain": {
        "name": "Dia Chuvoso", "icon": "🌧️", "multiplier": 0.65,
        "message": "Está a chover. Muitos ficaram em casa.",
        "fan_satisfaction_mod": -15, "safety_mod": -10,
        "staff_morale_mod": -10, "sustainability_mod": -5
    },
    "storm": {
        "name": "Tempestade Severa", "icon": "⛈️", "multiplier": 0.35,
        "message": "Tempestade perigosa! A maioria das pessoas ficou longe!",
        "fan_satisfaction_mod": -25, "safety_mod": -20,
        "staff_morale_mod": -20
    },
}

# ============================================
# GAME DATA
# ============================================
LOCATIONS = {
    "warehouse": {
        "name": "Armazém Abandonado",
        "icon": "🏚️",
        "cost": 3000,
        "capacity": 2000,
        "hype": 5,
        "risk": 20,
        "reputation": -5,
        "staff_morale": -5,
        "safety": -15,
        "sustainability": -10,
        "fan_satisfaction": -5,
        "description": "Barato e alternativo. Sem ar condicionado, bairro duvidoso, mas vibes underground autênticas."
    },
    "park": {
        "name": "Parque da Cidade",
        "icon": "🌳",
        "cost": 8000,
        "capacity": 6000,
        "hype": 10,
        "risk": 10,
        "reputation": 5,
        "staff_morale": 5,
        "safety": 5,
        "sustainability": 10,
        "fan_satisfaction": 10,
        "description": "Parque público com licenças. Familiar mas com restrições de ruído."
    },
    "field": {
        "name": "Campo Rural",
        "icon": "🏞️",
        "cost": 12000,
        "capacity": 12000,
        "hype": 15,
        "risk": 25,
        "reputation": 5,
        "staff_morale": 0,
        "safety": -5,
        "sustainability": 5,
        "fan_satisfaction": 5,
        "description": "Espaço aberto amplo. Ótimo para campismo, mas muito dependente do tempo."
    },
    "stadium": {
        "name": "Estádio Municipal",
        "icon": "🏟️",
        "cost": 28000,
        "capacity": 20000,
        "hype": 25,
        "risk": 8,
        "reputation": 15,
        "staff_morale": 10,
        "safety": 15,
        "sustainability": 0,
        "fan_satisfaction": 10,
        "description": "Recinto profissional com infraestruturas. Caro mas fiável."
    },
    "beach": {
        "name": "Resort de Praia",
        "icon": "🏖️",
        "cost": 38000,
        "capacity": 10000,
        "hype": 45,
        "risk": 30,
        "reputation": 20,
        "staff_morale": 5,
        "safety": -5,
        "sustainability": -5,
        "fan_satisfaction": 20,
        "description": "Frente de praia premium. Paraíso para o Instagram, mas tempestades podem arruinar tudo."
    },
    "castle": {
        "name": "Castelo Histórico",
        "icon": "🏰",
        "cost": 48000,
        "capacity": 6000,
        "hype": 55,
        "risk": 15,
        "reputation": 25,
        "staff_morale": 5,
        "safety": 5,
        "sustainability": 5,
        "fan_satisfaction": 15,
        "description": "Recinto medieval único. Capacidade limitada mas atmosfera inesquecível."
    },
}

ARTISTS = {
    "local": {
        "name": "Bandas Locais",
        "icon": "🎸",
        "cost": 2000,
        "hype": 5,
        "reputation": -5,
        "staff_morale": 10,
        "safety": 5,
        "sustainability": 5,
        "fan_satisfaction": -5,
        "description": "5 bandas locais entusiasmadas. Baratas, mas alguém vai vir vê-las?"
    },
    "tribute": {
        "name": "Bandas Tributo",
        "icon": "🎭",
        "cost": 6000,
        "hype": 12,
        "reputation": 0,
        "staff_morale": 5,
        "safety": 5,
        "sustainability": 0,
        "fan_satisfaction": 5,
        "description": "Bandas de covers a tocar hits. Músicas conhecidas, mas não são os originais."
    },
    "rising": {
        "name": "Estrelas em Ascensão",
        "icon": "⭐",
        "cost": 15000,
        "hype": 25,
        "reputation": 5,
        "staff_morale": 5,
        "safety": 0,
        "sustainability": 0,
        "fan_satisfaction": 5,
        "description": "Artistas emergentes. Podem ser a próxima grande revelação, ou um completo flop."
    },
    "dj": {
        "name": "DJ Famoso",
        "icon": "🎧",
        "cost": 28000,
        "hype": 40,
        "reputation": 10,
        "staff_morale": 0,
        "safety": -5,
        "sustainability": -5,
        "fan_satisfaction": 10,
        "description": "DJ conhecido com milhões de streams. Vibes de festa garantidas."
    },
    "legends": {
        "name": "Lendas do Rock",
        "icon": "🤘",
        "cost": 42000,
        "hype": 55,
        "reputation": 20,
        "staff_morale": 5,
        "safety": 0,
        "sustainability": 0,
        "fan_satisfaction": 20,
        "description": "Reunião de uma banda lendária. Atrai múltiplas gerações."
    },
    "superstar": {
        "name": "Superestrela Mundial",
        "icon": "👑",
        "cost": 55000,
        "hype": 70,
        "reputation": 30,
        "staff_morale": -10,
        "safety": -10,
        "sustainability": -5,
        "fan_satisfaction": 25,
        "description": "Celebridade de primeira linha. Atração massiva, mas leva a maior parte do orçamento."
    },
}

MARKETING = {
    "none": {
        "name": "Boca a Boca",
        "icon": "🗣️",
        "cost": 0,
        "hype": 2,
        "reputation": -10,
        "staff_morale": 0,
        "safety": 0,
        "sustainability": 5,
        "fan_satisfaction": 0,
        "description": "Gratuito mas lento. Só amigos e família podem ouvir falar."
    },
    "social": {
        "name": "Anúncios nas Redes Sociais",
        "icon": "📱",
        "cost": 4000,
        "hype": 15,
        "reputation": 5,
        "staff_morale": 5,
        "safety": 0,
        "sustainability": 5,
        "fan_satisfaction": 5,
        "description": "Campanhas no Instagram e TikTok. Bom para público jovem."
    },
    "radio": {
        "name": "Rádio e Cartazes",
        "icon": "📻",
        "cost": 10000,
        "hype": 25,
        "reputation": 10,
        "staff_morale": 0,
        "safety": 0,
        "sustainability": -5,
        "fan_satisfaction": 5,
        "description": "Mix de media tradicional. Alcança demografias mais amplas."
    },
    "influencers": {
        "name": "Campanha de Influencers",
        "icon": "🤳",
        "cost": 18000,
        "hype": 40,
        "risk_bonus": 10,
        "reputation": 5,
        "staff_morale": -5,
        "safety": 0,
        "sustainability": 0,
        "fan_satisfaction": 5,
        "description": "Parcerias com influencers. Alto engagement mas imprevisível."
    },
    "tv": {
        "name": "TV e Outdoors",
        "icon": "📺",
        "cost": 28000,
        "hype": 50,
        "reputation": 20,
        "staff_morale": 0,
        "safety": 0,
        "sustainability": -10,
        "fan_satisfaction": 10,
        "description": "Publicidade premium. Máxima visibilidade e credibilidade."
    },
    "viral": {
        "name": "Ação Viral",
        "icon": "🚀",
        "cost": 22000,
        "hype": 65,
        "risk_bonus": 25,
        "reputation": 15,
        "staff_morale": -10,
        "safety": -5,
        "sustainability": -5,
        "fan_satisfaction": 10,
        "description": "Stunt criativo de alto risco. Pode explodir ou sair completamente ao contrário."
    },
}

EXTRAS = {
    "security_basic": {
        "name": "Segurança Básica",
        "icon": "👮",
        "cost": 3000,
        "risk_reduction": 8,
        "reputation": 0,
        "staff_morale": -5,
        "safety": 15,
        "sustainability": 0,
        "fan_satisfaction": 0,
        "description": "Requisito legal mínimo. Pode não lidar bem com problemas."
    },
    "security_pro": {
        "name": "Segurança Profissional",
        "icon": "🛡️",
        "cost": 10000,
        "risk_reduction": 20,
        "reputation": 5,
        "staff_morale": 10,
        "safety": 30,
        "sustainability": 0,
        "fan_satisfaction": 5,
        "description": "Equipa experiente com pessoal médico. Tranquilidade garantida."
    },
    "food": {
        "name": "Zona de Restauração",
        "icon": "🍔",
        "cost": 6000,
        "hype": 5,
        "revenue_bonus": 4,
        "reputation": 5,
        "staff_morale": 5,
        "safety": -5,
        "sustainability": -5,
        "fan_satisfaction": 15,
        "description": "Vendedores de comida. Receita extra e clientes satisfeitos."
    },
    "vip": {
        "name": "Zona VIP",
        "icon": "🥂",
        "cost": 12000,
        "hype": 8,
        "revenue_bonus": 10,
        "reputation": 10,
        "staff_morale": -5,
        "safety": 0,
        "sustainability": -5,
        "fan_satisfaction": 10,
        "description": "Área premium com regalias. Atrai grandes gastadores."
    },
    "eco": {
        "name": "Montagem Ecológica",
        "icon": "♻️",
        "cost": 7000,
        "hype": 12,
        "reputation": 10,
        "staff_morale": 10,
        "safety": 0,
        "sustainability": 30,
        "fan_satisfaction": 5,
        "description": "Práticas sustentáveis. Ótimas relações públicas com público jovem."
    },
    "stream": {
        "name": "Transmissão em Direto",
        "icon": "📡",
        "cost": 9000,
        "hype": 15,
        "reputation": 15,
        "staff_morale": -5,
        "safety": 0,
        "sustainability": -5,
        "fan_satisfaction": 5,
        "description": "Streaming profissional. Alcance de audiência global online."
    },
}

# ============================================
# AFTERMATH SYSTEM
# ============================================
AFTERMATH_CATEGORIES = [
    {
        "key": "media_coverage",
        "title": "Cobertura Mediática",
        "icon": "📰",
        "metric": "reputation",
        "use_profit": True,
        "tiers": [
            {
                "name": "Festival do Ano",
                "condition": lambda m, p: m >= 80 and p > 10000,
                "text": "Todos os grandes meios de comunicação cobrem o teu festival. A Rolling Stone chama-o 'o evento que redefiniu a música ao vivo.' Ofertas de patrocínio inundam a tua caixa de entrada. Três marcas querem acordos exclusivos para o próximo ano.",
                "financial_impact": 15000,
                "card_class": "great",
            },
            {
                "name": "Imprensa Positiva",
                "condition": lambda m, p: m >= 60 and p > 0,
                "text": "Meios locais e nacionais publicam histórias positivas. A marca do teu festival ganha reconhecimento. Algumas marcas entram em contacto sobre oportunidades de parceria.",
                "financial_impact": 5000,
                "card_class": "positive",
            },
            {
                "name": "Críticas Mistas",
                "condition": lambda m, p: m >= 35,
                "text": "A cobertura é morna. Algumas críticas positivas, outras nem tanto. 'Um festival aceitável' não era o título que querias. A internet segue em frente rapidamente.",
                "financial_impact": 0,
                "card_class": "neutral",
            },
            {
                "name": "Imprensa Negativa",
                "condition": lambda m, p: m >= 15,
                "text": "Os títulos focam-se nos problemas. As redes sociais estão cheias de queixas. Um artigo tem como título 'Como NÃO Gerir um Festival.' Contratas uma empresa de RP para controlo de danos.",
                "financial_impact": -3000,
                "card_class": "negative",
            },
            {
                "name": "Escândalo Exposto",
                "condition": lambda m, p: True,
                "text": "Jornalistas de investigação expõem o desastre. O teu festival torna-se um exemplo viral de incompetência. O hashtag #FestivalFalhado é tendência durante três dias. O teu nome fica permanentemente associado ao fracasso.",
                "financial_impact": -8000,
                "card_class": "severe",
            },
        ]
    },
    {
        "key": "legal_consequences",
        "title": "Consequências Legais",
        "icon": "⚖️",
        "metric": "safety",
        "use_profit": False,
        "tiers": [
            {
                "name": "Registo Limpo",
                "condition": lambda m, p: m >= 85,
                "text": "Zero incidentes reportados. A tua equipa de segurança é elogiada pelas autoridades locais. A seguradora oferece um desconto para o próximo ano. Os funcionários da câmara chamam-te um organizador modelo.",
                "financial_impact": 2000,
                "card_class": "great",
            },
            {
                "name": "Queixas Menores",
                "condition": lambda m, p: m >= 60,
                "text": "Alguns relatórios de lesões menores, todos tratados corretamente. Nenhuma ação legal esperada. O teu seguro de responsabilidade cobre tudo. Resultado normal para um festival deste tamanho.",
                "financial_impact": 0,
                "card_class": "neutral",
            },
            {
                "name": "Processos Judiciais",
                "condition": lambda m, p: m >= 35,
                "text": "Vários participantes apresentam queixas por lesões. O teu advogado diz que a maioria pode ser resolvida fora do tribunal, mas não vai ser barato. Os custos legais acumulam-se. Dormir torna-se difícil.",
                "financial_impact": -10000,
                "card_class": "negative",
            },
            {
                "name": "Ação Legal Grave",
                "condition": lambda m, p: m >= 15,
                "text": "Múltiplas queixas graves de lesões acumulam-se. Uma ação coletiva está a formar-se. Funcionários da câmara questionam as tuas licenças. Os honorários do teu advogado triplicaram. O tribunal torna-se a tua segunda casa.",
                "financial_impact": -25000,
                "card_class": "severe",
            },
            {
                "name": "Investigação Criminal",
                "condition": lambda m, p: True,
                "text": "As autoridades abrem uma investigação por negligência criminal. Os teus bens podem ser congelados. Os advogados estimam que os danos podem chegar a seis dígitos. Recebes uma intimação formal. Isto já não é só sobre dinheiro.",
                "financial_impact": -50000,
                "card_class": "severe",
            },
        ]
    },
    {
        "key": "environmental_report",
        "title": "Relatório Ambiental",
        "icon": "🌍",
        "metric": "sustainability",
        "use_profit": False,
        "tiers": [
            {
                "name": "Prémio Ecológico",
                "condition": lambda m, p: m >= 80,
                "text": "O teu festival ganha um Prémio de Eventos Verdes! Grupos ambientais promovem-te como modelo para a indústria. Patrocinadores verdes alinham-se com ofertas. O presidente da câmara aperta-te a mão na cerimónia.",
                "financial_impact": 8000,
                "card_class": "great",
            },
            {
                "name": "Eco-Amigável",
                "condition": lambda m, p: m >= 55,
                "text": "O impacto ambiental foi mínimo. A câmara elogia os teus esforços. Sem multas, sem problemas. Um blog de sustentabilidade escreve uma peça positiva sobre a tua abordagem.",
                "financial_impact": 2000,
                "card_class": "positive",
            },
            {
                "name": "Impacto Médio",
                "condition": lambda m, p: m >= 35,
                "text": "Pegada ambiental normal. Nada de especial, nada de terrível. A limpeza corre como esperado. Os caixotes transbordaram um pouco, mas ninguém se queixa muito.",
                "financial_impact": 0,
                "card_class": "neutral",
            },
            {
                "name": "Danos Ambientais",
                "condition": lambda m, p: m >= 15,
                "text": "Resíduos e poluição significativos deixados para trás. Grupos ambientais locais apresentam queixas. A câmara emite um aviso formal e uma multa substancial. Imagens aéreas da confusão tornam-se virais.",
                "financial_impact": -8000,
                "card_class": "negative",
            },
            {
                "name": "Desastre Ecológico",
                "condition": lambda m, p: True,
                "text": "Resíduos tóxicos, habitat destruído, um rio de plástico. Drones de notícias filmam a devastação. As autoridades ambientais envolvem-se. Multas massivas e custos de remediação obrigatórios. És o vilão de todos os eco-documentários da próxima década.",
                "financial_impact": -20000,
                "card_class": "severe",
            },
        ]
    },
    {
        "key": "fan_reactions",
        "title": "Reações dos Fãs",
        "icon": "💬",
        "metric": "fan_satisfaction",
        "use_profit": False,
        "tiers": [
            {
                "name": "Lenda Instantânea",
                "condition": lambda m, p: m >= 85,
                "text": "Os fãs estão EUFÓRICOS. 'Melhor festival de sempre' é tendência nas redes sociais. Fan art aparece em horas. Os bilhetes de pré-venda para o próximo ano esgotam em 12 minutos. Construíste algo que as pessoas adoram.",
                "financial_impact": 10000,
                "card_class": "great",
            },
            {
                "name": "Multidão Feliz",
                "condition": lambda m, p: m >= 60,
                "text": "A maioria dos participantes divertiu-se imenso. As críticas positivas superam as negativas. O boca-a-boca cresce organicamente. As pessoas já perguntam 'quando é o próximo ano?'",
                "financial_impact": 3000,
                "card_class": "positive",
            },
            {
                "name": "Sentimentos Mistos",
                "condition": lambda m, p: m >= 40,
                "text": "As opiniões dividem-se. Alguns adoraram, outros ficaram desiludidos. 'Foi fixe, acho eu' é o sentimento predominante. O tópico no Reddit tem 47 comentários e nenhum consenso.",
                "financial_impact": 0,
                "card_class": "neutral",
            },
            {
                "name": "Pedidos de Reembolso",
                "condition": lambda m, p: m >= 20,
                "text": "Fãs furiosos inundam o teu email a exigir reembolsos. Tópicos de queixas dominam os fóruns. A DECO recebe queixas formais. A tua caixa de entrada é uma zona de guerra de mensagens em maiúsculas.",
                "financial_impact": -12000,
                "card_class": "negative",
            },
            {
                "name": "Revolta Geral",
                "condition": lambda m, p: True,
                "text": "Uma petição de reembolso coletivo com milhares de assinaturas torna-se viral. O teu processador de pagamentos congela as transações pendentes de investigação. Os media pegam na história. Podes nunca mais trabalhar em eventos.",
                "financial_impact": -25000,
                "card_class": "severe",
            },
        ]
    },
    {
        "key": "industry_standing",
        "title": "Posição na Indústria",
        "icon": "🏛️",
        "metric": "overall",
        "use_profit": True,
        "tiers": [
            {
                "name": "Ofertas de Investidores",
                "condition": lambda m, p: m >= 75 and p > 5000,
                "text": "Investidores de capital de risco querem entrar. Uma grande empresa de entretenimento oferece um acordo de parceria. O teu festival é agora uma marca. O teu telefone não para de tocar com oportunidades.",
                "financial_impact": 20000,
                "card_class": "great",
            },
            {
                "name": "Respeito da Indústria",
                "condition": lambda m, p: m >= 55 and p > 0,
                "text": "Os pares da indústria tomam nota. És convidado para falar em conferências. Outros promotores querem colaborar. As portas certas começam a abrir-se.",
                "financial_impact": 5000,
                "card_class": "positive",
            },
            {
                "name": "Sob o Radar",
                "condition": lambda m, p: m >= 35,
                "text": "A indústria mal reparou. És apenas mais um festival que aconteceu. Nenhuma porta abriu, mas nenhuma fechou. Existes no vasto meio-termo da mediocridade.",
                "financial_impact": 0,
                "card_class": "neutral",
            },
            {
                "name": "Dúvida da Indústria",
                "condition": lambda m, p: m >= 15,
                "text": "Corre a voz de que o teu festival foi um desastre. Os donos de recintos hesitam em trabalhar contigo. Os agentes de artistas deixam de atender chamadas. A tua reputação na indústria está danificada.",
                "financial_impact": -5000,
                "card_class": "negative",
            },
            {
                "name": "Lista Negra",
                "condition": lambda m, p: True,
                "text": "Estás efetivamente na lista negra da indústria de eventos. Nenhum recinto, nenhum manager de artistas, nenhum patrocinador te toca. Os colegas mudam de passeio para te evitar. A tua carreira em festivais acabou.",
                "financial_impact": -15000,
                "card_class": "severe",
            },
        ]
    },
    {
        "key": "personal_outcome",
        "title": "O Teu Destino",
        "icon": "🪞",
        "metric": "final",
        "use_profit": False,
        "tiers": [
            {
                "name": "Promotor Celebridade",
                "condition": lambda m, p: p > 40000,
                "text": "Conseguiste. Contra todas as probabilidades, não és apenas bem-sucedido — és uma lenda. Capas de revistas, contratos de livros e um documentário Netflix sobre a tua ascensão. O orçamento do teu próximo festival? Sete dígitos. O sonho tornou-se realidade.",
                "financial_impact": 0,
                "card_class": "great",
            },
            {
                "name": "Promotor de Sucesso",
                "condition": lambda m, p: p > 10000,
                "text": "Um sucesso sólido. Provaste que consegues fazer isto. A conta bancária está saudável, o futuro é brilhante e já estás a esboçar planos para o próximo ano. Nada mau para um estreante.",
                "financial_impact": 0,
                "card_class": "positive",
            },
            {
                "name": "Sobreviveste",
                "condition": lambda m, p: p > -5000,
                "text": "Ficaste mais ou menos no zero. Nem um desastre, nem um triunfo. Aprendeste mais do que qualquer escola de gestão te poderia ensinar. Se encontrares a coragem e o dinheiro, talvez o próximo ano seja diferente.",
                "financial_impact": 0,
                "card_class": "neutral",
            },
            {
                "name": "Endividado",
                "condition": lambda m, p: p > -30000,
                "text": "As contas acumulam-se. Deves dinheiro a fornecedores, recintos e artistas. Cartões de crédito no limite. Vai levar anos a pagar isto. O sonho do festival está em espera indefinida. O telefone toca e tu estremeces.",
                "financial_impact": 0,
                "card_class": "negative",
            },
            {
                "name": "Ruína Financeira",
                "condition": lambda m, p: True,
                "text": "Falência. Os credores ligam todos os dias. O teu apartamento foi-se. Dormes no sofá de um amigo, a vasculhar ofertas de emprego às 3 da manhã, a perguntar-te onde é que tudo correu mal. O sonho do festival não morreu apenas — levou tudo consigo.",
                "financial_impact": 0,
                "card_class": "severe",
            },
        ]
    },
]

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
    st.session_state.reputation = 30
    st.session_state.staff_morale = 50
    st.session_state.safety = 40
    st.session_state.sustainability = 20
    st.session_state.fan_satisfaction = 50
    st.session_state.location = None
    st.session_state.artist = None
    st.session_state.marketing = None
    st.session_state.extras = []
    st.session_state.ticket_price = 40
    st.session_state.game_started = True
    st.session_state.events = []
    st.session_state.weather = None
    st.session_state.cost_breakdown = {
        "venue": 0,
        "artists": 0,
        "marketing": 0,
        "extras": 0,
    }
    st.session_state.food_revenue_bonus = 0
    st.session_state.vip_revenue_bonus = 0

if "game_started" not in st.session_state:
    init_game()

# ============================================
# HELPER FUNCTIONS
# ============================================
def clamp_metrics():
    for key in ['reputation', 'staff_morale', 'safety', 'sustainability', 'fan_satisfaction']:
        st.session_state[key] = max(0, min(100, st.session_state[key]))
    st.session_state.risk = max(0, min(100, st.session_state.risk))
    st.session_state.hype = max(0, st.session_state.hype)

def apply_new_metrics(data):
    for key in ['reputation', 'staff_morale', 'safety', 'sustainability', 'fan_satisfaction']:
        st.session_state[key] += data.get(key, 0)
    clamp_metrics()

def apply_event_metrics(event):
    for mod_key in ['reputation_mod', 'staff_morale_mod', 'safety_mod', 'sustainability_mod', 'fan_satisfaction_mod']:
        if mod_key in event:
            metric = mod_key.replace('_mod', '')
            st.session_state[metric] += event[mod_key]
    clamp_metrics()

def calculate_demand(hype_val, price):
    """Price elasticity demand model. Returns demand factor and base demand."""
    fair_price = 20 + hype_val * 0.8
    base_demand = hype_val * 60
    if fair_price <= 0:
        return 0, fair_price
    if price <= fair_price:
        discount_ratio = (fair_price - price) / fair_price
        demand_factor = 1.0 + discount_ratio * 0.3
    else:
        price_ratio = price / fair_price
        demand_factor = max(0.02, (1.0 / price_ratio) ** 2.5)
    demand = base_demand * demand_factor
    return demand, fair_price

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
            <div class="stat-value {budget_class}">{budget:,}€</div>
            <div class="stat-label">Orçamento</div>
        </div>
        <div class="stat-card">
            <div class="stat-value hype">{st.session_state.hype}</div>
            <div class="stat-label">Hype</div>
        </div>
        <div class="stat-card">
            <div class="stat-value capacity">{st.session_state.capacity:,}</div>
            <div class="stat-label">Capacidade</div>
        </div>
        <div class="stat-card">
            <div class="stat-value risk">{st.session_state.risk}%</div>
            <div class="stat-label">Risco</div>
        </div>
    </div>
    <div class="stats-container">
        <div class="stat-card">
            <div class="stat-value reputation">{st.session_state.reputation}</div>
            <div class="stat-label">Reputação</div>
        </div>
        <div class="stat-card">
            <div class="stat-value morale">{st.session_state.staff_morale}</div>
            <div class="stat-label">Moral</div>
        </div>
        <div class="stat-card">
            <div class="stat-value safety">{st.session_state.safety}</div>
            <div class="stat-label">Segurança</div>
        </div>
        <div class="stat-card">
            <div class="stat-value sustainability">{st.session_state.sustainability}</div>
            <div class="stat-label">Eco</div>
        </div>
        <div class="stat-card">
            <div class="stat-value satisfaction">{st.session_state.fan_satisfaction}</div>
            <div class="stat-label">Fãs</div>
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
    paragraphs = story['text'].strip().split('\n\n')
    text_html = '<br><br>'.join(' '.join(p.split()) for p in paragraphs)
    st.markdown(
        f'<div class="story-card">'
        f'<span class="story-icon">{story["icon"]}</span>'
        f'<div class="story-title">{story["title"]}</div>'
        f'<div class="story-text">{text_html}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

def render_choice(key, data, choice_type):
    cost = data["cost"]
    can_afford = st.session_state.budget >= cost

    stats = [f'<span class="choice-stat cost">{cost:,}€</span>']
    if "hype" in data:
        stats.append(f'<span class="choice-stat hype">+{data["hype"]} Hype</span>')
    if "capacity" in data:
        stats.append(f'<span class="choice-stat capacity">{data["capacity"]:,} cap</span>')
    if "risk" in data:
        stats.append(f'<span class="choice-stat risk">+{data["risk"]}% risco</span>')
    if "risk_reduction" in data:
        stats.append(f'<span class="choice-stat bonus">-{data["risk_reduction"]}% risco</span>')
    if "revenue_bonus" in data:
        stats.append(f'<span class="choice-stat bonus">+{data["revenue_bonus"]}€/bilhete</span>')
    if "risk_bonus" in data:
        stats.append(f'<span class="choice-stat risk">+{data["risk_bonus"]}% risco</span>')

    for metric_key, label in [
        ("reputation", "Rep"),
        ("staff_morale", "Moral"),
        ("safety", "Seg"),
        ("sustainability", "Eco"),
        ("fan_satisfaction", "Fãs"),
    ]:
        val = data.get(metric_key, 0)
        if val != 0:
            sign = "+" if val > 0 else ""
            color_class = "bonus" if val > 0 else "risk"
            stats.append(f'<span class="choice-stat {color_class}">{sign}{val} {label}</span>')

    st.markdown(f"""
    <div class="choice-card">
        <div class="choice-title">{data['icon']} {data['name']}</div>
        <div class="choice-description">{data['description']}</div>
        <div class="choice-stats">{''.join(stats)}</div>
    </div>
    """, unsafe_allow_html=True)

    if can_afford:
        if st.button(f"Escolher {data['name']}", key=f"{choice_type}_{key}", use_container_width=True):
            return True
    else:
        st.button(f"Sem orçamento (precisas de {cost:,}€)", key=f"{choice_type}_{key}", disabled=True, use_container_width=True)
    return False

def calculate_aftermath(initial_profit, events_occurred):
    results = []
    running_profit = initial_profit

    overall = (
        st.session_state.reputation +
        st.session_state.staff_morale +
        st.session_state.safety +
        st.session_state.sustainability +
        st.session_state.fan_satisfaction
    ) / 5

    for category in AFTERMATH_CATEGORIES:
        metric_key = category["metric"]

        if metric_key == "overall":
            metric_val = overall
        elif metric_key == "final":
            metric_val = 0
        else:
            metric_val = st.session_state.get(metric_key, 50)

        if category.get("use_profit"):
            profit_val = initial_profit
        elif metric_key == "final":
            profit_val = running_profit
        else:
            profit_val = initial_profit

        for tier in category["tiers"]:
            if tier["condition"](metric_val, profit_val):
                impact = tier["financial_impact"]
                results.append({
                    "category_title": category["title"],
                    "category_icon": category["icon"],
                    "tier_name": tier["name"],
                    "text": tier["text"],
                    "financial_impact": impact,
                    "card_class": tier["card_class"],
                })
                running_profit += impact
                break

    return results, running_profit

# ============================================
# GAME PHASES
# ============================================
def show_start():
    st.markdown('<h1 class="main-title">🎪 Gestor de Festivais</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Consegues construir um festival de sucesso?</p>', unsafe_allow_html=True)

    display_story("intro")

    if st.button("🚀 Começar a Aventura", type="primary", use_container_width=True):
        st.session_state.phase = 1
        st.rerun()

def show_location():
    st.markdown('<h1 class="main-title">📍 Escolher Local</h1>', unsafe_allow_html=True)
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
            st.session_state.cost_breakdown["venue"] = data["cost"]
            apply_new_metrics(data)
            st.session_state.phase = 2
            st.rerun()

def show_artists():
    st.markdown('<h1 class="main-title">🎤 Contratar Artistas</h1>', unsafe_allow_html=True)
    display_phase_progress(2)
    display_stats()
    display_story("artists")

    for key, data in ARTISTS.items():
        if render_choice(key, data, "art"):
            st.session_state.budget -= data["cost"]
            st.session_state.hype += data["hype"]
            st.session_state.artist = data["name"]
            st.session_state.cost_breakdown["artists"] = data["cost"]
            apply_new_metrics(data)
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
            st.session_state.cost_breakdown["marketing"] = data["cost"]
            apply_new_metrics(data)
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

        stats = [f'<span class="choice-stat cost">{cost:,}€</span>']
        if "hype" in data:
            stats.append(f'<span class="choice-stat hype">+{data["hype"]} Hype</span>')
        if "risk_reduction" in data:
            stats.append(f'<span class="choice-stat bonus">-{data["risk_reduction"]}% risco</span>')
        if "revenue_bonus" in data:
            stats.append(f'<span class="choice-stat bonus">+{data["revenue_bonus"]}€/bilhete</span>')

        for metric_key, label in [
            ("reputation", "Rep"),
            ("staff_morale", "Moral"),
            ("safety", "Seg"),
            ("sustainability", "Eco"),
            ("fan_satisfaction", "Fãs"),
        ]:
            val = data.get(metric_key, 0)
            if val != 0:
                sign = "+" if val > 0 else ""
                color_class = "bonus" if val > 0 else "risk"
                stats.append(f'<span class="choice-stat {color_class}">{sign}{val} {label}</span>')

        st.markdown(f"""
        <div class="choice-card">
            <div class="choice-title">{data['icon']} {data['name']}</div>
            <div class="choice-description">{data['description']}</div>
            <div class="choice-stats">{''.join(stats)}</div>
        </div>
        """, unsafe_allow_html=True)

        if selected:
            st.button(f"✅ Adicionado!", key=f"ext_{key}", disabled=True, use_container_width=True)
        elif can_afford:
            if st.button(f"Adicionar {data['name']}", key=f"ext_{key}", use_container_width=True):
                st.session_state.budget -= data["cost"]
                st.session_state.hype += data.get("hype", 0)
                st.session_state.risk -= data.get("risk_reduction", 0)
                st.session_state.revenue_bonus += data.get("revenue_bonus", 0)
                st.session_state.cost_breakdown["extras"] += data["cost"]
                if key == "food":
                    st.session_state.food_revenue_bonus = data.get("revenue_bonus", 0)
                elif key == "vip":
                    st.session_state.vip_revenue_bonus = data.get("revenue_bonus", 0)
                st.session_state.extras.append(key)
                apply_new_metrics(data)
                st.rerun()
        else:
            st.button(f"Sem orçamento", key=f"ext_{key}", disabled=True, use_container_width=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    if st.button("➡️ Continuar para Preços", type="primary", use_container_width=True):
        st.session_state.phase = 5
        st.rerun()

def show_pricing():
    st.markdown('<h1 class="main-title">🎟️ Definir Preço</h1>', unsafe_allow_html=True)
    display_phase_progress(5)
    display_stats()
    display_story("pricing")

    st.markdown(f"""
    **O Teu Festival:**
    - Local: {st.session_state.location}
    - Artista: {st.session_state.artist}
    - Marketing: {st.session_state.marketing}
    """)

    price = st.slider("Preço do Bilhete (€)", 15, 200, 40, 5)
    st.session_state.ticket_price = price

    # Price elasticity demand model (preview only shows attendance)
    demand, _ = calculate_demand(st.session_state.hype, price)
    expected = min(int(demand), st.session_state.capacity)

    st.markdown(
        f'<div class="info-box">'
        f'<strong>Estimativa de assistência: ~{expected:,}</strong><br>'
        f'<em style="color: #fbbf24; font-size: 0.9rem;">O preço afeta diretamente quantas pessoas aparecem. Encontra o equilíbrio certo.</em>'
        f'</div>',
        unsafe_allow_html=True
    )

    # Metric warnings
    warnings = []
    if st.session_state.safety < 30:
        warnings.append("SEGURANÇA BAIXA: Espera custos de seguro elevados e risco legal grave nas consequências!")
    if st.session_state.sustainability < 25:
        warnings.append("SUSTENTABILIDADE BAIXA: Multas ambientais e custos de limpeza pesados são prováveis!")
    if st.session_state.fan_satisfaction < 35:
        warnings.append("SATISFAÇÃO DOS FÃS BAIXA: Pedidos de reembolso em massa podem eliminar os teus lucros!")
    if st.session_state.staff_morale < 25:
        warnings.append("MORAL DA EQUIPA BAIXA: A tua equipa está desmoralizada. Problemas durante o evento são muito mais prováveis!")
    if st.session_state.reputation < 20:
        warnings.append("REPUTAÇÃO BAIXA: Cobertura mediática negativa vai custar-te após o evento!")

    if st.session_state.risk > 20:
        warnings.append(f"RISCO ELEVADO ({st.session_state.risk}%): Eventos negativos são muito mais prováveis!")

    for w in warnings:
        st.markdown(f'<div class="warning-box">⚠️ {w}</div>', unsafe_allow_html=True)

    if st.button("🎲 Lançar Festival!", type="primary", use_container_width=True):
        st.session_state.phase = 6
        st.rerun()

def show_results():
    st.markdown('<h1 class="main-title">🎪 Dia do Festival!</h1>', unsafe_allow_html=True)
    display_story("results")

    # ---- ROLL EVENTS ----
    events_occurred = []
    total_cost_from_events = 0
    attendance_multiplier = 1.0
    hype_modifier = 0

    risk_factor = st.session_state.risk / 100
    morale_factor = st.session_state.staff_morale / 50.0
    disaster_modifier = max(0.5, 2.0 - morale_factor)

    # Disasters (max 1)
    for event in RANDOM_EVENTS["disasters"]:
        if random.random() < event["chance"] * (1 + risk_factor * 2) * disaster_modifier:
            events_occurred.append(("disaster", event))
            total_cost_from_events += event.get("cost", 0)
            attendance_multiplier *= event.get("attendance_multiplier", 1.0)
            hype_modifier -= event.get("hype_loss", 0)
            apply_event_metrics(event)
            break

    # Problems (max 2)
    problem_count = 0
    for event in RANDOM_EVENTS["problems"]:
        if random.random() < event["chance"] * (1 + risk_factor) * disaster_modifier:
            events_occurred.append(("problem", event))
            total_cost_from_events += event.get("cost", 0)
            attendance_multiplier *= event.get("attendance_multiplier", 1.0)
            hype_modifier -= event.get("hype_loss", 0)
            apply_event_metrics(event)
            problem_count += 1
            if problem_count >= 2:
                break

    # Lucky events
    if random.random() < 0.15 * (1 - risk_factor * 0.5):
        event = random.choice(RANDOM_EVENTS["lucky"])
        events_occurred.append(("lucky", event))
        attendance_multiplier *= event.get("attendance_multiplier", 1.0)
        hype_modifier += event.get("hype_bonus", 0)
        apply_event_metrics(event)

    # Weather
    weather_weights = [10, 20, 30, 25, 15]
    weather_weights[3] += int(st.session_state.risk * 0.5)
    weather_weights[4] += int(st.session_state.risk * 0.3)

    weather_key = random.choices(list(WEATHER_EFFECTS.keys()), weights=weather_weights, k=1)[0]
    weather = WEATHER_EFFECTS[weather_key]

    # Apply weather metric mods
    for mod_key in ['fan_satisfaction_mod', 'safety_mod', 'staff_morale_mod', 'sustainability_mod']:
        if mod_key in weather:
            metric = mod_key.replace('_mod', '')
            st.session_state[metric] += weather[mod_key]
    clamp_metrics()

    # ---- DISPLAY EVENTS ----
    for event_type, event in events_occurred:
        card_class = event_type
        impact_text = ""
        if event.get("cost"):
            impact_text += f"💸 -{event['cost']:,}€ "
        if event.get("attendance_multiplier") and event["attendance_multiplier"] < 1:
            loss = int((1 - event["attendance_multiplier"]) * 100)
            impact_text += f"👥 -{loss}% assistência "
        if event.get("attendance_multiplier") and event["attendance_multiplier"] > 1:
            gain = int((event["attendance_multiplier"] - 1) * 100)
            impact_text += f"👥 +{gain}% assistência "

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

    # ---- ATTENDANCE (with price elasticity) ----
    effective_hype = max(0, st.session_state.hype + hype_modifier)
    demand, _ = calculate_demand(effective_hype, st.session_state.ticket_price)
    demand *= attendance_multiplier
    demand *= weather["multiplier"]
    demand *= random.uniform(0.85, 1.15)
    actual_attendance = min(max(0, int(demand)), st.session_state.capacity)

    # ---- ATTENDANCE METRICS ----
    st.markdown(f"""
    <div class="metric-grid">
        <div class="metric-card">
            <div class="metric-value">👥 {actual_attendance:,}</div>
            <div class="metric-label">Presentes</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">🏟️ {st.session_state.capacity:,}</div>
            <div class="metric-label">Capacidade</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---- FINANCIAL BREAKDOWN ----
    cb = st.session_state.cost_breakdown
    safety_score = st.session_state.safety
    fan_sat = st.session_state.fan_satisfaction

    # Revenue
    ticket_revenue = actual_attendance * st.session_state.ticket_price
    food_revenue = actual_attendance * st.session_state.food_revenue_bonus
    vip_revenue = actual_attendance * st.session_state.vip_revenue_bonus
    total_revenue = ticket_revenue + food_revenue + vip_revenue

    # Costs
    insurance_cost = int(500 + (100 - safety_score) * 145)
    tax = int(total_revenue * 0.08)
    refund_rate = max(0, (100 - fan_sat) / 100 * 0.30)
    refund_cost = int(ticket_revenue * refund_rate)
    damage_base = 3000 if any(e[1].get("cost", 0) > 5000 for e in events_occurred) else 500
    equipment_damage = int(damage_base * (1 + st.session_state.risk / 100))
    cleanup_cost = int(500 + (100 - st.session_state.sustainability) * 75)

    total_costs = (
        cb["venue"] + cb["artists"] + cb["marketing"] + cb["extras"]
        + total_cost_from_events + insurance_cost + tax
        + refund_cost + equipment_damage + cleanup_cost
    )

    initial_profit = total_revenue - total_costs

    # ---- DISPLAY FINANCIAL BREAKDOWN ----
    st.markdown('<div class="section-header">💰 Análise Financeira</div>', unsafe_allow_html=True)

    # Revenue breakdown
    revenue_lines = [
        ("Venda de Bilhetes", ticket_revenue),
    ]
    if food_revenue > 0:
        revenue_lines.append(("Receita da Restauração", food_revenue))
    if vip_revenue > 0:
        revenue_lines.append(("Receita VIP", vip_revenue))

    revenue_html = ""
    for label, val in revenue_lines:
        revenue_html += f'<div class="financial-line"><span class="fl-label">{label}</span><span class="fl-value positive">+{val:,}€</span></div>'
    revenue_html += f'<div class="breakdown-total"><span class="fl-label">Receita Total</span><span class="fl-value positive">{total_revenue:,}€</span></div>'

    st.markdown(f"""
    <div class="breakdown-container">
        <div class="breakdown-header">📈 Receitas</div>
        {revenue_html}
    </div>
    """, unsafe_allow_html=True)

    # Cost breakdown
    cost_lines = [
        ("Aluguer do Local", cb["venue"]),
        ("Contratação de Artistas", cb["artists"]),
        ("Campanha de Marketing", cb["marketing"]),
    ]
    if cb["extras"] > 0:
        cost_lines.append(("Extras e Complementos", cb["extras"]))
    if total_cost_from_events > 0:
        cost_lines.append(("Custos de Emergência (Eventos)", total_cost_from_events))
    cost_lines.append(("Seguros", insurance_cost))
    cost_lines.append(("Impostos (8%)", tax))
    if refund_cost > 0:
        cost_lines.append(("Reembolsos (Reclamações)", refund_cost))
    if equipment_damage > 0:
        cost_lines.append(("Danos em Equipamento", equipment_damage))
    cost_lines.append(("Limpeza e Resíduos", cleanup_cost))

    costs_html = ""
    for label, val in cost_lines:
        costs_html += f'<div class="financial-line"><span class="fl-label">{label}</span><span class="fl-value negative">-{val:,}€</span></div>'
    costs_html += f'<div class="breakdown-total"><span class="fl-label">Custos Totais</span><span class="fl-value negative">{total_costs:,}€</span></div>'

    st.markdown(f"""
    <div class="breakdown-container">
        <div class="breakdown-header">📉 Custos</div>
        {costs_html}
    </div>
    """, unsafe_allow_html=True)

    # Initial profit
    profit_class = "positive" if initial_profit >= 0 else "negative"
    profit_sign = "+" if initial_profit >= 0 else ""
    st.markdown(
        f'<div class="breakdown-container">'
        f'<div class="breakdown-total" style="border-top: none;">'
        f'<span class="fl-label" style="font-size: 1.2rem;">Lucro do Dia do Festival</span>'
        f'<span class="fl-value {profit_class}" style="font-size: 1.4rem;">{profit_sign}{initial_profit:,}€</span>'
        f'</div></div>',
        unsafe_allow_html=True
    )

    # ---- AFTERMATH ----
    st.markdown('<div class="section-header">🌪️ As Consequências</div>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">O festival acabou, mas as consequências estão apenas a começar...</p>', unsafe_allow_html=True)

    aftermath_results, final_profit = calculate_aftermath(initial_profit, events_occurred)

    for result in aftermath_results:
        impact = result["financial_impact"]
        if impact > 0:
            impact_html = f'<div class="aftermath-impact gain">+{impact:,}€</div>'
        elif impact < 0:
            impact_html = f'<div class="aftermath-impact loss">{impact:,}€</div>'
        else:
            impact_html = f'<div class="aftermath-impact none">Sem impacto financeiro</div>'

        st.markdown(
            f'<div class="aftermath-card {result["card_class"]}">'
            f'<div class="aftermath-category">{result["category_icon"]} {result["category_title"]}</div>'
            f'<div class="aftermath-title">{result["tier_name"]}</div>'
            f'<div class="aftermath-text">{result["text"]}</div>'
            f'{impact_html}'
            f'</div>',
            unsafe_allow_html=True
        )

    # ---- ADJUSTMENT SUMMARY ----
    aftermath_total = sum(r["financial_impact"] for r in aftermath_results)
    aftermath_class = "positive" if aftermath_total >= 0 else "negative"
    aftermath_sign = "+" if aftermath_total >= 0 else ""

    final_class = "positive" if final_profit >= 0 else "negative"
    final_sign = "+" if final_profit >= 0 else ""

    st.markdown(
        f'<div class="adjustment-summary">'
        f'<div class="adjustment-line">'
        f'<span>Lucro do Dia do Festival:</span>'
        f'<span class="value {profit_class}">{profit_sign}{initial_profit:,}€</span>'
        f'</div>'
        f'<div class="adjustment-line">'
        f'<span>Ajustes Pós-Festival:</span>'
        f'<span class="value {aftermath_class}">{aftermath_sign}{aftermath_total:,}€</span>'
        f'</div>'
        f'<div style="height: 2px; background: #333; margin: 0.6rem 0;"></div>'
        f'<div class="adjustment-line">'
        f'<span style="font-size: 1.1rem; font-weight: 700; color: #e0e0e0;">RESULTADO FINAL VERDADEIRO:</span>'
        f'<span class="value {final_class}" style="font-size: 1.2rem;">{final_sign}{final_profit:,}€</span>'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    # ---- FINAL VERDICT ----
    if final_profit > 50000:
        result_class = "legendary"
        title = "👑 PROMOTOR LENDÁRIO"
        st.balloons()
    elif final_profit > 25000:
        result_class = "success"
        title = "🏆 GRANDE SUCESSO"
        st.balloons()
    elif final_profit > 10000:
        result_class = "success"
        title = "🎉 LUCRO SÓLIDO"
    elif final_profit > 0:
        result_class = "success"
        title = "✅ Pequena Vitória"
    elif final_profit > -10000:
        result_class = "failure"
        title = "😓 Perda Ligeira"
    elif final_profit > -30000:
        result_class = "failure"
        title = "😰 Perda Grave"
    elif final_profit > -60000:
        result_class = "bankrupt"
        title = "💀 DEVASTADOR"
    else:
        result_class = "bankrupt"
        title = "☠️ RUÍNA TOTAL"

    st.markdown(
        f'<div class="result-card {result_class}">'
        f'<div class="result-title">{title}</div>'
        f'<div class="result-profit {final_class}">{final_sign}{final_profit:,}€</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    if st.button("🔄 Jogar de Novo", use_container_width=True):
        init_game()
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
