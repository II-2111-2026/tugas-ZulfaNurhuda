"""
[JAWABAN ASSIGNMENT WEEK 13]

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di assignments/w13/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F     -> bool  (True=Benar, False=Salah)
- MC      -> str   ("A"/"B"/"C"/"D")
- Numeric -> int/float (desimal pakai '.')
"""

from __future__ import annotations

def q01() -> bool:
    """
    [T/F] Garis regresi meminimalkan jumlah total selisih absolut antara data dan garis.
    """
    return False

def q02() -> bool:
    """
    [T/F] Nilai R^2 sebesar 0,85 berarti 85% variasi pada variabel dependen dapat dijelaskan oleh variabel independen.
    """
    return True

def q03() -> bool:
    """
    [T/F] Regresi linear berganda menggunakan lebih dari satu variabel independen untuk memprediksi satu variabel dependen.
    """
    return True

def q04() -> str:
    """
    [MC] Dalam persamaan Y = a + bX, b merepresentasikan:
     A) Intersep.
     B) Kemiringan (slope).
     C) Varians.
     D) Galat.
    """
    return "B"

def q05() -> str:
    """
    [MC] Jika korelasi r = -0,9, maka hubungan antara kedua variabel adalah:
     A) Sangat lemah.
     B) Sangat kuat dan negatif.
     C) Tidak ada hubungan.
     D) Positif.
    """
    return "B"

def q06() -> str:
    """
    [MC] Manakah nilai R^2 yang menunjukkan model paling buruk?
     A) 0,99
     B) 0,50
     C) 0,00
     D) -1,00
    """
    return "C"

def q07() -> str:
    """
    [MC] Titik di mana garis regresi memotong sumbu Y disebut:
     A) Slope.
     B) Intersep.
     C) Origin.
     D) Outlier.
    """
    return "B"

def q08() -> float:
    """
    [Numeric] Jika persamaan regresi adalah Y = 5 + 2X, berapakah nilai prediksi Y untuk X = 10?
    """
    return 25.0

def q09() -> float:
    """
    [Numeric] Jika R^2 = 0,64, berapakah nilai korelasi r (ambil nilai positif)?
    """
    return 0.8

def q10() -> float:
    """
    [Numeric] Berapakah nilai rata-rata dari residual pada model regresi linear klasik?
    """
    return 0.0

def q11() -> float:
    """
    [Numeric] Jika Y naik 10 unit ketika X naik 2 unit, berapakah nilai slope b?
    """
    return 5.0

def q12() -> float:
    """
    [Numeric] Jika Sxy = 40 dan Sxx = 10, berapakah nilai estimasi slope b?
    """
    return 4.0
