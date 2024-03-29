TUGAS 6

    A. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

        Pada synchronous programming, operasi atau perintah dieksekusi secara berurutan, dimana kode berikutnya hanya akan dijalankan setelah kode sebelumnya selesai dieksekusi. Sehingga, hal tersebut dapat mengakibatkan perlambatan dalam aplikasi, terutama jika ada operasi yang memerlukan waktu lama untuk selesai.

        Sedangkan pada synchronous programming, operasi dapat mulai dan dibiarkan berjalan di latar belakang sementara kode lain tetap berjalan. Ketika operasi asinkron selesai, program akan menerima pemberitahuan dan dapat melanjutkan operasi tersebut, sehingga berguna untuk berbagai task yang tidak memerlukan pemblokiran eksekusi program, seperti permintaan jaringan.

    B. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
    
        Paradigma Event-Driven Programming adalah pendekatan dalam pemrograman dimana aplikasi merespons suatu peristiwa seperti tindakan pengguna, contohnya mengklik mouse atau menekan keyboard, dan lain-lain. Aplikasi yang menggunakan paradigma ini merespons peristiwa secara asinkron yaitu dengan menunggu dan merespons peristiwa ketika terjadi tanpa harus menjalankan baris kode secara berurutan. Dalam konteks JavaScript dan AJAX, penerapannya memungkinkan pembuatan halaman web yang interaktif yang merespons tindakan pengguna, seperti mengklik tombol, sehingga memungkinkan pengembangan antarmuka pengguna yang responsif tanpa memerlukan pembaruan halaman.

    C. Jelaskan penerapan asynchronous programming pada AJAX.
    
        AJAX (Asynchronous JavaScript And XML) menerapkan pemrograman asinkron. Ketika kita mengirim permintaan AJAX, tidak perlu menunggu suatu respons sehingga kode lain dapat tetap berjalan. Ketika respons diterima, sebuah fungsi callback dipanggil. Sehingga hal tersebut memungkinkan halaman web untuk mengirim permintaan ke server, menerima data baru, dan memperbarui tampilan tanpa harus me-reload keseluruhan halaman.

    D. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

        1. Kompleksitas:

            Fetch API: Lebih rinci dan memerlukan pemahaman tentang Promise, namun memberikan kontrol yang lebih besar.
            jQuery: Lebih sederhana dan menyederhanakan banyak detail dalam library.

        2. Ukuran:
            Fetch API: Lebih ringan dan berukuran lebih kecil sehingga cocok untuk kinerja tinggi.
            jQuery: Lebih besar dan dapat memperbesar ukuran halaman web sehingga perlu diperhatikan dalam efisiensi pemuatan halaman.
            
        3. Fleksibilitas:
            Fetch API: Lebih fleksibel, mendukung teknologi terbaru, dan memungkinkan pengembangan aplikasi kompleks.
            jQuery: Cocok untuk pengembangan web sederhana tanpa perlu mendalam dalam detail teknis, meskipun bisa kurang sesuai untuk kasus kompleks.

    E. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
        1. Pertama-tama, saya review kembali yang sudah diajarkan dalam tutorial 5 kemarin.
        2. Saya menambahkan fungsi-fungsi baru pada views.py untuk dapat mengambil dan menambahkan item dengan AJAX.
        3. Lalu, saya edit file main dengan menambahkan file-file javascript untuk mendukung implementasi AJAX tersebut.
        4. Lalu, saya mengedit fungsi refreshProducts agar mengupdate tipe cards sesuai dengan apa yang sudah saya buat sebelumnya.
        5. Setelah itu, saya juga membuat fungsi-fungsi baru untuk menambahkan, mengurangi, dan juga delete item menggunakan AJAX juga.
        6. Saya juga menambahkan 1 variabel product baru bernama genre agar lebih lengkap.
        7. Karena itu, saya menambahkan suatu dropdown menu untuk setiap card untuk melihat description dan juga genre dari game yang sudah ditambah.
        8. Saya juga mengupdate counter dari game agar menggunakan AJAX juga dan tidak perlu menunggu refresh dari web.
        9. Terakhir, saya menambahkan file-file yang diperlukan agar web dapat di deploy.


TUGAS 5

A. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

    1. Universal Selector (*)
    Digunakan jika ingin mengedit semua elemen dalam dokumen HTML.
    Contoh:
    * {
        font-family: montserrat;
    }

    2. Element Selector
    Digunakan jika ingin mengedit semua elemen dengan tipe tertentu seperti <p>, <h1>, <div>, dan lain-lain.
    p {
    color: white;
    }

    3. Class Selector
    Digunakan jika ingin mengedit elemen berdasarkan atribut class yang sama.
    .button {
    border-radius: 4px;
    }

    4. ID Selector
    Digunakan jika ingin mengedit elemen berdasarkan atribut id yang unik pada suatu laman.
    #header {
    background-color: black;
    }

    5. Pseudo-class Selector 
    Digunakan jika ingin mengedit elemen berdasarkan perilaku khusus seperti hover untuk mengarahkan kursor ke atas suatu elemen.
    .button:hover {
    background-color: blue;
    }

B. Jelaskan HTML5 Tag yang kamu ketahui.

    <header>: Bagian atas halaman web.
    <main>: Konten utama dalam halaman web.
    <footer>: Bagian bawah halaman web.
    <form>: Membuat formulir interaktif.
    <input>: Komponen dalam form untuk menginput data.
    <button>: Tombol yang dapat tekan oleh user.
    <title>: Menentukan judul halaman web yang akan ditampilkan di tab browser.
    <div>: Membuat wadah yang mengelompokkan dan mengatur konten dalam halaman web.
    <a>: Digunakan untuk membuat link ke halaman web atau sumber lainnya.
    <img>: Untuk menyisipkan gambar atau grafik ke dalam halaman web.
    <ul>: Membuat daftar tak terurut (unordered list).
    <ol>: Membuat daftar terurut (ordered list).
    <li>: Mengidentifikasi elemen dalam daftar (list item).
    <p>: Membuat paragraf teks.
    <h1> hingga <h6>: Menentukan tingkat judul dengan h1 sebagai judul utama dan h6 sebagai judul terkecil.
    <table>: Membuat tabel data.
    <tr>: Membuat baris dalam tabel.
    <td>: Membuat sel dalam tabel.
    <textarea>: Area teks untuk user memasukkan teks panjang.
    <label>: Label yang terkait elemen dalam formulir.
    <span>: Digunakan untuk menerapkan gaya pada teks atau elemen dalam baris teks.
    <strong> dan <em>: Menggunakan huruf bold dan italic untuk memberikan penekanan.
    <hr>: Menambahkan garis horizontal sebagai pemisah.
    <br>: Membuat jeda baris dalam teks.
    <b>: Mengubah teks menjadi bold.
    <i>: Mengubah teks menjadi italic.


C. Jelaskan perbedaan antara margin dan padding.
    
    Margin merupakan ruang kosong yang berada di luar batas elemen dalam desain halaman web. Margin digunakan untuk mengatur jarak antar elemen atau dengan elemen di luarnya. Ini memungkinkan untuk mengubah spasi di sekitar elemen seperti memberikan jarak antara dua blok teks atau memusatkan elemen di tengah halaman. Properti margin dapat memiliki nilai positif untuk menambahkan jarak atau negatif untuk mengurangi jarak dan tidak memiliki latar belakang atau warna.

    Sedangkan, padding merupakan ruang kosong yang berada di antara batas dalam elemen dan kontennya. Padding digunakan untuk mengatur jarak antara tepi elemen dan konten atau isi elemen tersebut, sehingga memengaruhi tampilan konten dalam elemen seperti memberikan ruang tambahan di sekitar teks atau gambar di dalam elemen. Padding memiliki latar belakang dan dapat memiliki warna atau gambar sebagai latar belakang konten, dan hanya memiliki nilai positif. Ketika digunakan bersama dengan margin, padding memungkinkan desain web untuk lebih dikendalikan tata letak dan tampilan elemennya secara lebih detail.

D. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

    Tailwind CSS merupakan framework CSS yang memiliki pendekatan "utility-first". Dalam Tailwind, user dapat membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya dalam CSS. Hal terseabut memberikan fleksibilitas dan memungkinkan kontrol detail dari tampilan yang sangat rinci sehingga membuat Tailwind cocok untuk proyek yang memerlukan tampilan yang sangat kustom. Tailwind juga dapat menghasilkan CSS yang lebih ringan karena hanya mengeluarkan gaya yang digunakan dalam proyek user sehingga dapat mengoptimalkan kinerja halaman web.

    Sedangkan, Bootstrap adalah framework CSS dengan komponen-komponen desain yang siap pakai atau "preset", sehingga memungkinkan user untuk membangun tampilan dengan cepat menggunakan komponen-komponen seperti tombol, form, dan navigasi yang telah disiapkan sebelumnya dari template Bootstrap. Bootstrap lebih cocok untuk pengembangan cepat atau prototyping sehingga memungkinkan user untuk membuat tampilan dengan sedikit usaha desain. Namun karena Bootstrap memiliki styling bawaan/template yang kuat, Bootstrap bisa menjadi kurang fleksibel untuk merancang tampilan yang sangat kustom.

    Pilihan antara Tailwind CSS dan Bootstrap tergantung pada kebutuhan. Jika yang dperlukan adalah fleksibilitas tinggi dan kontrol atas tampilan, user dapat menggunakan Tailwind. Sebaliknya, jika yang diperlukan adalah membangun tampilan dengan cepat dan memanfaatkan komponen-komponen siap pakai, maka user dapat menggunakan Bootstrap untuk mempercepat proses pembuatan proyek.

E. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Pertama-tama, saya mereview kembali apa yang saya pelajari dari tutorial-tutorial sebelumnya.
    2. Lalu setelah selesai tutorial kemarin saya langsung mencoba untuk mengimplementasikan Bootstrap dalam aplikasi web saya namun ternyata banyak yang overlap dengan styling CSS yang sudah saya buat, sehingga perlu saya sesuaikan lagi.
    3. Sebelum menyesuaikan styling, saya membuat halaman edit product untuk dapat mengedit product-product yang sudah diinput oleh user.
    4. Kemudian, saya mulai mengedit satu-satu halaman yang terefek oleh Bootstrap agar lebih sesuai dengan desain yang ingin saya implementasikan.
    5. Saya menggunakan campuran Bootstrap dan CSS, dengan adanya desain base yang lebih rapi dari Bootstrap dan juga elemen-elemen khusus yang sudah saya buat dari CSS seperti buttons lain lain-lain.
    6. Namun karena sizing agak berbeda di Bootstrap, segala macam padding dan margin perlu saya sesuaikan lagi juga dengan mengedit atribut class template Bootstrap.
    7. Saya juga memastikan agar template Bootstrap tidak melebihi style custom CSS yang sudah saya buat dengan mengedit base.html.
    8. Kemudian saya mengedit tampilan main.html agar menggunakan card untuk setiap product sehingga tampilan lebih rapi dan menambahkan footer dibawah yang dapat mengedit product-product yang sudah dibuat.
    9. Terakhir, saya juga mengedit register page agar tidak terlalu mengikuti template UserCreationForm agar lebih rapi juga, namun beberapa validasi masih salah sehingga perlu ditinjau kembali lagi.

TUGAS 4

 A. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

    Django UserCreationForm adalah suatu fungsi forms bawaan/package yang tersedia dari Django yang dapat memfasilitasi programmer untuk membuat login dan register page yang mudah untuk digunakan oleh user, agar proses autentikasi dapat berjalan dengan mudah. Beberapa kelebihan dari UserCreationForm adalah terdapat validasi yang sudah termasuk dalam package tersebut sehingga dapat mengurangi potensi kurangnya keamanan, dan juga relatif mudah digunakan karena banyak logika dan validasi sudah diimplementasikan sehingga pembuat web tinggal menggunakannya dalam program Django yang dibuat. Namun, beberapa kelemahan yang mungkin dimiliki adalah template dan tampilan yang cukup standar dan simpel sehingga perlu banyak kustomisasi desain oleh pembuat web, dan juga perlu mengimplementasi sendiri jika ingin menambahkan fungsi-fungsi lain yang tidak dicakup oleh UserCreationForm.

 B. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

    Autentikasi adalah dimana sistem memverifikasi atau mengenali seorang user yang sedang melakukan aksi login. Pentingnya autentikasi adalah untuk memastikan bahwa hanya user yang sudah login dan berada dalam database yang dapat mengakses suatu sistem. Sedangkan, otorisasi adalah suatu proses dimana seorang user perlu mengakses sesuatu dengan melihat apa saja yang dapat diakses dan seberapa luas akses seorang user tersebut. Otorisasi penting untuk menjaga privasi dan keamanan data, serta untuk mengontrol tindakan yang dapat diambil oleh user.

 C. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

    Cookies merupakan data/informasi kecil yang dikirim oleh server web ke browser dan kemudian dikirim kembali oleh browser pada permintaan halaman. Cookies digunakan dalam proses autentikasi, pelacakan pengguna, dan menjaga preferensi pengguna. Data dalam cookie terdiri dari satu pasangan nama/nilai yang dikirim dalam header permintaan HTTP GET atau POST dari klien. Django menggunakannya untuk mengelola data sesi pengguna dengan menyimpan informasi seperti ID sesi atau token autentikasi dalam suatu cookie, sehingga memungkinkan Django untuk mengidentifikasi permintaan berikutnya dari pengguna dan menjaga keadaan dari suatu session seperti status login dan preferensi.

 D. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

    Sebenarnya, cookies adalah berkas data kecil yang aman secara default, dimana cookies tidak dapat menghapus data atau membaca informasi dari komputer user dan juga tidak berfungsi sebagai pengintai atau "spyware". Pada umumnya, cookies biasanya bersifat anonim dan hanya menyimpan data dan bukan kode program. Namun, tetap penting untuk user dalam menghindari penyimpanan data pribadi dalam cookies untuk menjaga privasi user sendiri.

 E. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
 
    1. Pertama-tama, saya mereview kembali apa yang sudah saya pelajari dan latih dari tutorial 3 mengenai autentikasi dan aka mengimplementasikannya ke aplikasi web saya.
    2. Lalu saya mengaktifkan environment and mulai membuat proses autentikasi pada program web saya.
    3. Pada awalnya, saya menambahkan webpage baru bernama login yang akan menerima nama dan password beserta button untuk melakukan fungsi login pada seorang user dengan akun dan button lain yang me-register akun baru jika belum dibuat, sekaligus saya juga merestriksi akses ke laman main jika user belum login menggunakan akun yang tersedia.
    4. Setelah itu, saya juga membuat fungsi logout dan mengimplementasikannya ke laman main agar dapat keluar dari akun tersebut dan kembali ke login page dengan suatu button.
    5. Kemudian, saya juga membuat agar data cookies juga dapat ditrack setiap kali dilakukan request seperti login dan logout, beserta menambahkan informasi waktu terakhir kali login.
    6. Lalu dengan adanya laman register dan perlunya akun untuk autentikasi untuk bisa masuk ke laman main, saya juga menambahkan fungsi agar konten dari setiap user berbeda-beda seperti halnya akun-akun, dimana masing-masing user hanya dapat melihat dan mengakses item-item yang sudah dibuat oleh user tersebut.
    7. Setelah saya membuat proses autentikasi yang lengkap dengan register, logout, dan login, saya lanjut mengedit laman main saya. Saya membuat 3 button baru dalam kolom yang baru pada tabel konten, yaitu untuk menambahkan & mengurangi jumlah item, serta untuk menghapus satu kategori item. Hal tersebut tentu akan sangat membantu kustomisasi nantinya agar user juga mudah dalam mengedit data juga.
    8. Terakhir, saya juga mengedit semua laman yang sudah saya buat agar lebih sesuai dengan estetik desain yang saya inginkan. Karena belum terlalu diajarkan dan banyak lupa materi pembelajaran pada SMA, saya banyak mengandalkan Internet sebagai referensi apa saja setting dan efek yang dapat digunakan untuk melakukan suatu desain tertentu dan juga menggunakan ChatGPT agar mencari setting yang lebih sesuai sehingga saya dapat mendesain sesuai konsep yang saya mau sendiri.

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
