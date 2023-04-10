import easyocr


def text_read_to_foto(file_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(file_path, detail=0, paragraph=True)

    return result


def main():
    file_path = input("Путь к вашему файлу: ")
    #test1 = "img/text.jpg"
    #test2 = "img/write_heands.jpg"
    print(text_read_to_foto(file_path=file_path))


if __name__ == "__main__":
    main()