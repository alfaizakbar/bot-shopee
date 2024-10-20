from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Fungsi untuk membuka tab Shopee dan memulai live
def buka_tab_shopee(link: str, jumlah: int):
    options = Options()
    options.add_argument("--start-maximized")  # Memaksimalkan jendela
    options.add_argument("--disable-gpu")  # Nonaktifkan GPU untuk menghindari error
    options.add_argument("--no-sandbox")  # Nonaktifkan sandbox (opsi umum di headless Chrome)
    service = Service("C:/webdriver/chromedriver-win64/chromedriver.exe")  # Ganti dengan path ke ChromeDriver Anda

    # Buat instance Chrome
    driver = webdriver.Chrome(service=service, options=options)

    # Buka tab pertama
    driver.get(link)
    time.sleep(1)  # Tunggu agar halaman dimuat

    for _ in range(jumlah - 1):  # Karena satu tab sudah dibuka, kurangi jumlah loop
        driver.execute_script("window.open('');")  # Membuka tab baru
        driver.switch_to.window(driver.window_handles[-1])  # Fokus ke tab baru
        driver.get(link)  # Membuka link di tab baru
        time.sleep(1)  # Tunggu beberapa detik agar halaman dimuat

        try:
            # Cari tombol "Mulai Live" dan klik
            start_live_button = driver.find_element(By.XPATH, '//button[contains(text(), "Mulai Live")]')
            if start_live_button:
                start_live_button.click()
                print("Live dimulai!")
            else:
                print("Tombol play tidak ditemukan.")
        except Exception as e:
            print(f"Tombol tidak ditemukan atau ada kesalahan: {e}")

    # Tetap menjalankan driver, tidak langsung menutupnya
    input("Tekan Enter untuk keluar...")  # Program akan menunggu hingga pengguna menekan Enter

    # driver.quit()  # Uncomment jika ingin menutup driver setelah selesai

def main():
    # Input Pengguna
    link = input("Masukkan link Shopee: ")
    try:
        jumlah = int(input("Masukkan jumlah tab yang ingin dibuka: "))
        
        # Validasi link dan jumlah
        if 'shopee' in link and 0 < jumlah <= 1000:
            buka_tab_shopee(link, jumlah)
            print(f"Membuka {jumlah} tab untuk {link}.")
        else:
            print("Link tidak valid atau jumlah tab harus antara 1 hingga 1000!")
    except ValueError:
        print("Jumlah harus berupa angka!")

if __name__ == '__main__':
    main()
