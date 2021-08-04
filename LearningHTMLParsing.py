from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

def main():
    parser = MyHTMLParser()
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read()
        parser.feed('contents')

if __name__ == "__main__":
    main()