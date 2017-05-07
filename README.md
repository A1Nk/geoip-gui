# geoip-gui

Tool untuk melacak alamat IP atau website, dengan mode GUI penggunaanya pun sangat mudah.


Note:
karena menggunakan bahasa python di wajibkan menginstall python terlebih dahulu.

$ apt-get install python 


Eksekusi:
$ git clone https://github.com/A1Nk/geoip-gui.git
$ cd geoip-gui


untuk modulesnya bisa kalian download disni (file downloadnya wajib didalam direktori "geoip-gui"):
$ git clone https://github.com/simplegeo/pygeoip.git
$ cd pygeoip
$ chmod +x setup.py
$ python setup.py build
$ python setup.py install


setelah selesai mengisntall modulesnya, kembali ke direktori "geoip-gui"
$ cd ..
$ ls
geoip.py    GeoLiteCity.dat     pygeoip

$ python geoip.py


Selesai..
Semoga bermanfaat.
