import math

def evaluasi_fungsi(fungsi_str, x_val):
    try:
        fungsi_str = fungsi_str.replace('^', '**')
        env = {"x": x_val, "math": math, "e": math.e, "pi": math.pi, 
               "sin": math.sin, "cos": math.cos, "tan": math.tan, 
               "exp": math.exp, "log": math.log, "sqrt": math.sqrt}
        return eval(fungsi_str, {}, env)
    except:
        return None

def selesaikan_regula_falsi(fungsi_str, a, b, tol, max_iter):
    history = []
    
    # Cek Syarat Awal
    fa = evaluasi_fungsi(fungsi_str, a)
    fb = evaluasi_fungsi(fungsi_str, b)

    if fa is None or fb is None:
        return {"status": "GAGAL", "pesan": "Error evaluasi fungsi!", "history": [], "root": None}

    if fa * fb >= 0:
        return {"status": "GAGAL", "pesan": "Syarat Gagal: f(a)*f(b) > 0 (Akar tidak diapit)", "history": [], "root": None}
    
    c_old = a # Untuk menghitung error nanti

    for k in range(max_iter):
        # --- RUMUS REGULA FALSI ---
        # Hati-hati pembagian dengan nol
        if abs(fb - fa) < 1e-12:
            return {"status": "GAGAL", "pesan": "Division by Zero (f(b) - f(a) terlalu kecil)", "history": history, "root": None}
            
        c = b - (fb * (b - a) / (fb - fa))
        fc = evaluasi_fungsi(fungsi_str, c)
        
        if fc is None: return {"status": "GAGAL", "pesan": "Math Error", "history": [], "root": None}

        # Hitung Error (Selisih c sekarang dengan c sebelumnya)
        error = abs(c - c_old)
        c_old = c # Simpan c sekarang untuk iterasi besok

        history.append({
            "iterasi": k + 1,
            "a": a, "b": b, "c": c, "fa": fa, "fb": fb, "fc": fc, "error": error
        })

        # Cek Konvergensi (Jika f(c) mendekati 0 atau error sangat kecil)
        if abs(fc) < 1e-9 or error < tol:
            return {
                "status": "KONVERGEN",
                "pesan": f"Konvergen di iterasi {k+1}",
                "history": history,
                "root": c,
                "error_akhir": error
            }

        # Update Interval (Sama seperti Biseksi)
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return {
        "status": "DIVERGEN",
        "pesan": "Maksimum iterasi tercapai",
        "history": history,
        "root": c,
        "error_akhir": error
    }