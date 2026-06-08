# FILE: bisection.py
import math

def evaluasi_fungsi(fungsi_str, x_val):
    try:
        fungsi_str = fungsi_str.replace('^', '**')
        env = {"x": x_val, "math": math, "sin": math.sin, "cos": math.cos, "tan": math.tan, "exp": math.exp, "log": math.log, "sqrt": math.sqrt}
        return eval(fungsi_str, {}, env)
    except Exception as e:
        return None

def selesaikan_biseksi(fungsi_str, a, b, tol, max_iter):
    history = []
    
    fa = evaluasi_fungsi(fungsi_str, a)
    fb = evaluasi_fungsi(fungsi_str, b)

    if fa is None or fb is None:
        return {"status": "GAGAL", "pesan": "Rumus fungsi salah/error!", "history": [], "root": None}

    if fa * fb >= 0:
        return {"status": "GAGAL", "pesan": "Tebakan a dan b tidak mengapit akar! (f(a)*f(b) > 0)", "history": [], "root": None}

    for k in range(max_iter):
        c = (a + b) / 2
        fc = evaluasi_fungsi(fungsi_str, c)
        
        if fc is None: return {"status": "GAGAL", "pesan": "Math Error di iterasi", "history": [], "root": None}

        error = abs(b - a)

        history.append({
            "iterasi": k + 1,
            "a": a, "b": b, "c": c, "fa": fa, "fb": fb, "fc": fc, "error": error
        })

        if error < tol or abs(fc) < 1e-9:
            return {
                "status": "KONVERGEN",
                "pesan": f"Akar ditemukan di iterasi {k+1}",
                "history": history,
                "root": c,
                "error_akhir": error
            }

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