TUGAS 3

A. Apa perbedaan antara form POST dan form GET dalam Django?

    - Pengiriman Data:
    POST: Data dikirim dalam HTTP dan tidak terlihat pada URL.
    GET: Data disertakan dalam URL.

    - Kemampuan Data:
    POST: Cocok untuk data besar atau sensitif.
    GET: Cocok untuk mengambil data dari suatu server.

    - Keamanan:
    POST: Lebih aman karena data tidak terlihat di URL.
    GET: Data terlihat di URL sehingga kurang aman jika melibatkan data sensitif.

B. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

    1. XML:
    - Struktur: Bahasa markup dengan dokumen hierarki berbasis tag.
    - Tujuan Utama: Pertukaran data antara sistem yang berbeda.
    - Kelebihan: Dapat digunakan untuk struktur data yang kompleks.
    - Kekurangan: Struktur lebih rumit sehingga dokumen biasanya lebih besar.
    
    2. JSON:
    - Struktur: Format pertukaran data ringan dengan struktur yang serupa dengan objek JavaScript.
    - Tujuan Utama: Pertukaran data dalam aplikasi web.
    - Kelebihan: Ringan, mudah dibaca dan ditulis, dan cocok untuk data semi-terstruktur.
    - Kekurangan: Terbatas dalam jenis data khusus.

    3. HTML:
    - Struktur: Bahasa markup untuk membuat halaman web.
    - Tujuan Utama: Membuat tampilan dan konten halaman web, diakses oleh browser.
    - Kelebihan: Cocok untuk pembuatan antarmuka pengguna web.
    - Kekurangan: Kurang cocok untuk pertukaran atau penyimpanan data terstruktur karena lebih fokus pada tampilan dan presentasi.

C. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

    JSON sering digunakan dalam komunikasi data antara aplikasi web modern karena beberapa alasan yang mendasar. Pertama-tama, JSON memiliki format yang ringan dan responsif sehingga lebih efisien dalam respons permintaan data. Selain itu, JSON juga mudah dibaca dan dimengerti oleh manusia dan mesin. Lalu, JSON mendukung kemampuan untuk menyimpan data dalam bentuk array, yang mempermudah dalam proses transfer data. JSON juga efektif dalam menangani API baik untuk aplikasi web dan mobile. Terakhir, JSON bersifat independen dari bahasa pemrograman tertentu sehingga dapat digunakan dengan mudah dalam berbagai jenis aplikasi tanpa menghadapi masalah kompatibilitas.

D. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step 

    1. Pertama-tama, saya mereview kembali apa yang sudah saya pelajari dari tutorial 2 kemarin mengenai form dan data delivery dan akan mencoba mengimplementasikannya ke aplikasi web yang saya susun.
    2. Lalu, saya menyalakan environment dan melakukan routing dari main/ ke / pada localhost.
    3. Setelah itu, saya membuat file html bernama base.html yang akan digunakan sebagai base dari template html yang diextend juga oleh output-output lainnya seperti main dan juga create_product nanti. Saya juga mengubah settings dan juga layout pada main.html agar sesuai dengan penggunaan base juga. Untuk sementara ini, semua style CSS juga saya simpan disini agar dapat digunakan oleh kedua subclass.
    4. Kemudian, saya mulai membuat form untuk input data dengan membuat file forms.py. Saya menggunakan attribute name, amount, dan description sesuai dengan apa yang sudah saya bentuk minggu lalu. Selain itu saya juga membuat file html yang bernama create-product yang nantinya akan menerima input dari user untuk membuat product baru, atau lebih tepatnya game baru di project saya. Saya juga menyesuaikan file views, urls, dan juga main untuk bisa melakukan input data menggunakan forms.
    5. Lalu, saya membuat konfigurasi agar data yang sudah diinput pada form bisa diakses dengan XML, XML by ID, JSON, dan juga JSON by ID dengan membuat method-method yang mengembalikan HttpResponse. Dengan ini, semua data yang telah diinput juga dapat terlihat dengan jelas menggunakan web ataupun juga Postman.
    6. Setelah itu saya membuat link-link yang dapat mengakses input dapat melalui HTML, XML, XML by ID, JSON, dan juga JSON by ID lalu mencoba membukanya di Postman dan ternyata bisa.
    7. Lalu, saya menambahkan fungsi pada menu untuk menghitung berapa items yang berada pada stock products.
    7. Terakhir, saya mencoba mendesign juga webnya sedikit menggunakan apa yang sudah saya pelajari saat SMA namun belum terlalu bagus dan banyak yang masih perlu saya review lagi.

Berikut adalah screenshot fungsi views yang dibuat:
HTML:
![Show HTML](<Screenshot 2023-09-20 004018.png>)
JSON:
![Show JSON](<Screenshot 2023-09-20 004036.png>)
JSON by ID:
![Show JSON by ID](<Screenshot 2023-09-20 004056.png>)
XML:
![Show XML](<Screenshot 2023-09-20 004113.png>)
XML by ID:
![Show XML by ID](<Screenshot 2023-09-20 004127.png>)

TUGAS 2

Link Adaptable:
https://arcaders-plus.adaptable.app

A. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    1. Pertama-tama, saya membuat repository GitHub dengan nama arcaders-plus, yang merupakan nama ide aplikasi yang ingin saya kembangkan, yaitu Arcaders+. Konsep Arcaders+ adalah semacam aplikasi streaming game, seperti Xbox Live Game Pass, Playstation Plus, dan lain-lain.
    2. Setelah itu, saya membuat file README ini untuk menjawab pertanyaan-pertanyaan yang diberikan serta deskripsi program yang disusun.
    3. Lalu, saya set-up git pada directory dan push dahulu README untuk memastikan bahwa repo berjalan dengan benar dan sesuai.
    4. Lalu, saya start dahulu virtual environment di pada comment prompt.
    5. Kemudian, saya memasang danm meng-install dependencies yang diperlukan sesuai dengan yang ada di tutorial kemarindan juga membuat project Django dengan nama arcaders-plus.
    6. Setelah itu, saya konfigurasi project kemudian mencoba menjalankan server dan ternyata berhasil dijalankan.
    7. Setelah berhasil, saya tambahkan .gitignore dan push lagi ke GitHub.
    8. Kemudian, saya mulai mengimplementasikan MVT pada project tersebut, yang dimulai dengan membuat file html bernama main serta mengonfigurasi agar dapat menjadi aplikasi dalam project ini. 
    9. Lalu, saya konfigurasi file models.py dan views.py sesuai ketentuan, dimana file models diisi dengan attribute dan variabel yang dibutuhkan (untuk sekarang baru attribute wajib) yang nantinya akan digunakan untuk menyimpan data, sedangkan file view diisi dengan data nama, kelas, dan NPM yang akan tampil pada website.
    10. Kemudian, saya konfigurasi routing URL agar dapat diakses oleh web browser.
    11. Lalu, saya coba run dan ternyata perubahan dapat tampak di web localhost, yang kemudian saya utak-atik lagi designnya secara basic agar tampilan sedikit lebih menarik juga.
    12. Setelah itu, saya coba melakukan unit testing dan push pada repo.
    13. Terakhir, saya coba deploy di Adaptable namun karena server penuh tidak bisa dan akun saya ter-disable.

B. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Bagan MVT](<Bagan MVT Django-1.png>)

    1. Pertama-tama, routing akan terjadi sesuai dengan route yang terkonfigurasi pada urls.py.
    2. File view.py akan menampilkan tampilan yang sudah disesuaikan dengan atribut-atribut yang ada pada file models.py.
    3. Models.py menyimpan atribut-atribut yang kemudian dapat digunakan dan ditampilkan oleh views.py.
    4. Database dapat menerima ataupun menerima (read/write) data yang diminta oleh file models.py.
    5. Template akan menampilkan kepada format yang sesuai dengan yang ada pada views.py kepada user menggunakan main.html. 

C. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

    Pada aplikasi Django, virtual environment digunakan untuk beberapa alasan. Pertama, virtual environment memungkinkan proyek-proyek yang berbeda yaitu package dan dependencies untuk memiliki lingkungan yang terisolasi, sehingga menghindari konflik dalam penggunaan dependencies. Lalu, virtual environment mempermudah manajemen dependencies dengan penggunaan pip sehingga pengelolaan dan penginstalan menjadi lebih efisien. Kemudian, virtual environment membantu dalam pemeliharaan proyek, memastikan bahwa dependensi tetap konsisten seiring berjalannya waktu. Meskipun itu, aplikasi Django dapat dikembangkan tanpa menggunakan virtual environment. Namun penggunaan virtual environment lebih baik untuk jangka panjang karena adanya pengelolaan dependencies dan lain-lain.

D. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

    MVT, MVC, dan MVVM merupakan konsep-konsep arsitektur web development yang banyak digunakan oleh web developer. Dari ketiga konsep tersebut, terdapat persamaan yaitu konsep MV pada MVT, MVC, dan MVVM, dimana M adalah model yang melakukan penyimpanan data dan V yaitu view yang merupakan komponen yang akan ditampilkan pada user yang membuka web tersebut. Sehingga, terdapat beberapa perbedaan antara ketiga konsep tersebut, dimana T pada MVT adalah Template yang menentukan tampilan antarmuka pengguna. C pada MVC adalah Controller yang mengontrol alur aplikasi dan menerima input dari user. Terakhir, VM pada MVVM adalah ViewModel, yaitu komponen yang memisahkan antara "View" dan "Model", dimana VM berlaku sebagai perantara.

    Perbedaan antara ketiga konsep tersebut adalah cara mengelola antara tampilan dan logika pada sebuah aplikasi. Dalam MVC,, Controller mengendalikan alur aplikasi dan interaksi antara Model dan View. Sedangkan, komponen Template fokus pada presentasi tampilan kepada pengguna, sementara Model masih bertanggung jawab atas logika bisnis. Terakhir, MVVM menggunakan ViewModel yang memisahkan logika tampilan dari komponen View serta antara tampilan dan logika. Pemilihan klonsep arsitektur tersebut bergantung pada kebutuhan proyek, preferensi developer, dan penggunaan kerangka kerja yang sesuai. Sementara MVC sering digunakan dalam berbagai bahasa pemrograman, MVT adalah karakteristik Django, dan MVVM biasanya digunakan dalam pengembangan aplikasi berbasis JavaScript.
