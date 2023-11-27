from django.shortcuts import render
import mysql.connector as sql
first_name=''
last_name=''
sex=''
email=''
password=''
def Register(request):
    global first_name, last_name, sex, email, password
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="Imad", database='student')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "first_name":
                first_name = value
            if key == "last_name":
                last_name = value
            if key == "sex":
                sex = value
            if key == "email":
                email = value
            if key == "password":
                password = value
        c = "insert into user Values('{}','{}','{}','{}','{}')".format(first_name, last_name, sex, email, password)
        cursor.execute(c)
        m.commit()
    return render(request, 'Register_page.html')


