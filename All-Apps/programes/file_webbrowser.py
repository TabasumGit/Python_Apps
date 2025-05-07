import webbrowser

user = input('enter a serach term').replace(" ", "+")


webbrowser.open('https://www.google.com/search?q=' + user)

