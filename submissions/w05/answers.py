"""
[JAWABAN ASSIGNMENT WEEK 05]

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di assignments/w05/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F     -> bool  (True=Benar, False=Salah)
- MC      -> str   ("A"/"B"/"C"/"D")
- Numeric -> int/float (desimal pakai '.')
"""

from __future__ import annotations

def q01() -> bool:
    """
    [T/F] Nilai harapan dari sebuah variabel acak harus merupakan salah satu nilai yang mungkin muncul dari variabel tersebut.
    """
    return False

def q02() -> bool:
    """
    [T/F] Variansi dari sebuah variabel acak tidak pernah bernilai negatif.
    """
    return True

def q03() -> bool:
    """
    [T/F] Jika X adalah konstanta c, maka E[X] = c dan Var(X) = 0.
    """
    return True

def q04() -> str:
    """
    [MC] Jika E[X] = 5, maka E[2X+3] adalah:
     A) 10
     B) 13
     C) 8
     D) 5
    """
    return "B"

def q05() -> str:
    """
    [MC] Variansi dari variabel acak X didefinisikan sebagai:
     A) E[X2] - (E[X])2
     B) E[X] - E[X2]
     C) E[X]
     D) E[X]2
    """
    return "A"

def q06() -> str:
    """
    [MC] Fungsi yang memberikan probabilitas P(X = x) disebut:
     A) PMF.
     B) PDF.
     C) CDF.
     D) MGF.
    """
    return "C"

def q07() -> str:
    """
    [MC] Simpangan baku (sigma) adalah:
     A) Akar kuadrat dari variansi.
     B) Kuadrat dari mean.
     C) Selisih antara nilai maksimum dan minimum.
     D) Nilai harapan dari X.
    """
    return "A"

def q08() -> float:
    """
    [Numeric] Jika X memiliki nilai 0, 1 dengan probabilitas 0,4, 0,6, berapakah E[X]?
    """
    return 0.6

def q09() -> float:
    """
    [Numeric] Hitung Var(X) untuk variabel pada soal nomor 8.
    """
    return 0.24

def q10() -> float:
    """
    [Numeric] Jika E[X] = 10 dan E[X2] = 116, berapakah variansinya?
    """
    return 16.0

def q11() -> float:
    """
    [Numeric] Sebuah variabel acak memiliki nilai 1, 2, 3 dengan peluang sama. Berapakah nilai harapannya?
    """
    return 2.0

def q12() -> float:
    """
    [Numeric] Jika Var(X) = 4, berapakah Var(3X+5)?
    """
    return 36.0
