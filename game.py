# game.py (ВЕРСІЯ 6.0 - НАДІЙНИЙ ПЕРЕЗАПУСК)

import streamlit as st
import time
import base64
import os

# --- ФУНКЦІЇ-ПОМІЧНИКИ (без змін) ---
def get_image_as_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

# --- НОВА ФУНКЦІЯ: ІНІЦІАЛІЗАЦІЯ/СКИДАННЯ СТАНУ ---
# Ця функція буде встановлювати початкові значення, якщо їх немає,
# і буде викликатися для скидання гри.
def initialize_state():
    # Встановлюємо початкові значення для нової гри
    st.session_state.level = 0
    st.session_state.score = 0
    # Зберігаємо ім'я гравця, якщо воно вже було введене
    if 'player_name' not in st.session_state:
        st.session_state.player_name = ""

# Перевіряємо, чи був стан вже ініціалізований.
# Це робиться лише один раз за сесію.
if 'level' not in st.session_state:
    initialize_state()


# --- НАЛАШТУВАННЯ СТОРІНКИ ТА ФОНУ (без змін) ---
st.set_page_config(
    page_title="Cesta Python Mága",
    page_icon="🧙‍♂️",
    layout="wide"
)

image_file = "static/background.jpg"
if os.path.exists(image_file):
    image_base64 = get_image_as_base64(image_file)
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{image_base64}");
        background-size: cover;
    }}
    /* ... решта CSS без змін ... */
    .stApp .stMarkdown, .stApp .stHeader, .stApp .stTitle, .stApp .st-emotion-cache-1gulkj5 {{
        color: #FFFFFF; text-shadow: 1px 1px 3px #000000;
    }}
    .stTextInput, .stTextArea, .stButton {{
        background-color: rgba(20, 20, 40, 0.7); border-radius: 10px; padding: 10px; border: none;
    }}
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {{
        background-color: rgba(255, 255, 255, 0.1); color: #FFFFFF; border: 2px solid #9370DB; border-radius: 5px;
    }}
    .stButton > button {{
        background-color: #9370DB; color: white; border-radius: 10px; border: 2px solid #4B0082; width: 100%;
    }}
    .stButton > button:hover {{
        background-color: #4B0082; border-color: #9370DB;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# --- ФУНКЦІЇ РІВНІВ (зміни в display_level_0 та display_final_screen) ---

def display_level_0():
    st.title("🧙‍♂️ Vítej na Cestě Python Mága! 📜")
    st.image("static/wizard.png", width=200)
    st.markdown("### Tvá zkouška začíná, mladý učedníku!")
    st.markdown("Jsi v prastaré Akademii Kódu...")
    
    # Використовуємо st.session_state.player_name як значення за замовчуванням
    player_name = st.text_input(
        "Jak ti máme říkat, budoucí mágu?",
        value=st.session_state.player_name,  # Це дозволить зберегти ім'я при перезапуску
        key="player_name_input"
    )

    if st.button("Začít dobrodružství!"):
        if player_name:
            st.session_state.player_name = player_name
            st.session_state.level = 1
            st.rerun() # Тут rerun безпечний, бо ми не чистимо весь стан
        else:
            st.warning("Musíš zadat své jméno...")

# ... Функції для рівнів 1, 2, 3, 4, 5 залишаються абсолютно такими ж ...
def display_level_1():
    st.header("Úroveň 1: Komnata ozvěn 🗣️")
    st.markdown("První komnata testuje tvou schopnost **představit se**...")
    st.info("💡 **Tip:** Jména (řetězce) se v Pythonu píší do uvozovek...")
    user_code = st.text_area("Napiš své kouzlo zde:", height=100, key="level1_code")
    if st.button("Seslat kouzlo ✨"):
        correct_part1 = f"jmeno=\"{st.session_state.player_name}\""
        correct_part2 = "print(jmeno)"
        if correct_part1.replace(" ", "") in user_code.replace(" ", "") and correct_part2.replace(" ", "") in user_code.replace(" ", ""):
            st.success(f"Výborně, {st.session_state.player_name}! Dveře se otevírají!")
            st.balloons()
            st.session_state.score += 10
            st.session_state.level = 2
            time.sleep(2)
            st.rerun()
        else:
            st.error("Strážce ti nerozumí...")

def display_level_2():
    st.header("Úroveň 2: Síň číselných lektvarů 🧪")
    st.markdown("K odemčení dalších dveří musíš namíchat **lektvar síly**...")
    st.info("💡 **Tip:** Python používá `+`, `-`, `*`...")
    user_code = st.text_area("Napiš své kouzlo zde:", height=100, key="level2_code")
    if st.button("Namíchat lektvar 🧪"):
        if "vysledek" in user_code and "5" in user_code and "3" in user_code and "*" in user_code and "+" in user_code:
            try:
                loc = {}
                exec(user_code, {}, loc)
                if loc.get('vysledek') == 24:
                    st.success("Cítíš, jak ti v žilách proudí síla!...")
                    st.balloons()
                    st.session_state.score += 20
                    st.session_state.level = 3
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("Lektvar má divnou barvu...")
            except Exception as e:
                st.error(f"Kouzlo selhalo s chybou: {e}...")
        else:
            st.error("Zdá se, že ti chybí nějaká ingredience...")

def display_level_3():
    st.header("Úroveň 3: Knihovna rozhodnutí 📚")
    st.markdown("Před tebou stojí mluvící socha...")
    st.info("💡 **Tip:** Zde je příklad, jak funguje podmínka `if/else`...")
    st.code("vek = 20\nif vek >= 18:\n    print('Vstup povolen')\nelse:\n    print('Vstup odepřen')", language='python')
    user_code = st.text_area("Napiš své rozhodovací kouzlo:", height=150, key="level3_code")
    if st.button("Vyslovit slovo 🗣️"):
        normalized_code = user_code.replace(" ", "")
        if "volba='světlo'" in normalized_code and "ifvolba=='světlo':" in normalized_code and "else:" in normalized_code and "print(" in normalized_code:
            st.success("Správná volba! Socha ustupuje...")
            st.balloons()
            st.session_state.score += 30
            st.session_state.level = 4
            time.sleep(2)
            st.rerun()
        else:
            st.error("Socha nereaguje...")

def display_level_4():
    st.header("Úroveň 4: Zahrada opakování 🌳")
    st.markdown("K přípravě dalšího kouzla potřebuješ sesbírat tři ingredience...")
    st.info("💡 **Tip:** Cyklus `for` opakuje kód pro každý prvek v seznamu...")
    user_code = st.text_area("Napiš své sběrací kouzlo:", height=200, key="level4_code")
    if st.button("Začít sbírat 🌿"):
        is_correct = "for" in user_code and "in ingredience" in user_code and "print" in user_code and "kořen mandragory" in user_code and "hadí kůže" in user_code and "dračí šupina" in user_code
        if is_correct:
            st.success("Všechny ingredience jsou v tvém váčku!...")
            st.balloons()
            st.session_state.score += 40
            st.session_state.level = 5
            time.sleep(2)
            st.rerun()
        else:
            st.error("Něco ti chybí...")

def display_level_5():
    st.header("Úroveň 5: Svatyně mistrů 🏛️")
    st.markdown("Jsi u posledních dveří...")
    st.info("💡 **Tip:** Funkce se definuje pomocí `def nazev_funkce(argument):`...")
    user_code = st.text_area("Napiš své mistrovské kouzlo:", height=250, key="level5_code")
    if st.button("Vyslovit mistrovské zaklínadlo 🪄"):
        normalized_code = user_code.replace(" ", "")
        is_defined = "defotevri_dvere(heslo):" in normalized_code
        has_return = "return" in normalized_code
        has_if = "ifheslo==" in normalized_code
        is_called = "otevri_dvere(" in normalized_code
        if is_defined and has_return and has_if and is_called:
            st.success("Slyšíš skřípění kamene...")
            st.balloons()
            st.session_state.score += 50
            st.session_state.level = 6
            time.sleep(2)
            st.rerun()
        else:
            st.error("Pečeť je příliš silná...")


def display_final_screen():
    st.title(f"🎉 Gratuluji, Mágule {st.session_state.player_name}! 🎉")
    st.balloons()
    st.markdown(f"## Dosáhl jsi celkového skóre: **{st.session_state.score} bodů!**")
    st.markdown("Prošel jsi všemi zkouškami...")
    st.image("static/wizard.png", width=300, caption="Mistr Mág Pythonu")
    
    # --- НОВА ЛОГІКА КНОПКИ "ГРАТИ ЗНОВУ" ---
    if st.button("Hrát znovu?"):
        # Просто скидаємо рівень і рахунок. Ім'я залишається.
        st.session_state.level = 0
        st.session_state.score = 0
        st.rerun() # Перезапускаємо, щоб повернутися на стартовий екран

# --- ГОЛОВНА ЛОГІКА ГРИ (без змін) ---
st.sidebar.title("🐍 Panel Mága")
if st.session_state.player_name:
    st.sidebar.write(f"**Učedník:** {st.session_state.player_name}")
    # Показуємо рівень коректно
    level_to_show = st.session_state.level
    if st.session_state.level == 0: level_to_show = 1
    if st.session_state.level > 5: level_to_show = 5
    st.sidebar.write(f"**Úroveň:** {level_to_show} / 5")
    
    st.sidebar.write(f"**Skóre:** {st.session_state.score} bodů")
    st.sidebar.progress(st.session_state.level / 5 if st.session_state.level <= 5 else 1.0)
else:
    st.sidebar.write("Čekám na nového učedníka...")

# Роутер, який відображає правильний рівень в залежності від стану гри
if st.session_state.level == 0:
    display_level_0()
elif st.session_state.level == 1:
    display_level_1()
elif st.session_state.level == 2:
    display_level_2()
elif st.session_state.level == 3:
    display_level_3()
elif st.session_state.level == 4:
    display_level_4()
elif st.session_state.level == 5:
    display_level_5()
elif st.session_state.level == 6:
    display_final_screen()
