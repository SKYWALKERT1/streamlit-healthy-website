import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
st.image(image="https://media.istockphoto.com/id/1318478175/tr/foto%C4%9Fraf/ye%C5%9Fil-ah%C5%9Fap-masa-arka-plan-%C3%BCzerinde-vegan-%C3%A7i%C4%9F-sebzeler.jpg?s=612x612&w=0&k=20&c=1w9kyKIu38SJd8YeeTLj8Iorp11sNltLSeqS4nTBSXs=")
st.title("Sebzelerin Yararları")
st.write("- **Vitamin ve Mineral Kaynağı**: Meyveler, vücut için gerekli olan birçok vitamin ve minerali içerir. C vitamini, A vitamini, potasyum, folat, magnezyum gibi besin öğeleri meyvelerde bulunur.")
st.write("- **Antioksidan İçeriği**: Birçok sebze, antioksidanlar açısından zengindir. Antioksidanlar, vücuttaki serbest radikallerle savaşarak hücre hasarını azaltabilir ve çeşitli hastalıklara karşı koruma sağlayabilir.")
st.write("- **Lif İçeriği**: Sebzeler genellikle lif bakımından zengindir. Lif, sindirim sistemi sağlığını destekler, bağırsak hareketliliğini artırır, tokluk hissi sağlar ve kan şekeri seviyelerini kontrol altında tutabilir. ")
st.write("- **Düşük Kalori ve Yağ İçeriği**: Genellikle düşük kalori içeren sebzeler, kilo kontrolüne yardımcı olabilir. Ayrıca, sağlıklı yağlar içerirler. ")
st.write("- **Kanser Riskini Azaltma**: Sebzelerde bulunan antioksidanlar ve fitokimyasallar, kanser riskini azaltabilecek özelliklere sahiptir.")
st.write("- **Kardiyovasküler Sağlık**: Sebzeler, kalp sağlığını destekleyebilen potasyum, lif ve folat gibi öğeler içerir. Bu, kalp hastalıkları riskini azaltmaya yardımcı olabilir. ")
st.write("- **Bağışıklık Sistemini Güçlendirme**: Sebzeler, bağışıklık sistemini destekleyen C vitamini ve diğer vitaminleri içerir.")
st.write("- **Kemik Sağlığı**: Kalsiyum, magnezyum ve K vitamini içeren sebzeler, kemik sağlığını destekleyebilir. ")
st.write("- **Diyabet Kontrolü**: Lif içeriği sayesinde sebzeler, kan şekerini kontrol altında tutmaya yardımcı olabilir.")
st.write("- **Göz Sağlığı**: A vitamini içeren sebzeler, göz sağlığını destekleyebilir ve görme bozuklukları riskini azaltabilir.")
st.write("Yine de, sebzelerin tüketilmesinde çeşitlilik ve dengeli bir yaklaşım önemlidir. Farklı renkte ve çeşitte sebzeler tüketmek, vücuda farklı besin öğeleri sağlar. Aynı zamanda sebzelerin doğal halde, çiğ veya hafif pişirilmiş olarak tüketilmesi, içerdikleri vitamin ve mineral kaybını en aza indirir.")
data = {
    'Aylar': ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'],
    'Sebze Tüketimi': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
}

df = pd.DataFrame(data)

# Streamlit uygulaması
st.title('Sebze Tüketimi Ay Bazında')

# Veri setini göster
st.dataframe(df)

# Sebze tüketimi grafiği
fig = px.bar(df, x='Aylar', y='Sebze Tüketimi', title='Sebze Tüketimi Ay Bazında')
st.plotly_chart(fig)

# Aylara özel öneriler
st.header('Aylara Özel Öneriler')

selected_month = st.selectbox('Bir ay seçin:', df['Aylar'])

if selected_month:
    st.write(f"{selected_month} ayında sebze tüketimini artırmak için:")
    if selected_month in ['Mayıs', 'Haziran', 'Temmuz', 'Ağustos']:
        st.write("- Taze meyve ve sebzeleri tercih edin.")
        st.write("- Sezonluk meyve ve sebzeleri kullanarak çeşitlilik ekleyin.")
    else:
        st.write("- Taze sebzeleri haftalık alışveriş listenize ekleyin.")
        st.write("- Mevsimine uygun sebzeleri tercih edin.")
data_countries = {
    'Ülke': ['Çin', 'Hindistan', 'Brezilya', 'Türkiye', 'Diğer Ülkeler'],
    'Üretim (milyon ton)': [272, 90.8, 39.6, 25, 100]  # Varsayımsal veri
}

df_countries = pd.DataFrame(data_countries)

# Streamlit uygulaması
st.title('Sebzeler Üretimi - Ülkelerin Sıralaması')

# Veri setini göster
st.dataframe(df_countries)

# Bar grafiği
fig, ax = plt.subplots()
ax.bar(df_countries['Ülke'], df_countries['Üretim (milyon ton)'], color=['blue', 'orange', 'green', 'red', 'gray'])
ax.set_ylabel('Üretim (milyon ton)')
ax.set_title('Sebzeler Üretimi - Ülkelerin Sıralaması')

# Streamlit'e göre ayarlamalar
st.pyplot(fig)