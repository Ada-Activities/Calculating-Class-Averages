def calculate_class_averages(classrooms):
    class_averages = {}

    # loop through classrooms getting access to class names and students in class
    for classroom, students in classrooms.items():
    
        # if a class does not have students then set the class average to zero
        # go to next class
        if not students:
            class_averages[classroom] = 0
            continue
        
        # initial scores and number of grades
        scores = 0
        num_grades = 0

        # loop through each student's grade 
        for grades in students.values():
            # if a student does not have grades then continue to next student
            if not grades:
                continue
            
            # loop through grades
            for grade in grades:
                # sum up scores and number of grades
                scores += grade
                num_grades += 1

        # calculate average and assign key/value pair
        avg = scores / num_grades
        class_averages[classroom] = avg
    
    return class_averages