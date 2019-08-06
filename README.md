# robot-telegram-steemit
Robot ini sudah dapat melakukan jual beli steem vs sbd di internal market steem --> https://steemitwallet.com/market
diperlukan 1 akun telegram untuk mengecek rasio harga

Install
1. Install steem
setting akun dengan steempy
      steempy importaccount namaakun
      masukkan passpahre.
2. Install telethon
pip3 install -U telethon --user
pip3 install -U https://github.com/LonamiWebs/Telethon/archive/master.zip --user

Jalannya robot
Ada 2 robot
1. Robot telegram cek rasio harga
   robot.py
   configrobot.py

2. Robot Eksekusi Steemit
   run.py
   dll
   Main.py hanya memanggil run.py
   run.py akan memerintahkan robotgabung.py dst
