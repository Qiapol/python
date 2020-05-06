import folium

# 地図を作って書き出す
m = folium.Map(location=[35.95601513, 136.17586812], zoom_start=16)
# 地図上にマーカーを付け足す
folium.Marker([35.95601513, 136.17586812]).add_to(m)
m.save('manage.html')
