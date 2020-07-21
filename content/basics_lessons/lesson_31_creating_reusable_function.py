def emoji_convert(message):
    words = message.split(" ")

    emojis = {
        ":)": "\U0001F638",
        ":(": "\U0001F63F"
    }

    output = ""

    for word in words:
        output += emojis.get(word, word) + " "

    return output


input_message = input("> ")


print(emoji_convert(input_message))
