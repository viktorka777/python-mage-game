# game.py (ФІНАЛЬНА ВЕРСІЯ 3.0)

import streamlit as st
import time

# --- НАЛАШТУВАННЯ СТОРІНКИ ---
st.set_page_config(
    page_title="Cesta Python Mága",
    page_icon="🧙‍♂️",
    layout="wide"
)

# --- СТИЛІЗАЦІЯ (CSS) ---
st.markdown("""
<style>
    .stTextInput > div > div > input {
        border: 2px solid #4B0082; /* Індиго */
        border-radius: 5px;
    }
    .stTextArea > div > div > textarea {
        border: 2px solid #4B0082;
        border-radius: 5px;
    }
    .stButton > button {
        background-color: #9370DB; /* Середній фіолетовий */
        color: white;
        border-radius: 10px;
        border: 2px solid #4B0082;
    }
    .stButton > button:hover {
        background-color: #4B0082;
        border-color: #9370DB;
    }
</style>
""", unsafe_allow_html=True)


# --- ІНІЦІАЛІЗАЦІЯ СТАНУ ГРИ ---
if 'level' not in st.session_state:
    st.session_state.level = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'player_name' not in st.session_state:
    st.session_state.player_name = ""
if 'error_message' not in st.session_state:
    st.session_state.error_message = ""

# --- ФУНКЦІЇ ДЛЯ РІВНІВ ---

def display_level_0():
    """Вступний екран гри"""
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
    """Рівень 1: Змінні та print()"""
    st.header("Úroveň 1: Komnata ozvěn 🗣️")
    st.markdown(
        "První komnata testuje tvou schopnost **představit se**. "
        "Strážce komnaty se tě ptá na tvé jméno. "
        "Vytvoř proměnnou `jmeno` a ulož do ní své jméno v uvozovkách. "
        "Poté ho vypiš pomocí funkce `print()`."
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
    """Рівень 2: Арифметика"""
    st.header("Úroveň 2: Síň číselných lektvarů 🧪")
    st.markdown(
        "K odemčení dalších dveří musíš namíchat **lektvar síly**. "
        "Recept zní: *'Vezmi 5 kapek dračí krve a přidej 3 gramy prachu z jednorožcova rohu. Celé to pak ztrojnásob.'*"
        "\n\nNapiš kód, který vypočítá výsledek a uloží ho do proměnné `vysledek`."
    )
    st.info("💡 **Tip:** Python používá `+`, `-`, `*` (násobení), `/` (dělení) a závorky `()` pro určení pořadí operací.")
    
    user_code = st.text_area("Napiš své kouzlo zde:", height=100, key="level2_code")
    
    if st.button("Namíchat lektvar 🧪"):
        if "vysledek" in user_code and "5" in user_code and "3" in user_code and "*" in user_code and "+" in user_code:
            try:
                loc = {}
                exec(user_code, {}, loc)
                if loc.get('vysledek') == 24:
                    st.success("Cítíš, jak ti v žilách proudí síla! Lektvar funguje! Postupuješ dál.")
                    st.balloons()
                    st.session_state.score += 20
                    st.session_state.level = 3
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("Lektvar má divnou barvu. Výsledek není správný. Zkontroluj výpočet!")
            except Exception as e:
                st.error(f"Kouzlo selhalo s chybou: {e}. Zkus to znovu.")
        else:
            st.error("Zdá se, že ti chybí nějaká ingredience nebo operace. Pečlivě si přečti recept!")

def display_level_3():
    """Рівень 3: Умови if/else"""
    st.header("Úroveň 3: Knihovna rozhodnutí 📚")
    st.markdown(
        "Před tebou stojí mluvící socha. Říká: *'Vyslov jedno ze dvou magických slov: **světlo** nebo **tma**. Jen jedno tě pustí dál.'*"
        "\n\nTvým úkolem je napsat kód, který se **rozhodne**. Vytvoř proměnnou `volba` s hodnotou `'světlo'`. "
        "Poté napiš podmínku `if`, která zkontroluje, jestli se `volba` rovná `'světlo'`. Pokud ano, vypiš `'Dveře se otevírají'`, jinak ( `else` ) vypiš `'Socha mlčí'`."
    )
    
    st.info("💡 **Tip:** Zde je příklad, jak funguje podmínka `if/else` pro kontrolu věku. Zkus použít stejnou logiku pro svou úlohu!")
    st.code(
        "vek = 20\n"
        "if vek >= 18:\n"
        "    print('Vstup povolen')\n"
        "else:\n"
        "    print('Vstup odepřen')", 
        language='python'
    )
    
    user_code = st.text_area("Napiš své rozhodovací kouzlo:", height=150, key="level3_code")
    
    if st.button("Vyslovit slovo 🗣️"):
        normalized_code = user_code.replace(" ", "")
        
        if "volba='světlo'" in normalized_code and \
           "ifvolba=='světlo':" in normalized_code and \
           "else:" in normalized_code and \
           "print(" in normalized_code:
            st.success("Správná volba! Socha ustupuje a odhaluje tajný průchod.")
            st.balloons()
            st.session_state.score += 30
            st.session_state.level = 4
            time.sleep(2)
            st.rerun()
        else:
            st.error("Socha nereaguje. Ujisti se, že tvůj kód má správnou strukturu `if/else` a porovnává správnou hodnotu.")
            
def display_level_4():
    """Рівень 4: Цикли for"""
    st.header("Úroveň 4: Zahrada opakování 🌳")
    st.markdown(
        "K přípravě dalšího kouzla potřebuješ sesbírat tři ingredience ze Zahrady opakování: **'kořen mandragory'**, **'hadí kůže'** a **'dračí šupina'**. "
        "Místo psaní tří příkazů pro každou ingredienci použij **cyklus `for`**, který projde seznam ingrediencí a vypíše je."
        "\n\n1. Vytvoř seznam `ingredience = [...]`."
        "\n2. Použij cyklus `for`, který pro každou položku v seznamu vypíše: `Sbírám: [název ingredience]`."
    )
    st.info("💡 **Tip:** Cyklus `for` opakuje kód pro každý prvek v seznamu. Příklad: `for i in muj_seznam: ...`")
    
    user_code = st.text_area("Napiš své sběrací kouzlo:", height=200, key="level4_code")
    
    if st.button("Začít sbírat 🌿"):
        is_correct = "for" in user_code and \
                     "in ingredience" in user_code and \
                     "print" in user_code and \
                     "kořen mandragory" in user_code and \
                     "hadí kůže" in user_code and \
                     "dračí šupina" in user_code
        
        if is_correct:
            st.success("Všechny ingredience jsou v tvém váčku! Cesta je volná.")
            st.balloons()
            st.session_state.score += 40
            st.session_state.level = 5
            time.sleep(2)
            st.rerun()
        else:
            st.error("Něco ti chybí. Použil jsi cyklus `for` a správně vytvořil seznam `ingredience`?")
            
def display_level_5():
    """Рівень 5: Функції"""
    st.header("Úroveň 5: Svatyně mistrů 🏛️")
    st.markdown(
        "Jsi u posledních dveří. Jsou zapečetěny mocnou magií. Aby sis je otevřel, musíš vytvořit své vlastní, znovupoužitelné kouzlo - **funkci**."
        "\n\nVytvoř funkci jménem `otevri_dvere`, která přijímá jeden argument `heslo`. "
        "Uvnitř funkce zkontroluj, jestli je `heslo` rovno `'SEZAME, OTEVŘI SE!'`. Pokud ano, funkce by měla vrátit (pomocí `return`) text `'Dveře se s rachotem otevírají!'`. Jinak by měla vrátit `'Ticho...'`."
        "\n\nPoté svou funkci zavolej se správným heslem."
    )
    st.info("💡 **Tip:** Funkce se definuje pomocí `def nazev_funkce(argument):`. Hodnota se vrací pomocí `return`.")

    user_code = st.text_area("Napiš své mistrovské kouzlo:", height=250, key="level5_code")
    
    if st.button("Vyslovit mistrovské zaklínadlo 🪄"):
        # --- ВИПРАВЛЕНА ЧАСТИНА ---
        # Тепер ми шукаємо шаблони без пробілів у коді, з якого теж видалені пробіли.
        normalized_code = user_code.replace(" ", "")
        
        is_defined = "defotevri_dvere(heslo):" in normalized_code
        has_return = "return" in normalized_code
        has_if = "ifheslo==" in normalized_code
        is_called = "otevri_dvere(" in user_code # Тут пробіл не важливий, бо ми не видаляємо його з коду
        
        if is_defined and has_return and has_if and is_called:
            st.success("Slyšíš skřípění kamene... Dveře se otevírají a za nimi vidíš sál plný světla. Dokázal jsi to!")
            st.balloons()
            st.session_state.score += 50
            st.session_state.level = 6
            time.sleep(2)
            st.rerun()
        else:
            st.error("Pečeť je příliš silná. Zkontroluj definici funkce (`def`), podmínku (`if`), použití `return` a její zavolání.")

def display_final_screen():
    """Фінальний екран"""
    st.title(f"🎉 Gratuluji, Mágule {st.session_state.player_name}! 🎉")
    st.balloons()
    st.markdown(f"## Dosáhl jsi celkového skóre: **{st.session_state.score} bodů!**")
    st.markdown(
        "Prošel jsi všemi zkouškami a dokázal, že jsi hoden titulu Python Mág. "
        "Tvá cesta teprve začíná, ale základy máš pevné jako skála. Pokračuj v učení a staň se nejmocnějším kodérem v zemi!"
    )
    st.image("static/wizard.png", width=300, caption="Mistr Mág Pythonu")
    
    if st.button("Hrát znovu?"):
        # Скидаємо стан гри, але зберігаємо ім'я гравця для зручності
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
