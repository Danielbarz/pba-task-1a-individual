from nltk import word_tokenize
import math

# Function to calculate TF for a term in a document
def calculate_tf(term, document):
    words = word_tokenize(document.lower())
    return words.count(term) / len(words) if len(words) > 0 else 0

# Function to calculate IDF for a term across all documents
def calculate_idf(term, all_documents):
    num_documents_with_term = sum(1 for doc in all_documents if term.lower() in word_tokenize(doc.lower()))
    if num_documents_with_term > 0:
        return math.log(len(all_documents) / num_documents_with_term)
    else:
        return 0


paragraph_danantara = """Jakarta: Badan Pengelola Investasi Daya Anagata Nusantara (BPI Danantara) siap mengawal realisasi investasi yang telah disepakati dengan Qatar. Kesepakatan antara Indonesia dan Qatar merupakan buah dari kunjungan resmi Presiden Prabowo Subianto ke Doha.

Pemerintah Republik Indonesia dan Pemerintah Qatar menggelar diskusi untuk menyepakati kemitraan strategis (co-partnership) dalam pengelolaan dana investasi untuk Indonesia yang akan berfokus di berbagai sektor pembangunan.

Salah satu hasil utama dari kunjungan tersebut adalah untuk membentuk dana investasi bersama senilai USD4 miliar. Dana ini akan difokuskan pada pengembangan berbagai sektor di antaranya termasuk tapi tidak terbatas pada hilirisasi industri, energi terbarukan, dan fasilitas kesehatan di Indonesia.

"Kami menyambut baik kepercayaan yang diberikan oleh Pemerintah Qatar melalui pembentukan dana bersama ini," kata CEO Danantara Indonesia Rosan Perkasa Roeslani dalam keterangan tertulis, Selasa, 15 April 2025.

Presiden Prabowo menyampaikan masing-masing negara akan berkontribusi sebesar USD2 miliar dalam dana tersebut. Dana itu akan dikelola oleh BPI Danantara bersama dengan Qatar Investment Authority (QIA) dalam co-partnership. Buka peluang investasi sektor strategis
Dana tersebut akan difokuskan pada peluang investasi di berbagai sektor strategis, antara lain hilirisasi, kesehatan, energi terbarukan, teknologi, serta sektor-sektor lain yang dipandang relevan oleh pengelola dana.

"Danantara Indonesia siap menjalankan mandat tersebut dengan menerapkan tata kelola investasi yang prudent, transparan, dan berorientasi pada hasil. Fokus kami adalah memastikan bahwa setiap proyek yang didanai memberikan dampak strategis dan berkelanjutan bagi perekonomian nasional," ujar Rosan.

Lebih lanjut, Rosan menegaskan, kolaborasi ini menjadi bukti kepercayaan dunia internasional terhadap kapasitas kelembagaan Indonesia dalam mengelola investasi berskala besar.

"Kemitraan ini merupakan langkah konkret dalam membangun kepercayaan dengan mitra global strategis seperti Qatar. Ini menunjukkan bahwa Indonesia tidak hanya menjadi tujuan investasi, tetapi juga memiliki kapasitas kelembagaan yang mumpuni untuk mengelola nvestasi secara profesional dan akuntabel," ungkapnya.

Inisiatif co-partnership dan perluasan kerja sama strategis ini diharapkan tidak hanya memperkuat hubungan diplomatik kedua negara, tetapi juga memberikan kontribusi nyata terhadap percepatan pembangunan ekonomi dan peningkatan kesejahteraan masyarakat Indonesia. Jangan lupa ikuti update berita lainnya dan follow  akun
Google News Metrotvnews.com dan Channel WhatsApp Metro TV

(Eko Nordiansyah)"""

paragraph_manchester = """
Manchester City makes history by winning Club World Cup

Manchester City capped off its incredible year with yet another trophy, dismantling Fluminense 4-0 to win the Club World Cup on Friday.

Having already won the Premier League, Champions League, FA Cup and Super Cup, Pep Guardiola’s side now boasts five trophies this calendar year, becoming the first English club to ever hold all those titles simultaneously.

The final piece of the jigsaw came on a highly charged night in Saudi Arabia as Manchester City outclassed its Brazilian opponents.

“We’ve shown over the past 12 months we are the best team in the world. Our results prove that and the consistency we have managed has been amazing,” club captain Kyle Walker said after the game, per Sky Sports.

“To win these five trophies – for me, the five biggest prizes available to us – is incredible. I am so proud to have been a part of this and I can honestly say it’s an honour to play alongside these players. I couldn’t ask for better teammates.”

It took just 40 seconds for Manchester City to take the lead.

Brazilian left-back Marcelo miscued a pass in the opening exchanges which let Nathan Aké free to shoot from distance. The defender’s effort cannoned back off the post but forward Julián Álvarez was in the right place to turn the rebound into the net with his chest.

City continued to look dangerous and doubled its lead before the break after Phil Foden’s attempted cross was deflected into his own net by Fluminense defender Nino.

Foden then got on the scoresheet himself in the 72nd minute after a prodding home from close range.

The rout was completed in the 88th minute when Álvarez capped off a brilliant performance with a clinical finish into the far corner.

City’s defence was largely untested for during the game, underlining the team’s dominance during this unforgettable year.

“As a manager it is what I am most proud of; that we are always there. No matter how much we win, no matter what trophies we lift, we are there again to fight for the next one,” City boss Guardiola said after the match, according to Sky Sports.

“To win the Treble was truly special, but to win two more trophies and now hold these five major titles shows the unique mentality of this team, of the Club and its fans.

“It is something no other English team has ever achieved, and we will always remember this incredible time we spent together.”

The game ended in some unsavoury scenes as a scuffle broke out between players on the pitch after the final whistle, but the game will be remembered as yet another successful night for City.

The champion heads back to England where it faces a tough title defence in the Premier League.

It currently sits fourth in the table and will face Everton in its next fixture on Wednesday.
"""

# taken from https://www.tempo.co/hukum/duduk-perkara-protes-warga-soal-lapangan-padel-di-cilandak-2116800
paragraph_padel = """
Lapangan padel yang berdempetan dengan permukiman warga dianggap menimbulkan kebisingan. Bagaimana respon manajemen?

KEBERADAAN sebidang lapangan padel di Jalan Haji Nawi Raya, Cilandak, Jakarta Selatan, memancing protes. Arena olahraga tersebut dinilai menimbulkan kebisingan yang mengganggu aktivitas masyarakat karena jaraknya yang berdempetan dengan permukiman warga.

Kebisingan lapangan milik Fourtwall Padel tersebut mulai dirasakan warga sekitar sejak akhir 2026 lalu. "Saat itu sepertinya masih trial lapangan, itu saya melapor tanggal 27 November," ujar Naufal pada Kamis, 19 Februari 2026.

Naufal dan keluarga merasa sangat terganggu akibat aktivitas di lapangan tersebut. "Suara pukulan bola dan teriakan mulai jam 6 pagi hingga jam 12 malam, itu menyiksa kami," tutur Naufal saat ditemui Tempo di kediaman pribadinya.

Menurut Naufal, kondisi tersebut membuat penghuni rumah kehilangan fokus. Dia bercerita sering sengaja pulang larut malam karena tidak tahan dengan bising dari lapangan padel. "Mandi saja tidak fokus karena berisik," ucap Naufal.

Naufal mengatakan dirinya sudah berkali-kali melancarkan protes terkait operasional lapangan tersebut. Setidaknya ada total 15 laporan dia daftarkan lewat aplikasi Jakarta Kini (JAKI) serta sekali aduan ke pihak kepolisian, tetapi tidak satupun yang berbuahkan hasil.

Warga lainnya, Idham Rahmanarto, juga merasakan hal serupa. Dia merasa sangat terganggu dengan kebisingan yang disebabkan oleh lapangan Fourthwall Padel, terutama terhadap anaknya yang masih berumur 1,5 tahun.

Sama seperti Naufal, protes juga dilakukan oleh Idham lewat jalur resmi maupun media sosial. Namun dari beberapa kali mediasi yang dijalani belum ada solusi yang didapat. "Semua hasil mediasi cuma janji-janji lisan, tidak ada kesepakatan tertulis," kata Idham saat ditemui di kesempatan yang sama.

Idham mencontohkan dengan janji manajemen untuk memasang peredam suara. Namun janji itu tidak ditepati karena pihak lapangan justru hanya sebatas mengganti penutup jaring-jaring menjadi polycarbonat. "Itu sela-selanya masih besar, suara bising masih kedengaran," ujar Idham.

Berdasarkan pengamatan Tempo di lokasi, jarak antara lapangan padel dengan bangunan rumah bahkan tidak mencapai satu meter. "Dari yang aku pahami, ini tidak sesuai (aturan) jarak bebas bangunan," kata Idham.

Perwakilan dari PT Kreasi Arena Indonesia selaku pemilik Fourthwall Padel, Fajar Ediputra, mengatakan pihaknya berjanji akan membatasi jam buka serta memasang peredam suara. "Kami akan memperkuat dinding, supaya suara dari lapangan padel itu bisa teredam di dalam sehingga tak ganggu yang di luar," kata Fajar seperti dilansir dari Antara.

Fajar menjelaskan pemasangan peredam suara direncanakan akan dikebut dalam jangka waktu sebulan ke depan. Jam operasional selama puasa juga akan dibatasi mulai jam 14.00 hingga 19.00 WIB untuk menghindari protes lanjutan.

Meski begitu, Fajar berkukuh pihaknya tidak melanggar aturan apapun selama beroperasi. "Kalau mengikuti aturan sebenarnya, di lapangan kami masih 70 desibel. Cuman ini yang menjadi permasalahan adalah zonasi yakni berdampingan langsung dengan rumah tinggal," ucapnya.
"""