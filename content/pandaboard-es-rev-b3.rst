Pandaboard ES Rev B3		
###########################
:date: 2021-05-23 22:12
:category: IT
:tags: arm, armhf, cortex-a9, it, komputery, pandaboard
:slug: pandaboard-es-rev-b3
:status: published
:cover: images/2021/05/pandaboard-es-b3-3.jpg
:attachments: images/2021/05/pandaboard-es-b3-2.jpg, images/2021/05/pandaboard-es-b3-1.jpg, images/2021/05/pandaboard-es-b3-3.jpg

Ze względu na zmiany w mojej firmie, dostałem do moich rąk trochę szrotu. Mianowicie Pandaboard ES Rev B3.

[gallery ids="147,146,145"]

Jest to minikomputer oczywiście na procesorze ARM, a dokładniej OMAP4460. Był to jeden z wielu minikomputerów, które wyrosły niczym grzyby po deszczu, zaraz po ogłoszeniu Raspberry Pi. No bo każdy chciał pokazać, że umie lepiej, a co ważniejsze - ugryźć chociaż kawałek tortu.

Krótko o specyfikacji
---------------------

Sprzęt został wydany w 2010 roku, a więc 11 lat temu. Pierwsze rewizje wyposażono w 2 rdzeniowy Cortex-A9 o taktowaniu 1GHz. Wspierany był przez 1GB DDR2. W dodatku wbudowane została karta WLAN i BT, Port Ethernet, 2x USB 2.0 + chyba jeszcze 2 na konektorach, no i czytnik kart SDHC (max 32GB). Gwóździem programu miało być GPU z hardwarowym wsparciem filmów FullHD (30fps). Dzisiaj może to szału nie robi, ale wtedy? Pamiętam, jak te maszynki pojawiły się w firmie. Akceleracja sprzętowa FHD na takim  małym sprzęcie to naprawdę robiła wrażenie.

Rewizji było więcej, a ostateczna nazywała się właśnie ES. Zamiast początkowego OMAP4430, użyto 4460 (o którym wspomniałem na samym początku). Miał on taktowanie 200Mhz większe, a więc 2x 1.2Ghz.

|image1|

Pandaboard szczycił się mnogością konektorów na mobo. Popatrzcie tylko na diagram powyżej. Do kamerki, 2x dla rozszerzeń (w tym GPIO, UART, I2C), LCD, JTAG, no i debugowanie przez wbudowny port RS-232. Czego chcieć więcej?

Jeżeli siedzisz trochę w IT (a zwłaszcza w minikomputerach), możesz się zastanawiać "Skoro to był taki fajny sprzęt, to dlaczego nigdy o nim nie słyszałem/am?". I jest to bardzo dobre pytanie. Myślę, że powodów jest wiele.

The good, the bad and the ugly
------------------------------

Rozmiary
~~~~~~~~

Czy płytka jest duża? No... nie. 10cm na 11cm to nie aż tak dużo przecież. Ale nie jest też tak mała jak malinka. A moim zdaniem, w sukcesie malinki ogromną rolę odegrała kompaktowość. Płyta po zamknięciu w pudełko spokojnie mieści się w kieszeni nastolatka. A Pandaboard? No właśnie. Jest taki... pokraczny. Ni to mały, ni to duży. W dodatku port ethernet jest portem combo z dwoma USB poniżej. Czyli sam ten element, ma 3,3cm wysokości. Do tego producenci chcieli dobrze... i dokleili na stałe gumowe nóżki pod spód płyty. Nóżki mają 7mm. Czyli cała płyta ma już 4cm wysokości.

Z 2 lata temu projektowałem obudowę do tej płytki (żeby wydrukować na drukarce 3D). Skończyłem na wymiarach 12x12x4. A to trzeba było pamiętać o karcie SD co wystaje, a to o porcie COM... Najgorsze było to, że pudełko miało bardzo dużo niezagospodarowanego miejsca. Zarówno pod, jak i nad i po bokach płytki. Myślę, że nie skłamię, gdy powiem, że 80% pudełka to była wolna przestrzeń.

Zasilanie
~~~~~~~~~

Pandaboard jest zasilany za pomocą zasilacza zakończonego popularnym "bolcem". Dołączany jest zasilacz 5V 4A. Tak, 4A. Co prawda z moich testów panda nie zjadała więcej niż 8.8W z gniazdka, ale zapewne są one niepełne, bo (jak zaraz się dowiesz) nie można używać w pełni wbudowanego GPU. Czy zatem nie można komputerka zasilić za pomocą USB (ponownie - jak w malince)? Tak, można. Manual podaje, że można zasilić za pomocą USB OTG. Ale...

USB OTG to port USB mini. Ja wiem, że mogę sie czepiać, ale dlaczego USB mini? Nie micro? W 2011 każdy miał kabelek i ładowarkę USB micro. A z tego co kojarzę, to przejściówki OTG przychodziły właśnie w formie USB micro - USB A, a nie USB mini - USB A. Jeszcze rozumiem, gdyby producent dodawał taki kabelek w zestawie. Ale nie - dostawało się tylko pudełko, płytkę i zasilacz.

Załóżmy, że jednak port USB mini to nie problem. Czeka nas natomiast kolejny zawód. Nawet jeżeli jesteśmy w posiadaniu ładowarki USB 5V 4A to panda będzie działać... wolniej. Tak, wolniej. Otóż wg manuala gniazdko USB OTG jak i normalne gniazdko zasilania idą przez układ, który hardwarowo steruje mocą procesora. Nie wiem o jakim spadku mocy mówimy (jeszcze nie robiłem testów), ale no nie jest to wesoła wiadomość.

Sterowniki
~~~~~~~~~~

Pamiętasz jak pisałem, że panda ma układ graficzny wspierający sprzętową akceleracje zarówno filmów FullHD (H.264) jak i grafiki 3D (OpenGL)? Tak... nigdy nie zdołałem zobaczyć tego w akcji. Bo widzisz, producent wybrał układ PowerVR SGX540, który wspiera OpenGL ES 2.0, OpenGL ES 1.1, OpenVG 1.1 i EGL 1.3. Super. Tylko że... producent wspomnianego układu nie otworzył sterowników. A więc - nie ma do tego dostępnych sterowników. Wypuszczono 1 paczkę z Ubuntu 12.04, gdzie były dedykowane sterowniki wyłącznie dla tego systemu operacyjnego, oraz jedną paczkę z Androidem 4.4 (tak, można było na tym odpalić Androida). Co więcej, producent SGX540 nie udostępnił nawet dokumentacji, żeby ktoś mógł sobie sam napisać sterowniki.

Także kupujący pandusię w momencie zakupu byli na przegranej pozycji. Minikomputer, który na tamte czasy zdawał się wręcz idealny jako komputer pod TV... tracił praktycznie największego asa w rękawie. Bo softwarowe dekodowanie filmów na tym procesorze, uwierz mi, delikatnie mówiąc - działa słabo.

Oczywiście byli odważni, którzy próbowali to obejść, ale z tego co wiem, wszystkie (2) inicjatywy padły jeszcze w 2012 roku.

Wsparcie
~~~~~~~~

Ja nie zliczę ile razy podchodziłem w pracy do tematu tych płytek. Nie lubię gdy sprzęt leży nieużywany. Mierzwiło mnie, że w 4 pudełkach leżą 4 komputery, praktycznie nigdy nie używane. I niszczeją. Ale ile razy siadałem do tematu - przegrywałem. Nie jestem specem od komputerów na bazie ARM. Ponieważ te komputery rządzą się swoimi prawami. Nie mają BIOSu czy UEFI. Zazwyczaj wszystko sprowadza się do czytania dokumentacji producenta, i jak on sobie wymyślił, że jaka zworka musi być w jakiej pozycji, i na którym bajcie na karcie SD (lub pendrivie) ma rozpoczynać się bootloader. I nie daj Boże, jeżeli nie wiesz jakie dokładnie masz kości pamięci.

Z mojego doświadczenia, bez wsparcia odpalenie czegokolwiek na tym sprzęcie graniczyło z cudem. Nie mówię wyłącznie o wsparciu producenta, ale przede wszystkim community.  A Panda miała dość "małą" rzeszę fanów. Dolicz jeszcze wspomniane problemy powyżej i masz przepis na gwarantowany sukces. Myślę, że dużo się skłamię, jeżeli stwiedzę, że panda prawdziwego community nie miała, a większość linuxów usunęła pandaboarda z listy wspieranych platform do 2017 roku.

Rewizje
~~~~~~~

Możesz spytać "Marek, ale jak to - chcesz mi powiedzieć, że producent nie udostępniał obrazu Ubuntu na swojej stronie?". Tak, udostępniał... dla pierwszych 2 rewizji. A one nie były ze sobą kompatybilne. Obraz dla rewizji A3 nie działał dla rewizji B3. I to było dla mnie największym mindfuckiem. Jak można namieszać tak bardzo we własnym ekosystemie. Nie zliczę ile razy miałem sytuację, że już znalazłem instrukcję jak odpalić Ubuntu ze sterownikami GPU (!!!), ale... dla pierwszej wersji pandy. Nie ES Rev B3 (czyli ostatniej).

Możesz zatem spytać "Ale to była, aż taka duża różnica? Nie wystarczyło gdzieś zamienić A na B i już?". Pandaboard ma CPU, RAM i GPU na jednym kawałku krzemu. Czyli jak w rewisji ES B3 producent postawnowił użyć kości Elpida, to cały krzem był inny. A co za tym idzie adresy w pamięci. Do dziś, jak chcesz bootloader (u-boot'a) dla ES B3, to najpierw musisz ściągnąć osobno źródła u-boot'a, i później osobno patche dla kości Elpida. No i na końcu zbudować to ze źródła.

Ciepełko
~~~~~~~~

Jestem starym PCtowcem, więc mam wyrobione zdanie o Intel, AMD, NVIDIA czy nawet zapomnianej już VIA. Ale rynek ARM to dla mnie trochę czarna magia. Ciężko mi więc wypowiadać się na temat procesora OMAP4460. Wiem jedno: grzeje się. Oj, grzeje. Po zakończenu aktualizacji Ubuntu palca na krzemie nie położysz. No, tzn. położysz ale bardzo szybko zdejmiesz ;) I to jest chyba dla mnie największe zdziwienie - dlaczego producent, nie zamontował żadnego radiatora fabrycznie? Ja kupiłem na znanym serwisie (już nie) aukcyjnym  kilka aluminiowych radiatorów + klej termoprzewodzący. Ale mimo tego, procesor bez problemu osiaga 70 stopni.

Podsumowanie
------------

Tak więc nie dziwie się, że pandaboardy nie stały się hitem. A ile one w ogóle kosztowały? Z informacji, które znalazłem, w 2010 roku $174. Po uwzględnieniu inflacji, dzisiejsze $214. Revolut pokazuje mi 798,85zł. Dla porównania Raspberry Pi 4 z 4GB RAM kosztuje dzisiaj ok. 290zł.  Jest różnica, prawda?

Nie mniej, skoro mam takowe w rączkach, postaram się je jakoś wykorzystać.

W następnym poście: instalowanie Alpine Linux na Pandaboard ES Rev B3! :)

 

.. |image1| image:: https://upload.wikimedia.org/wikipedia/commons/0/07/PandaBoard_described.png
   :class: alignnone
   :width: 640px
   :height: 500px
   :target: https://upload.wikimedia.org/wikipedia/commons/0/07/PandaBoard_described.png
