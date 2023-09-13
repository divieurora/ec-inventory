# inventory-assignment-2
Adaptable Link:
https://euroras-closet.adaptable.app

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Membuat sebuah proyek Django baru
Untuk membuat sebuah proyek Django baru, pertama-tama saya membuat direktori baru yang saya beri nama "inventory". Kemudian saya juga membuat repositori baru di GitHub yang nantinya akan dikonfigurasi dengan direktori inventory.
Setelah itu, saya melakukan inisiasi (git init), konfigurasi global dengan username dan email GitHub (git config --global), menyalin alamat url repositori, dan menghubungkan direktori dengan repositori (git remote add origin)
Setelah direktori dan repositori saya terhubung, saya mengaktifkan virtual environment agar proyek Django kali ini terisolasi dan tidak terganggu oleh program luar. Kemudian, di dalam direktori saya menambahkan depedencies yang akan mendukung proyek berjalan masing-masing. Depedencies yang saya gunakan mengikuti requirements.txt yang ada pada tutorial. Setelah depedencies diinstall, proyek Django akan terbuat ketika dijalankan perintah "django-admin startproject inventory .".
Kemudian setelah proyek Django terbuat, muncul beberapa file seperti settings.py dan manage.py. Untuk keperluan deployment, ALLOWED_HOSTS pada settings.py saya isi ["*"] yang artinya mengizinkan semua host. Pada manage.py saya melakukan run server untuk melihat situasi proyek Django pada local host di peramban web. 

<!-- Ketika sudah berjalan dengan normal, saya mengunggah proyek ke repositori yang tadi sudah dihubungkan.
Namun sebelum mengunggah ke repositori, saya menambahkan berkas .gitignore seperti yang dicontohkan pada tutorial yang berguna untuk membatasi berkas lainnya agar proses unggah ke repositori tidak terganggu. Setelah itu saya melakukan git add, git commit, dan git push ke repositori GitHub. -->

- Membuat aplikasi dengan nama main pada proyek tersebut
Saya menjalankan perintah "python manage.py startapp main" di dalam direktori untuk memunculkan direktori baru bernama main dan berisi struktur awal aplikasi main. Kemudian menambahkan "main" pada settings.py di variabel INSTALLED_APPS dan secara otomatis aplikasi main sudah terdaftar di proyek inventory saya.

- Melakukan routing pada proyek agar dapat menjalankan aplikasi main
Dalam direktori inventory, ada berkas urls.py yang saya tambahkan path ke main. Dengan cara mengimpor fungsi include kemudian menambahkan "path('main/', include('main.urls'))" di variabel urlpatterns. 

- Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib: name sebagai nama item dengan tipe CharField, amount sebagai jumlah item dengan tipe IntegerField, dan description sebagai deskripsi item dengan tipe TextField
Dalam direktori inventory, ada berkas models.py yang isinya saya atur sebagai berikut:
class Item(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    description = models.TextField()
    category = models.CharField(max_length=100, null=True, blank=True)
Terlihat dalam class Item saya juga menambahkan atribut category dengan tipe CharField.
Setelah itu, saya melakukan migrasi model agar dapat diaplikasikan ke basis data dengan perintah "python manage.py makemigrations" dan "python manage.py migrate"

- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu
Saya kemudian menambahkan direktori baru bernama templates di dalam direktori main yang berisi berkas main.html yang akan menampilkan nama aplikasi, nama saya, dan kelas saya. Saya kemudian lanjut mengisi berkas tersebut dengan syntax html yang sesuai.
Setelah itu, dalam views.py di bagian function show_main dalam variabel context, saya menambahkan dictionary untuk nama aplikasi, nama saya, dan kelas saya. Kemudian mereturn function tersebut dengan "return render(request, "main.html", context)".

- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
Berbeda dengan urls.py di proyek, ada juga urls.py yang memetakan fungsi pada views.py. Saya membuat berkas urls.py baru kemudian menambahkan isinya dengan:
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

- Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet
Sebelum mendeploy, saya melakukan testing proyek Django saya terlebih dahulu dan ketika sudah OK maka saya melakukan git add, commit, dan push ke GitHub yang nantinya akan dilakukan deployment.
Dalam proses mendeploy, saya menggunakan cara dan langkah yang kurang lebih sama seperti yang dicontohkan pada tutorial, hanya saja saya merubah start command menjadi "python manage.py migrate && gunicorn inventory.wsgi".

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Bagan](inventory_assignment_2\image\Bagan Tugas 2 PBP.drawio (1).png)
Client dapat berupa web atau aplikasi yang merequest HTTP ke Django, yang akan berhubungan dengan uRLS yang sudah dipetakan ke fungsi dalam views.py yang sesuai. Kemudian, views.py dan models.py berinteraksi dalam mendefisinikan struktur data proyek Django. HTML file pada templates kemudian akan dirender dan ditampilkan kepada Client melalui HTTP.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual Environment adalah tools dari Python yang memungkinkan pengembang untuk membuat project environment yang "private" atau dalam kata lain terisolasi dari proyek-proyek lainnya. Virtual Environment sangat bermanfaat untuk digunakan,karena penggunaan Virtual Environment bisa memastikan masing-masing proyek memiliki depedencies yang sesuai dan tidak bertabrakan, masing-masing proyek dapat menggunakan versi python yang berbeda, serta dapat memastikan proyek bekerja dengan keinginan pengembang meskipun dijalankan di mesin lain.
Namun, meskipun begitu aplikasi web berbasis Django mungkin saja dibuat tanpa menggunakan Virtual Environment. Tentu saja dengan beberapa konsekuensi seperti terjadinya konflik antarproyek, kesulitan migrasi ketika proyek berpindah tangan, dan alasan keamanan proyek lainnya. Maka dari itu, penggunaan Virtual Environment pada proyek Django merupakan best practice.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

MVC adalah Model-View-Controller. MTV adalah Model-Template-View. MVVM adalah Model-View-ViewModel. Ketiganya adalah pola arsitektur dari pengembangan website atau aplikasi.
Model pada ketiganya sama-sama mempresentasikan data, berhubungan dengan database, dan akan memperbarui view yang berubah sesuai perubahan data. 
View merepresentasikan interaksi antarmuka dengan pengguna atau UI. Secara garis besar, View akan mengambil data dari model kemudian menampilkan ke pengguna serta mengirim perintah dari pengguna ke Controller. View ini terdapat pada MVC dan MVVM, namun pada MTV dianalogikan dengan Template. 
Controller berfungsi menerima input dari pengguna, memproses input, dan mengembalikan output. Controller ini terdapat pada MVC dan dianalogikan sebagai View pada MTV. 
ViewModel pada MVVM juga sama-sama menangani input dari pengguna dan mengembalikan output, secara khusus menggunakan teknik two-way data binding yang secara otomatis berubah ketika data berubah.