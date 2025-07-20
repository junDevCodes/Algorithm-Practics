phonecall_book = {
"홍길동": "010-1111-1111",
"이순신": "010-1111-2222",
"강감찬": "010-1111-3333",
}

def find_phone_num(name) :
    phone_num = phonecall_book[name]
    return f"{name}의 전화번호는 {phone_num}입니다."

def app():
    print("아래 학생들의 전화번호를 조회할 수 있습니다.")
    for name, phone_num in phonecall_book.items():
        print(name)
    print("전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.")
    name = str(input())
    print(find_phone_num(name))

app()