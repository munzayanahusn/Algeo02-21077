# Algeo02-21077

## TUGAS BESAR 2 IF2123 ALJABAR LINIER DAN GEOMETRI

GITHUB : https://github.com/munzayanahusn/Algeo02-21077.git
<br>
PROGRESS : https://docs.google.com/document/d/1MR4CVEdj-aEkqGHDWCFWQ1I6XtWMzkE628MIL3aXyZM/edit?usp=sharing
<br>
LAPORAN : https://docs.google.com/document/d/11QG1-Ifns59gBzsFQroQLCowIUrNrL_4D6BoLtERE5k/edit?usp=sharing
<br>

SPESIFIKASI : http://bit.ly/TubesAlgeo2eigen
<br>
QnA : https://bit.ly/DataTubes2AlgeoXXII
<br>
SUBMISI : https://bit.ly/SubmitTubes2Algeo
<br>

REFERENSI : <br>
OpenCV : https://bit.ly/DataTubes2AlgeoXXII <br>
EigenFace : https://jurnal.untan.ac.id/index.php/jcskommipa/article/download/9727/9500 <br>
https://www.geeksforgeeks.org/ml-face-recognition-using-eigenfaces-pca-algorithm/ <br>
Basis data wajah : https://www.kaggle.com/datasets/hereisburak/pins-face-recognition <br>
README : https://github.com/ritaly/README-cheatsheet <br>

# EIGENFACE FACE RECOGNITION

Tugas Besar IF2123 Aljabar Linier dan Geometri

## Daftar Isi

- [Penjelasan Ringkas Program](#penjelasan-ringkas-program)
- [Kebutuhan Kompilasi](#kebutuhan-kompilasi)
- [Cara Menjalankan Program](#cara-menjalankan-program)
- [Pembagian Tugas](#pembagian-tugas)
- [Status Pengerjaan](#status-pengerjaan)
- [Screenshot program](#screenshot-program)
- [Struktur Program](#struktur-program)

## Penjelasan Ringkas Program

Eigenface Face Recognition adalah program pengenalan wajah dengan metode eigenface yang memanfaatkan eigen value, eigen vector, eigenface, sehingga dapat ditentukan euclidean distance terkecil untuk menentukan citra wajah yang paling mirip dengan test face. Program Face Recognition ini berbasis GUI(Graphical User Interface) yang diimplementasikan dalam bahasa pemrograman Python.

## Kebutuhan Kompilasi

1. Library PIL
    `pip install PIL`
2. Library tkinter
    `pip install tk`
3. Library customtkinter
    `pip3 install customtkinter`
4. Library SciPy
    `python -m pip install scipy`
5. Library numpy
    `pip install numpy`
6. Library time
    `pip install python-time`


## Cara Menjalankan Program

1. Pastikan sudah melakukan kompilasi pada program
2. Jalankan program GUI.py pada ../src
3. Jika berhasil dilakukan kompilasi akan muncul pop-up GUI
4. Masukkan folder dataset dan test image pada button tertera
5. Tekan START
6. Tunggu hinga gambar hasil pencarian muncul

## Pembagian Tugas

| PIC                             | JOBDESC                                                                          |
| ------------------------------- | -------------------------------------------------------------------------------- |
| 13521077 Husnia Munzayana       | Ekstraksi gambar<br>Pemrosesan training image<br>Laporan Bab 1, 2, 3, 5          |
| 13521084 Austin Gabriel Pardosi | GUI<br> Laporan Bab 3                                                            |
| 13521088 Puti Nabilla Aidira    | Pemrosesan training image<br>Proses pengenalan test image<br> Laporan Bab 3, 4   |

## Status Pengerjaan

- Seluruh fitur selesai dikerjakan.

## Screenshot Program

![Face Recognition Eigenface Program](./program.jpg)

## Struktur Program

```bash
└───Algeo02-21077
    ├───src
    │   ├───GUI/test_images
    │   ├───GUI.py
    │   ├───imageExt.py
    │   └───eigenFace.py
    ├───test
    │   ├───dataset
    │   ├───res.png
    │   └───queryface.jpg
    └───README.md
```
