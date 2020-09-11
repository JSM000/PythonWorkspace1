class ThailandPackage:
    def detail(self):
        print("[태국패키지 3박 5일] 방콕, 파타야, 야시장 투어 50만원")

if __name__ == "__main__":
    print("이 문장은 모듈을 직접 실행할 때만 실행 됨")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("이 문장은 외부에서 모듈을 호출했을 때만 실행됨")