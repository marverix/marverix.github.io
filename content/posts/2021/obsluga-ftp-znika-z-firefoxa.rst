Obsługa FTP znika z Firefoxa		
###################################
:date: 2021-05-28 20:10
:category: IT
:tags: alpine, firefox, ftp, internet, it, komputery, mozilla, software
:slug: obsluga-ftp-znika-z-firefoxa
:status: published
:cover: images/2021/05/firefox-nie-lubi-ftp.png
:attachments: images/2021/05/firefox-nie-umie-w-ftp.png, images/2021/05/firefox-wlacz-ftp.png, images/2021/05/firefox-nie-lubi-ftp.png

W trakcie, gdy pracowałem nad `postawieniem Alpine Linux na Pandaboardzie <https://marek.sierocinscy.pl/2021/05/25/alpine-linux-na-pandaboard-es-rev-b3/>`__, potrzebowałem szybko pobrać kilka plików z serwera `FTP <https://pl.wikipedia.org/wiki/Protok%C3%B3%C5%82_transferu_plik%C3%B3w>`__ polskiego mirrora dla tejże dystrybucji linuxa. Wtem pojawiło się takie onkienko:

|image1|

Myślę sobie "O co chodzi?", przecież Firefox zawsze pięknie listował zawartość serwera FTP pozwalając na łatwe przeglądanie i pobieranie plików. Po krótkich poszukiwaniach dowiedziałem się, że od wersji 88 przeglądarki, obsługa FTP nadal jest wbudowana, ale domyślnie wyłączona. Natomiast Mozilla na swoim blogu `poinformowała, że od wersji 90 zniknie całkowicie <https://blog.mozilla.org/addons/2021/04/15/built-in-ftp-implementation-to-be-removed-in-firefox-90/>`__.

Wydawca tłumaczy się, że FTP jest już bardzo przestarzałą technologią i chodzi o bezpieczeństwo użytkowników.

No i ok. FTP jest już mega stare (starsze chyba od wszystkich, którzy czytają tego bloga - pierwsze wydanie w 1971 roku). Ale nadal używamy bardzo dużo starych i niebezpiecznych technologii. Chociażby SMSy. Wiadomości są nieszyfrowane. Czyli posiadając radio umożliwiające nasłuchiwanie na częstotliwościach 2G i 3G (bo zakładam, że nadal część ludzi nie ma komórek z 4G, nie mówiąc "rakotwórczym" o 5G) każdy użytkownik jest w stanie przeczytać wszystkie wiadomości, jakie "lecą" do/z komórek wokół niego. Ale jakoś nadal używamy SMSów.

Moim zdaniem Mozilla po prostu szukała argumentu jak pozbyć się z kodu niewygodnej funkcjonalności, której nie chce im się już wspierać (i tym samym łatać jej dziur). Co z resztą pokrywałoby się z "bezpieczeństwem użytkowników" o którym mówią.

Dobra wiadomość? Dla przeciętnego użytkownika nic się nie zmieni. Jeszcze nie widziałem, żeby jakiś zwykły użytkownik szukał czegoś na serwerach lustrzanych. Raczej wszyscy aktualnie wystawiają wszystko przez HTTP. A że HTTP już też jest "be", to zdecydowana większość ruchu sieciowego leci już przez HTTPS. A tzw. power userzy? No cóż, oni umieją doinstalować sobie i używać zewnętrznego klienta FTP takiego jak `FileZilla <https://filezilla-project.org/>`__ czy `WinSCP <https://winscp.net/eng/index.php>`__.

A, no i ponieważ w wersji 88 i 89 ta funkcja jeszcze jest wbudowana, to wystarczy wejść w *about:config*, poszukać właściwości *network.ftp.enabled* i przestawić na *true*.

|image2|

Ja tak zrobiłem i jeszcze przez dwie wersje zrobię na złość Mozilli :D

.. |image1| image:: {static}/images/2021/05/firefox-nie-umie-w-ftp.png
   :class: alignnone wp-image-169 size-full
   :width: 741px
   :height: 322px
   :target: images/2021/05/firefox-nie-umie-w-ftp.png
.. |image2| image:: {static}/images/2021/05/firefox-wlacz-ftp.png
   :class: alignnone wp-image-170 size-full
   :width: 1267px
   :height: 461px
   :target: images/2021/05/firefox-wlacz-ftp.png
