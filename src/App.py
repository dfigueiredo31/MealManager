"""
## Lic. Engenharia Informatica ##
## 2024/2025 - 2o semestre ##
## Lab. Programacao ##
## Trab. Pratico 2 ##

# Objetivos #
    1. Escolha de Dieta e Preferências:
        Implementar  uma  função  que  permite  aos  utilizadores  escolherem  o  tipo  de  dieta  que desejam explorar e definirem as suas preferências alimentares, como restrições dietéticas e/ou preferências de ingredientes (por exemplo, os ingredientes que têm na despensa/frigorifico).
    2. Integração de API de Culinária:
        Utilizar API de serviços de culinária, como Spoonacular, CalorieNinjas, Edamam (https://rapidapi.com/collection/nutrition), para obter receitas  com base  nas preferências dos utilizadores, fornecendo informações detalhadas sobre ingredientes, instruções e valores nutricionais.
    3. Planeamento de Refeições:
        Desenvolver  uma  funcionalidade  que  permita  aos  utilizadores  criar  planos  de  refeições diárias ou semanais, escolhendo receitas e ajustando facilmente as porções.

    4. Listas de Compras Automáticas:
        Implementar a geração automática de listas de compras com base nas receitas escolhidas, simplificando o processo de compra de ingredientes necessários.

    5. Substituições de Ingredientes:
        Adicionar uma funcionalidade que sugira substituições de ingredientes, tendo em consideração as preferências e restrições alimentares dos utilizadores.

    6. Avaliações e Comentários de Utilizadores:
        Integrar  a  exibição  de  avaliações  e  comentários  de  outros  utilizadores  sobre  as  receitas, permitindo que os utilizadores tomem decisões informadas sobre o que cozinhar.

    7. Outras Funcionalidades:
        Podem ser acrescentadas outras funcionalidades à aplicação que possam majorar a qualidade da solução.
"""

import streamlit as st
from infrastructure import *
from entities import *

## inicialização do user ##

if not st.user.is_logged_in:
    if st.button("Log in with Google"):
            st.login("google")


st.secrets["api"]["api_key"]

if "user" not in st.session_state:
    st.session_state["user"] = None

if "firstRun" not in st.session_state:
    st.session_state["firstRun"] = True

if st.session_state["firstRun"]:
    try:
        userSerializer = Serializer.Serializer[User.User]()
        user = userSerializer.deserialize()
        st.session_state["user"] = user
        st.session_state["firstRun"] = False
    except:
        st.toast("Não há nenhum utilizador criado")

## configuração da sidebar de navegação ##

if st.session_state["user"] is not None:
    pages = {
        "Pessoal": [
            st.Page("pages/Home.py", title="Home"),
            st.Page("pages/Profile.py", title="Perfil"),
        ],
        "Recursos": [
            st.Page("pages/Meal plan.py", title="Plano Alimentar"),
            st.Page("pages/Shopping list.py", title="Lista de Compras"),
        ],
    }
else:
    pages = [st.Page("pages/Profile.py", title="Perfil")]

pg = st.navigation(pages)
pg.run()
