"""
[JAWABAN ASSIGNMENT WEEK 12]

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di assignments/w12/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F     -> bool  (True=Benar, False=Salah)
- MC      -> str   ("A"/"B"/"C"/"D")
- Numeric -> int/float (desimal pakai '.')
"""

from __future__ import annotations

def q01() -> bool:
    """
    [T/F] Jika p-value lebih kecil dari tingkat signifikansi alpha, maka kita gagal menolak hipotesis nol.
    """
    raise NotImplementedError

def q02() -> bool:
    """
    [T/F] Galat Tipe I adalah kesalahan menolak H0 padahal H0 benar.
    """
    raise NotImplementedError

def q03() -> bool:
    """
    [T/F] Meningkatkan ukuran sampel biasanya akan meningkatkan kekuatan uji (power).
    """
    raise NotImplementedError

def q04() -> str:
    """
    [MC] Nilai probabilitas yang menunjukkan kekuatan bukti melawan hipotesis nol disebut:
     A) Tingkat kepercayaan.
     B) p-value.
     C) Statistik uji.
     D) Parameter.
    """
    raise NotImplementedError

def q05() -> str:
    """
    [MC] Jika kita menguji H0: mu = 50 vs H1: mu != 50, maka kita melakukan uji:
     A) Satu arah (kanan).
     B) Satu arah (kiri).
     C) Dua arah.
     D) Tanpa arah.
    """
    raise NotImplementedError

def q06() -> str:
    """
    [MC] Kondisi di mana kita menolak hipotesis nol padahal sebenarnya salah disebut:
     A) Keputusan yang benar (Power).
     B) Galat Tipe I.
     C) Galat Tipe II.
     D) Signifikansi.
    """
    raise NotImplementedError

def q07() -> str:
    """
    [MC] Tingkat signifikansi alpha yang umum digunakan dalam penelitian adalah:
     A) 0,5
     B) 0,05
     C) 0,95
     D) 1,0
    """
    raise NotImplementedError

def q08() -> float:
    """
    [Numeric] Jika statistik uji Z = 2,58 dan nilai kritis Zc = 1,96 untuk uji dua arah, apakah H0 ditolak? (Tulis 1 untuk Ya, 0 untuk Tidak)
    """
    raise NotImplementedError

def q09() -> float:
    """
    [Numeric] Berapakah nilai alpha jika tingkat kepercayaan adalah 99%?
    """
    raise NotImplementedError

def q10() -> float:
    """
    [Numeric] Dalam uji t dengan sampel n = 10, berapakah derajat kebebasannya?
    """
    raise NotImplementedError

def q11() -> float:
    """
    [Numeric] Jika p-value = 0,02 dan alpha = 0,05, apakah kita menolak H0? (Tulis 1 untuk Ya, 0 untuk Tidak)
    """
    raise NotImplementedError

def q12() -> float:
    """
    [Numeric] Jika statistik Z = 0, berapakah p-value untuk uji dua arah?
    """
    raise NotImplementedError
