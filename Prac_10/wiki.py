
import wikipedia

page_title_or_phrase = input("Please enter a page title or search phrase: ")


while page_title_or_phrase != "":
    try:
        page = wikipedia.page(page_title_or_phrase)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    except wikipedia.PageError as d:
        print("No such page my dude")

    page_title_or_phrase = input("Please enter a page title or search phrase: ")

print("Thank you!")

