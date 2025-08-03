Niechciany pracownik sklepu w twojej przeglądarce		
########################################################
:date: 2021-06-06 14:38
:category: IT
:tags: firefox, it, komp, reklamy, serviceworkers, webdevelopment
:slug: niechciany-pracownik-sklepu-w-twojej-przegladarce
:status: published
:cover: images/2021/06/5ca9gj.jpg
:attachments: images/2021/06/5ca9gj.jpg, images/2021/06/firefox-sw-plugin-2.png, images/2021/06/firefox-sw-disabled.png, images/2021/06/osmy-pasazer-nostromo.jpeg, images/2021/06/firefox-sw-plugin-1.png, images/2021/06/morele-powiadomienie-reklama.png, images/2021/06/morele-sw.png, images/2021/06/firefox-sw-webnotification-disabled.png

Ostatnio chciałem sprawdzić coś na sklepie Morele.net, i wyskoczyło, mi chyba wszystkim znane, powiadomienie, że sklep chce pozwolenia na wyświetlanie powiadomień. Spiesząc się kliknąłem na "Zezwól" (zwyczajny miss-click). I zaczęło się... Było to jakoś tydzień temu, i od tamtego momentu, prawie przy każdym włączeniu przeglądarki,  oraz w trakcie zwykłego korzystania - np. oglądania YouTube'a, wyświetlają mi się powiadomienia o takie:

|image1|

Gdyby nie to, że pisałem Omódlmy Net, to w życiu nie wiedziałbym gdzie szukać i jak to wyłączyć. Omódlmy Net to aplikacja typu PWA. Bez wdawania się w szczegóły, to taka aplikacja musi spełniać pewne wymagania. Po spełnieniu tych wymagań, normalna "strona internetowa" staje się "aplikacją". Jednym z tych wymagań jest posiadanie i zarejestrowanie Service Workera.

Niechciany pasażer
------------------

Z założenia Service Worker (w dosłownym tłumaczeniu "pracownik serwisu") ma pomagać w komunikacji między użytkownikiem (tobą i mną), a serwerem. To trochę jak doradca finansowy. Możesz sam rozmawiać bezpośrednio z bankiem i próbować wszystko samemu załatwiać, ale wtedy musisz wiedzieć o której bank jest otwarty, z kim rozmawiać o czym, kiedy są godziny sesji itp... A możesz skorzystać z usług wspomnianego doradcy. Wtedy jemu zlecasz co i jak, a to już w jego gestii zajęcie się wspomnianymi wczoraj kwestiami.

W dużym uproszczeniu po to zostały stworzone SW. Np. YouTube działa szybciej dzięki tej technologii. Co więcej, potrafi rozpoznać czy odłączył Ci się Internet (albo masz niestabilne łącze) i odpowiednio działać, aby nie pojawił Ci się jakiś nieznany komunikat błędu itp. To wszystko zasługa właśnie SW.

(Nie)Stety, zostało to pomyślane tak, że SW ma być "transparentny" zarówno dla użytkownika, jak i serwera. Wszystko ma działać niezależnie czy on jest, czy go nie ma. W związku z tym jego rejestracja (instalacja) i aktywacja jest niewidzialna. Po prostu wchodząc na stronę internetową, która deklaruje pod spodem, że używa SW, automatycznie (bez pytania nikogo o zdanie) następuje instalacja. Nieważne, że być może nigdy więcej na tą stronę nie wejdziesz. Stało się. Niczym ósmy pasażer Nostromo.

|image2|

No i jest jeden mały szkopuł... Ci pracownicy mogą pracować w tle. A skoro mogą pracować w tle, i np. odbierać informacje o reklamach, i w dodatku mają pozwolenie na wyświetlanie powiadomień... No to przepis na upierdliwe reklamy gotowy.

Co mogę zrobić?
---------------

Otwieramy listę
~~~~~~~~~~~~~~~

Ku mojemu zdziwieniu, zarówno Firefox i Chrome nie dają jawnego i łatwego sposobu na zarządzanie pracownikami. W Firefoxie trzeba wpisać w adres przeglądarki *about:serviceworkers* i wyświetli się lista wszystkich zarejestrowanych SW. U mnie to 171...

W Chromie to adres *chrome://serviceworker-internals*

Wyrejestruj
~~~~~~~~~~~

Jeżeli wiemy jaki to sklep, to połowa sukcesu. U mnie wspomniane *Morele*:

|image3|

I klikamy przycisk **Wyrejestruj**.

Natomiast jeżeli nie wiemy, to szukamy tego, który ma coś wpisane w polu *pushEndpoint*. To z tego źródła pracownik dostaje informacje o "nowościach" (reklamach).

Jest jeszcze jeden ostatni problem. To wróci. Usunęliśmy pasażera, ale po wejściu na daną stronę (w tym wypadku www.morele.net), SW zostanie ponownie zarejestrowany.

Zapobiegać?
~~~~~~~~~~~

Naturalnym tokiem myślenia jest zatem "ok, no to trzeba zablokować to rejestrowanie". Tak, ale jak wspomniałem wcześniej - możemy też na tym stracić. Na chociażby płynności działania takich usług jak YouTube czy GMail.  Niestety (przynajmniej na Firefoxie) nie ma możliwości wybiórczego blokowania SW.

Opcja 1: Ukryte ustawienia - wyłączamy całkowicie
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

W Firefoxie wchodzimy na adres *about:config* i klikamy przycisk *Akceptuję ryzyko*. Teraz w polu wyszukiwania wpisujemy *dom.serviceWorkers.enabled*. Po prawej klikamy w strzałki. Zrobione.

|image4|

Opcja 2: Ukryte ustawienia - wyłączamy tylko powiadomienia
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ta opcja powoduje, że SW będą nadal włączone, ale będą mogły wyświetlać powiadomienia, wyłącznie wtedy, kiedy będziemy na danej stronie. Czyli Morele będzie mogło wyświetlać powiadomienia (reklamy) tylko wtedy, kiedy będę na ich sklepie.

W Firefoxie wchodzimy na adres *about:config* i klikamy przycisk *Akceptuję ryzyko*. Teraz w polu wyszukiwania wpisujemy *dom.webnotifications.serviceworker.enabled*. Po prawej klikamy w strzałki. Zrobione.

|image5|

Opcja 3: Instalujemy wtyczkę
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Wchodzimy na https://addons.mozilla.org/pl/firefox/addon/block-service-workers/ i klikamy przycisk *Dodaj do Firefox*.

|image6|

A następnie potwierdzamy przez kliknięcie *Dodaj*.

|image7|

Zrobione.

 

.. |image1| image:: {static}/images/2021/06/morele-powiadomienie-reklama.png
   :class: alignnone size-full wp-image-202
   :width: 433px
   :height: 312px
   :target: images/2021/06/morele-powiadomienie-reklama.png
.. |image2| image:: {static}/images/2021/06/osmy-pasazer-nostromo.jpeg
   :class: alignnone size-full wp-image-203
   :width: 474px
   :height: 296px
   :target: images/2021/06/osmy-pasazer-nostromo.jpeg
.. |image3| image:: {static}/images/2021/06/morele-sw.png
   :class: alignnone size-large wp-image-204
   :width: 660px
   :height: 129px
   :target: images/2021/06/morele-sw.png
.. |image4| image:: {static}/images/2021/06/firefox-sw-disabled.png
   :class: alignnone size-large wp-image-205
   :width: 660px
   :height: 131px
   :target: images/2021/06/firefox-sw-disabled.png
.. |image5| image:: {static}/images/2021/06/firefox-sw-webnotification-disabled.png
   :class: alignnone size-large wp-image-206
   :width: 660px
   :height: 128px
   :target: images/2021/06/firefox-sw-webnotification-disabled.png
.. |image6| image:: {static}/images/2021/06/firefox-sw-plugin-1.png
   :class: alignnone size-large wp-image-207
   :width: 660px
   :height: 381px
   :target: images/2021/06/firefox-sw-plugin-1.png
.. |image7| image:: {static}/images/2021/06/firefox-sw-plugin-2.png
   :class: alignnone size-full wp-image-208
   :width: 419px
   :height: 220px
   :target: images/2021/06/firefox-sw-plugin-2.png
