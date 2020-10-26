from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

def cekr(resi,kurir):
	driver = webdriver.Chrome(chrome_options=chrome_options)
	try:
		url = f'https://www.cekpengiriman.com/?tab=resi&resi={resi}&kurir={kurir.lower()}'
		driver.get(url)
		detail = driver.find_element_by_class_name("detail")
		status = driver.find_element_by_class_name("statusPengiriman")
		riwayat = driver.find_element_by_class_name("riwayatPengiriman")
		pesan = "-----Resi Terdaftar-----\n\n"+detail.text+"\n\n\n"+status.text.replace("Status pengiriman","-----Status pengiriman-----\n")+"\n\n\n"+riwayat.text.replace("Riwayat pengiriman","-----Riwayat pengiriman-----").replace("Tanggal Kota Keterangan","")
	except:
		pesan = "Periksa kembali no resi kamu dan kurir pengiriman, atau periksa kembali cara penggunaan /resi."

	driver.quit()
	return pesan