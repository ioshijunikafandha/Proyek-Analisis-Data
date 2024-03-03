import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Memasukkan data tabel
day_df = pd.read_csv('data/day.csv')
hour_df = pd.read_csv('data/hour.csv')

season_label = {
    1: 'Summer',
    2: 'Autumn',
    3: 'Spring',
    4: 'Winter'
}

# Menggunakan metode .map() untuk menambahkan kolom season_label ke dalam DataFrame
day_df['season_label'] = day_df['season'].map(season_label)

weekday_label = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}

# Menambahkan kolom 'weekday_label' menggunakan metode .map()
day_df['weekday_label'] = day_df['weekday'].map(weekday_label)

# Hitung rata-rata jumlah pengguna sepeda berdasarkan musim
avg_season = day_df.groupby('season_label')['cnt'].mean().reset_index()

# Set up plot
plt.figure(figsize=(10, 7))
plt.barh(avg_season['season_label'], avg_season['cnt'], color=('#432818', '#582f0e', '#eddea4', '#685634'))
plt.title('Rata-rata Jumlah Pengguna Sepeda berdasarkan Musim')
plt.xlabel('Rata-rata Jumlah Pengguna Sepeda')
plt.ylabel('Musim')
plt.yticks(rotation=45)
plt.grid(axis='x', linestyle='--', alpha=0.7)

st.write("### Rata-rata Penyewaan Sepeda Berdasarkan Musim")
st.write(avg_season)

# Show plot
st.pyplot(plt)

avg_weekday = day_df.groupby('weekday')['cnt'].mean()

# Membuat plot pie chart
fig, ax = plt.subplots()
ax.pie(avg_weekday, labels=avg_weekday.index, autopct='%1.1f%%', colors=('#7f4f24', '#eddea4', '#432818', '#f6f4d2'), wedgeprops=dict(width=0.4))
ax.set_title('Rata-rata Penyewaan Sepeda pada Hari dalam Seminggu')

st.write("### Rata-rata Penyewaan Sepeda pada Hari dalam Seminggu")
st.write(avg_weekday)

# Menampilkan plot menggunakan Streamlit
st.pyplot(fig)