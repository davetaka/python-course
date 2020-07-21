message = input("> ")

words = message.split(" ")

emojis = {
    ":)": "\U0001F638",
    ":(": "\U0001F63F"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)
