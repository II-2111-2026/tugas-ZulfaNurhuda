"""
[JAWABAN ASSIGNMENT WEEK 06]

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di assignments/w06/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F     -> bool  (True=Benar, False=Salah)
- MC      -> str   ("A"/"B"/"C"/"D")
- Numeric -> int/float (desimal pakai '.')
"""

from __future__ import annotations

def q01() -> bool:
    """
    [T/F] Distribusi Binomial digunakan untuk eksperimen dengan jumlah percobaan yang tidak terbatas.
    """
    return False

def q02() -> bool:
    """
    [T/F] Parameter mean dan variansi pada distribusi Poisson memiliki nilai yang sama.
    """
    return True

def q03() -> bool:
    """
    [T/F] Distribusi Bernoulli adalah kasus khusus dari distribusi Binomial dengan n = 1.
    """
    return True

def q04() -> str:
    """
    [MC] Jika X ~ Bin(10, 0,2), maka nilai harapannya adalah:
     A) 2
     B) 0,2
     C) 8
     D) 1,6
    """
    return "A"

def q05() -> str:
    """
    [MC] Distribusi yang paling tepat untuk memodelkan jumlah telepon yang masuk ke call center dalam satu menit adalah:
     A) Binomial.
     B) Poisson.
     C) Uniform.
     D) Normal.
    """
    return "B"

def q06() -> str:
    """
    [MC] Pada distribusi Binomial, probabilitas sukses p harus:
     A) Berubah tiap percobaan.
     B) Tetap konstan tiap percobaan.
     C) Selalu 0,5.
     D) Berkurang seiring waktu.
    """
    return "B"

def q07() -> str:
    """
    [MC] Rumus P(X = k) = (lambda^k * e^-lambda) / k! adalah untuk distribusi:
     A) Binomial.
     B) Poisson.
     C) Geometrik.
     D) Eksponensial.
    """
    return "B"

def q08() -> float:
    """
    [Numeric] Jika X ~ Bin(4, 0,5), hitung P(X = 2).
    """
    return 0.375

def q09() -> float:
    """
    [Numeric] Untuk distribusi Poisson dengan lambda = 2, berapakah probabilitas P(X = 0)? (Gunakan 3 desimal)
    """
    return 0.135

def q10() -> float:
    """
    [Numeric] Hitung variansi dari variabel acak X ~ Bin(100, 0,1).
    """
    return 9.0

def q11() -> float:
    """
    [Numeric] Berapakah nilai maksimum yang mungkin dari variabel acak X ~ Bin(10, 0,5)?
    """
    return 10.0

def q12() -> float:
    """
    [Numeric] Jika rata-rata kedatangan paket adalah 5 per ms, berapakah variansi jumlah paket per ms?
    """
    return 5.0
