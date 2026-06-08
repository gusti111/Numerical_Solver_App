import math

def evaluasi_fungsi(fungsi_str, x_val):
    """Mengubah string 'x^2 - 4' menjadi angka."""
    try:
        fungsi_str = fungsi_str.replace('^', '**')
        env = {"x": x_val, "math": math, "e": math.e, "pi": math.pi, 
               "sin": math.sin, "cos": math.cos, "tan": math.tan, 
               "exp": math.exp, "log": math.log, "sqrt": math.sqrt}
        return eval(fungsi_str, {}, env)
    except:
        return None

def turunan_numerik(fungsi_str, x, h=1e-5):
    """
    Menghitung f'(x) menggunakan pendekatan selisih pusat (Central Difference).
    Rumus: f'(x) ≈ (f(x+h) - f(x-h)) / 2h
    """
    fx_plus = evaluasi_fungsi(fungsi_str, x + h)
    fx_min = evaluasi_fungsi(fungsi_str, x - h)
    
    if fx_plus is None or fx_min is None: return None
    return (fx_plus - fx_min) / (2 * h)

def selesaikan_newton_raphson(fungsi_str, x0, tol, max_iter):
    history = []
    x_curr = x0

    for k in range(max_iter):
        # 1. Hitung f(x) dan f'(x)
        fx = evaluasi_fungsi(fungsi_str, x_curr)
        f_aksen = turunan_numerik(fungsi_str, x_curr)

        if fx is None or f_aksen is None:
            return {"status": "GAGAL", "pesan": "Error evaluasi fungsi!", "history": [], "root": None}

        # Cek pembagian dengan nol (Turunan 0 = Garis datar)
        if abs(f_aksen) < 1e-12:
            return {"status": "GAGAL", "pesan": "Turunan mendekati 0 (Gagal konvergen)", "history": history, "root": None}

        # 2. Rumus Newton-Raphson: x_new = x - f(x)/f'(x)
        x_next = x_curr - (fx / f_aksen)
        
        # Hitung Error
        error = abs(x_next - x_curr)

        history.append({
            "iterasi": k + 1,
            "x_curr": x_curr,
            "fx": fx,
            "f_aksen": f_aksen,
            "x_next": x_next,
            "error": error
        })

        x_curr = x_next # Update x untuk iterasi berikutnya

        # Cek Konvergensi
        if error < tol:
            return {
                "status": "KONVERGEN",
                "pesan": f"Konvergen di iterasi {k+1}",
                "history": history,
                "root": x_next,
                "error_akhir": error
            }

    return {
        "status": "DIVERGEN",
        "pesan": "Maksimum iterasi tercapai",
        "history": history,
        "root": x_curr,
        "error_akhir": error
    }