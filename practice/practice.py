def profile(name, age, *language):
    print("이름 : {}\t나이 : {}\t".format(name, age), end=" ") #end="줄바꿈 하지않음"
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "Python", "Java", "C", "C++", "C#")