# Derin-Ogrenme-Film-Onericisi
Bu proje, TMDB (The Movie Database) veri seti kullanılarak geliştirilen, içerik tabanlı bir film öneri sistemidir. Film özetleri ve içerik bilgileri metin işleme teknikleri ile sayısallaştırılmış, ardından tamamen kullanıcı tarafından eğitilen çok katmanlı bir AutoEncoder modeli kullanılarak filmler arasındaki anlamsal benzerlikler öğrenilmiştir.

Öneriler, cosine similarity metriği ile hesaplanmakta ve Streamlit tabanlı web arayüzü üzerinden kullanıcıya sunulmaktadır.

🚀 Projenin Amacı
Film içeriklerine dayalı olarak benzer filmleri önerebilen bir sistem geliştirmek
Derin öğrenme tabanlı, denetimsiz ve tamamen eğitilen bir model kullanmak
Kullanıcı geçmişi gerektirmeyen bir öneri yaklaşımı sunmak
Web tabanlı ve kullanıcı dostu bir arayüz oluşturmak

📊 Kullanılan Veri Seti
TMDB 5000 Movies
TMDB 5000 Credits

Veri setleri Kaggle platformu üzerinden temin edilmiştir.
Filmler hakkında şu bilgiler kullanılmaktadır:
Film özeti (overview)
Türler (genres)
Anahtar kelimeler (keywords)
Oyuncular (cast)
Yönetmen bilgisi (crew)

🧠 Kullanılan Yöntemler
Metin Ön İşleme (lowercase, noktalama temizleme)
TF-IDF vektörleştirme
Çok Katmanlı AutoEncoder (PyTorch)
Cosine Similarity
Yazım hatalarına toleranslı arama (difflib)
Streamlit Web Arayüzü

🎥 Web Arayüzü Özellikleri
Büyük/küçük harf duyarsız film arama
Yazım hatalarına tolerans
En yakın film adını otomatik tespit etme
Kart tabanlı, estetik öneri gösterimi

📈 Model Eğitimi ve Değerlendirme
Model, TF-IDF ile vektörleştirilmiş film metinlerini giriş olarak alır ve AutoEncoder yapısı ile daha düşük boyutlu, anlamlı temsiller öğrenir. Eğitim sürecinde loss değerlerinin azalması modelin başarılı şekilde öğrendiğini göstermektedir. Öneriler cosine similarity metriği ile değerlendirilmiştir.

📌 Sonuç
Bu proje, derin öğrenme tabanlı ve tamamen eğitilen bir içerik tabanlı öneri sisteminin başarılı şekilde uygulanabileceğini göstermektedir. Kullanıcı verisi bulunmayan senaryolarda etkili bir çözüm sunmakta ve geliştirilmeye açık bir yapı sağlamaktadır.

📚 Kaynakça
Kaggle – TMDB Movie Dataset
Aggarwal, C. C., Recommender Systems: The Textbook
Hinton & Salakhutdinov, Reducing the Dimensionality of Data with Neural Networks
Scikit-learn & PyTorch Dokümantasyonları
