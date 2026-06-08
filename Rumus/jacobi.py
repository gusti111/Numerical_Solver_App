import numpy as np

def selesaikan_jacobi(A, b, x0, tol, max_iter):
    """
    Input: Matriks A, Vektor b, Tebakan x0, Toleransi, Max Iterasi
    Output: Dictionary {status, history, x_final, error}
    """
    n = len(b)
    x = x0.copy()
    x_new = np.zeros_like(x)
    history = [] # Menyimpan riwayat iterasi

    # Cek Diagonal 0 (Pencegahan Error)
    for i in range(n):
        if A[i, i] == 0:
            return {"status": "GAGAL", "pesan": "Diagonal utama bernilai 0!", "history": []}

    for k in range(max_iter):
        for i in range(n):
            s1 = np.dot(A[i, :i], x[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]

        # Hitung Error
        error = np.linalg.norm(x_new - x)
        
        # Simpan data iterasi ini
        history.append({
            "iterasi": k + 1,
            "x": x_new.copy(),
            "error": error
        })

        # Update x
        x = np.copy(x_new)

        # Cek Konvergensi
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
        "pesan": "Maksimum iterasi tercapai (Belum konvergen)",
        "history": history,
        "x_final": x,
        "error_akhir": error
    }