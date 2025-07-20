phonecall_book = {
"홍길동": "010-1111-1111",
"이순신": "010-1111-2222",
"강감찬": "010-1111-3333",
}

def app():
    print("아래 학생들의 전화번호를 조회할 수 있습니다.")
    for name, phone_num in phonecall_book.items():
        print(name)

app()