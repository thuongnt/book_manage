books = []
def show_all_books():
    if books:
        for book in books:
            print(book)
    else:
        print("Không có cuốn sách nào")


def search_book(title):
    for book in books:
        if book["title"] == title:
            return book
    return None


def add_book(book):
    books.append(book)


def count_read_book():
    count = 0
    for book in books:
        if book.get("completed") == True:
            count += 1
    return count


def update_completed_book(title):
    for book in books:
        if book["title"] == title:
            book["completed"] = True
            return True
    return False


def delete_book(title):
    for book in books:
        if book["title"] == title:
            books.remove(book)
            return True
    return False

