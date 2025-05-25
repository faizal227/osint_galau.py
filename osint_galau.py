#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import socket
import requests
import whois
import platform
import sys

def banner():
    os.system("clear")
    print("""
    ============================================
    |            OSINT G A L A U . P Y         |
    |       Created by: harry_h4xOr_Zploit     |
    |------------------------------------------|
    |   aku sepi sering kali aku rindu dia     |
    |   tapi kau tak tau...                    |
    ============================================
    """)

def ip_lookup():
    ip = input("Masukkan IP: ")
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json")
        print(r.text)
    except:
        print("Gagal dapatkan info IP.")

def whois_lookup():
    domain = input("Masukkan domain: ")
    try:
        w = whois.whois(domain)
        print(w)
    except:
        print("Gagal WHOIS.")

def dns_lookup():
    domain = input("Masukkan domain: ")
    try:
        result = socket.gethostbyname(domain)
        print("IP:", result)
    except:
        print("DNS gagal.")

def user_agent():
    print("User-Agent system kau:", requests.get("https://httpbin.org/user-agent").json())

def system_info():
    print("Platform:", platform.system())
    print("Release:", platform.release())
    print("Versi:", platform.version())
    print("Processor:", platform.processor())

def phone_info():
    number = input("Masukkan nombor telefon (dengan kod negara): ")
    print(f"Fungsi ni mockup je. Info untuk {number} tak tersedia dalam versi ni.")

def email_breach_check():
    email = input("Masukkan email: ")
    print(f"Fungsi ni dummy. Kalau nak real, kena guna API dari haveibeenpwned.com")

def port_scan():
    host = input("Masukkan IP/Domain untuk scan port: ")
    print("Scanning port 1 - 100...")
    for port in range(1, 101):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} TERBUKA")
        s.close()

def reverse_ip():
    domain = input("Masukkan domain: ")
    print("Fungsi ni bukan real-time reverse IP. Guna external service kalau nak result penuh.")

def exit_tool():
    print("Tool dihentikan. Hati-hati dengan rindu yang datang tiba-tiba.")
    sys.exit()

def menu():
    while True:
        banner()
        print("""
[1] IP Lookup
[2] WHOIS Lookup
[3] DNS Lookup
[4] Lihat User-Agent
[5] Info Sistem
[6] Info Nombor Telefon
[7] Check Email Breach
[8] Port Scanner (1-100)
[9] Reverse IP Lookup
[10] Keluar

Pilih fungsi galau mu ------------------=>>>
        """)
        choice = input(">> ")

        if choice == '1':
            ip_lookup()
        elif choice == '2':
            whois_lookup()
        elif choice == '3':
            dns_lookup()
        elif choice == '4':
            user_agent()
        elif choice == '5':
            system_info()
        elif choice == '6':
            phone_info()
        elif choice == '7':
            email_breach_check()
        elif choice == '8':
            port_scan()
        elif choice == '9':
            reverse_ip()
        elif choice == '10':
            exit_tool()
        else:
            print("Pilihan tak sah.")
        input("\nTekan ENTER untuk kembali ke menu...")

if __name__ == "__main__":
    menu()
