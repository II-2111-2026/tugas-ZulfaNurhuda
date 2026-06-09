"""
[JAWABAN ASSIGNMENT WEEK 11]

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di assignments/w11/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F     -> bool  (True=Benar, False=Salah)
- MC      -> str   ("A"/"B"/"C"/"D")
- Numeric -> int/float (desimal pakai '.')
"""

from __future__ import annotations

def q01() -> bool:
    """
    [T/F] Semakin tinggi tingkat kepercayaan yang diinginkan, semakin lebar interval kepercayaan yang dihasilkan.
    """
    return True

def q02() -> bool:
    """
    [T/F] Interval kepercayaan 95% berarti ada peluang 95% bahwa parameter populasi berada dalam rentang tersebut untuk satu interval yang sudah dihitung.
    """
    return False

def q03() -> bool:
    """
    [T/F] Distribusi t-Student mendekati distribusi Normal saat derajat kebebasan (df) menjadi sangat besar.
    """
    return True

def q04() -> str:
    """
    [MC] Jika kita ingin mempersempit interval kepercayaan tanpa mengubah tingkat kepercayaan, kita harus:
     A) Mengurangi ukuran sampel.
     B) Meningkatkan ukuran sampel.
     C) Meningkatkan simpangan baku.
     D) Tidak melakukan apa-apa.
    """
    return "B"

def q05() -> str:
    """
    [MC] Nilai kritis Z untuk tingkat kepercayaan 95% adalah:
     A) 1,645
     B) 1,96
     C) 2,58
     D) 1,00
    """
    return "B"

def q06() -> str:
    """
    [MC] Derajat kebebasan (df) untuk interval kepercayaan rata-rata satu sampel berukuran n adalah:
     A) n
     B) n+1
     C) n-1
     D) n/2
    """
    return "C"

def q07() -> str:
    """
    [MC] Estimasi titik terbaik untuk rata-rata populasi adalah:
     A) Median sampel.
     B) Modus sampel.
     C) Rata-rata sampel (X-bar).
     D) Standar deviasi sampel.
    """
    return "C"

def q08() -> float:
    """
    [Numeric] Jika X-bar = 100, Margin Error = 5, berapakah batas bawah interval kepercayaan?
    """
    return 95.0

def q09() -> float:
    """
    [Numeric] Untuk sampel n = 16 dan simpangan baku sampel s = 4, berapakah nilai estimasi Standard Error-nya?
    """
    return 1.0

def q10() -> float:
    """
    [Numeric] Berapakah derajat kebebasan jika ukuran sampel adalah 25?
    """
    return 24.0

def q11() -> float:
    """
    [Numeric] Jika interval kepercayaan adalah [45, 55], berapakah nilai estimasi titik rata-ratanya?
    """
    return 50.0

def q12() -> float:
    """
    [Numeric] Jika margin error adalah 2 dan nilai kritis Z = 2, berapakah Standard Error-nya?
    """
    return 1.0
