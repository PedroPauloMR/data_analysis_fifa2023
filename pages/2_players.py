import streamlit as st
st.set_page_config(layout = 'wide')


df_data = st.session_state['data']

clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('Clube',clubes)

df_players = df_data.loc[df_data['Club'] == club]

players = df_players['Name'].value_counts().index
player = st.sidebar.selectbox('Jogadores',players)

player_ = 'Marquinhos'
player_stats = df_players.loc[df_players['Name'] == player].iloc[0]

st.image(player_stats['Photo'])
st.title(f"{player_stats['Name']}")

st.markdown(f"**Clube**: {player_stats['Club']}")
st.markdown(f"**Posição**: {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade**: {player_stats['Age']} anos")
col2.markdown(f"**Altura**: {player_stats['Height(cm.)']/100:.2f} m")
col3.markdown(f"**Peso**: {player_stats['Weight(lbs.)']*0.453:.2f} kg")


barra = '----------------------------------'
st.write(barra + barra + barra + barra + barra)
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label = 'Valor de Mercado', value = f"£ {player_stats['Value(£)']:,}")
col2.metric(label = 'Remuneração Semanal', value = f"£ {player_stats['Wage(£)']:,}")
col3.metric(label = 'Cláusula de Rescisão', value = f"£ {player_stats['Release Clause(£)']:,}")