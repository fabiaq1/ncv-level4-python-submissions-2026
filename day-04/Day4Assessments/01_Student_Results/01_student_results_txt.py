# Practical 1 - Student results


# Check if one student record has the right details
def validate_student(line, students):
    fields = line.strip().split(",")
    field_count = 0
    for field in fields:
        field_count += 1
    if field_count != 3:
        return None, "Expected student_number,name,mark1;mark2;mark3"

    student_number = fields[0].strip()
    student_name = fields[1].strip()
    mark_parts = fields[2].split(";")
    if not student_number.isdigit():
        return None, "Student number must contain digits"
    if student_name == "":
        return None, "Student name is missing"
    if student_number in students:
        return None, "Duplicate student number"

    mark_count = 0
    marks = []
    for mark_text in mark_parts:
        mark_count += 1
        mark_text = mark_text.strip()
        if not mark_text.isdigit():
            return None, "Mark is not a whole number"
        mark = int(mark_text)
        if mark < 0 or mark > 100:
            return None, "Mark must be between 0 and 100"
        marks.append(mark)
    if mark_count != 3:
        return None, "Exactly three marks are required"
    return {"number": student_number, "name": student_name, "marks": marks}, ""



# Work out the average of the three marks
def calculate_average(marks):
    total = 0
    count = 0
    for mark in marks:
        total += mark
        count += 1
    return total / count



# Put the students in order, starting with the highest average 

# Arrange the results from highest to lowest
def sort_by_average(records):
# Look for the next highest average
    index = 0
    while index < len(records):
        best = index
        other = index + 1
        while other < len(records):
            if records[other]["average"] > records[best]["average"]:
                best = other
            other += 1
        records[index], records[best] = records[best], records[index]
        index += 1


# Read the file and keep the student records that are correct

def main():
    students = {}               
    errors = []                 
    line_number = 0
    try:
        with open("learners.txt", "r", encoding="utf-8") as input_file:
            for original_line in input_file:
                line_number += 1
                line = original_line.strip()
                if line == "":
                    continue
                record, reason = validate_student(line, students)
                if reason != "":
                    errors.append("Line " + str(line_number) + ": " + reason + " | " + line)
                else:
                    record["average"] = calculate_average(record["marks"])
                    students[record["number"]] = record
    except FileNotFoundError:
        print("ERROR: Put learners.txt in the same folder as this program.")
        return

# Make a list so we can rank the students
    ranking = []
    for student_number in students:
        ranking.append(students[student_number])
    sort_by_average(ranking)

    
# Save the student results in a report
    
    with open("report.txt", "w", encoding="utf-8") as report:
        report.write("RANK | NUMBER | NAME | AVERAGE | RESULT\n")
        rank = 0
        for record in ranking:
            rank += 1
            status = "PASS"
            if record["average"] < 50:
                status = "FAIL"
            report.write(f'{rank} | {record["number"]} | {record["name"]} | '
                         f'{record["average"]:.2f} | {status}\n')

    
# Save the errors and the records that passed the checks
    
    with open("errors.log", "w", encoding="utf-8") as error_file:
        for message in errors:
            error_file.write(message + "\n")

    with open("clean.txt", "w", encoding="utf-8") as clean_file:
        for record in ranking:
            marks = record["marks"]
            clean_file.write(f'{record["number"]},{record["name"]},'
                             f'{marks[0]};{marks[1]};{marks[2]}\n')

   
    # Check the saved file and show how many records we have
  
    saved_count = 0
    with open("clean.txt", "r", encoding="utf-8") as clean_file:
        for saved_line in clean_file:
            if saved_line.strip() != "":
                saved_count += 1
    accepted_count = 0
    for record in ranking:
        accepted_count += 1
    rejected_count = 0
    for message in errors:
        rejected_count += 1
    print("STUDENT RESULTS PROCESSOR")
    print("Accepted:", accepted_count, "Rejected:", rejected_count)
    print("Saved and reloaded counts match:", saved_count == accepted_count)
    print("Files created: report.txt, errors.log, clean.txt")



# Run the program

if __name__ == "__main__":
    main()
