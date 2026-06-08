import numpy as np

def selesaikan_seidel(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.copy()
    history = []

    # Cek Diagonal 0
    for i in range(n):
        if A[i, i] == 0:
            return {"status": "GAGAL", "pesan": "Diagonal utama bernilai 0!", "history": []}

    for k in range(max_iter):
        x_old = np.copy(x) # Simpan nilai lama untuk hitung error
        
        for i in range(n):
            sum_ax = 0
            for j in range(n):
                if i != j:
                    sum_ax += A[i, j] * x[j] # Pakai x terbaru
            
            x[i] = (b[i] - sum_ax) / A[i, i]

        error = np.linalg.norm(x - x_old)
        
        history.append({
            "iterasi": k + 1,
            "x": x.copy(),
            "error": error
        })

        if error < tol:
            return {
                "status": "KONVERGEN",
                "pesan": f"Konvergen di iterasi {k+1}",
                "history": history,
                "x_final": x,
                "error_akhir": error
            }
    
    return {
        "status": "DIVERGEN",
        "pesan": "Maksimum iterasi tercapai",
        "history": history,
        "x_final": x,
        "error_akhir": error
    }