Alpine Linux na Pandaboard ES Rev B3		
###########################################
:date: 2021-05-25 20:44
:category: IT
:tags: alpine, arm, armhf, armv7, it, komputery, linux, pandaboard
:slug: alpine-linux-na-pandaboard-es-rev-b3
:status: published
:cover: images/2021/05/pandaboardalpine.png
:attachments: images/2021/05/pandaboardalpine.png

W poprzednim wpisie było trochę o historii tej płytki. Dziś pokażę jak można postawić na nim `Alpine Linux. <https://alpinelinux.org/>`__

Krótko o Alpine Linux
---------------------

Dla nie wtajemniczonych, Alpine to bardzo minimalistyczna dystrybucja Linuxa oparta o `busybox <https://busybox.net/>`__. Dystrybucja jest bardzo popularnym wyborem jako OS dla kontenerów dockerowych. Co nie oznacza, że nadaje się tylko do tego. Ma własnego menedżera pakietów pt. "apk". Bez problemu śmiga na nim Python 3, nginx, php, mysql itp.

Ze źródła krok po kroku
~~~~~~~~~~~~~~~~~~~~~~~

Na wstępie zaznaczam, że instrukcję piszę głównie dla siebie - żebym mógł później zajrzeć i przypomnieć sobie jak zrobiłem to, czy tamto :) Instrukcja będzie głównie opierała się o `świetny tutorial ze strony DigiKey.com <https://forum.digikey.com/t/debian-getting-started-with-the-pandaboard/12839>`__. Nie ukrywam, że jest to w pewnym sensie archiwizacja tego wpisu, jako że zauważyłem, że strona zmieniła się już któryś raz, i po prostu boję się, że instrukcję czeka ten sam los co główna strona projektu - pandaboard.org - a więc przestanie isnieć.

Prerequisite
^^^^^^^^^^^^

Radzę stworzyć sobie jakiś folder (np. *pandaboard*) i robić wszystko w nim:

.. code:: sh

   mkdir pandaboard
   cd pandaboard

Przygotowujemy kompilator
^^^^^^^^^^^^^^^^^^^^^^^^^

Ściągamy gcc-linaro:

.. code:: sh

   wget -c https://releases.linaro.org/components/toolchain/binaries/7.5-2019.12/arm-linux-gnueabihf/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf.tar.xz

Rozpakowujemy:

.. code:: sh

   tar xf gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf.tar.xz

Ścieżkę eksportujemy na czas trwania sesji terminala:

.. code:: sh

   export CC=`pwd`/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-

Testujemy czy działa:

.. code:: sh

   ${CC}gcc --version

Powinno pojawić się coś takiego:

.. code:: sh

   arm-linux-gnueabihf-gcc (Linaro GCC 7.5-2019.12) 7.5.0
   Copyright (C) 2017 Free Software Foundation, Inc.
   This is free software; see the source for copying conditions.  There is NO
   warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Przygotowujemy bootloader (U-Boot)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Klonujemy branch *v2019.04*. Uwaga: Jest to ostatnia wersja, dla której są potrzebne nam patche dla rewizji B3!

.. code:: sh

   git clone -b v2019.04 https://github.com/u-boot/u-boot --depth=1
   cd u-boot/

i aplikujemy patche:

.. code:: sh

   wget -c https://github.com/eewiki/u-boot-patches/raw/master/v2019.04/0001-omap4_common-uEnv.txt-bootz-n-fixes.patch
   patch -p1 < 0001-omap4_common-uEnv.txt-bootz-n-fixes.patch

W końcu konfigurujemy i budujemy:

.. code:: sh

   make ARCH=arm CROSS_COMPILE=${CC} distclean
   make ARCH=arm CROSS_COMPILE=${CC} omap4_panda_defconfig
   make ARCH=arm CROSS_COMPILE=${CC}

Jeżeli wszystko zbudowało się prawidłowo, to powinniśmy uzyskać przede wszystkim *MLO* i *u-boot.img*:

.. code:: sh

   $ ls -l | grep -e "MLO\|u-boot.img"
   -rw-rw-r--   1 marverix marverix   41860 mar 19 22:06 MLO
   -rw-rw-r--   1 marverix marverix  365136 mar 19 22:06 u-boot.img

Wracamy do naszego katalogu *pandaboard*:

.. code:: sh

   cd ..

Kernel
^^^^^^

Klonujemy repo:

.. code:: sh

   git clone https://github.com/RobertCNelson/armv7-multiplatform
   cd armv7-multiplatform/

Proponuję scheckoutować najnowszą wersję 4.xx. W moim wypadku było to *4.20.x*:

.. code:: sh

   git checkout origin/v4.20.x -b tmp

No i budujemy:

.. code:: sh

   ./build_kernel.sh

Jeżeli wszystko poszło w porządku, to pod koniec mniej-więcej powinno być coś takiego:

.. code:: sh

   -----------------------------
   Script Complete
   eewiki.net: [user@localhost:~$ export kernel_version=4.20.17-armv7-x15]
   -----------------------------

Kopiujemy to *export kernel_version=...* i wykonujemy:

.. code:: sh

   export kernel_version=4.20.17-armv7-x15

Natomiast w podkatalogu *deploy* powinniśmy zobaczyć pliki:

.. code:: sh

   $ ls -l deploy
   -rw-rw-r-- 1 marverix marverix  4806577 maj 22 13:20 4.20.17-armv7-x15-dtbs.tar.gz
   -rw-rw-r-- 1 marverix marverix 19001283 maj 22 13:20 4.20.17-armv7-x15-modules.tar.gz
   -rwxrwxr-x 1 marverix marverix  9433600 maj 22 13:19 4.20.17-armv7-x15.zImage

Wracamy do naszego katalogu *pandaboard*:

.. code:: sh

   cd ..

Rootfs
^^^^^^

Ściągamy minirootfs Alpine Linuxa dla architektury *armv7* (lub bardziej generycznej *armhf*). I chociaż najnowszy działa (w momencie jak to piszę, to jest to 3.13.5), to na końcu całego procesu potrafi się bardzo długo włączać, bo jakiś proces crashuje. Szczerze mówiąc nie spodziewałem się, żeby najnowsza wersja systemu operacyjnego działała na tym sprzęcie bez żadnego "ale". Natomiast Alpine Linux oficjalnie wspirało Pandę do +/- 2019 roku. A więc wersja 3.7.x, dokładniej 3.7.3. Tak więc takowej będę używał:

.. code:: sh

   wget -c https://dl-cdn.alpinelinux.org/alpine/v3.7/releases/armhf/alpine-minirootfs-3.7.3-armhf.tar.gz

Będzie nam też potrzebny "gotowy" obraz w tej samej wersji i architekturze. Można go rozpoznać po tym, że posiada człon "u-boot" w linku:

.. code:: sh

   wget -c https://dl-cdn.alpinelinux.org/alpine/v3.7/releases/armhf/alpine-uboot-3.7.3-armhf.tar.gz

| Minirootfs to naprawdę takie minimum minimum (w końcu ma niecałe 2MB!). Są  to najbardziej podstawowe komendy, ale brak jest obsługi jakichkolwiek usług (w tym DHCP czy SSH). Dlatego potrzebujemy paczek, które umożliwą nam pracę w normalnych warunkach. Możemy ściągać te paczki jedna po drugiej, a możemy skorzystać z folderu *apks*, który znajduje się w tym "gotowcu".
| Wypakowujemy zawartość pierwszej paczki do folderu *rootfs*:

.. code:: sh

   mkdir rootfs
   tar xf alpine-minirootfs-3.7.3-armhf.tar.gz -C rootfs

Wypakowujemy folder *apks*:

.. code:: sh

   tar xf alpine-uboot-3.7.3-armhf.tar.gz -C rootfs ./apks

A także podstawowe ustawienia:

.. code:: sh

   tar xf alpine-uboot-3.7.3-armhf.tar.gz ./alpine.apkovl.tar.gz
   tar xf alpine.apkovl.tar.gz -C rootfs/

Przygotowujemy kartę SD
^^^^^^^^^^^^^^^^^^^^^^^

Sprawdzamy jak się nazywa nasze urządzenie blokowe:

.. code:: sh

   $ lsblk
   NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
   sda           8:0    1  29,9G  0 disk 

I dla ułatwienia:

.. code:: sh

   export DISK=/dev/sda

Czyścimy kartę:

.. code:: sh

   sudo dd if=/dev/zero of=${DISK} bs=1M count=10

Instalujemy bootloader:

.. code:: sh

   sudo dd if=./u-boot/MLO of=${DISK} count=1 seek=1 bs=128k
   sudo dd if=./u-boot/u-boot.img of=${DISK} count=2 seek=1 bs=384k

Partycjonujemy:

.. code:: sh

   sudo sfdisk ${DISK} <<-EOF
   4M,,L,*
   EOF

A następnie formatujemy na *ext4*:

.. code:: sh

   sudo mkfs.ext4 -L rootfs ${DISK}1

Montujemy:

.. code:: sh

   export ROOTFS=/media/rootfs
   sudo mkdir -p ${ROOTFS}/
   sudo mount ${DISK}1 ${ROOTFS}/

Firmware WiFi
^^^^^^^^^^^^^

Po prostu klonujemy:

.. code:: sh

   git clone git://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git --depth=1

Kopiujemy rzeczy
^^^^^^^^^^^^^^^^

Rootfs:

.. code:: sh

   sudo cp -r rootfs/* ${ROOTFS}
   sync
   sudo chown root:root ${ROOTFS}/
   sudo chmod 755 ${ROOTFS}/

Dajemy odpowiednie uprawnienia *busybox*:

.. code:: sh

   sudo chmod 4755 ${ROOTFS}/bin/busybox

Tworzymy tymczasowego użytkownika *sheldon* z hasłem *bazinga*:

.. code:: sh

   sudo sh -c "echo 'sheldon:x:1000:1000:Sheldon Cooper:/tmp:/bin/ash' >> ${ROOTFS}/etc/passwd"
   sudo sh -c "echo 'sheldon:\$1\$bbt\$SY4ikXOUxJn9uf666cVtp.:0:0:99999:7:::' >> ${ROOTFS}/etc/shadow"
   sudo sh -c "echo 'sheldon:x:1000:sheldon' >> ${ROOTFS}/etc/group"

Enablujemy użytkownika root i zmieniamy mu hasło na *toor* (oczywiście później należy zmienić za pomocą *passwd*):

.. code:: sh

   sudo sed -i "1s/root:\!:/root:\$1\$bbt\$3YaV3qqIqN3RzpOd92eju0:/" ${ROOTFS}/etc/shadow

Tworzymy plik *eEnv.txt*:

.. code:: sh

   sudo mkdir -p ${ROOTFS}/boot
   sudo sh -c "echo 'uname_r=${kernel_version}' >> ${ROOTFS}/boot/uEnv.txt"
   sudo sh -c "echo 'dtb=omap4-panda-es-b3.dtb' >> ${ROOTFS}/boot/uEnv.txt"

Kernel i wszystko co z nim związane:

.. code:: sh

   sudo cp -v ./armv7-multiplatform/deploy/${kernel_version}.zImage ${ROOTFS}/boot/vmlinuz-${kernel_version}
   sudo mkdir -p ${ROOTFS}/boot/dtbs/${kernel_version}/
   sudo tar xfv ./armv7-multiplatform/deploy/${kernel_version}-dtbs.tar.gz -C ${ROOTFS}/boot/dtbs/${kernel_version}/
   sudo tar xfv ./armv7-multiplatform/deploy/${kernel_version}-modules.tar.gz -C ${ROOTFS}/

Firmware WiFi:

.. code:: sh

   sudo mkdir -p ${ROOTFS}/lib/firmware/ti-connectivity
   sudo cp -v ./linux-firmware/ti-connectivity/* ${ROOTFS}/lib/firmware/ti-connectivity

fstab:

.. code:: sh

   sudo sh -c "echo '/dev/mmcblk0p1  /  auto  remount,rw  0  1' >> ${ROOTFS}/etc/fstab"

Upewniamy się, że wszystko zostało zsynchronizowane:

.. code:: sh

   sync

Odmontowujemy:

.. code:: sh

   sudo umount ${ROOTFS}

Setup
^^^^^

| Odpinamy kartę, podpinamy HDMI, RJ45, klawiaturę i myszkę, no i kartę. Odpalamy. Jeżeli wszystko się udało, to powinniśmy zobaczyć terminal z zachętą do zalogowania. Logujemy się na sheldona.
| Teraz możemy się zmienić użytkownika na *root:*

.. code:: sh

   su root

Przemontowujemy:

.. code:: sh

   mount -t proc proc /proc
   mount -o remount,rw /

Instalujemy wszystkie paczki:

.. code:: sh

   apk add /apks/armhf/*.apk

| Nie przejmuj się warningami i errorami, że nie może znaleźć adresu URL. Wszystko dlatego, że serwer DHCP nie działa, więc nic dziwnego. Jeżeli natomiast dostaniesz błąd, że nie może wybrać jakiejś paczki, bo coś tam breaks, no to przenieś na chwilę psującą tą paczkę np. folder wyżej - tak żeby nie trzeba było instalować jej. Najbardziej nas interesuje wszystko co zaczyna się na *alpine*, *busybox* oraz *openrc*
| Rebootujemy maszynę.

.. code:: sh

   reboot

Tym razem powinniśmy mogli odrazu wbić się na roota (bez potrzeby najpierw logowania się na sheldona).

(Opcjonalnie) Jeżeli mamy podłączony kabel sieciowy, a ale diody nie świecą, to oznacza, że najprawdopodobniej moduł ethernet nie jest załadowany:

.. code:: sh

   modprobe -a smsc95xx

Odpalamy DHCP:

.. code:: sh

   rc-service networking start

Przechodzimy główny setup:

.. code:: sh

   setup-alpine

Aktualizujemy repozytorium:

.. code:: sh

   apk update
   apk upgrade

No i włączamy automatyczne odpalanie sieci i daemona ssh:

.. code:: sh

   rc-update add networking
   rc-update add sshd

Skończone!

Instalowanie paczek
^^^^^^^^^^^^^^^^^^^

Jeżeli chcemy zaintalować np. *nano* i Pythona 3 to wykonujemy:

.. code:: sh

   apk add nano python3

Gotowiec
--------

Jeżeli nie chce Ci się robić tego zgodnie z powyższą instrukcją (nie dziwię się), to możesz skorzystać z gotowca. Najważniejsze skompilowane pliki wrzuciłem na `OneDrive <https://1drv.ms/u/s!ApFPU1DG0Ozygrl04G3qjoN4cmLFQQ?e=fEXbe3>`__.

Wystarczy pobrać skompresowany backup (*alpine-3.7-250521.img.xz*) i następnie:

.. code:: sh

   cat alpine-3.7-250521.img.xz | unxz | sudo dd of=/dev/sdX

Gdzie *X* to oczywiście odpowiednia litera, zgodnie z tym co pokazuje *lsblk*.

Uwaga: Backup był robiony dla karty 4GB, więc jest to minimalny rozmiar na jaki można przywrócić obraz. Oczywiście może być większy. W takim wypadku po zakończonym procesie proponuję odpalić jakieś narzędzie do zarządania partycjami (np. *gparted*) i po prostu rozszerzyć partycję na całą wolną przestrzeń karty.

 
