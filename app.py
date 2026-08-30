import streamlit as st

st.set_page_config(
    page_title="電気設計Tools ポータル",
    page_icon="🧭",
    layout="wide",
)

APPS = [
    {
        "name": "DXF-diff-manager",
        "icon": "🗂️",
        "description": "DXF図面のペアリング・差分抽出・図面管理台帳（親子関係）の作成",
        "url": "https://dxf-diff-manager-cyapxlphcaajzu5mcchlcp.streamlit.app/",
        "placeholder": False,
    },
    {
        "name": "Ledger-merger",
        "icon": "🧩",
        "description": "DXF-diff-manager が出力した図面親子管理台帳（複数プロジェクト分）を統合",
        "url": "https://ledger-merger-5hjdmtqn56kbaazzzqcc8c.streamlit.app/",
        "placeholder": False,
    },
    {
        "name": "Drawing-genealogy",
        "icon": "🌳",
        "description": "図面親子関係台帳をアップロードし、図番の改訂・流用系譜を可視化",
        "url": "https://drawinggenealogy-tgk8fi3darlzaewppqmd7e.streamlit.app/",
        "placeholder": False,
    },
    {
        "name": "HostPL-extractor",
        "icon": "🔌",
        "description": "ULKESパーツリストExcelから指定アセンブリの機器符号リストを抽出",
        "url": "https://hostpl-extractor-ct5db325tefzpzcbobxeul.streamlit.app/",
        "placeholder": False,
    },
]

st.title("🧭 電気設計Tools ポータル")
st.caption("各アプリはそれぞれ独立したアプリとして動作します。カードの「起動」をクリックすると新しいタブで開きます。")

st.divider()

COLUMNS_PER_ROW = 2
rows = [APPS[i:i + COLUMNS_PER_ROW] for i in range(0, len(APPS), COLUMNS_PER_ROW)]

for row in rows:
    cols = st.columns(COLUMNS_PER_ROW)
    for col, app in zip(cols, row):
        with col:
            with st.container(border=True):
                st.subheader(f"{app['icon']} {app['name']}")
                st.write(app["description"])
                if app["placeholder"]:
                    st.caption("⚠️ URLは仮のプレースホルダーです（デプロイ後に差し替え）")
                st.link_button("起動 ↗", app["url"], type="primary")
