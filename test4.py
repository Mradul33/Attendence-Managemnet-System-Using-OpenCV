def savefile(Enrollment_No,Name,Father_Name,EMail,Contact):
        p=(f'\n{Enrollment_No},{Name},{Father_Name},{EMail},{Contact}')
        filename=("C:\\Users\\mradu\\Documents\\projct 2\\StudentList\\StudentList.csv")
        with open(filename,"a") as f:
                f.writelines(p)