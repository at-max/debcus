import subprocess
import os

def show_menu():
    print("1. LXDE kur")
    print("2. KDE Plasma kur")
    print("3. MATE kur")
    print("4. Cinnamon kur")
    choice = input("Seçiminizi girin: ")
    return choice

def install_lxde():
    subprocess.run(['sudo', 'apt-get', 'update'])
    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'lxde'])

def install_kde_plasma():
    subprocess.run(['sudo', 'apt-get', 'update'])
    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'kde-plasma-desktop'])

def install_mate():
    subprocess.run(['sudo', 'apt-get', 'update'])
    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'mate-desktop'])

def install_cinnamon():
    subprocess.run(['sudo', 'apt-get', 'update'])
    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'cinnamon'])

choice = show_menu()

if choice == "1":
    install_lxde()
    web()
elif choice == "2":
    install_kde_plasma()
    web()
elif choice == "3":
    install_mate()
    web()
elif choice == "4":
    install_cinnamon()
    web()
else:
    print("Geçersiz seçim.")

def web():
    print("Web tarayıcısı seçiniz:")
    print("1. Google Chrome")
    print("2. Mozilla Firefox")
    print("3. Opera")

    # Kullanıcı seçimini al
    secim = input("Seçiminiz (1/2/3): ")

    if secim == "1":
        # Google Chrome'u indir ve kur
        os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
        os.system("sudo dpkg -i google-chrome-stable_current_amd64.deb")
    elif secim == "2":
        # Mozilla Firefox'u kur
        os.system("sudo apt-get update")
        os.system("sudo apt-get install firefox")
    elif secim == "3":
        # Opera'yı indir ve kur
        os.system("wget https://download3.operacdn.com/pub/opera/desktop/80.0.4170.16/linux/opera-stable_80.0.4170.16_amd64.deb")
        os.system("sudo dpkg -i opera-stable_80.0.4170.16_amd64.deb")
    else:
        print("Geçersiz seçim!")
