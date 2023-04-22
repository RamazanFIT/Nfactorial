from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)

def check_of_digit(str_1):
    massive_of_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in massive_of_digits:
        if i in str_1:
            return False
    return True
def check_float(str_1):
    if '.' in str_1:
        massive_of_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        cnt = 0
        for i in str_1:
            if i in massive_of_digits:
                cnt += 1
        if len(str_1) - 1 == cnt:
            return False
        else:
            return True
    else:
        if not str_1.isdigit():
            return True
        else:
            return False
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        flag = True
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        course = request.form['course']
        gpa = request.form["gpa"]
        special = request.form["special"]
        # image = request.files["image"]
        # file_name = image.filename
        # image.save("image\\" + file_name)

        # photos_ = open("Image.json")
        # g0 = json.load(photos_)

        g_p_a = open("GPA.json")
        g1 = json.load(g_p_a)

        age_ = open("year.json")
        g2 = json.load(age_)
        
        course_ = open("Which_course.json")
        g3 = json.load(course_)

        special_ = open("direction.json")
        g4 = json.load(special_)

        if "first" in request.form and flag:
            if not check_of_digit(firstname) or len(firstname) == 0:
                flag = False
            if not check_of_digit(lastname) or len(lastname) == 0:
                flag = False
            if not check_of_digit(special) or len(special) == 0:
                flag = False
            if not age.isdigit() or not course.isdigit() or (len(gpa) == 0 or len(age) == 0 or len(course) == 0):
                flag = False
            if check_float(gpa):
                flag = False
           
            if not flag:
                return render_template("sorry.html")
            g1[firstname + "_" + lastname] = gpa
            
            g2[firstname + "_" + lastname] = age
            
            g3[firstname + "_" + lastname] = course
        
            g4[firstname + "_" + lastname] = special

            # g0[firstname + "_" + lastname] = file_name

            # g0_ = json.dumps(g0)
            g1_ = json.dumps(g1)
            g2_ = json.dumps(g2)
            g3_ = json.dumps(g3)
            g4_ = json.dumps(g4)
            # photos = open("Image.json", "w")
            g_p_a = open("GPA.json", 'w')
            age_ = open("year.json", "w")
            course_ = open("Which_course.json", "w")
            special_ = open("direction.json", 'w')
            # photos.write(g0_)
            g_p_a.write(g1_)
            age_.write(g2_)
            course_.write(g3_)
            special_.write(g4_)
            
            return render_template("success.html")
        if "get_all_student" in request.form:
            my_list = list(g1.keys())
            # return render_template("table.html",g0 = g0, g1 = g1, g2 = g2, g3 = g3, g4 = g4)
            return render_template("table.html",my_list = my_list, g1 = g1, g2 = g2, g3 = g3, g4 = g4)
        elif "by_gpa" in request.form:
            g1 = sorted_dict = dict(sorted(g1.items(), key=lambda x: x[1]))
            my_list = list(g1.keys())
            return render_template("table.html",my_list = my_list, g1 = g1, g2 = g2, g3 = g3, g4 = g4)
        elif "by_name" in request.form:
            g1 = sorted_dict = dict(sorted(g1.items(), key=lambda x: x[0]))
            my_list = list(g1.keys())
            return render_template("table.html",my_list = my_list, g1 = g1, g2 = g2, g3 = g3, g4 = g4)
        elif "by_year" in request.form:
            g2 = sorted_dict = dict(sorted(g2.items(), key=lambda x: x[1]))
            my_list = list(g2.keys())
            return render_template("table.html",my_list = my_list, g1 = g1, g2 = g2, g3 = g3, g4 = g4)
        elif "by_uni" in request.form:
            g3 = sorted_dict = dict(sorted(g3.items(), key=lambda x: x[1]))
            my_list = list(g3.keys())
            return render_template("table.html",my_list = my_list, g1 = g1, g2 = g2, g3 = g3, g4 = g4)
        elif "by_spec" in request.form:
            g4 = sorted_dict = dict(sorted(g4.items(), key=lambda x: x[1]))
            my_list = list(g4.keys())
            return render_template("table.html",my_list = my_list, g1 = g1, g2 = g2, g3 = g3, g4 = g4)
        if "find_user" in request.form:
            find_user = request.form['find']
            print(find_user)
            g_p_a = open("GPA.json")
            g1 = json.load(g_p_a)
            my_list = list(g1.keys())
            # print(my_list)
            if not check_of_digit(find_user) or len(find_user) == 0:
                return render_template("sorry.html")
            elif find_user not in my_list:
                return render_template("doesnotexist.html")
            else:
                # return render_template("table.html", )
                # my_list = list(g1.keys())
                my_list = [find_user]
                return render_template("table.html",my_list = my_list, g1 = g1, g2 = g2, g3 = g3, g4 = g4)

        if "delete_user" in request.form:
            student_to_del = request.form["delete_user"]
            if not check_of_digit(student_to_del) and len(student_to_del) != 0:
                return render_template("sorry.html")
            if student_to_del in g1:
                # del g0[student_to_del]
                del g1[student_to_del]
                del g2[student_to_del]
                del g3[student_to_del]
                del g4[student_to_del]
                # g0_ = json.dumps(g0)
                g1_ = json.dumps(g1)
                g2_ = json.dumps(g2)
                g3_ = json.dumps(g3)
                g4_ = json.dumps(g4)
                # photos = open("Image.json", "w")
                g_p_a = open("GPA.json", 'w')
                age_ = open("year.json", "w")
                course_ = open("Which_course.json", "w")
                special_ = open("direction.json", 'w')
                # photos.write(g0_)
                g_p_a.write(g1_)
                age_.write(g2_)
                course_.write(g3_)
                special_.write(g4_)
            else:
                return render_template("doesnotexist.html")
        

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
