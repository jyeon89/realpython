def enrollment_stats():
    University = [
        ['Caltech', 2175, 37704],
        ['Harvard', 19627, 39849],
        ['MIT', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500]
    ]
    return University

def total():
    es = enrollment_stats()
    tot_s = 0
    tot_t = 0
    
    for i in range(len(es)):
        tot_s = tot_s + es[i][1]

    for j in range(len(es)):
        tot_t = tot_t + es[j][2]
    return tot_s, tot_t

def mean():
    es = enrollment_stats()
    n = len(es)

    mean_s = total()[0]/n    
    mean_t = total()[1]/n
    
    return int(mean_s), int(mean_t)

def median():
    es = enrollment_stats()
    n = len(es)
    student = []
    tuition = []
    
    for i in range(n):
        student.append(es[i][1])
        tuition.append(es[i][2])

    student.sort()
    tuition.sort()

    mid = int((n-1)/2)
    return student[mid], tuition[mid]

def output():
    print("**************************")
    print("Total students:   ", total()[0])
    print("Total tuition:   $", total()[1])
    print("")
    print("Student mean:     ", mean()[0])
    print("Student median:   ", median()[0])
    print("")
    print("Tuition mean:    $", mean()[1])
    print("Tuition median:  $", median()[1])
    print("**************************")    
