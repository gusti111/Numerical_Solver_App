import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QFileDialog
from PySide6.QtGui import QIcon


# Import UI
from ui_mainMenu import Ui_MainWindow


# Import Logic
from Rumus import jacobi
from Rumus import gauss_seidel
from Rumus import gauss_jordan
from Rumus import bisection
from Rumus import newton
from Rumus import regulafalsi


# Cek Library Excel
try:
    import pandas as pd
    import openpyxl
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

class NumericalSolverApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Numerical Solver App")
        
        # Pasang Icon
        self.setWindowIcon(QIcon("logo.ico"))

        # Setup Awal
        self.ui.stackedWidget.setCurrentIndex(0)

        # ==========================================
        # 1. NAVIGASI & MENU
        # ==========================================
        self.setup_connections()
        
        # Init Table Structure (Biar gak kosong pas dibuka)
        self.update_table_structure(self.ui.spinOrde, self.ui.tableInput)
        if hasattr(self.ui, 'spinOrdeSeidel'):
            self.update_table_structure(self.ui.spinOrdeSeidel, self.ui.tableInputSeidel)
        if hasattr(self.ui, 'spinOrdeJordan'):
            self.update_table_structure(self.ui.spinOrdeJordan, self.ui.tableInputJordan)


    def setup_connections(self):
        """Mengumpulkan SEMUA koneksi tombol di sini biar rapi"""
        
        # --- [1] MENU BAR (EXPORT EXCEL) ---
        # (Ini yang tadi hilang karena tertimpa)
        if hasattr(self.ui, 'actionExportExcel'):
            self.ui.actionExportExcel.triggered.connect(self.export_to_excel)
        elif hasattr(self.ui, 'actionExport_Excel'):
            self.ui.actionExport_Excel.triggered.connect(self.export_to_excel)

        # --- [2] MENU ABOUT ---
        if hasattr(self.ui, 'actionAbout'):
            self.ui.actionAbout.triggered.connect(self.show_about)
        
        # --- [3] NAVIGASI PINDAH HALAMAN ---
        if hasattr(self.ui, 'btnJacobi'): self.ui.btnJacobi.clicked.connect(lambda: self.pindah_halaman(1))
        if hasattr(self.ui, 'btnSeidel'): self.ui.btnSeidel.clicked.connect(lambda: self.pindah_halaman(2))
        if hasattr(self.ui, 'btnJordan'): self.ui.btnJordan.clicked.connect(lambda: self.pindah_halaman(3))
        if hasattr(self.ui, 'btnBiseksi'): self.ui.btnBiseksi.clicked.connect(lambda: self.pindah_halaman(4))
        if hasattr(self.ui, 'btnNewton'): self.ui.btnNewton.clicked.connect(lambda: self.pindah_halaman(5))
        if hasattr(self.ui, 'btnRegula'): self.ui.btnRegula.clicked.connect(lambda: self.pindah_halaman(6))

        # Tombol Kembali (Universal)
        btns_kembali = [
            'btnKembaliJacobi', 'btnKembaliSeidel', 'btnKembaliJordan',
            'btnKembaliBiseksi', 'btnKembaliNewton', 'btnKembaliRegula'
        ]
        for btn_name in btns_kembali:
            if hasattr(self.ui, btn_name):
                getattr(self.ui, btn_name).clicked.connect(lambda: self.pindah_halaman(0))

        # --- [4] LOGIKA TOMBOL HITUNG & RESET ---
        
        # 1. Jacobi
        self.ui.spinOrde.valueChanged.connect(lambda: self.update_table_structure(self.ui.spinOrde, self.ui.tableInput))
        self.ui.btnHitung.clicked.connect(self.proses_jacobi)
        if hasattr(self.ui, 'btnReset'): self.ui.btnReset.clicked.connect(self.reset_jacobi)

        # 2. Gauss Seidel
        if hasattr(self.ui, 'btnHitungSeidel'):
            self.ui.spinOrdeSeidel.valueChanged.connect(lambda: self.update_table_structure(self.ui.spinOrdeSeidel, self.ui.tableInputSeidel))
            self.ui.btnHitungSeidel.clicked.connect(self.proses_seidel)
            self.ui.btnResetSeidel.clicked.connect(self.reset_seidel)

        # 3. Gauss Jordan
        if hasattr(self.ui, 'btnHitungJordan'):
            self.ui.spinOrdeJordan.valueChanged.connect(lambda: self.update_table_structure(self.ui.spinOrdeJordan, self.ui.tableInputJordan))
            self.ui.btnHitungJordan.clicked.connect(self.proses_jordan)
            self.ui.btnResetJordan.clicked.connect(self.reset_jordan)

        # 4. Biseksi
        if hasattr(self.ui, 'btnHitungBiseksi'):
            self.ui.btnHitungBiseksi.clicked.connect(self.proses_biseksi)
            self.ui.btnResetBiseksi.clicked.connect(self.reset_biseksi)

        # 5. Newton
        if hasattr(self.ui, 'btnHitungNewton'):
            self.ui.btnHitungNewton.clicked.connect(self.proses_newton)
            self.ui.btnResetNewton.clicked.connect(self.reset_newton)

        # 6. Regula Falsi
        if hasattr(self.ui, 'btnHitungRegula'):
            self.ui.btnHitungRegula.clicked.connect(self.proses_regula)
            self.ui.btnResetRegula.clicked.connect(self.reset_regula)

    def pindah_halaman(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)

    # ==========================================
    # HELPER FUNCTIONS (Input & Output)
    # ==========================================
    def update_table_structure(self, spin_widget, table_widget):
        n = spin_widget.value()
        table_widget.setRowCount(n)
        table_widget.setColumnCount(n + 1)
        headers = [f"x{i+1}" for i in range(n)] + ["b (Hasil)"]
        table_widget.setHorizontalHeaderLabels(headers)

    def get_float_input(self, widget, field_name="Input"):
        """Fungsi pembantu untuk validasi angka. Kalau kosong/salah -> Error."""
        text = widget.text().strip()
        if not text:
            raise ValueError(f"Kolom '{field_name}' tidak boleh kosong!")
        try:
            return float(text)
        except ValueError:
            raise ValueError(f"Kolom '{field_name}' harus berupa angka valid!")

    def ambil_matriks_aman(self, spin_widget, table_widget):
        """Mengambil input matriks dengan Try-Except"""
        n = spin_widget.value()
        A = []
        b = []
        
        # Validasi Tabel Tidak Boleh Kosong
        for i in range(n):
            row = []
            for j in range(n):
                item = table_widget.item(i, j)
                if not item or not item.text().strip():
                    raise ValueError(f"Matriks Baris {i+1} Kolom {j+1} masih kosong!")
                try:
                    row.append(float(item.text()))
                except:
                    raise ValueError(f"Input di Baris {i+1} Kolom {j+1} bukan angka!")
            A.append(row)
            
            # Ambil vektor b
            item_b = table_widget.item(i, n)
            if not item_b or not item_b.text().strip():
                raise ValueError(f"Nilai b (hasil) di Baris {i+1} kosong!")
            try:
                b.append(float(item_b.text()))
            except:
                raise ValueError(f"Nilai b di Baris {i+1} bukan angka!")
                
        return np.array(A), np.array(b)

    def tampilkan_hasil_matriks(self, hasil, table_output, label_status, txt_solusi):
        if hasil["status"] == "GAGAL":
            label_status.setText(f"Status: {hasil['pesan']}")
            QMessageBox.warning(self, "Gagal Konvergen", hasil["pesan"])
            return

        label_status.setText(f"Status: {hasil['pesan']}")
        table_output.setRowCount(0)
        
        # Deteksi apakah ini Jordan (tanpa error) atau Iterasi
        if "history" in hasil:
            hist = hasil["history"]
            if not hist: return
            
            # Cek kolom pertama data untuk nentuin header
            first_row = hist[0]
            if "error" in first_row: # Iterasi (Jacobi/Seidel)
                n_vars = len(first_row["x"])
                table_output.setColumnCount(n_vars + 2)
                headers = ["Iterasi"] + [f"x{i+1}" for i in range(n_vars)] + ["Error"]
                table_output.setHorizontalHeaderLabels(headers)
                
                for row_data in hist:
                    r = table_output.rowCount()
                    table_output.insertRow(r)
                    table_output.setItem(r, 0, QTableWidgetItem(str(row_data["iterasi"])))
                    for i, val in enumerate(row_data["x"]):
                        table_output.setItem(r, i+1, QTableWidgetItem(f"{val:.5f}"))
                    table_output.setItem(r, n_vars+1, QTableWidgetItem(f"{row_data['error']:.2e}"))
            else: # Jordan (Step by step)
                n_vars = len(first_row["x"])
                table_output.setColumnCount(n_vars + 1)
                headers = ["Langkah"] + [f"x{i+1}" for i in range(n_vars)]
                table_output.setHorizontalHeaderLabels(headers)

                for row_data in hist:
                    r = table_output.rowCount()
                    table_output.insertRow(r)
                    table_output.setItem(r, 0, QTableWidgetItem(f"Step {row_data['iterasi']}"))
                    for i, val in enumerate(row_data["x"]):
                        table_output.setItem(r, i+1, QTableWidgetItem(f"{val:.5f}"))

        # Solusi
        if "x_final" in hasil:
            solusi_final = []
            for val in hasil["x_final"]:
                if abs(val - round(val)) < 1e-3:
                    solusi_final.append(f"{int(round(val))}")
                else:
                    solusi_final.append(f"{val:.5f}")
            str_hasil = "\n".join([f"x{i+1} = {v}" for i, v in enumerate(solusi_final)])
            txt_solusi.setPlainText(f"Solusi Akhir:\n{str_hasil}")

    # ==========================================
    # LOGIC PROCESSORS (Dengan Error Handling Kuat)
    # ==========================================
    
    # 1. JACOBI
    def proses_jacobi(self):
        try:
            A, b = self.ambil_matriks_aman(self.ui.spinOrde, self.ui.tableInput)
            x0_str = self.ui.inputX0.text().strip()
            tol = self.get_float_input(self.ui.inputToleransi, "Toleransi")
            max_iter = self.ui.inputMaxIter.value() or 100
            
            x0 = np.zeros(len(b))
            if x0_str:
                parts = x0_str.replace(',', ' ').split()
                if len(parts) == len(b):
                    x0 = np.array([float(p) for p in parts])
            
            hasil = jacobi.selesaikan_jacobi(A, b, x0, tol, max_iter)
            self.tampilkan_hasil_matriks(hasil, self.ui.tableHasil, self.ui.labelStatus, self.ui.txtSolusi)
            
        except Exception as e:
            QMessageBox.critical(self, "Error Eksekusi", str(e))

    def reset_jacobi(self):
        self.ui.tableInput.clearContents() # Bersihkan isi sel
        self.ui.tableHasil.setRowCount(0)  # Hapus baris hasil
        self.ui.txtSolusi.clear()
        self.ui.inputX0.clear()
        self.ui.labelStatus.setText("Status: Ready")

    # 2. SEIDEL
    def proses_seidel(self):
        try:
            A, b = self.ambil_matriks_aman(self.ui.spinOrdeSeidel, self.ui.tableInputSeidel)
            x0_str = self.ui.inputX0Seidel.text().strip()
            tol = self.get_float_input(self.ui.inputTolSeidel, "Toleransi")
            max_iter = self.ui.inputIterSeidel.value() or 100
            
            x0 = np.zeros(len(b))
            if x0_str:
                parts = x0_str.replace(',', ' ').split()
                if len(parts) == len(b): x0 = np.array([float(p) for p in parts])

            hasil = gauss_seidel.selesaikan_seidel(A, b, x0, tol, max_iter)
            self.tampilkan_hasil_matriks(hasil, self.ui.tableHasilSeidel, self.ui.labelStatusSeidel, self.ui.txtSolusiSeidel)

        except Exception as e:
            QMessageBox.critical(self, "Error Eksekusi", str(e))

    def reset_seidel(self):
        self.ui.tableInputSeidel.clearContents()
        self.ui.tableHasilSeidel.setRowCount(0)
        self.ui.txtSolusiSeidel.clear()
        self.ui.inputX0Seidel.clear()
        self.ui.labelStatusSeidel.setText("Status: Ready")

    # 3. JORDAN
    def proses_jordan(self):
        try:
            A, b = self.ambil_matriks_aman(self.ui.spinOrdeJordan, self.ui.tableInputJordan)
            hasil = gauss_jordan.selesaikan_gauss_jordan(A, b)
            self.tampilkan_hasil_matriks(hasil, self.ui.tableHasilJordan, self.ui.labelStatusJordan, self.ui.txtSolusiJordan)
        except Exception as e:
            QMessageBox.critical(self, "Error Eksekusi", str(e))

    def reset_jordan(self):
        self.ui.tableInputJordan.clearContents()
        self.ui.tableHasilJordan.setRowCount(0)
        self.ui.txtSolusiJordan.clear()
        self.ui.labelStatusJordan.setText("Status: Ready")

    # 4. BISEKSI
    def proses_biseksi(self):
        try:
            fungsi = self.ui.inputFungsiBiseksi.text().strip()
            if not fungsi: raise ValueError("Rumus fungsi belum diisi!")
            
            a = self.get_float_input(self.ui.inputABiseksi, "Batas a")
            b = self.get_float_input(self.ui.inputBBiseksi, "Batas b")
            tol = self.get_float_input(self.ui.inputTolBiseksi, "Toleransi")
            max_iter = self.ui.inputIterBiseksi.value() or 100

            hasil = bisection.selesaikan_biseksi(fungsi, a, b, tol, max_iter)
            
            # Tampilkan Hasil Non-Linear
            self.tampilkan_hasil_nonlinear(hasil, self.ui.tableHasilBiseksi, self.ui.labelStatusBiseksi, self.ui.txtSolusiBiseksi)

        except Exception as e:
            QMessageBox.critical(self, "Error Biseksi", str(e))

    def reset_biseksi(self):
        self.ui.inputFungsiBiseksi.clear()
        self.ui.inputABiseksi.clear()
        self.ui.inputBBiseksi.clear()
        self.ui.tableHasilBiseksi.setRowCount(0)
        self.ui.txtSolusiBiseksi.clear()
        self.ui.labelStatusBiseksi.setText("Status: Ready")

    # 5. NEWTON
    def proses_newton(self):
        try:
            fungsi = self.ui.inputFungsiNewton.text().strip()
            if not fungsi: raise ValueError("Rumus fungsi belum diisi!")
            
            x0 = self.get_float_input(self.ui.inputX0Newton, "Tebakan x0")
            tol = self.get_float_input(self.ui.inputTolNewton, "Toleransi")
            max_iter = self.ui.inputIterNewton.value() or 100

            hasil = newton.selesaikan_newton_raphson(fungsi, x0, tol, max_iter)
            
            # Tampilan Khusus Newton
            self.ui.labelStatusNewton.setText(f"Status: {hasil['pesan']}")
            if hasil["status"] == "GAGAL":
                QMessageBox.warning(self, "Gagal", hasil["pesan"])
                return

            self.ui.tableHasilNewton.setRowCount(0)
            self.ui.tableHasilNewton.setColumnCount(6)
            self.ui.tableHasilNewton.setHorizontalHeaderLabels(["Iterasi", "x", "f(x)", "f'(x)", "x_new", "Error"])
            
            for d in hasil["history"]:
                r = self.ui.tableHasilNewton.rowCount()
                self.ui.tableHasilNewton.insertRow(r)
                self.ui.tableHasilNewton.setItem(r, 0, QTableWidgetItem(str(d["iterasi"])))
                self.ui.tableHasilNewton.setItem(r, 1, QTableWidgetItem(f"{d['x_curr']:.6f}"))
                self.ui.tableHasilNewton.setItem(r, 2, QTableWidgetItem(f"{d['fx']:.6f}"))
                self.ui.tableHasilNewton.setItem(r, 3, QTableWidgetItem(f"{d['f_aksen']:.6f}"))
                self.ui.tableHasilNewton.setItem(r, 4, QTableWidgetItem(f"{d['x_next']:.6f}"))
                self.ui.tableHasilNewton.setItem(r, 5, QTableWidgetItem(f"{d['error']:.2e}"))

            if hasil["root"] is not None:
                self.ui.txtSolusiNewton.setPlainText(f"Akar: {hasil['root']:.6f}")
            else:
                self.ui.txtSolusiNewton.setPlainText("Gagal.")

        except Exception as e:
            QMessageBox.critical(self, "Error Newton", str(e))

    def reset_newton(self):
        self.ui.inputFungsiNewton.clear()
        self.ui.inputX0Newton.clear()
        self.ui.tableHasilNewton.setRowCount(0)
        self.ui.txtSolusiNewton.clear()

    # 6. REGULA FALSI
    def proses_regula(self):
        try:
            fungsi = self.ui.inputFungsiRegula.text().strip()
            if not fungsi: raise ValueError("Isi Rumus Dulu!")
            a = self.get_float_input(self.ui.inputARegula, "Batas a")
            b = self.get_float_input(self.ui.inputBRegula, "Batas b")
            tol = self.get_float_input(self.ui.inputTolRegula, "Tol")
            max_iter = self.ui.inputIterRegula.value() or 100

            hasil = regulafalsi.selesaikan_regula_falsi(fungsi, a, b, tol, max_iter)
            self.tampilkan_hasil_nonlinear(hasil, self.ui.tableHasilRegula, self.ui.labelStatusRegula, self.ui.txtSolusiRegula)
        
        except Exception as e:
            QMessageBox.critical(self, "Error Regula Falsi", str(e))

    def reset_regula(self):
        self.ui.inputFungsiRegula.clear()
        self.ui.inputARegula.clear()
        self.ui.inputBRegula.clear()
        self.ui.tableHasilRegula.setRowCount(0)
        self.ui.txtSolusiRegula.clear()

    def tampilkan_hasil_nonlinear(self, hasil, table, label, txt):
        label.setText(f"Status: {hasil['pesan']}")
        if hasil["status"] == "GAGAL":
            QMessageBox.warning(self, "Gagal", hasil["pesan"])
            return
        
        table.setRowCount(0)
        # Setup kolom dinamis (sesuai data yg ada)
        if not hasil["history"]: return
        keys = list(hasil["history"][0].keys())
        table.setColumnCount(len(keys))
        table.setHorizontalHeaderLabels(keys)
        
        for d in hasil["history"]:
            r = table.rowCount()
            table.insertRow(r)
            for i, k in enumerate(keys):
                val = d[k]
                if isinstance(val, (int, float)):
                    table.setItem(r, i, QTableWidgetItem(f"{val:.6f}"))
                else:
                    table.setItem(r, i, QTableWidgetItem(str(val)))
        
        if hasil["root"] is not None:
            txt.setPlainText(f"Akar: {hasil['root']:.6f}")

    # ==========================================
    # EXPORT EXCEL
    # ==========================================
    def export_to_excel(self):
        if not HAS_PANDAS:
            QMessageBox.critical(self, "Error", "Library 'pandas' belum terinstall!\nJalankan: pip install pandas openpyxl")
            return

        print("Tombol Export Ditekan...") # Debugging
        
        curr_idx = self.ui.stackedWidget.currentIndex()
        
        # Mapping Halaman -> Tabel
        # Pastikan index ini sesuai urutan di Designer kamu!
        # 0=Menu, 1=Jacobi, 2=Seidel, 3=Jordan, 4=Biseksi, 5=Newton, 6=Regula
        mapping = {
            1: (self.ui.tableHasil, "Jacobi.xlsx"),
            2: (self.ui.tableHasilSeidel, "Seidel.xlsx"),
            3: (self.ui.tableHasilJordan, "Jordan.xlsx"),
            4: (self.ui.tableHasilBiseksi, "Biseksi.xlsx"),
            5: (self.ui.tableHasilNewton, "Newton.xlsx"),
            6: (self.ui.tableHasilRegula, "RegulaFalsi.xlsx"),
        }

        if curr_idx not in mapping:
            QMessageBox.information(self, "Info", "Halaman ini tidak ada tabel hasil.")
            return

        target_table, default_name = mapping[curr_idx]
        
        if target_table.rowCount() == 0:
            QMessageBox.warning(self, "Kosong", "Tabel masih kosong. Hitung dulu!")
            return

        path, _ = QFileDialog.getSaveFileName(self, "Simpan Excel", default_name, "Excel Files (*.xlsx)")
        if path:
            try:
                # Ambil Header
                headers = [target_table.horizontalHeaderItem(i).text() for i in range(target_table.columnCount())]
                data = []
                for r in range(target_table.rowCount()):
                    row_data = []
                    for c in range(target_table.columnCount()):
                        item = target_table.item(r, c)
                        row_data.append(item.text() if item else "")
                    data.append(row_data)
                
                df = pd.DataFrame(data, columns=headers)
                df.to_excel(path, index=False)
                QMessageBox.information(self, "Sukses", f"Data tersimpan di:\n{path}")
            except Exception as e:
                QMessageBox.critical(self, "Gagal Export", str(e))

    def show_about(self):
        # Pesan HTML biar bisa di-bold dan rapi
        pesan = """
        <h3><b>NUMERICAL SOLVER APP</b></h3>
        <p>Aplikasi penyelesaian masalah matematis Linear & Non-Linear.</p>
        <hr>
        <p><b>Dibuat oleh Group 13:</b></p>
        <ul style='margin-left: -20px;'>
            <li>Gusty Faqikh</li>
            <li>Alya Sashi Kirana</li>
        </ul>
        <br>
        <p><i>"Technology is best when it brings people together."</i></p>
        <hr>
        <p style='font-size: 10px; color: gray;'>
            © 2026 - Teknik Informatika<br>
            All Rights Reserved.
        </p>
        """
        
        
        QMessageBox.about(self, "Tentang Aplikasi", pesan)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NumericalSolverApp()
    window.show()
    sys.exit(app.exec())