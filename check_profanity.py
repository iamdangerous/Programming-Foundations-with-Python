import urllib
def read_txt():
    quotes = open("D:\Learning\Udacity\Web Dev\Programming foundations with Python\movie_quotes.txt")
    content_of_file = quotes.read()
    #print(content_of_file)
    quotes.close();
    check_profanity(content_of_file)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read()
    print (output)
    connection.close();
read_txt();    
