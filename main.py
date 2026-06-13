#Quản lý sách
#Bài tập về trang quản lý sách gồm các chức năng
#1. Show toàn bộ sách show_all_books()
#2. Tìm kiếm sách theo title, rồi show thông tin cuốn đó search_book()
#3. Thêm sách vào thư viện add_book()
#4. Đếm số sách đã đọc count_completed_book()
#5. Update sách đã đọc update_read_book()
#6. Xoá sách delete_book()
#7. Thoát
#Viết hết 1 loạt hàm trước
#Sau đó đến chương trình sẽ có các lựa chọn từ 1 đến 7 để người dùng chọn
#Trong khi còn chọn từ 1 đến 6 thì chương trình vẫn chạy, chọn số nào, gọi hàm đó.
#Khi nào break thì thoát hẳn chương trình

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


while True:
    print("1. Hien thi thu viện")
    print("2. Tim sach")
    print("3. Them sach")
    print("4. Xem tong so sach da doc")
    print("5. Cap Nhat sach da doc")
    print("6. Xoa sách")
    print("7. Thoát chương trình")
    select = int(input("Hay chon tu 1 den 7: "))
    if select == 1:
        show_all_books()
    elif select == 2:
        title = input("Nhập tên sách muốn tìm: ")
        result = search_book(title)
        if result == None:
            print("Khong tim thay sach")
        else:
            print(result)
    elif select == 3:
        book = {}
        print("Hay nhap sach muốn thêm")
        title = input("Nhap ten sach")
        completed = int(input("Đã đọc nhập 1, chưa đọc nhập 0: "))
        book["title"] = title
        if completed ==1:
            book["completed"] = True
        else:
            book["completed"] = False
        add_book(book)
        print("Da them thanh cong")
    elif select == 4:
        count = count_read_book()
        print(f"Tong so sach da doc {count}")
    elif select == 5:
        title = input("Nhap ten sach can cap nhat: ")
        if update_completed_book(title):
            print("Cap nhat thanh cong")
        else:
            print("Khong tim thay sach de cap nhat")
    elif select == 6:
        title = input("Nhap ten sach muon xoa: ")
        if delete_book(title):
            print("Da xoa sach")
        else:
            print("Khong tim thay sach")
    elif select == 7:
        break
    else:
        print("Lua chon khong hop le")
