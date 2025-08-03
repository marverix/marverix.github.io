Hurricane Electric Free DNS - Moje odkrycie roku		
#######################################################
:date: 2021-07-07 20:20
:category: IT
:tags: DNS, internet, it, komputery, odkrycia, serwery, usługi
:slug: hurricane-electric-free-dns-moje-odkrycie-roku
:status: published
:cover: images/2021/07/he-cover.png
:attachments: images/2021/07/2021-07-07_18-26.png, images/2021/07/2021-07-07_19-52.png, images/2021/07/2021-07-07_20-00.png, images/2021/07/he-cover.png, images/2021/07/2021-07-07_19-46.png, images/2021/07/2021-07-07_19-35.png

W trakcie formatu mojego VPS'a (o którym `pisałem w poprzednim poście <https://marek.sierocinscy.pl/2021/07/06/virtualmin-nigdy-wiecej/>`__) dotarło do mnie, że WordOps nie ogarnia DNS'ów. Nie był to dla mnie problem, bo korzystałem kiedyś z `MaraDNS <https://maradns.samiam.org/>`__, który wg mnie jest o niebo bardziej czytelny i lepszy od rozpowszechnionego i antycznego Bind9 (mogę w sumie kiedyś o tym napisać więcej). Ale nie chciałem chyba się znowu pchać w utrzymywanie serwera DNS na własnym VPS'ie. Co prawda były tego zalety, ale nie po to przenosiłem się na WordOps, żeby teraz znowu dokładać sobie manualnej roboty. Przypomniałem sobie, że lata temu czytałem gdzieś, że ktoś gdzieś mówił, że amerykański dostawca Hurricane Electric, udostępnia darmowy serwer DNS. Wtedy z tego zrezygnowałem, bo wydawało mi się, że muszę przecież mieć serwer DNS lokalnie, ale dzisiaj dotarło do mnie, że no nie muszę. Postanowiłem więc przyjrzeć się niemu bliżej.

Na pierwszy rzut oka
--------------------

`Strona Hurricane Electric <http://he.net/>`__ jest dość... niepozorna. Kojarzy się raczej z jakąś stroną nie zmienianą od 2001 roku.

|Screenshot storny głównej he.net|

Link do darmowego serwera DNS to po prawej "Free DNS" (zaznaczyłem na czerwono). Co ciekawe każda podstrona jest inna pod względem linków. Nawigacja po systemie jest dla mnie dość wymagająca, ale chyba powoli się przyzyczajam (no i porobiłem sobie zakładki, do tego czego potrzebuje ;) ).

Polecam sobie poczytać "ficzery" jakie wspomniana usługa posiada:

-  Wsparcie zarówno dla zapytań przez IPv4 jak i natywnego IPv6.
-  Obsługa rekordów A, AAAA, ALIAS, CNAME, CAA, MX, NS, TXT, SRV, SSHFP, SPF, RP, NAPTR, HINFO, LOC i PTR
-  Jakiś tam "sprytny tryb" do ogarniania odwrotnej stref (reverse zones)
-  Wsparcie dla "slavów".
-  Wiele formatów odwrotnych stref: Standard, RFC 4183, RFC 2317, DeGroot.
-  Odpytywanie geograficznie najbliższego serwera HE.
-  Sprawdzanie poprawności delegacji stref (w obie strony).
-  Podstawowe sprawdzanie składni rekordów.
-  Wiele domen dla jednego konta.

Jak na darmową obsługę, to muszę powiedzieć, że jestem w szoku. W dodatku 0 reklam na stronie.

Konto
-----

Do korzystania z konta trzeba zarejestrowć darmowe konto. Niestety formularz rejestracyjny jest dość długi (trzeba podać wszystkie dane teleadresowe).

|Widok prezentujący formularz rejestracji na he.net|

Plusem jest to, że jedno konto gwarantuje nam dostęp do wszystkich usług HE.

Na pochwałę zasługuje możliwość włączenia uwierzytelnienia wieloskładnikowego (co z resztą czym prędzej uczyniłem).

Minusem jest to, że do każdej usługi musimy logować się osobno. Jest to zapewne związane z bezpieczeństwem. Podejrzewam, że twórcy używają ciasteczek do trzymania sesji, i nie chcieli używać wildcarda dla wszystkich subdomen \*.he.net (co z resztą jest mądrym posunięciem). A tak to już jest, że najczęściej się wybiera: albo UX, albo security, albo ficzery.

Usługa
------

UI jest ponownie skromny, ale czytelny. Po lewej mamy to co zapewne najbardziej zainteresuje, a więc "Add a new domain". Po kliknięciu pojawia się modal z polem do wpisania nazwy domeny. Przejście dalej spowoduje nie tylko dodanie domeny do naszej listy, ale także sprawdzenie czy na pewno domeny są skierowane na odpowiednie serwery he.net.

|Widok prezentujący listę domen na dns.he.net|

Po dodaniu pojawia nam się widok szczegółów domeny (ten sam jak byśmy kliknęli daną domenę na liście). Ponownie: widok jest prosty i czytelny. Przyciski w wierszu tuż nad tabelką pozwalają w bardzo szybko dodać nowe rekordy, których potrzebujemy. Skonfigurowanie wszystkich moich domen zajęło mi może 10 minut. Zero bawienia się z dokumentacją Bind9, itp.

|Widok stonry dns.he.net, który prezentuje szczegóły domeny marverix.blog|

Działa
------

`DNSPerf <https://www.dnsperf.com/dns-provider/he-net>`__ dał he.net 41/71 pozycję w rankingu. Czy to daleko? Cóż, pewnie do takich gigantów jak Google czy CloudFlare. Ale za 0zł otrzymujemy dostęp do usługi, która z Europy odpowiada w 30ms (z mojego komputera 35ms), uptime 99.97% i prosty UI, bez reklam i pierdyliardem okienek do zamknięcia. Jasne, mógłbym pewnie zapłacić za utrzymanie na płatnym serwerze, ale czy ktoś zauważy różnicę? 35ms to naprawdę dla mnie niewiele (zwłaszcza, że DNSy są później cachowane lokalnie, więc to tylko za pierwszym razem dodatkowy czas).

|Zrzut ze strony DNSPerf przedstawiającą wyniki testów wydajności dla he.net|

Najfajniejsze dla mnie jest to, że to po prostu działa. Koniec z utrzymywaniem serwera u siebie. Koniec z bawieniem się w dodatkowe serwery mirrorowe.  Mi to totalnie wystarcza i nie zapowiada się, żebym w najbliższych latach zmieniał usługodawcę :)

.. |Screenshot storny głównej he.net| image:: {static}/images/2021/07/2021-07-07_18-26.png
   :class: alignnone wp-image-232 size-large
   :width: 660px
   :height: 529px
   :target: images/2021/07/2021-07-07_18-26.png
.. |Widok prezentujący formularz rejestracji na he.net| image:: {static}/images/2021/07/2021-07-07_19-35.png
   :class: alignnone wp-image-233 size-large
   :width: 660px
   :height: 555px
   :target: images/2021/07/2021-07-07_19-35.png
.. |Widok prezentujący listę domen na dns.he.net| image:: {static}/images/2021/07/2021-07-07_19-46.png
   :class: alignnone size-large wp-image-234
   :width: 660px
   :height: 469px
   :target: images/2021/07/2021-07-07_19-46.png
.. |Widok stonry dns.he.net, który prezentuje szczegóły domeny marverix.blog| image:: {static}/images/2021/07/2021-07-07_19-52.png
   :class: alignnone size-large wp-image-235
   :width: 660px
   :height: 433px
   :target: images/2021/07/2021-07-07_19-52.png
.. |Zrzut ze strony DNSPerf przedstawiającą wyniki testów wydajności dla he.net| image:: {static}/images/2021/07/2021-07-07_20-00.png
   :class: alignnone size-large wp-image-236
   :width: 660px
   :height: 725px
   :target: images/2021/07/2021-07-07_20-00.png
