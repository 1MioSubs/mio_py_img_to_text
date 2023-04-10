import easyocr
from datetime import datetime


def text_read_to_foto(file_path):
    reader = easyocr.Reader(["en", "ru", "uk"])
    result = reader.readtext(file_path, paragraph=True)

    return result


def main():
    #file_path = input("Путь к вашему файлу: ")
    test1 = "img/text.jpg"
    test3 = "img/text2.jpg"
    #test2 = "img/write_heands.jpg"
    test11 = float((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds())
    print(text_read_to_foto(file_path=test3))
    test22 = float((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds())
    print(test22 - test11)

if __name__ == "__main__":
    main()