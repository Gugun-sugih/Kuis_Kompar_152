#Nama: Deden Roga Nurhidayah
#NRP: 152024152
#Kelas: CC

import multiprocessing
import time

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"Input: {celsius}°C -> Hasil: {fahrenheit}°F (Diproses oleh: {multiprocessing.current_process().name})")
    return fahrenheit

if __name__ == "__main__":
    data_suhu = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
    
    print(f"--- Memulai Eksekusi Data Parallelism (NRP: 152) ---")
    start_time = time.time()

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(convert_to_fahrenheit, data_suhu)

    end_time = time.time()
    
    print("-" * 50)
    print(f"Hasil Konversi Akhir: {results}")
    print(f"Total waktu eksekusi paralel: {end_time - start_time:.4f} detik")