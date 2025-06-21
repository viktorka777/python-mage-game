# game.py (ВЕРСІЯ 12.0 - ФІНАЛЬНА ЧИТАБЕЛЬНІСТЬ)

import streamlit as st
import time

# --- НАЛАШТУВАННЯ СТОРІНКИ ---
st.set_page_config(
    page_title="Cesta Python Mága",
    page_icon="🧙‍♂️",
    layout="wide"
)

# --- ФІНАЛЬНИЙ БЛОК СТИЛІВ ДЛЯ ІДЕАЛЬНОЇ ЧИТАБЕЛЬНОСТІ ---

# !!! ВАЖЛИВО: ПЕРЕВІР, ЩО ТУТ ТВОЄ ПРАВИЛЬНЕ ПРЯМЕ ПОСИЛАННЯ З GITHUB !!!
image_url = "https://raw.githubusercontent.com/viktorka777/python-mage-game/refs/heads/main/static/background.png"

page_bg_style = f"""
<style>
/* --- ГОЛОВНИЙ ФОН --- */
.stApp {{
    background-image: url("{image_url}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* --- ОСНОВНИЙ ТЕКСТ (ЗАГОЛОВКИ, ПИТАННЯ) --- */
.stApp .stMarkdown, .stApp .stHeader, .stApp .stTitle, .stApp label {{
    color: #FFFFFF !important;
    text-shadow: 1px 1px 3px #000000;
}}

/* --- ПОЛЯ ДЛЯ ВВОДУ --- */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {{
    background-color: rgba(0, 0, 0, 0.4);
    color: #FFFFFF;
    border: 2px solid #9370DB;
    border-radius: 5px;
}}

/* --- КНОПКИ --- */
.stButton > button {{
    background-color: #9370DB;
    color: white;
    border-radius: 10px;
    border: 2px solid #4B0082;
}}
.stButton > button:hover {{
    background-color: #4B0082;
    border-color: #9370DB;
}}

/* --- ПІДКАЗКИ (st.info, st.success, і т.д.) --- */
[data-testid="stAlert"] {{
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    background-color: rgba(0, 0, 0, 0.2);
}}
[data-testid="stAlert"] p {{
    color: white !important;
    text-shadow: none;
}}

/* --- ВЕЛИКІ БЛОКИ КОДУ --- */
[data-testid="stCodeBlock"] {{
    background-color: rgba(0, 0, 0, 0.5) !important;
    border-radius: 10px;
}}

/* --- БІЧНА ПАНЕЛЬ --- */
[data-testid="stSidebar"] {{
    background-color: rgba(0, 0, 0, 0.5);
}}
[data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] .stTitle {{
     color: #FFFFFF !important;
}}

/* --- НОВЕ ВИПРАВЛЕННЯ: Маленькі вбудовані блоки коду в тексті --- */
.stMarkdown code {{
    background-color: rgba(255, 255, 255, 0.2) !important; /* Світлий напівпрозорий фон */
    color: #f0f2f6 !important; /* Яскравий світло-сірий текст */
    padding: 0.1em 0.3em;
    border-radius: 5px;
}}
</style>
"""
st.markdown(page_bg_style, unsafe_allow_html=True)


# --- ІНІЦІАЛІЗАЦІЯ СТАНУ ГРИ (стабільна версія) ---
if 'level' not in st.session_state:
    st.session_state.level = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'player_name' not in st.session_state:
    st.session_state.player_name = ""
if 'error_message' not in st.session_state:
    st.session_state.error_message = ""

# --- ФУНКЦІЇ РІВНІВ (без змін, стабільна логіка) ---
def display_level_0():
    st.title("🧙‍♂️ Vítej na Cestě Python Mága! 📜")
    st.image("static/wizard.png", width=200)
    st.markdown("### Tvá zkouška začíná, mladý učedníku!")
    st.markdown(
        "Jsi v prastaré Akademii Kódu. Aby ses stal pravým Python Mágem, "
        "musíš projít pěti začarovanými komnatami. V každé z nich musíš seslat "
        "správné kouzlo (napsat správný kód), abys otevřel dveře dál."
    )
    player_name = st.text_input("Jak ti máme říkat, budoucí mágu?", key="player_name_input")
    if st.button("Začít dobrodružství!"):
        if player_name:
            st.session_state.player_name = player_name
            st.session_state.level = 1
            st.rerun()
        else:
            st.warning("Musíš zadat své jméno, aby kronikáři věděli, o kom psát!")

def display_level_1():
    st.header("Úroveň 1: Komnata ozvěn 🗣️")
    st.markdown(
        "První komnata testuje tvou schopnost **představit se**. Strážce komnaty se tě ptá na tvé jméno. Vytvoř proměnnou `jmeno` a ulož do ní své jméno v uvozovkách. Poté ho vypiš pomocí funkce `print()`."
    )
    st.info("💡 **Tip:** Jména (řetězce) se v Pythonu píší do uvozovek, např. `\"Albus\"`.")
    user_code = st.text_area("Napiš své kouzlo zde:", height=100, key="level1_code")
    if st.button("Seslat kouzlo ✨"):
        correct_part1 = f"jmeno=\"{st.session_state.player_name}\""
        correct_part2 = "print(jmeno)"
        if correct_part1.replace(" ", "") in user_code.replace(" ", "") and \
           correct_part2.replace(" ", "") in user_code.replace(" ", ""):
            st.success(f"Výborně, {st.session_state.player_name}! Dveře se otevírají!")
            st.balloons()
            st.session_state.score += 10
            st.session_state.level = 2
            time.sleep(2)
            st.rerun()
        else:
            st.error("Strážce ti nerozumí. Zkontroluj, zda jsi správně vytvořil proměnnou `jmeno` a použil funkci `print()`.")

def display_level_2():
    st.header("Úroveň 2: Síň číselných lektvarů 🧪")
    st.markdown(
        "K odemčení dalších dveří musíš namíchat **lektvar síly**. "
        "Recept zní: *'Vezmi 5 kapek dračí krve a přidej 3 gramy prachu z jednorožcova rohu. Celé to pak ztrojnásob.'*"
    )
    st.info("💡 **Tip:** Python používá `+`, `-`, `*`, `/` a `()`.")
    user_code = st.text_area("Napiš své kouzlo zde:", height=100, key="level2_code")
    if st.button("Namíchat lektvar 🧪"):
        if "vysledek" in user_code and "5" in user_code and "3" in user_code and "*" in user_code and "+" in user_code:
            try:
                loc = {}
                exec(user_code, {}, loc)
                if loc.get('vysledek') == 24:
                    st.success("Cítíš, jak ti v žilách proudí síla! Postupuješ dál.")
                    st.balloons()
                    st.session_state.score += 20
                    st.session_state.level = 3
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("Lektvar má divnou barvu. Zkontroluj výpočet!")
            except Exception as e:
                st.error(f"Kouzlo selhalo s chybou: {e}.")
        else:
            st.error("Zdá se, že ti chybí nějaká ingredience nebo operace.")

def display_level_3():
    st.header("Úroveň 3: Knihovna rozhodnutí 📚")
    st.markdown(
        "Před tebou stojí mluvící socha. Říká: *'Vyslov jedno ze dvou magických slov: **světlo** nebo **tma**. Jen jedno tě pustí dál.'*"
    )
    st.info("💡 **Tip:** Zde je příklad `if/else`... `if vek >= 18: ...`")
    st.code("vek = 20\nif vek >= 18:\n    print('Vstup povolen')\nelse:\n    print('Vstup odepřen')", language='python')
    user_code = st.text_area("Napiš své rozhodovací kouzlo:", height=150, key="level3_code")
    if st.button("Vyslovit slovo 🗣️"):
        normalized_code = user_code.replace(" ", "")
        has_variable = "volba='světlo'" in normalized_code or 'volba="světlo"' in normalized_code
        has_condition = "ifvolba=='světlo':" in normalized_code or 'ifvolba=="světlo":' in normalized_code
        has_else = "else:" in normalized_code
        has_print = "print(" in normalized_code
        if has_variable and has_condition and has_else and has_print:
            st.success("Správná volba! Socha ustupuje.")
            st.balloons()
            st.session_state.score += 30
            st.session_state.level = 4
            time.sleep(2)
            st.rerun()
        else:
            st.error("Socha nereaguje. Zkontroluj strukturu `if/else`.")

def display_level_4():
    st.header("Úroveň 4: Zahrada opakování 🌳")
    st.markdown("K přípravě dalšího kouzla potřebuješ sesbírat tři ingredience...")
    st.info("💡 **Tip:** Cyklus `for` opakuje kód pro každý prvek v seznamu...")
    user_code = st.text_area("Napiš své sběrací kouzlo:", height=200, key="level4_code")
    if st.button("Začít sbírat 🌿"):
        is_correct = "for" in user_code and "in ingredience" in user_code and "print" in user_code and "kořen mandragory" in user_code and "hadí kůže" in user_code and "dračí šupina" in user_code
        if is_correct:
            st.success("Všechny ingredience jsou v tvém váčku!")
            st.balloons()
            st.session_state.score += 40
            st.session_state.level = 5
            time.sleep(2)
            st.rerun()
        else:
            st.error("Něco ti chybí. Použil jsi `for` a seznam `ingredience`?")

def display_level_5():
    st.header("Úroveň 5: Svatyně mistrů 🏛️")
    st.markdown("Vytvoř funkci jménem `otevri_dvere`, která přijímá `heslo`...")
    st.info("💡 **Tip:** Funkce se definuje pomocí `def nazev_funkce(argument):`...")
    user_code = st.text_area("Napiš své mistrovské kouzlo:", height=250, key="level5_code")
    if st.button("Vyslovit mistrovské zaklínadlo 🪄"):
        normalized_code = user_code.replace(" ", "")
        is_defined = "defotevri_dvere(heslo):" in normalized_code
        has_return = "return" in normalized_code
        has_if = "ifheslo==" in normalized_code
        is_called = "otevri_dvere(" in user_code
        if is_defined and has_return and has_if and is_called:
            st.success("Slyšíš skřípění kamene... Dokázal jsi to!")
            st.balloons()
            st.session_state.score += 50
            st.session_state.level = 6
            time.sleep(2)
            st.rerun()
        else:
            st.error("Pečeť je příliš silná. Zkontroluj definici `def` a її zavolání.")

def display_final_screen():
    st.title(f"🎉 Gratuluji, Mágule {st.session_state.player_name}! 🎉")
    st.balloons()
    st.markdown(f"## Dosáhl jsi celkového skóre: **{st.session_state.score} bodů!**")
    st.markdown("Prošel jsi všemi zkouškami...")
    st.image("static/wizard.png", width=300, caption="Mistr Mág Pythonu")
    if st.button("Hrát znovu?"):
        st.session_state.level = 1
        st.session_state.score = 0
        st.rerun()

# --- ГОЛОВНА ЛОГІКА ГРИ ---
st.sidebar.title("🐍 Panel Mága")
if st.session_state.player_name:
    st.sidebar.write(f"**Učedník:** {st.session_state.player_name}")
    st.sidebar.write(f"**Úroveň:** {st.session_state.level if st.session_state.level <= 5 else 5} / 5")
    st.sidebar.write(f"**Skóre:** {st.session_state.score} bodů")
    st.sidebar.progress(st.session_state.level / 5 if st.session_state.level <= 5 else 1.0)
else:
    st.sidebar.write("Čekám na nového učedníka...")

# Роутер
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
