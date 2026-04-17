import streamlit as st

# ─── CONFIG ───
st.set_page_config(
    page_title="FitLife App",
    page_icon="🏋️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ─── SESSION STATE ───
if "screen" not in st.session_state:
    st.session_state.screen = "splash"
if "user_name" not in st.session_state:
    st.session_state.user_name = "Santiago"
if "user_plan" not in st.session_state:
    st.session_state.user_plan = None
if "puntos" not in st.session_state:
    st.session_state.puntos = 2450
if "reservas" not in st.session_state:
    st.session_state.reservas = [
        {"maquina": "🏃 Cinta de correr #3", "sede": "Palermo", "horario": "Hoy 18:00"},
        {"maquina": "🚴 Bicicleta estática #7", "sede": "Belgrano", "horario": "Mañana 09:00"},
    ]
if "auth_tab" not in st.session_state:
    st.session_state.auth_tab = "login"
if "objetivo_nutricional" not in st.session_state:
    st.session_state.objetivo_nutricional = None
if "qr_verificado" not in st.session_state:
    st.session_state.qr_verificado = False
if "clase_seleccionada" not in st.session_state:
    st.session_state.clase_seleccionada = None

def goto(screen):
    st.session_state.screen = screen
    st.rerun()

# ─── ESTILOS ───
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;600;700&display=swap');

:root {
    --yellow: #E8FF47;
    --green: #1A3A2A;
    --green-mid: #2D5A3D;
    --green-accent: #4CAF6F;
    --white: #FAFFF5;
    --gray: #8A9E8F;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
    background-color: #1A3A2A !important;
    color: #FAFFF5 !important;
}

.stApp {
    background-color: #1A3A2A !important;
    max-width: 480px;
    margin: 0 auto;
}

/* Ocultar elementos de Streamlit */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1rem 1.5rem 2rem !important; max-width: 480px; margin: 0 auto; }

/* Botones principales */
.stButton > button {
    background: #E8FF47 !important;
    color: #1A3A2A !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    padding: 14px 20px !important;
    width: 100% !important;
    transition: all 0.2s !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stButton > button:hover {
    background: #F2FF8A !important;
    transform: translateY(-1px) !important;
}

/* Inputs */
.stTextInput > div > div > input,
.stSelectbox > div > div,
.stNumberInput > div > div > input {
    background: rgba(255,255,255,0.07) !important;
    border: 1.5px solid rgba(255,255,255,0.15) !important;
    border-radius: 10px !important;
    color: #FAFFF5 !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stTextInput > div > div > input:focus {
    border-color: #E8FF47 !important;
    box-shadow: none !important;
}

/* Labels */
.stTextInput label, .stSelectbox label { color: #8A9E8F !important; font-size: 12px !important; font-weight: 600 !important; text-transform: uppercase !important; letter-spacing: 0.5px !important; }

/* Divider */
hr { border-color: rgba(255,255,255,0.1) !important; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.05) !important;
    border-radius: 10px !important;
    padding: 4px !important;
    gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px !important;
    color: #8A9E8F !important;
    font-weight: 600 !important;
}
.stTabs [aria-selected="true"] {
    background: #E8FF47 !important;
    color: #1A3A2A !important;
}
.stTabs [data-baseweb="tab-border"] { display: none !important; }

/* Radio */
.stRadio > div { gap: 8px !important; }
.stRadio [data-testid="stMarkdownContainer"] p { color: #FAFFF5 !important; }

/* Success / Error */
.stSuccess { background: rgba(76,175,111,0.2) !important; border: 1px solid rgba(76,175,111,0.4) !important; color: #4CAF6F !important; border-radius: 10px !important; }
.stError { background: rgba(255,68,68,0.15) !important; border: 1px solid rgba(255,68,68,0.3) !important; color: #FF6B6B !important; border-radius: 10px !important; }
.stWarning { background: rgba(232,255,71,0.1) !important; border: 1px solid rgba(232,255,71,0.3) !important; border-radius: 10px !important; }

/* Expander */
.streamlit-expanderHeader {
    background: rgba(255,255,255,0.05) !important;
    border-radius: 10px !important;
    color: #FAFFF5 !important;
}

/* Selectbox dropdown */
[data-baseweb="select"] { background: rgba(255,255,255,0.07) !important; }
[data-baseweb="menu"] { background: #2D5A3D !important; }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# HELPERS DE UI
# ═══════════════════════════════════════════════════════════

def card(content, border_color="rgba(255,255,255,0.08)", bg="rgba(255,255,255,0.05)", padding="18px", radius="14px"):
    st.markdown(f"""
    <div style="background:{bg}; border:1.5px solid {border_color}; border-radius:{radius}; padding:{padding}; margin-bottom:10px;">
        {content}
    </div>
    """, unsafe_allow_html=True)

def yellow_badge(text):
    return f'<span style="background:#E8FF47; color:#1A3A2A; font-size:11px; font-weight:700; padding:3px 10px; border-radius:20px;">{text}</span>'

def green_badge(text):
    return f'<span style="background:rgba(76,175,111,0.2); color:#4CAF6F; font-size:11px; font-weight:700; padding:3px 10px; border-radius:20px;">{text}</span>'

def tag(text, color="#8A9E8F", bg="rgba(255,255,255,0.08)"):
    return f'<span style="background:{bg}; color:{color}; font-size:12px; font-weight:600; padding:4px 12px; border-radius:20px;">{text}</span>'

def section_title(text):
    st.markdown(f'<div style="font-family:Space Grotesk,sans-serif; font-size:18px; font-weight:700; color:#FAFFF5; margin:20px 0 12px;">{text}</div>', unsafe_allow_html=True)

def subtitle(text):
    st.markdown(f'<p style="color:#8A9E8F; font-size:14px; margin-bottom:16px;">{text}</p>', unsafe_allow_html=True)

def back_button(dest):
    if st.button("← Volver"):
        goto(dest)

def nav_bar():
    st.markdown("<hr>", unsafe_allow_html=True)
    cols = st.columns(5)
    nav_items = [
        ("🏠", "Inicio", "home"),
        ("🎥", "Clases", "clases"),
        ("📱", "QR", "qr"),
        ("📍", "Sedes", "sedes"),
        ("⚡", "Puntos", "puntos"),
    ]
    for col, (icon, label, dest) in zip(cols, nav_items):
        with col:
            active = st.session_state.screen == dest
            color = "#E8FF47" if active else "#8A9E8F"
            st.markdown(f'<div style="text-align:center; cursor:pointer;" onclick="">'
                        f'<div style="font-size:20px;">{icon}</div>'
                        f'<div style="font-size:10px; font-weight:600; color:{color};">{label}</div></div>',
                        unsafe_allow_html=True)
            if st.button(label, key=f"nav_{dest}"):
                goto(dest)


# ═══════════════════════════════════════════════════════════
# PANTALLAS
# ═══════════════════════════════════════════════════════════

# ─── SPLASH ───
def screen_splash():
    st.markdown("""
    <div style="text-align:center; padding: 60px 0 40px;">
        <div style="font-size:80px; margin-bottom:16px;">🏋️</div>
        <div style="font-family:Space Grotesk,sans-serif; font-size:48px; font-weight:700; color:#FAFFF5; letter-spacing:-2px;">
            Fit<span style="color:#E8FF47;">Life</span>
        </div>
        <div style="color:#8A9E8F; font-size:16px; margin-top:8px;">Tu gimnasio, en tu bolsillo</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀  Comenzar"):
        goto("auth")


# ─── AUTH ───
def screen_auth():
    st.markdown("""
    <div style="padding: 20px 0 28px;">
        <div style="display:inline-block; background:rgba(232,255,71,0.15); border:1px solid rgba(232,255,71,0.3); color:#E8FF47; font-size:12px; font-weight:600; padding:4px 12px; border-radius:20px; margin-bottom:14px; letter-spacing:1px;">BIENVENIDO</div>
        <div style="font-family:Space Grotesk,sans-serif; font-size:34px; font-weight:700; color:#FAFFF5; line-height:1.1; margin-bottom:8px;">
            Entrená más<br><span style="color:#E8FF47;">inteligente</span>
        </div>
        <div style="color:#8A9E8F; font-size:14px;">Tu app de gimnasio todo en uno</div>
    </div>
    """, unsafe_allow_html=True)

    tab_login, tab_register = st.tabs(["Iniciar Sesión", "Registrarse"])

    with tab_login:
        st.markdown("<br>", unsafe_allow_html=True)
        email = st.text_input("Email", placeholder="tucorreo@gmail.com", key="login_email")
        password = st.text_input("Contraseña", type="password", placeholder="••••••••", key="login_pass")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Iniciar Sesión", key="btn_login"):
            if not email or not password:
                st.error("Completá todos los campos")
            else:
                st.success("¡Bienvenido de vuelta! 👋")
                goto("home")

    with tab_register:
        st.markdown("<br>", unsafe_allow_html=True)
        nombre = st.text_input("Nombre completo", placeholder="Juan García", key="reg_name")
        email_r = st.text_input("Email", placeholder="tucorreo@gmail.com", key="reg_email")
        pass_r = st.text_input("Contraseña", type="password", placeholder="••••••••", key="reg_pass")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Crear cuenta", key="btn_register"):
            if not nombre or not email_r or not pass_r:
                st.error("Completá todos los campos")
            else:
                st.session_state.user_name = nombre.split()[0]
                st.success("¡Cuenta creada! 🎉")
                goto("subscription")
        st.markdown('<p style="color:#8A9E8F; font-size:12px; text-align:center; margin-top:12px;">Al registrarte aceptás los <span style="color:#E8FF47;">Términos y Condiciones</span></p>', unsafe_allow_html=True)


# ─── SUSCRIPCION ───
def screen_subscription():
    st.markdown("""
    <div style="font-family:Space Grotesk,sans-serif; font-size:26px; font-weight:700; color:#FAFFF5; margin-bottom:4px;">Elegí tu plan</div>
    """, unsafe_allow_html=True)
    subtitle("Seleccioná el plan que mejor se adapte a tus objetivos")

    planes = [
        {
            "nombre": "Básico",
            "precio": "$8.999",
            "features": ["Acceso a 1 sede", "Clases virtuales ilimitadas", "Plan de rutinas básico"],
            "featured": False,
        },
        {
            "nombre": "Premium ⭐",
            "precio": "$14.999",
            "features": ["Acceso a todas las sedes", "Clases virtuales ilimitadas", "Plan nutricional personalizado", "Sistema Vida Puntos", "Reserva de máquinas"],
            "featured": True,
        },
        {
            "nombre": "Elite",
            "precio": "$24.999",
            "features": ["Todo lo del Premium", "Entrenador personal virtual", "Doble de puntos Vida", "Clases presenciales incluidas"],
            "featured": False,
        },
    ]

    for plan in planes:
        border = "#E8FF47" if plan["featured"] else "rgba(255,255,255,0.1)"
        bg = "rgba(232,255,71,0.06)" if plan["featured"] else "rgba(255,255,255,0.04)"
        features_html = "".join([f'<div style="font-size:13px; color:#8A9E8F; padding:3px 0;">✓ {f}</div>' for f in plan["features"]])
        card(f"""
        {"<div style='font-size:11px; font-weight:700; color:#1A3A2A; background:#E8FF47; display:inline-block; padding:2px 12px; border-radius:20px; margin-bottom:8px;'>⭐ Más popular</div>" if plan["featured"] else ""}
        <div style="font-size:18px; font-weight:700; color:#FAFFF5; margin-bottom:4px;">{plan["nombre"]}</div>
        <div style="font-family:Space Grotesk,sans-serif; font-size:32px; font-weight:700; color:#E8FF47; margin-bottom:12px;">{plan["precio"]} <span style="font-size:15px; color:#8A9E8F;">/mes</span></div>
        {features_html}
        """, border_color=border, bg=bg)

        if st.button(f"Elegir {plan['nombre']}", key=f"plan_{plan['nombre']}"):
            st.session_state.user_plan = plan["nombre"]
            goto("payment")

    st.markdown("<br>", unsafe_allow_html=True)


# ─── PAGO ───
def screen_payment():
    st.markdown(f"""
    <div style="font-family:Space Grotesk,sans-serif; font-size:24px; font-weight:700; color:#FAFFF5; margin-bottom:4px;">Método de pago</div>
    """, unsafe_allow_html=True)
    subtitle(f"Plan {st.session_state.user_plan} — confirmá tu pago")

    metodo = st.radio("Elegí cómo pagar:", ["💳 Tarjeta de crédito/débito", "🏦 Transferencia bancaria", "📱 Billetera virtual"], label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Confirmar y pagar"):
        st.success(f"✓ Pago procesado con {metodo}")
        goto("home")

    if st.button("← Cambiar plan", key="back_sub"):
        goto("subscription")


# ─── HOME ───
def screen_home():
    st.markdown(f"""
    <div style="padding: 8px 0 20px;">
        <div style="color:#8A9E8F; font-size:14px;">Buenos días 👋</div>
        <div style="font-family:Space Grotesk,sans-serif; font-size:28px; font-weight:700; color:#FAFFF5; margin-bottom:20px;">
            {st.session_state.user_name} <span style="color:#E8FF47;">Estevez</span>
        </div>
        <div style="background:linear-gradient(135deg,#E8FF47,#C8E000); border-radius:14px; padding:20px; display:flex; justify-content:space-between; align-items:center;">
            <div>
                <div style="font-size:11px; font-weight:600; color:#1A3A2A; opacity:0.7; text-transform:uppercase; letter-spacing:0.5px;">Vida Puntos</div>
                <div style="font-family:Space Grotesk,sans-serif; font-size:36px; font-weight:700; color:#1A3A2A;">{st.session_state.puntos:,}</div>
                <div style="font-size:12px; color:#1A3A2A; opacity:0.6;">Plan {st.session_state.user_plan or "Premium"} activo</div>
            </div>
            <div style="font-size:48px;">⚡</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    section_title("¿Qué querés hacer?")

    col1, col2 = st.columns(2)
    menu_items = [
        ("📱", "QR de Acceso", "Entrá a tu sede", "qr"),
        ("🥗", "Nutrición", "Plan personalizado", "nutricion"),
        ("🎥", "Clases", "Virtuales y presenciales", "clases"),
        ("🎁", "Vida Puntos", "Canjea beneficios", "puntos"),
        ("📍", "Sedes", "Encontrá tu gimnasio", "sedes"),
        ("📅", "Reservas", "Máquinas y horarios", "reservas"),
    ]

    for i, (icon, title, sub, dest) in enumerate(menu_items):
        col = col1 if i % 2 == 0 else col2
        with col:
            card(f"""
            <div style="font-size:26px; margin-bottom:8px;">{icon}</div>
            <div style="font-size:14px; font-weight:700; color:#FAFFF5; margin-bottom:3px;">{title}</div>
            <div style="font-size:12px; color:#8A9E8F;">{sub}</div>
            """, padding="16px")
            if st.button(title, key=f"menu_{dest}"):
                goto(dest)

    section_title("Rutina de hoy")
    card("""
    <div style="font-size:16px; font-weight:700; color:#FAFFF5; margin-bottom:6px;">💪 Fuerza — Tren Superior</div>
    <span style="background:rgba(232,255,71,0.1); color:#E8FF47; font-size:11px; font-weight:600; padding:3px 10px; border-radius:20px;">Ganar músculo</span>
    <div style="font-size:13px; color:#8A9E8F; margin-top:10px;">8 ejercicios · 45 min · Intermedio</div>
    """)
    if st.button("Ver rutina completa"):
        goto("rutinas")


# ─── QR ───
def screen_qr():
    back_button("home")
    st.markdown('<div style="font-family:Space Grotesk,sans-serif; font-size:22px; font-weight:700; color:#FAFFF5; margin-bottom:4px;">QR de Acceso</div>', unsafe_allow_html=True)
    subtitle("Mostrá este código en la entrada de tu sede")

    if not st.session_state.qr_verificado:
        st.markdown("""
        <div style="text-align:center; padding:30px 0;">
            <div style="font-size:80px; margin-bottom:16px;">👆</div>
            <div style="color:#FAFFF5; font-size:16px; margin-bottom:20px;">Se requiere verificación biométrica</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔐  Verificar huella digital"):
            with st.spinner("Verificando..."):
                import time; time.sleep(2)
            st.session_state.qr_verificado = True
            st.rerun()
    else:
        st.markdown("""
        <div style="text-align:center; padding:20px 0;">
            <div style="background:#FAFFF5; border-radius:20px; padding:20px; width:200px; margin:0 auto 20px; box-shadow:0 20px 60px rgba(0,0,0,0.4);">
                <div style="font-size:120px; line-height:1;">▓▒▓<br>▒▓▒<br>▓▒▓</div>
            </div>
            <div style="display:inline-flex; align-items:center; gap:10px; background:rgba(232,255,71,0.1); border:1px solid rgba(232,255,71,0.3); border-radius:30px; padding:10px 24px;">
                <div style="width:8px; height:8px; background:#E8FF47; border-radius:50%; animation:blink 1s infinite;"></div>
                <span style="color:#E8FF47; font-weight:600; font-size:14px;">Válido por 5 minutos</span>
            </div>
            <div style="color:#8A9E8F; font-size:12px; margin-top:12px;">Presentá este QR en el lector de acceso</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔄  Generar nuevo QR"):
            st.session_state.qr_verificado = False
            st.rerun()


# ─── NUTRICION ───
def screen_nutricion():
    back_button("home")
    st.markdown('<div style="font-family:Space Grotesk,sans-serif; font-size:22px; font-weight:700; color:#FAFFF5; margin-bottom:4px;">Plan Nutricional</div>', unsafe_allow_html=True)
    subtitle("Elegí tu objetivo y te mostramos el plan ideal")

    section_title("¿Cuál es tu objetivo?")
    objetivo = st.radio("Objetivo", ["🔥 Perder peso", "⚖️ Mantenerme", "💪 Ganar músculo", "⚡ Rendimiento"], horizontal=True, label_visibility="collapsed")
    st.session_state.objetivo_nutricional = objetivo
    st.markdown("<br>", unsafe_allow_html=True)

    section_title("Dietas recomendadas")

    dietas = [
        {
            "nombre": "🫒 Mediterránea",
            "kcal": "1.800 kcal",
            "desc": "Rica en vegetales, aceite de oliva, proteínas magras y cereales integrales. Ideal para déficit calórico saludable.",
            "carbos": "45%", "prot": "30%", "grasas": "25%"
        },
        {
            "nombre": "🥩 Alta en proteínas",
            "kcal": "2.200 kcal",
            "desc": "Maximiza la síntesis muscular con alta ingesta proteica. Ideal para ganancia de masa muscular.",
            "carbos": "35%", "prot": "45%", "grasas": "20%"
        },
        {
            "nombre": "🌱 Plant-based",
            "kcal": "1.600 kcal",
            "desc": "100% de origen vegetal. Rica en legumbres, tofu, tempeh y proteínas vegetales completas.",
            "carbos": "55%", "prot": "25%", "grasas": "20%"
        },
    ]

    for dieta in dietas:
        with st.expander(f"{dieta['nombre']}  —  {dieta['kcal']}"):
            st.markdown(f'<p style="color:#8A9E8F; font-size:14px;">{dieta["desc"]}</p>', unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown(f'<div style="text-align:center;"><div style="font-size:22px; font-weight:700; color:#E8FF47;">{dieta["carbos"]}</div><div style="font-size:11px; color:#8A9E8F;">Carbos</div></div>', unsafe_allow_html=True)
            with c2:
                st.markdown(f'<div style="text-align:center;"><div style="font-size:22px; font-weight:700; color:#E8FF47;">{dieta["prot"]}</div><div style="font-size:11px; color:#8A9E8F;">Proteína</div></div>', unsafe_allow_html=True)
            with c3:
                st.markdown(f'<div style="text-align:center;"><div style="font-size:22px; font-weight:700; color:#E8FF47;">{dieta["grasas"]}</div><div style="font-size:11px; color:#8A9E8F;">Grasas</div></div>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("**Comida sugerida hoy:**")
            st.markdown("🌅 **Desayuno** — Avena con frutas y proteína en polvo")
            st.markdown("☀️ **Almuerzo** — Pollo grillado con quinoa y vegetales")
            st.markdown("🌙 **Cena** — Salmón con batata y espinaca")
            if st.button(f"Guardar plan {dieta['nombre']}", key=f"save_diet_{dieta['nombre']}"):
                st.success(f"✓ Plan {dieta['nombre']} guardado")


# ─── VIDA PUNTOS ───
def screen_puntos():
    back_button("home")
    st.markdown('<div style="font-family:Space Grotesk,sans-serif; font-size:22px; font-weight:700; color:#FAFFF5; margin-bottom:16px;">Vida Puntos</div>', unsafe_allow_html=True)

    card(f"""
    <div style="text-align:center; padding:10px 0;">
        <div style="color:#8A9E8F; font-size:13px; margin-bottom:8px;">Tus puntos disponibles</div>
        <div style="font-family:Space Grotesk,sans-serif; font-size:56px; font-weight:700; color:#E8FF47; line-height:1;">{st.session_state.puntos:,}</div>
        <div style="color:#8A9E8F; font-size:13px; margin-top:8px;">Equivalen a ${st.session_state.puntos:,} en beneficios</div>
    </div>
    """, border_color="rgba(232,255,71,0.2)", bg="linear-gradient(135deg,rgba(45,90,61,0.8),rgba(61,122,82,0.4))", padding="24px")

    section_title("Canjear beneficios")

    beneficios = [
        ("🧴", "Proteína en polvo (1kg)", "Whey protein vainilla o chocolate", 1500),
        ("👕", "Remera FitLife", "Talle a elección, varios colores", 800),
        ("🥤", "Botella de agua", "Acero inoxidable 750ml", 400),
        ("🎟️", "1 mes gratis", "Extensión de suscripción", 5000),
    ]

    for icon, nombre, desc, costo in beneficios:
        col_info, col_btn = st.columns([3, 1])
        with col_info:
            card(f"""
            <div style="display:flex; align-items:center; gap:14px;">
                <div style="width:44px; height:44px; background:rgba(232,255,71,0.1); border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:20px; flex-shrink:0;">{icon}</div>
                <div>
                    <div style="font-size:14px; font-weight:600; color:#FAFFF5;">{nombre}</div>
                    <div style="font-size:12px; color:#8A9E8F;">{desc}</div>
                    <div style="font-size:13px; font-weight:700; color:#E8FF47; margin-top:3px;">{costo:,} pts</div>
                </div>
            </div>
            """, padding="14px")
        with col_btn:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Canjear", key=f"canje_{nombre}"):
                if st.session_state.puntos >= costo:
                    st.session_state.puntos -= costo
                    st.success(f"¡{nombre} canjeado! 🎉")
                    st.rerun()
                else:
                    st.error("Puntos insuficientes")


# ─── CLASES ───
def screen_clases():
    back_button("home")
    st.markdown('<div style="font-family:Space Grotesk,sans-serif; font-size:22px; font-weight:700; color:#FAFFF5; margin-bottom:4px;">Clases Virtuales</div>', unsafe_allow_html=True)

    filtro = st.selectbox("Filtrar por categoría:", ["Todas", "HIIT", "Fuerza", "Yoga", "Cardio", "Pilates"], label_visibility="collapsed")

    clases = [
        {"nombre": "Full Body HIIT", "tipo": "HIIT", "icono": "🔥", "duracion": "45 min", "nivel": "Intermedio", "inscriptos": 12},
        {"nombre": "Yoga Restore", "tipo": "Yoga", "icono": "🧘", "duracion": "60 min", "nivel": "Principiante", "inscriptos": 8},
        {"nombre": "Strength & Power", "tipo": "Fuerza", "icono": "💪", "duracion": "50 min", "nivel": "Avanzado", "inscriptos": 5},
        {"nombre": "Cardio Dance", "tipo": "Cardio", "icono": "💃", "duracion": "40 min", "nivel": "Principiante", "inscriptos": 20},
    ]

    for clase in clases:
        if filtro != "Todas" and clase["tipo"] != filtro:
            continue
        card(f"""
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:10px;">
            <div style="font-size:36px;">{clase['icono']}</div>
            <span style="background:#E8FF47; color:#1A3A2A; font-size:10px; font-weight:700; padding:3px 8px; border-radius:20px;">{clase['tipo']}</span>
        </div>
        <div style="font-size:16px; font-weight:700; color:#FAFFF5; margin-bottom:8px;">{clase['nombre']}</div>
        <div style="display:flex; gap:14px;">
            <span style="font-size:12px; color:#8A9E8F;">⏱ {clase['duracion']}</span>
            <span style="font-size:12px; color:#8A9E8F;">📊 {clase['nivel']}</span>
            <span style="font-size:12px; color:#8A9E8F;">👤 {clase['inscriptos']} inscriptos</span>
        </div>
        """)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Ver detalles", key=f"detalle_{clase['nombre']}"):
                st.session_state.clase_seleccionada = clase
                goto("clase_detalle")
        with col2:
            if st.button("Inscribirme", key=f"inscribir_{clase['nombre']}"):
                st.success(f"¡Inscripto a {clase['nombre']}! 🎉")
        st.markdown("<br>", unsafe_allow_html=True)


# ─── CLASE DETALLE ───
def screen_clase_detalle():
    back_button("clases")
    clase = st.session_state.clase_seleccionada
    if not clase:
        goto("clases"); return

    st.markdown(f"""
    <div style="text-align:center; padding:20px 0 16px;">
        <div style="font-size:60px;">{clase['icono']}</div>
        <div style="font-family:Space Grotesk,sans-serif; font-size:24px; font-weight:700; color:#FAFFF5; margin-top:10px;">{clase['nombre']}</div>
        <div style="display:flex; justify-content:center; gap:8px; margin-top:10px; flex-wrap:wrap;">
            <span style="background:rgba(232,255,71,0.1); color:#E8FF47; font-size:12px; font-weight:600; padding:4px 12px; border-radius:20px;">{clase['tipo']}</span>
            <span style="background:rgba(255,255,255,0.08); color:#FAFFF5; font-size:12px; padding:4px 12px; border-radius:20px;">⏱ {clase['duracion']}</span>
            <span style="background:rgba(255,255,255,0.08); color:#FAFFF5; font-size:12px; padding:4px 12px; border-radius:20px;">📊 {clase['nivel']}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    subtitle("Clase en vivo con instructor certificado. Sesión grabada disponible por 7 días.")

    section_title("Elegí día y horario")
    horarios = ["Lun 07:00", "Lun 19:00", "Mar 19:00", "Mié 08:00", "Jue 19:00", "Vie 18:00"]
    horario_sel = st.radio("Horario", horarios, horizontal=True, label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("✅  Confirmar inscripción"):
        st.success(f"¡Inscripto a {clase['nombre']} — {horario_sel}! 🎉")
    if st.button("Volver al catálogo", key="back_clases"):
        goto("clases")


# ─── SEDES ───
def screen_sedes():
    back_button("home")
    st.markdown('<div style="font-family:Space Grotesk,sans-serif; font-size:22px; font-weight:700; color:#FAFFF5; margin-bottom:16px;">Sedes</div>', unsafe_allow_html=True)

    card("""
    <div style="text-align:center; padding:20px;">
        <div style="font-size:40px;">🗺️</div>
        <div style="color:#8A9E8F; font-size:14px; margin-top:8px;">Mapa de sedes</div>
    </div>
    """)

    sedes = [
        {"nombre": "FitLife Palermo", "dir": "Honduras 4523, CABA", "open": True, "horario": "6:00 - 23:00", "concurrencia": "Media"},
        {"nombre": "FitLife Belgrano", "dir": "Av. Monroe 2101, CABA", "open": True, "horario": "6:00 - 22:00", "concurrencia": "Baja"},
        {"nombre": "FitLife Microcentro", "dir": "Av. Corrientes 1285, CABA", "open": False, "horario": "7:00 - 21:00", "concurrencia": "—"},
    ]

    for sede in sedes:
        estado_color = "#4CAF6F" if sede["open"] else "#FF6B6B"
        estado_bg = "rgba(76,175,111,0.2)" if sede["open"] else "rgba(255,68,68,0.15)"
        estado_text = "Abierto" if sede["open"] else "Cerrado"
        card(f"""
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px;">
            <div style="font-size:16px; font-weight:700; color:#FAFFF5;">{sede['nombre']}</div>
            <span style="background:{estado_bg}; color:{estado_color}; font-size:11px; font-weight:700; padding:3px 10px; border-radius:20px;">{estado_text}</span>
        </div>
        <div style="font-size:13px; color:#8A9E8F; margin-bottom:10px;">📍 {sede['dir']}</div>
        <div style="display:flex; gap:16px;">
            <span style="font-size:12px; color:#8A9E8F;">🕐 {sede['horario']}</span>
            <span style="font-size:12px; color:#8A9E8F;">👥 Afluencia {sede['concurrencia']}</span>
        </div>
        """)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Ver detalles", key=f"det_{sede['nombre']}"):
                st.info(f"📍 {sede['nombre']}\n\n🏋️ 40 máquinas · 🚴 20 bicis · 🏃 15 cintas")
        with col2:
            if sede["open"]:
                if st.button("📍 Cómo llegar", key=f"gps_{sede['nombre']}"):
                    st.success("Abriendo navegación GPS...")
        st.markdown("<br>", unsafe_allow_html=True)


# ─── RESERVAS ───
def screen_reservas():
    back_button("home")
    st.markdown('<div style="font-family:Space Grotesk,sans-serif; font-size:22px; font-weight:700; color:#FAFFF5; margin-bottom:16px;">Mis Reservas</div>', unsafe_allow_html=True)

    if st.button("＋  Nueva reserva"):
        goto("nueva_reserva")

    section_title("Reservas activas")

    if not st.session_state.reservas:
        st.markdown('<p style="color:#8A9E8F; text-align:center; padding:20px;">No tenés reservas activas</p>', unsafe_allow_html=True)
    else:
        to_delete = None
        for i, r in enumerate(st.session_state.reservas):
            card(f"""
            <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
                <div style="font-size:15px; font-weight:700; color:#FAFFF5;">{r['maquina']}</div>
                <span style="background:rgba(76,175,111,0.2); color:#4CAF6F; font-size:11px; font-weight:700; padding:3px 10px; border-radius:20px;">Confirmada</span>
            </div>
            <div style="font-size:13px; color:#8A9E8F;">📍 {r['sede']} · {r['horario']}</div>
            """)
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Modificar", key=f"mod_{i}"):
                    st.info("Redirigiendo a modificación...")
            with col2:
                if st.button("Cancelar", key=f"del_{i}"):
                    to_delete = i
            st.markdown("<br>", unsafe_allow_html=True)

        if to_delete is not None:
            st.session_state.reservas.pop(to_delete)
            st.warning("Reserva cancelada")
            st.rerun()


# ─── NUEVA RESERVA ───
def screen_nueva_reserva():
    back_button("reservas")
    st.markdown('<div style="font-family:Space Grotesk,sans-serif; font-size:22px; font-weight:700; color:#FAFFF5; margin-bottom:4px;">Nueva Reserva</div>', unsafe_allow_html=True)
    subtitle("Elegí sede, máquina y horario")

    sede = st.selectbox("Sede", ["FitLife Palermo", "FitLife Belgrano"])
    maquina = st.selectbox("Máquina", ["🏃 Cinta de correr", "🚴 Bicicleta estática", "🏋️ Banco de press", "💪 Rack de sentadillas"])
    horario = st.selectbox("Horario disponible", ["08:00", "09:00", "11:00", "18:00", "19:00"])

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("✅  Confirmar reserva"):
        st.session_state.reservas.append({
            "maquina": maquina,
            "sede": sede.replace("FitLife ", ""),
            "horario": f"Hoy {horario}"
        })
        st.success("¡Reserva confirmada! ✓")
        goto("reservas")


# ─── RUTINAS ───
def screen_rutinas():
    back_button("home")
    st.markdown('<div style="font-family:Space Grotesk,sans-serif; font-size:22px; font-weight:700; color:#FAFFF5; margin-bottom:4px;">Rutinas</div>', unsafe_allow_html=True)
    subtitle("Personalizadas según tus objetivos")

    rutinas = [
        {
            "nombre": "💪 Fuerza — Tren Superior",
            "obj": "Ganar músculo",
            "ejercicios": ["Press de banca", "Pull-ups", "Remo con barra", "Curl de bíceps", "Tríceps polea", "Hombros con mancuernas", "Face pull", "Aperturas"],
            "duracion": "45 min", "nivel": "Intermedio"
        },
        {
            "nombre": "🔥 Cardio — HIIT 20 min",
            "obj": "Perder peso",
            "ejercicios": ["Burpees", "Saltos al cajón", "Mountain climbers", "Sprint en cinta", "Jumping jacks", "Battle ropes"],
            "duracion": "20 min", "nivel": "Avanzado"
        },
        {
            "nombre": "🧘 Movilidad y Flexibilidad",
            "obj": "Rendimiento",
            "ejercicios": ["Estiramiento dinámico", "Movilidad de cadera", "Yoga flows", "Respiración diafragmática", "Roll de columna", "Apertura de pecho", "Pigeon pose"],
            "duracion": "30 min", "nivel": "Principiante"
        },
    ]

    for r in rutinas:
        with st.expander(f"{r['nombre']}  ·  {r['duracion']}  ·  {r['nivel']}"):
            st.markdown(f'<span style="background:rgba(232,255,71,0.1); color:#E8FF47; font-size:11px; font-weight:600; padding:3px 10px; border-radius:20px;">{r["obj"]}</span>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            for ej in r["ejercicios"]:
                st.markdown(f"• {ej}")
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button(f"▶ Iniciar rutina", key=f"start_{r['nombre']}"):
                st.success(f"¡Rutina iniciada! 💪")


# ═══════════════════════════════════════════════════════════
# ROUTER
# ═══════════════════════════════════════════════════════════

screen = st.session_state.screen

if screen == "splash":          screen_splash()
elif screen == "auth":          screen_auth()
elif screen == "subscription":  screen_subscription()
elif screen == "payment":       screen_payment()
elif screen == "home":          screen_home()
elif screen == "qr":            screen_qr()
elif screen == "nutricion":     screen_nutricion()
elif screen == "puntos":        screen_puntos()
elif screen == "clases":        screen_clases()
elif screen == "clase_detalle": screen_clase_detalle()
elif screen == "sedes":         screen_sedes()
elif screen == "reservas":      screen_reservas()
elif screen == "nueva_reserva": screen_nueva_reserva()
elif screen == "rutinas":       screen_rutinas()
else:                           screen_splash()
