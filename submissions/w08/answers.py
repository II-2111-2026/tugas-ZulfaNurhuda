"""
[JAWABAN ASSIGNMENT WEEK 08]

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di assignments/w08/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F     -> bool  (True=Benar, False=Salah)
- MC      -> str   ("A"/"B"/"C"/"D")
- Numeric -> int/float (desimal pakai '.')
"""

from __future__ import annotations

def q01() -> bool:
    """
    [T/F] Dalam model probabilistik, output yang sama akan selalu dihasilkan dari input yang sama terlepas dari variasi acak.
    """
    raise NotImplementedError

def q02() -> bool:
    """
    [T/F] Probabilitas dari gabungan dua kejadian selalu lebih besar daripada probabilitas masing-masing kejadian.
    """
    raise NotImplementedError

def q03() -> bool:
    """
    [T/F] Pada distribusi kontinu, P(X <= x) selalu sama dengan P(X < x).
    """
    raise NotImplementedError

def q04() -> str:
    """
    [MC] Jika P(A) = 0,5, P(B) = 0,4 dan A,B independen, maka P(A∩B) adalah:
     A) 0,9
     B) 0,1
     C) 0,2
     D) 0,5
    """
    raise NotImplementedError

def q05() -> str:
    """
    [MC] Variansi dari variabel acak X didefinisikan sebagai:
     A) E[X2] - (E[X])2
     B) E[X] - E[X2]
     C) E[X]
     D) E[X]2
    """
    raise NotImplementedError

def q06() -> str:
    """
    [MC] Pada distribusi Binomial, probabilitas sukses p harus:
     A) Berubah tiap percobaan.
     B) Tetap konstan tiap percobaan.
     C) Selalu 0,5.
     D) Berkurang seiring waktu.
    """
    raise NotImplementedError

def q07() -> str:
    """
    [MC] Jika lambda = 0,5 pada distribusi Eksponensial, maka nilai harapannya adalah:
     A) 0,5
     B) 2,0
     C) 1,0
     D) 0,25
    """
    raise NotImplementedError

def q08() -> float:
    """
    [Numeric] Berapa jumlah elemen dalam ruang sampel jika kita melempar dua buah dadu bersisi enam?
    """
    raise NotImplementedError

def q09() -> float:
    """
    [Numeric] Sebuah sistem memiliki probabilitas gagal 0,05. Berapakah probabilitas sistem tersebut berhasil?
    """
    raise NotImplementedError

def q10() -> float:
    """
    [Numeric] Sebuah sistem memiliki reliabilitas 0,99. Berapa probabilitas kegagalannya?
    """
    raise NotImplementedError

def q11() -> float:
    """
    [Numeric] Jika P(A) = 0,3, P(B|A) = 0,7 dan P(B|Ac) = 0,4, hitung P(B) menggunakan Hukum Probabilitas Total.
    """
    raise NotImplementedError

def q12() -> float:
    """
    [Numeric] Jika rata-rata kedatangan paket adalah 5 per ms, berapakah variansi jumlah paket per ms?
    """
    raise NotImplementedError
