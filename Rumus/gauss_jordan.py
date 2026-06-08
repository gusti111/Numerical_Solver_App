import numpy as np

def selesaikan_gauss_jordan(A, b):
    """
    Menyelesaikan SPL dengan Eliminasi Gauss-Jordan.
    Output: Dictionary {status, pesan, x_final, steps}
    """
    n = len(b)
    # Gabungkan A dan b menjadi Augmented Matrix [A|b]
    M = np.hstack([A, b.reshape(-1, 1)])
    
    # Kita simpan langkah-langkahnya buat gaya-gayaan di tabel (opsional)
    steps = [] 

    # --- PROSES ELIMINASI ---
    for i in range(n):
        # 1. Pivot (Tukar baris jika diagonal 0 biar gak error)
        pivot = M[i, i]
        if abs(pivot) < 1e-10:
            # Cari baris di bawahnya yang tidak nol
            for k in range(i+1, n):
                if abs(M[k, i]) > 1e-10:
                    M[[i, k]] = M[[k, i]] # Tukar baris
                    pivot = M[i, i]
                    break
            else:
                return {"status": "GAGAL", "pesan": "Matriks Singular (Tidak ada solusi unik)", "x_final": [], "history": []}

        # 2. Normalisasi Baris Pivot (Biar diagonal jadi 1)
        M[i] = M[i] / pivot
        
        # 3. Eliminasi Baris Lain (Biar jadi 0 di kolom i)
        for k in range(n):
            if k != i:
                factor = M[k, i]
                M[k] -= factor * M[i]

        # Simpan snapshot solusi sementara (kolom terakhir)
        # Ini bukan "iterasi" sebenarnya, tapi progres eliminasi
        current_x = M[:, -1].copy()
        steps.append({
            "iterasi": i + 1,
            "x": current_x,
            "error": 0.0 # Gauss Jordan gak punya error iterasi
        })

    # Ambil kolom terakhir sebagai solusi
    x_final = M[:, -1]

    return {
        "status": "SELESAI",
        "pesan": "Solusi Ditemukan (Direct Method)",
        "history": steps,
        "x_final": x_final,
        "error_akhir": 0.0
    }