"""
This program creates the following dictionaries:
1. A dict containing course numbers and room numbers where the courses meet.
2. A dict containing course numbers and the names of the instructors that teach the course.
3. A dict containing the course numbers and the meeting times of each course.

Usage: The user will be prompted for a number. The program will return the room number, instructor, and meeting time.
    - If the course is not in the dict, an error message will be displayed and ask again for a course number.
"""

COURSE_NUMBERS = ["CS101", "CS102", "CS103", "NT110", "CM241"]
ROOM_NUMBERS = ["3004", "4501", "6755", "1244", "1411"]
INSTRUCTORS = ["Haynes", "Alvarado", "Rich", "Burke", "Lee"]
MEETING_TIMES = ["8:00 a.m.", "9:00 a.m.", "10:00 a.m.", "11:00 a.m.", "1:00 p.m."]

def main():
    course_rooms = {key: value for key, value in zip(COURSE_NUMBERS, ROOM_NUMBERS)}
    course_instructors = {key: value for key, value in zip(COURSE_NUMBERS, INSTRUCTORS)}
    course_times = {key: value for key, value in zip(COURSE_NUMBERS, MEETING_TIMES)}


    while True:
        try:
            course = input("Enter a course number: ").upper()
            if course == "":
                print("\nBye!")
                return

            while course not in COURSE_NUMBERS:
                course = input(f"Course number {course} not found. "
                               f"Please enter a valid course number or press ENTER to stop: ").upper()
                if course == "":
                    print("\nBye!")
                    return

        except KeyboardInterrupt:
            print("\nBye!")
            return

        print(f"\nThe details for course {course} are:\n"
            f"Room: {course_rooms[course]}\n"
            f"Instructor: {course_instructors[course]}\n"
            f"Time: {course_times[course]}\n")

if __name__ == "__main__":
    main()