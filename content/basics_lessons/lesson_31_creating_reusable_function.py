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

message = input("> ")


print(emoji_convert(message))