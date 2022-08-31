subjects = ["Mathematics", "Physics", "Biotech", "Chemistry", "Engineering"]
accepted = dict.fromkeys(sorted(subjects))
students = []
students_to_remove = []
# Initializes the dictionary values so they can contain multiple lists
for i in accepted:
    accepted[i] = []


# Pulls list of students from text file and adds them to a list
def sort_students():
    with open("applicants.txt") as f:
        for i in f:
            students.append(i.split())


# Grabs the indexes for the scores required for each department
def dep_indexes(department):
    index = {"Physics": [2, 4],
             "Chemistry": [3],
             "Biotech": [3, 2],
             "Mathematics": [4],
             "Engineering": [5, 4]}
    return index[department]


def enroll(cap):
    # Iterates through the students first, second, and third pick
    for y in range(7, 10):
        # Updates the student list each wave of admission, removing the accepted students
        student = [x for x in students if x not in students_to_remove]
        for i in accepted:
            # Sorts students by their higher test scores, subject choice, first name, and last name
            student.sort(key=lambda o: (-max(get_average(i, o), float(o[6])), o[y], o[0], o[1]))
            # Iterates through the list of students waiting for admission
            for x in student:
                # Adds students to the accepted dictionary if spots are available
                if x[y] == i and len(accepted[i]) < int(cap):
                    accepted[i].append(x)
                    students_to_remove.append(x)
                else:
                    continue


# Returns the average scores required
def get_average(department, student):
    dep = dep_indexes(department)
    if len(dep) == 2:
        average = (float(student[dep[0]]) + float(student[dep[1]])) / 2
        return average
    else:
        return float(student[dep[0]])


# Sorts and writes sorted students onto a text file
def print_accepted():
    for i in accepted:
        with open(f"{i}.txt", "w") as f:
            accepted[i].sort(key=lambda x: (-max(get_average(i, x), float(x[6])), x[0], x[1]))
            for x in accepted[i]:
                average = get_average(i, x)
                name = " ".join(x[:2])
                f.write(f"{name} {max(get_average(i, x), float(x[6]))}\n")


capacity = input()
sort_students()
enroll(capacity)
print_accepted()
