def emoji_convert(message):
    words = message.split(" ")

    emojis = {
        ":)": "smile",
        ":(": "sad"
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "

    return output


input_message = input("> ")


print(emoji_convert(input_message))
