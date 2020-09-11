
# class # 
    # [a=0 / def(b)=a+b] 일때 def를 또 쓰려면 a와 def(b)를 다시 만들어야 됨
    # class = [a=0] + [def(b)=a+b] = 객체변수 + 메소드(함수) 
    # class에 객체변수 값을 넣으면 자동으로 a와 def(b)를 만들어서 객체에 저장해줌
    # class > 변수, 메소드(함수), 생성자(객체생성시 자동실행되는 메소드)
    # class사용과정 : class정의 -> 객체생성 -> 객체변수 지정 -> 메소드 사용
    # 멤버변수 > 클래스변수(Unit.defense), 객체변수(self.name)
    # marine = 객체 = AttackUnit의 인스턴스
    # isinstance(이것이, 이 class의 인스턴스인가?)
from random import*
def start():
    print("[알림]게임을 시작합니다.")
def over():
    pass # pass # 제대로 안써도 일단 패스
        print("현재체력 : {}".format(self.hp))
class Unit: # 부모 클래스
    defense = 2 # 클래스 변수
    def __init__(self, name, hp, speed): # ​생성자 __init__ / 객체생성 시 자동 실행, 객체변수를 정의 / 없으면 밖에서 일일이 객체변수를 지정 해줘야함
        self.name = name # self의 필요성 : marine.attack() 에서 aa->self로 들어가고 "탱크"->좨로 들어감
        self.hp = hp
        self.speed = speed
        print("[{} 생성완료]".format(name))
    
    def move(self, where):
        print("{} : {} 방향으로 이동 [속도 : {}]".format(self.name, where, self.speed)) # 객체변수 호출(class안):self.~~

    def damaged(self, damaged):
        self.hp -= damaged - Unit.defense # 클래스변수 호출(밖에서도 동일):클래스이름.~~
        print("{} : {} 데미지 / 현재체력 : {}".format(self.name, damaged - Unit.defense, self.hp))
        if self.hp <=0:
            print("{} : 사망".format(self.name))

class AttackUnit(Unit): # 상속 # 자식 클래스
    def __init__(self, name, hp, damage, speed):
        #Unit.__init__(self, name, hp,speed)
        super().__init__(name, hp, speed)  # super # self없이 사용 # 다중상속하면 하나만 상속됨
        self.damage = damage
    
    def attack(self, who):
        print("{} : {}을(를) 공격 [공격력 : {}]".format(self.name, who, self.damage))

class FlyableUnit:
    def __init__(self, flyingspeed):
        self.flyingspeed = flyingspeed
    
    def fly(self, name, where):
        print("{} = {}방향으로 날아갑니다. [속도 : {}]"\
            .format(name, where, self.flyingspeed))

    
class FlyableAttackUnit(FlyableUnit, AttackUnit): # 다중 상속
    def __init__(self, name, hp, damage, flyingSpeed):
        AttackUnit.__init__(self, name, hp, damage, 0) # 지상스피드는 0으로 처리
        FlyableUnit.__init__(self, flyingSpeed)

    def move (self, name, where): # 메소드 오버로딩 # 자식 클래스의 메소드 우선 실행
        self.fly(name, where)

start()
over()
marine = AttackUnit("마린", 40, 5, 5) # 객체생성, 객체변수 지정 # 모든 변수를 넣어줘야 함
tank = AttackUnit("탱크", 150, 35, 5)
wraith = FlyableAttackUnit("레이스", 150, 10, 10)
wraith.armor = 5 # 객체변수 추가
marine.attack("탱크") # 메소드 사용
tank.damaged(marine.damage)
marine.move("11시") # 연산자 오버로딩
wraith.move(wraith.name, "11시") # 객체변수 호출(class밖):객체이름.~~


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 5, 1)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{} : 스팀팩 사용 [HP : {}]".format(self.name, self.hp))
        else:
            print("{} : 체력부족으로 스팀팩 사용 취소")

class Tank(AttackUnit):

    seize = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 1)
        self.seizemode = False

    def set_seize(self):
        if Tank.seize == False:
            return
        
        if self.seizemode == False:
            print("탱크 : 시즈모드 [공격력 : 40]")
            self.damage += 5
            self.seizemode == True
        else:
            print("탱크 : 시즈모드 해제 [공격력 : 35]")
            self.damage -= 5
            self.seizemode == False

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == False:
            print("레이스 : 클로킹모드")
            self.clocked = True
        else :
            print("레이스 : 클로킹모드 해제")
            self.clocked = False

m1 = Marine()
m2 = Marine()
m3 = Marine()
t1 = Tank()
t2 = Tank()
w1 = Wraith()

attack_unit = []
attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(m3)
attack_unit.append(t1)
attack_unit.append(t2)
attack_unit.append(w1)

for unit in attack_unit:
    if isinstance(unit, Wraith):
        unit.move(unit.name, "1시")
    else:
        unit.move("1시")

Tank.seize = True
print("시즈모드 개발")

for unit in attack_unit:
    if isinstance(unit, Marine): # isinstance(이것이, 이 class의 인스턴스인가?)
        unit.stimpack()
    elif isinstance(unit, Tank): 
        unit.set_seize()
    elif isinstance(unit, Wraith): 
        unit.clocking()

for unit in attack_unit:
    unit.attack("1시")

for unit in attack_unit:
    unit.damaged(randint(5, 21))

# 예외처리
try:
    print("[나누기 전용계산기]")
    nums = []
    nums.append(int(input("첫 번째 숫자 : ")))
    nums.append(int(input("두 번째 숫자 : ")))
    nums.apeend(int(nums[0] / nums[1]))
    print("{} / {} = {}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # 에러문장 그대로 출력
    print(err)
except: # 나머지 모든 에러 처리
    print("알 수 없는 에러가 발생하였습니다.")
except Exception as err: # 나머지 모든 에러 에러문장 그대로 출력
    print(err)

class BigNumberError(Exception): # 사용자정의 예외처리
    def __init__(self, msg):
        self.msg = msg
    
    def __str___(self):
        return self.msg

try:
    print("[한자리 나누기 전용 계산기]")
    num1 = int(input("첫 번째 숫자 : "))
    num2 = int(input("두 번째 숫자 : "))
    if num1 >= 10 or num2 >=10:
        raise BigNumberError("입력값 : {}, {}".format(num1, num2)) # 에러발생시키기
    print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
except BigNumberError as err:
    print("[에러] 한자리 숫자만 입력하세요")
    print(err)
finally: # finally #에러 발생해도 무조건 실행
    print("계산기를 이용해 주셔서 감사합니다.")

# 모듈 # 같은 경로, 폴더에 모여있어야 사용가능
    # 같은 폴더안에 practice_module.py 생성
        # def price(people):
        #     print("{}명 가격은 {}원 입니다.".format(people, people*10000))

        # def price_morning(people):
        #     print("{}명 조조 할인 가격은 {}원 입니다.".format(people, people*6000))

        # def price_soldier(people):
        #     print("{}명 군인 할인 가격은 {}원 입니다.".format(people, people*4000))

import practice_module
practice_module.price(3)

import practice_module as mv # as ~~ : 별명 붙이기
mv.price(3)

from practice_module import* # 별명조차 없이 사용
price(3)

from practice_module import price, price_morning # import ~~ : ~~만 임포트 하기
price(3)

from practice_module import price as mv # price만 임포트해서 함수이름까지 별명 붙이기
mv(3)

# 패키지
    # 같은 폴더에 travel폴더 생성
    # travel 폴더
        # __init__.py
            # __all__ = ["veitnam", "Tailand"]
        # thailand.py
            # class ThailandPackage:
                # def detail(self):
                #     print("[태국패키지 3박 5일] 방콕, 파타야, 야시장 투어 50만원")
    # 모듈이 직접 실행됐는지, 호출되었는지 확인하는법
            # if __name__ == "__main__":
                # print("이 문장은 모듈을 직접 실행할 때만 실행 됨")
                # trip_to = ThailandPackage()
                # trip_to.detail()
            # else:
                # print("이 문장은 외부에서 모듈을 호출했을 때만 실행됨")
        # vietnam.py
            # ""

import travel.thailand
    #import travel.thailand.ThailandPackage() # 오류, 패키지 모듈 단위까지만 임포트 가능
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage # from 사용하면 클래스 단위로 임포트 가능
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam # from 패키지하면 모듈까지만
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# __all__ # 패키지를 *(전부 임포트)할때는 공개 범위를 지정해야함
from travel import*
trip_to = vietnam.VietnamPackage()
trip_to.detail()

#패키지, 모듈 위치 확인하는 법 # 라이브러리에 가져다 두면 다른 곳에서도 사용가능
import inspect
print(inspect.getfile(vietnam))

# pip install # 패키지 설치
    # https://pypi.org/
    # 터미널에 pip ~~
    # pip list : 설치된 패키지 확인
    # show ~~ for : ~~패키지의 정보 확인
    # pip install --upgrade ~~ : ~~ 패키지 업그레이드
    # pip uninstall ~~ : ~~패키지 삭제
    
# 내장 함수 # 이미 임포트 되어있는 함수
    # dir(객체의 변수와 함수 표시)
    # 구글 검색 list of python builtins : 파이썬의 내장 함수 확인 가능
# print(dir()) # 현재 임포드 된 것들 표시.
# import random
# print(dir(random)) # random의 변수와 함수 표시
# a = "문자열"
# print(dir(a)) # 문자열의 변수와 함수 표시

# 외장 함수(모듈) # 임포트 해서 사용해야하는 함수
    # 구글 검색 list of python modules : 외장 함수 확인 가능
import glob # 경로 내의 폴더 / 파일 목록 조회 (윈도우의 dir)
print(glob.glob("*.py")) # 확장자가 py인 모든 파일 조회
import os # 운영체제에서 제공하는 기본 기능
print(os.getcwd()) # 현재 디렉토리
folder = "sample_dir"
if os.path.exists(folder): # sample_dir라는 폴더가 있는지 검색
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder) # sample_dir 폴더생성
    print(folder, "폴더를 생성하였습니다.")
print(os.listdir()) # 폴더 검색
import time # 시간관련 함수
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
import datetime
print("오늘 날짜는", datetime.date.today())
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # '100일' 저장
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후