Title: gah - GitHub Releases app installer
Date: 2025-09-09 17:03
Category: IT
Tags: bash, skrypt, programowanie, github
Cover: images/2025/08/gah.png

Strasznie nie lubię robić powtarzających się rzeczy, ale takich no... głupich.
Co raz więcej aplikacji w formie binarek można znaleźć na GitHubie, a dokładniej w Release'ach. Nic dziwnego - devi tworzą opensource'owe oprogramowanie, udostępniają je na GitHubie, w zamian otrzymują za darmo dostęp do pipeline'ów i maszyn GitHub'a, co pozwala na zautomatyzowanie całego CI/CD.
Dzięki temu binarki apek trafiają do GitHub Release'ów repo gotowe do pobrania pod właściwą platformę. No właśnie... za każdym razem jak chciałem pobrać sobie aplikację, którą potrzebowałem, ogólnie rzecz biorąc kończyło się to mniej więcej tym samym flow:

1. Idź do repo
2. Otwórz Releases
3. Otwórz zakładkę "Assets" najwnoszego Release'u
4. I teraz weź się przebij przez całą listę (czasami naprawdę bardzo długą!) artefaktów budowania, aby znaleźć tą jedną właściwą paczkę pod mojego Linuxa i moją architekturę procesora.
5. Pobiersz znalezisko
6. Wypakuj
7. Wrzuć do `~/.local/bin`
8. Zrób `chmod +x` na tej nowej binarce (lub binarkach)
9. Usuń archiwum i ew. niepotrzebne pliki (np. README)

Chyba najbardziej jest irytujące to szukanie tego artefaktu, bo raz to jest `x86_64`, raz `x86-64`, albo `amd64` czy `AMD64`.

I wtedy mnie olśniło: zaraz... przecież ja kocham automatyzować i kocham wyrażenia regularne!

I tak powstał [gah](https://github.com/marverix/gah). W sumie to powstał już
prawie rok temu, ale myślę, że po tych 9 miesiącach można mówić o pewnej dojrzałości :) Jak więc zatem po tym okresie czasu? Zarąbiście! Jestem bardzo zadowolony z efektu pracy i jak dobrze radzi sobie `gah`.

![gah demo](https://github.com/marverix/gah/blob/master/_static/demo.gif?raw=true)

Nawet przez pewien czas [był na topce Hacker News](https://news.ycombinator.com/item?id=42387519). Aktualnie ma 151 gwiazdek na GitHubie i nadal rośnie :)  
