# Desain Pemrograman Berorientasi Objek

## Praktikum 
> Muhammad Azar Nuzy 
> 2004191
> Ilmu Komputer - C1
> Universitas Pendidikan Indonesia

Repositori ini dibuat sebagai latihan dari mata kuliah Desain Pemprograman Berorientasi Objek di UPI pada semester 4. Di dalamnya terdapat implementasi kelas dalam bahasa **Python**.

### Project Description
Terdapat 6 kelas pada project kali ini yaitu kelas Vehicle, Ship, Airplane, Person, Job, dan Driver.
- Ship dan Airplane merupakan anak dari kelas Vehicle. Ship dan Airplane termasuk ke dalam Vehicle maka dari itu keduanya merupakan anak dari Vehicle. Dan hubungan antar Ship, Airplane, dan Vehicle adalah Hierarchical Inheritance. Ship dan Airplane sebagai child dan Vehicle sebagai parent.
- Atribut age masuk ke dalam bagian vehicle karena atribut tersebut menunjukan umur dari kendaraan dan berlaku untuk anak-anak dari kelas vehicle
- Hubungan kelas Person, Job, dan Driver adalah Multiple Inheritance. Person dan Job sebagai parent dan Driver sebagai child. Person dijadikan sebagai parent karena Driver sendiri merupakan seorang manusia dan Job dijadikan sebagai parent karena Driver sendiri merupakan bagian dari sebuah pekerjaan. 
Berikut merupakan diagram dari kelas tersebut:
<img src="https://github.com/azarnuzy/LATIHAN4DPBO2022/blob/master/diagramClasspng.png" style="height:500px;" align="center">  


Materi latihan dari kode di repositori ini dapat di temukan di file  [Modul 4 - Multiple _ Hierarchical Inheritance](https://github.com/azarnuzy/LATIHAN4DPBO2022.git)

### Tools
- [Python](https://www.python.org/) : Python
- Text Editor

### Usage

Untuk menjalankan kode repository di atas dapat dijalankan di terminal pada komputer. Path pada terminal ditujukan ke arah folder yang ingin dijalankan:

#### Python
```
py [name].py
```

### Result
- Input
<img src="https://github.com/azarnuzy/LATIHAN4DPBO2022/blob/master/Screenshot/inputShip.jpg" align="left"> 
 <img src="https://github.com/azarnuzy/LATIHAN4DPBO2022/blob/master/Screenshot/inputAirplane.jpg" align="left"> 
 <img src="https://github.com/azarnuzy/LATIHAN4DPBO2022/blob/master/Screenshot/inputDriver.jpg" align="left"> 

- Output
<img src="https://github.com/azarnuzy/LATIHAN4DPBO2022/blob/master/Screenshot/outputShip.jpg" align="left"> 
<img src="https://github.com/azarnuzy/LATIHAN4DPBO2022/blob/master/Screenshot/outputAirplane.jpg" align="left"> 
<img src="https://github.com/azarnuzy/LATIHAN4DPBO2022/blob/master/Screenshot/outputDriver.jpg" align="left"> 
