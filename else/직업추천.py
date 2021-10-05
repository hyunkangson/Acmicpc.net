from collections import defaultdict

def solution(table, languages, preference):
    pref = defaultdict(int)

    for i in range(len(languages)):
        pref[languages[i]] = preference[i]

    score = defaultdict(int)
    for t in table:
        t = list(map(str, t.split()))
        for i in range(1,len(t)):
            if pref[t[i]]:
                score[t[0]] += pref[t[i]] * (len(t)-i)

    answer = sorted(score.items(), key=lambda x:(-x[1],x[0]))[0][0]

    return answer

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#",
                "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"],
               ["PYTHON", "C++", "SQL"],
               [7, 5, 5]))