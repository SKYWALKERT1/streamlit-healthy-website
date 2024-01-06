import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.title('Sağlıklı Besinler')
st.image(image="https://media.istockphoto.com/id/589415708/tr/foto%C4%9Fraf/fresh-fruits-and-vegetables.jpg?s=612x612&w=0&k=20&c=TzaFmq6d1_F621JGJv1YIYe-NWijB4T-j2JKkxvPqI0=")
st.header('Mevsim meyveleri ve sebzeleri:')
st.subheader('Meyvelerin Yararları')
st.write("- **Vitamin ve Mineral Kaynağı**: Meyveler, vücut için gerekli olan birçok vitamin ve minerali içerir. C vitamini, A vitamini, potasyum, folat, magnezyum gibi besin öğeleri meyvelerde bulunur.")
st.write("- **Antioksidan İçeriği**: Birçok meyve, antioksidanlar açısından zengindir. Antioksidanlar, vücuttaki serbest radikallerle savaşarak hücre hasarını azaltabilir ve çeşitli hastalıklara karşı koruma sağlayabilir.")
st.write("- **Lif İçeriği**: Meyveler genellikle lif bakımından zengindir. Lif, sindirim sistemi sağlığını destekler, bağırsak hareketliliğini artırır ve tokluk hissi sağlar.")
st.write("- **Kalp Sağlığı**: Meyveler, kalp sağlığını destekleyebilen potasyum, lif ve antioksidanlar gibi öğeler içerir. Bu, kalp hastalıkları riskini azaltmaya yardımcı olabilir.")
st.write("- **Kan Şekerini Dengeleme**: Bazı meyveler, düşük glisemik indekse sahip oldukları için kan şekerini düzenleyebilir. Lif içerikleri, şekerin daha yavaş emilmesine yardımcı olabilir.")
st.write("- **Kilo Kontrolü**: Lif içeriği ve düşük kalori değerleri sayesinde meyveler, kilo kontrolüne yardımcı olabilir.")
st.write("- **Bağışıklık Sistemini Güçlendirme**: C vitamini içeren meyveler, bağışıklık sistemini güçlendirerek hastalıklara karşı direnci artırabilir.")
st.write("- **Cilt Sağlığı**: Bazı meyveler, cilt sağlığını destekleyen vitamin ve antioksidanları içerir. Özellikle A vitamini içeren meyveler, cildin genç ve sağlıklı kalmasına yardımcı olabilir.")
st.write("Ancak, meyvelerin tüketilmesi konusunda dengeli bir yaklaşım önemlidir. Aşırı miktarda şeker içerebilirler, bu nedenle diyabet veya aşırı kilo sorunu olan kişilerin miktarlarına dikkat etmeleri gerekebilir. Ayrıca, her meyvenin özellikleri farklıdır, bu nedenle çeşitli meyveler tüketmek genel sağlığınız için daha iyidir.")


data_meyve = {
    'Aylar': ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'],
    'Meyve Tüketimi': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
}

df_meyve = pd.DataFrame(data_meyve)

# Streamlit uygulaması
st.title('Meyve Tüketimi Ay Bazında')

# Veri setini göster
st.dataframe(df_meyve)

# Meyve tüketimi grafiği
fig_meyve = px.bar(df_meyve, x='Aylar', y='Meyve Tüketimi', title='Meyve Tüketimi Ay Bazında')
st.plotly_chart(fig_meyve)

# Aylara özel öneriler
st.header('Aylara Özel Meyve Önerileri')

selected_month_meyve = st.selectbox('Bir ay seçin:', df_meyve['Aylar'])

if selected_month_meyve:
    st.write(f"{selected_month_meyve} ayında meyve tüketimini artırmak için:")
    if selected_month_meyve in ['Mayıs', 'Haziran', 'Temmuz', 'Ağustos']:
        st.write("- Taze meyve ve sebzeleri tercih edin.")
        st.write("- Sezonluk meyve ve sebzeleri kullanarak çeşitlilik ekleyin.")
    else:
        st.write("- Taze meyveleri haftalık alışveriş listenize ekleyin.")
        st.write("- Mevsimine uygun meyveleri tercih edin.")
data_countries = {
    'Ülke': ['Çin', 'Hindistan', 'Brezilya', 'Diğer Ülkeler'],
    'Üretim (milyon ton)': [272, 90.8, 39.6, 100]  # Varsayımsal veri
}

df_countries = pd.DataFrame(data_countries)

# Streamlit uygulaması
st.title('Yaş Meyve Üretimi - Ülkelerin Sıralaması')

# Veri setini göster
st.dataframe(df_countries)

# Bar grafiği
fig, ax = plt.subplots()
ax.bar(df_countries['Ülke'], df_countries['Üretim (milyon ton)'], color=['blue', 'orange', 'green', 'gray'])
ax.set_ylabel('Üretim (milyon ton)')
ax.set_title('Yaş Meyve Üretimi - Ülkelerin Sıralaması')

# Streamlit'e göre ayarlamalar
st.pyplot(fig)