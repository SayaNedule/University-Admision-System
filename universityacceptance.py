N = int(input())
applicant_file = open('applicant_list.txt', 'r', encoding='utf-8')
applicant_list = []
accepted_students = []
subjects_list = []
b_spots = N
c_spots = N
e_spots = N
m_spots = N
p_spots = N

def make_applicant_list():
    lines = applicant_file.readlines()
    for line in lines:
        data = line.split()
        applicant_list.append(data)
make_applicant_list()

def list_creator():
    for i in range(5):
        s = []
        a = []
        b = []
        c = []
        d = []
        s.append(a)
        s.append(b)
        s.append(c)
        s.append(d)
        subjects_list.append(s)
list_creator()

def select_students():
    n = 0
    for i in range(3):
        for applicant in applicant_list:
            if applicant[7 + n] == 'Biotech':
                a = []
                full_name = applicant[0] + ' ' + applicant[1]
                a.append(full_name)
                if ((float(applicant[3]) + float(applicant[2]))/2) > float(applicant[6]):
                    a.append((float(applicant[3]) + float(applicant[2]))/2)
                else:
                    a.append(float(applicant[6]))
                subjects_list[0][n].append(a)
            elif applicant[7 + n] == 'Chemistry':
                a = []
                full_name = applicant[0] + ' ' + applicant[1]
                a.append(full_name)
                if float(applicant[3]) > float(applicant[6]):
                    a.append(float(applicant[3]))
                else:
                    a.append(float(applicant[6]))
                subjects_list[1][n].append(a)
            elif applicant[7 + n] == 'Engineering':
                a = []
                full_name = applicant[0] + ' ' + applicant[1]
                a.append(full_name)
                if ((float(applicant[5]) + float(applicant[4]))/2) > float(applicant[6]):
                    a.append((float(applicant[5]) + float(applicant[4]))/2)
                else:
                    a.append(float(applicant[6]))
                subjects_list[2][n].append(a)
            elif applicant[7 + n] == 'Mathematics':
                a = []
                full_name = applicant[0] + ' ' + applicant[1]
                a.append(full_name)
                if float(applicant[4]) > float(applicant[6]):
                    a.append(float(applicant[4]))
                else:
                    a.append(float(applicant[6]))
                subjects_list[3][n].append(a)
            elif applicant[7 + n] == 'Physics':
                a = []
                full_name = applicant[0] + ' ' + applicant[1]
                a.append(full_name)
                if ((float(applicant[2]) + float(applicant[4]))/2) > float(applicant[6]):
                    a.append((float(applicant[2]) + float(applicant[4]))/2)
                else:
                    a.append(float(applicant[6]))
                subjects_list[4][n].append(a)
        successful_applicants(n)
        removing_successful_applicants()
        n += 1

def successful_applicants(n):
    sorted_bio = sorted(subjects_list[0][n], key=lambda x: (x[0], x[1]))
    sorted_GPA = sorted(sorted_bio, key=lambda x: (-x[1], x[0]))
    limit = 0
    global b_spots
    for num in range(N):
        if b_spots > 0:
            try:
                success = sorted_GPA[limit]
                limit += 1
                accepted_students.append(success)
                subjects_list[0][3].append(success)
                b_spots -= 1
            except IndexError:
                break
    sorted_chem = sorted(subjects_list[1][n], key=lambda x: (x[0], x[1]))
    sorted_GPA = sorted(sorted_chem, key=lambda x: (-x[1], x[0]))
    limit = 0
    global c_spots
    for num in range(N):
        if c_spots > 0:
            try:
                success = sorted_GPA[limit]
                limit += 1
                accepted_students.append(success)
                subjects_list[1][3].append(success)
                c_spots -= 1
            except IndexError:
                break
    sorted_eng = sorted(subjects_list[2][n], key=lambda x: (x[0], x[1]))
    sorted_GPA = sorted(sorted_eng, key=lambda x: (-x[1], x[0]))
    limit = 0
    global e_spots
    for num in range(N):
        if e_spots > 0:
            try:
                success = sorted_GPA[limit]
                limit += 1
                accepted_students.append(success)
                subjects_list[2][3].append(success)
                e_spots -= 1
            except IndexError:
                break
    sorted_math = sorted(subjects_list[3][n], key=lambda x: (x[0], x[1]))
    sorted_GPA = sorted(sorted_math, key=lambda x: (-x[1], x[0]))
    limit = 0
    global m_spots
    for num in range(N):
        if m_spots > 0:
            try:
                success = sorted_GPA[limit]
                limit += 1
                accepted_students.append(success)
                subjects_list[3][3].append(success)
                m_spots -= 1
            except IndexError:
                break
    sorted_phy = sorted(subjects_list[4][n], key=lambda x: (x[0], x[1]))
    sorted_GPA = sorted(sorted_phy, key=lambda x: (-x[1], x[0]))
    limit = 0
    global p_spots
    for num in range(N):
        if p_spots > 0:
            try:
                success = sorted_GPA[limit]
                limit += 1
                accepted_students.append(success)
                subjects_list[4][3].append(success)
                p_spots -= 1
            except IndexError:
                break

def removing_successful_applicants():
    for student in accepted_students:
        for applicant in applicant_list:
            name = student[0].split()
            if name[0] == applicant[0] and name[1] == applicant[1]:
                applicant_list.remove(applicant)
    accepted_students.clear()

def printing():
    biotech = open('biotech.txt', 'a', encoding='utf-8')
    biotech.truncate(0)
    sorted_bio = sorted(subjects_list[0][3], key=lambda x: (x[0], x[1]))
    sorted_GPA = sorted(sorted_bio, key=lambda x: (-x[1], x[0]))
    limit = 0
    for n in range(N):
        try:
            success = sorted_GPA[limit]
            limit += 1
            biotech.write(f'{success[0]} {success[1]}')
            biotech.write('\n')
        except IndexError:
            break
    biotech.close()
    chemistry = open('chemistry.txt', 'a', encoding='utf-8')
    chemistry.truncate(0)
    sorted_bio = sorted(subjects_list[1][3], key=lambda x: (x[0], x[1]))
    sorted_GPA = sorted(sorted_bio, key=lambda x: (-x[1], x[0]))
    limit = 0
    for n in range(N):
        try:
            success = sorted_GPA[limit]
            limit += 1
            chemistry.write(f'{success[0]} {success[1]}')
            chemistry.write('\n')
        except IndexError:
            break
    chemistry.close()
    engineering = open('engineering.txt', 'a', encoding='utf-8')
    engineering.truncate(0)
    sorted_bio = sorted(subjects_list[2][3], key=lambda x: (x[0], x[1]))
    sorted_GPA = sorted(sorted_bio, key=lambda x: (-x[1], x[0]))
    limit = 0
    for n in range(N):
        try:
            success = sorted_GPA[limit]
            limit += 1
            engineering.write(f'{success[0]} {success[1]}')
            engineering.write('\n')
        except IndexError:
            break
    engineering.close()
    mathematics = open('mathematics.txt', 'a', encoding='utf-8')
    mathematics.truncate(0)
    sorted_bio = sorted(subjects_list[3][3], key=lambda x: (x[0], x[1]))
    sorted_GPA = sorted(sorted_bio, key=lambda x: (-x[1], x[0]))
    limit = 0
    for n in range(N):
        try:
            success = sorted_GPA[limit]
            limit += 1
            mathematics.write(f'{success[0]} {success[1]}')
            mathematics.write('\n')
        except IndexError:
            break
    mathematics.close()
    physics = open('physics.txt', 'a', encoding='utf-8')
    physics.truncate(0)
    sorted_bio = sorted(subjects_list[4][3], key=lambda x: (x[0], x[1]))
    sorted_GPA = sorted(sorted_bio, key=lambda x: (-x[1], x[0]))
    limit = 0
    for n in range(N):
        try:
            success = sorted_GPA[limit]
            limit += 1
            physics.write(f'{success[0]} {success[1]}')
            physics.write('\n')
        except IndexError:
            break
    physics.close()

select_students()
printing()
