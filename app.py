import streamlit as st

st.set_page_config(
    page_title="電気設計Tools ポータル",
    layout="wide",
)

APPS = [
    {
        "name": "DXF-diff-manager",
        "name_ja": "図面差分管理ツール",
        "description": "図面の流用元との差分抽出・図面管理台帳の作成",
        "url": "https://dxf-diff-manager-cyapxlphcaajzu5mcchlcp.streamlit.app/",
        "placeholder": False,
    },
    {
        "name": "Ledger-merger",
        "name_ja": "図面管理台帳統合ツール",
        "description": "図面差分管理ツールが出力した複数の図番管理台帳を統合",
        "url": "https://ledger-merger-5hjdmtqn56kbaazzzqcc8c.streamlit.app/",
        "placeholder": False,
    },
    {
        "name": "Drawing-genealogy",
        "name_ja": "図番親子関係グラフツール",
        "description": "図番管理台帳から図番の親子関係を家系図として可視化",
        "url": "https://drawinggenealogy-tgk8fi3darlzaewppqmd7e.streamlit.app/",
        "placeholder": False,
    },
    {
        "name": "HostPL-extractor",
        "name_ja": "部品表比較ツール",
        "description": "ULKESと図面のパーツリストの機器符号を抽出・比較",
        "url": "https://hostpl-extractor-ct5db325tefzpzcbobxeul.streamlit.app/",
        "placeholder": False,
    },
]

st.title("電気設計ツール ポータル")
st.caption("各アプリはそれぞれ独立したアプリとして動作します。カードの「起動」をクリックすると新しいタブで開きます。")

# st.divider()

COLUMNS_PER_ROW = 2
rows = [APPS[i:i + COLUMNS_PER_ROW] for i in range(0, len(APPS), COLUMNS_PER_ROW)]

for row in rows:
    cols = st.columns(COLUMNS_PER_ROW)
    for col, app in zip(cols, row):
        with col:
            with st.container(border=True):
                st.subheader(app["name"])
                st.markdown(
                    f"<div style='font-size:1.1rem; font-weight:600; margin:-0.5rem 0 0.5rem 0;'>{app['name_ja']}</div>",
                    unsafe_allow_html=True,
                )
                st.write(app["description"])
                if app["placeholder"]:
                    st.caption("URLは仮のプレースホルダーです（デプロイ後に差し替え）")
                st.link_button("起動", app["url"], type="primary")
