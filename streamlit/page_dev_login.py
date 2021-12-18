import streamlit as st
import webbrowser

def is_authenticated(username):
    return username == "admin"

def is_authenticated(password):
    return password == "admin"


def generate_login_block():
    block1 = st.empty()
    block2 = st.empty()
    block3 = st.empty()

    return block1, block2, block3


def clean_blocks(blocks):
    for block in blocks:
        block.empty()

def login(blocks):
    return blocks[1].text_input('Username')

def loginP(blocks):
    blocks[0].markdown("""
            <style>
                input {
                    -webkit-text-security: disc;
                }
            </style>
        """, unsafe_allow_html=True)
    return blocks[2].text_input('Password')


def main():
    st.header('ML Monitoring')
    st.markdown("____")
    

    url_prom = 'https://news-analysis-monitoring-px7gwe6txq-uk.a.run.app'
    url_graf = "https://snapshot.raintank.io/dashboard/snapshot/PEqNUsyI1czoHp9Et6x8U4KSWOziE79Q?orgId=2"

    if st.button('Prometheus'):
        webbrowser.open_new_tab(url_prom)
    st.markdown("____")
    if st.button("Grafana"):
        webbrowser.open_new_tab(url_graf)
        

st.header("Developer site for News Analysis")
login_blocks = generate_login_block()
username = login(login_blocks)
password = loginP(login_blocks)

if is_authenticated(username) and is_authenticated(password):
    clean_blocks(login_blocks)
    main()
elif username or password:
    st.info("Please enter a valid username or password")
