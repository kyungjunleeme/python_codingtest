

def test():
    d = {}
    # 에러가 발생하지 않고 - False가 출력됨. 키 에러가 나지 않는다는 사실을 활용함
    print('a' in d and d['a'])

if __name__ == "__main__":
    test()
