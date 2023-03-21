def rytm(text):
    firstCount = 0
    glasn = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
    for let in glasn:
        firstCount += text[0].count(let)
            
    for word in text:
        newCount = 0
        for let in glasn:
            newCount += word.count(let)
        if (newCount != firstCount):
            return "Пам парам"
    return "Парам пам-пам"


text = input("Введите кричалку")
textArray = text.split(" ")

print(rytm(textArray))