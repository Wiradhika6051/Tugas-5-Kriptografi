from lib.HanonMapRNG import HanonMapRNG
import time


if __name__=="__main__":
 # Inisialisasi Parameter
 x0 = 0.009260419
 a = 1.4
 b = -0.3
 size = 16
 base_iteration = 100
 # Inisialisasi RNG
 rng = HanonMapRNG(x0,a,b,size,base_iteration)
 # Melakukan Pengujian
 avg_time = 0
 total_time = 0
 salts = []
 for i in range(1_000):
    # Bangkitkan salt
    start_time = time.time()
    salt = rng.get_salt()
    end_time = time.time()
    salts.append(salt)
    # Hitung waktu yang dibutuhkan
    elapsed_time = end_time - start_time
    total_time += elapsed_time
    avg_time = total_time / (i+1)
    if (i+1) % 100 == 0:
      print(f"Berhasil membangkitkan {i+1} salt.")
print("="*5,"HASIL","="*5)
# Tes Kolisi
salts_set = set(salts)
if len(salts) == len(salts_set):
  print("> Tidak ada kolisi yang terjadi.")
else:
  print(f"> Terdapat {len(salt)-len(salts_set)} kasus kolisi.")
# Statistik Waktu
print("> Total Waktu Pembangkitan 1.000 Salt:",total_time)
print("> Rata-rata Waktu Pembangkitan 1 Salt:",avg_time)
