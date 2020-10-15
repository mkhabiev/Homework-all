import wikipedia

def main():
    language = input('Choose a language for Wiki: (en, ru, fr) ')
    wiki = wikipedia
    wiki.set_lang(language)
    while True:
        query = input('What do you want to search? ')
        results = wiki.search(query)

        for key, result in enumerate(results):
            print(key, result)
        print()
        about = input('Choose a short information\n ')
        summary = wiki.summary(about)
        d = 0
        for i in range(0, len(summary), 50):
            try:
                print(summary[d:d+i] + '-')
            except Exception:
                print(summary[d:])
            d += i

        ask_url = input('Do you want link? ')
        if ask_url.lower() == 'yes':
            article = wiki.page(about)
            print(article.url)

main()