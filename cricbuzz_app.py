<<<<<<< HEAD
import streamlit as st
from sklearn.cluster import KMeans

st.title("Cricbuzz Match Analysis")

st.write("This dashboard shows match data scraped from Cricbuzz website")

import pandas as pd

df = pd.read_csv("matches1.csv")

# Display data
st.write("Match Data")
st.dataframe(df)

# Filter by Team
teams = df['team1'].unique()
selected_team = st.selectbox("Select Team", teams)

filtered_df = df[df['team1'] == selected_team]

st.write("Filtered Data")
st.dataframe(filtered_df)

# Filter by Team1
team1_list = df['team1'].unique()
selected_team1 = st.selectbox("Select Team 1", team1_list)

# Filter by Team2
team2_list = df['team2'].unique()
selected_team2 = st.selectbox("Select Team 2", team2_list)

# Apply both filters
filtered_df = df[
    (df['team1'] == selected_team1) &
    (df['team2'] == selected_team2)
]

st.write("Filtered Match Data")
st.dataframe(filtered_df)
if filtered_df.empty:
    st.write("No matches found for selected teams")

st.metric("Total Matches", len(df))


team_counts = filtered_df['team1'].value_counts()
st.write("Matches per Team")
st.bar_chart(team_counts)

match_counts = df.groupby(['team1', 'team2']).size().reset_index(name='count')

st.write("Matches between Teams")
st.bar_chart(match_counts.set_index('team1')['count'])


st.write("Add New Match")

new_match = st.text_input("Match (Team1 vs Team2)")
new_team1 = st.text_input("Team 1")
new_team2 = st.text_input("Team 2")

if st.button("Add Match"):
    insert_query = f"""
    INSERT INTO matches (match, team1, team2)
    VALUES ('{new_match}', '{new_team1}', '{new_team2}')
    """
    
    cur = conn.cursor()
    cur.execute(insert_query)
    conn.commit()
    
    st.success("Match added successfully!")


    st.write("Delete Match")

match_to_delete = st.selectbox("Select Match to Delete", df['match'])

if st.button("Delete Match"):
    delete_query = f"""
    DELETE FROM matches
    WHERE match = '{match_to_delete}'
    """
    
    cur = conn.cursor()
    cur.execute(delete_query)
    conn.commit()
    
    st.warning("Match deleted successfully!")

    # Count matches per team
team_counts = df['team1'].value_counts().reset_index()
team_counts.columns = ['Team', 'Matches']

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0)
team_counts['Cluster'] = kmeans.fit_predict(team_counts[['Matches']])

st.write("Team Clustering (ML)")
st.dataframe(team_counts)

=======
import streamlit as st
from sklearn.cluster import KMeans

st.title("Cricbuzz Match Analysis")

st.write("This dashboard shows match data scraped from Cricbuzz website")

import psycopg2
import pandas as pd

# Database connection
conn = psycopg2.connect(
    host="localhost",
    database="cricbuzz_db",
    user="postgres",
    password="1234",
    port="5433"
)

# Query
query = "SELECT * FROM matches;"
df = pd.read_sql(query, conn)

# Display data
st.write("Match Data")
st.dataframe(df)

# Filter by Team
teams = df['team1'].unique()
selected_team = st.selectbox("Select Team", teams)

filtered_df = df[df['team1'] == selected_team]

st.write("Filtered Data")
st.dataframe(filtered_df)

# Filter by Team1
team1_list = df['team1'].unique()
selected_team1 = st.selectbox("Select Team 1", team1_list)

# Filter by Team2
team2_list = df['team2'].unique()
selected_team2 = st.selectbox("Select Team 2", team2_list)

# Apply both filters
filtered_df = df[
    (df['team1'] == selected_team1) &
    (df['team2'] == selected_team2)
]

st.write("Filtered Match Data")
st.dataframe(filtered_df)
if filtered_df.empty:
    st.write("No matches found for selected teams")

st.metric("Total Matches", len(df))


team_counts = filtered_df['team1'].value_counts()
st.write("Matches per Team")
st.bar_chart(team_counts)

match_counts = df.groupby(['team1', 'team2']).size().reset_index(name='count')

st.write("Matches between Teams")
st.bar_chart(match_counts.set_index('team1')['count'])


st.write("Add New Match")

new_match = st.text_input("Match (Team1 vs Team2)")
new_team1 = st.text_input("Team 1")
new_team2 = st.text_input("Team 2")

if st.button("Add Match"):
    insert_query = f"""
    INSERT INTO matches (match, team1, team2)
    VALUES ('{new_match}', '{new_team1}', '{new_team2}')
    """
    
    cur = conn.cursor()
    cur.execute(insert_query)
    conn.commit()
    
    st.success("Match added successfully!")


    st.write("Delete Match")

match_to_delete = st.selectbox("Select Match to Delete", df['match'])

if st.button("Delete Match"):
    delete_query = f"""
    DELETE FROM matches
    WHERE match = '{match_to_delete}'
    """
    
    cur = conn.cursor()
    cur.execute(delete_query)
    conn.commit()
    
    st.warning("Match deleted successfully!")

    # Count matches per team
team_counts = df['team1'].value_counts().reset_index()
team_counts.columns = ['Team', 'Matches']

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0)
team_counts['Cluster'] = kmeans.fit_predict(team_counts[['Matches']])

st.write("Team Clustering (ML)")
st.dataframe(team_counts)

>>>>>>> e8b2e25bd895523c7d736437e0d6d91adff06067
    