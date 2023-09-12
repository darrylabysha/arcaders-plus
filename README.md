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
