Virtualmin? Nigdy więcej		
###############################
:date: 2021-07-06 22:32
:category: IT
:tags: it, komputery, oprogramowanie, serwery, software, vps
:slug: virtualmin-nigdy-wiecej
:status: published
:cover: images/2021/07/7ee65ed8e3a0-1.jpg
:attachments: images/2021/07/7ee65ed8e3a0-1.jpg

Virtualmin to  panel administracyjny o otwartym źródle (ale istnieje też płatna wersja Pro), który ma być alternatywą chociażby dla cPanel'u czy Plesk'a. Zainstalowałem go 5 lat temu na swoim VPS'ie. Na początku zaimponował mi możliwościami i mnogością opcji.

Panel ma wbudowane mega dużo funkcji, które pozwalają za skonfigurowanie i zarządzanie swoim serwerem. Ale po czasie ta mnogość zaczęła mnie przytłaczać. Dlaczego? Bo jest rzucona użytkownikowi na twarz. UI jest stary i toporny (co prawda jest "nowa" wersja, ale umówmy się, że to taki bardziej 2013 niż 2021). Nauka gdzie jest jaka opcja zajęło mi trochę czasu.

Do tego UI'a można się przyzwyczaić. Mój VPS ma 4 wirtualne rdzenie i 8GB RAM'u. Ktoś powie, że mało jak na dzisiejsze czasy, ale ja powiem, że mi to wystarcza. Mimo tego, było gołym okiem widać jak Virtualmin kocha zasoby. Nic dziwnego - w końcu ten system robi tak dużo. Ale ponownie - jeżeli ktoś np. chce znaleźć darmowy system dla swojej startującej firmy hostingowej... no to ok. Podejrzewam, że będzie miał sprzęt lepszy niż mój.

Nie mam na to dowodu, ale nie grzebałem w konfiguracji manualnie. Wszystkimi konfiguracjami Apache'a, MySQL'a, PHP'a itp zarządzał on. Ale gdy odpalałem np. bloga mojej żony, to "strona potrafiła myśleć" najpierw 10 sekund zanim cokolwiek się otworzyło. Na wykresach Virtualmin'a było ewidentnie widać jakieś dziwne piki zużycia CPU. Po co? Dlaczego? Jak to zdebugować? Nie wiem. Wiem jedno - na moim hostingu na Linuxpl.com, gdzie nie miałem nawet pół rdzenia procesora, ta sama strona po prostu śmigała.

Ostatnio robiłem stronę radiodroga.net, i szukałem jakieś prostego panelu lub narzędzia, który szybko skonfiguruje za mnie Ngnix'a, PHP'a i inne takie. I tak natrafiłem w sieci na CLI `WordOps <https://wordops.net/>`__. Zainstalowaliśmy. Instalacja i postawienie działającego WordPress'a trwało 5 minut, a może nawet mniej. Byłem w szoku. Szybko, bez zbędnego UI'a, który zżera zasoby. No i twórcy zarzekają się, że projekt jest "security-oriented".

Postanowiłem spróbować u mnie. Zgodnie z instrukcją na stronie WordOps o migracji z innych serwerów (ale nie systemów!) zrobiłem backup baz WordPress'ów. Skopiowałem pliki. Sprawdziłem 5 razy czy wszystko mam i postanowiłem odinstalować Virtualmina... Na stronie panelu jest "jednolinijkowiec", który (teoretycznie) robi deinstalację. Spróbowałem.

Gdy skrypt skończył, okazało się, że tak, odinstalował wszystkie swoje paczki, ale syf konfiguracyjny jaki po sobie pozostawił to była tragedia. Wszyscy użytkownicy i grupy? Zostawione (nawet "webmin" i "virtualmin"!). Usługi? Część wyłączona, a część nie. Konfiguracje usług? Zostawione. Efekt był taki, że WordOps nie mógł dobić się do MySQL'a (MariaDB).  Robiłem *apt purge*, szukałem na necie how-to, próbowałem wszystkiego. Nic. Jeden problem rozwiązywałem, pojawiał się kolejny i kolejny.

Usiadłem do tego o 21, bo miałem nadzieję, że w godzinę się uwinę. Od konsoli SSH do mojego VPS'a odszedłem zrezygnowany i załamany o 00:30. Odinstalowanie Virtualmin'a rozpierniczyło mojego VPS'a. Wyjście było jedno... format. Na szczęście w panelu klienta OVH to 3 kliknięcia.

Jako programista, **oprogramowanie, które nie potrafi posprzątać po sobie, jest nic warte**. Jeżeli umiesz napisać instalator, to napisz kuźwa porządny deinstalator. Zwłaszcza jeżeli chodzi o coś, co ma pracować na serwerach, które są gdzieś hen daleko i nie masz do niego fizycznego dostępu.

Moją przygodę z Virtualmin'em mogę porównać chyba jak do jakiegoś toksycznego związku. Gdy masz dość i ogłaszasz, że czas się rozejść, to druga połowa robi scenę i za karę demoluje ci mieszkanie.

Nigdy więcej. Nie polecam.
