"""
[JAWABAN ASSIGNMENT WEEK 09]

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di assignments/w09/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F     -> bool  (True=Benar, False=Salah)
- MC      -> str   ("A"/"B"/"C"/"D")
- Numeric -> int/float (desimal pakai '.')
"""

from __future__ import annotations

def q01() -> bool:
    """
    [T/F] Jika korelasi antara dua variabel adalah nol, maka kedua variabel tersebut pasti independen.
    """
    raise NotImplementedError

def q02() -> bool:
    """
    [T/F] PDF marginal fX(x) didapatkan dengan mengintegralkan fX,Y(x,y) terhadap y dari -tak hingga ke tak hingga.
    """
    raise NotImplementedError

def q03() -> bool:
    """
    [T/F] Nilai koefisien korelasi selalu berada di antara -1 dan 1.
    """
    raise NotImplementedError

def q04() -> str:
    """
    [MC] Jika X dan Y independen, maka E[XY] sama dengan:
     A) E[X]+E[Y]
     B) E[X]E[Y]
     C) E[X]/E[Y]
     D) 0
    """
    raise NotImplementedError

def q05() -> str:
    """
    [MC] Manakah ukuran yang menunjukkan kekuatan hubungan linear antara dua variabel?
     A) Variansi.
     B) Mean.
     C) Korelasi.
     D) CDF.
    """
    raise NotImplementedError

def q06() -> str:
    """
    [MC] Jika Var(X) = 4, Var(Y) = 9, dan X, Y independen, maka Var(X+Y) adalah:
     A) 13
     B) 5
     C) 36
     D) 6,5
    """
    raise NotImplementedError

def q07() -> str:
    """
    [MC] Fungsi probabilitas kondisional fX|Y(x|y) didefinisikan sebagai:
     A) fX,Y(x,y) / fY(y)
     B) fX,Y(x,y) / fX(x)
     C) fX(x) fY(y)
     D) fX,Y(x,y) - fX(x)
    """
    raise NotImplementedError

def q08() -> float:
    """
    [Numeric] Jika Cov(X,Y) = 2, sigmaX = 2, sigmaY = 2, berapakah koefisien korelasinya?
    """
    raise NotImplementedError

def q09() -> float:
    """
    [Numeric] Berapakah nilai E[X+Y] jika E[X] = 10 dan E[Y] = 20?
    """
    raise NotImplementedError

def q10() -> float:
    """
    [Numeric] Jika f(x,y) = 1/4 untuk 0 <= x <= 2 dan 0 <= y <= 2, berapakah P(X <= 1, Y <= 1)?
    """
    raise NotImplementedError

def q11() -> float:
    """
    [Numeric] Dalam tabel diskrit, jika P(1,1) = 0,1, P(1,2) = 0,2, P(2,1) = 0,3, P(2,2) = 0,4, berapakah probabilitas marginal P(X = 1)?
    """
    raise NotImplementedError

def q12() -> float:
    """
    [Numeric] Jika X dan X memiliki korelasi 1 dan Var(X) = 4, berapakah Var(X+X)?
    """
    raise NotImplementedError
