# Syllabus for Programming Fundamental I: Python

Welcome to our course! I've included below all the essential information needed to navigate through the semester successfully. Please take a look at each section carefully and let me know if you have any questions.

## Instructor Information

- **Name:** Truc L. Huynh
- **Email:** [truc.huynh@austincc.edu](mailto:truc.huynh@austincc.edu)
- **Class and Lab Hours**
  - LEC MW 6:10 PM - 8:35 PM DIL DLS
  - LAB MW 8:35 PM - 9:20 PM DIL DLS
- **Office Hours:**
  - Fridays: 11:30 PM - 1:30 PM
  - Wednesdays: 5:00 PM - 6:00 PM
  - *Note:* For office hours and our meeting, please access the Zoom link via the "Zoom Class and Office Hour" menu item in Blackboard. Available by appointment outside these hours. Email responses within 24 hours, excluding weekends.

## Instructor Bio

As a software developer, I bring real-world insights and practical teaching to prepare you for today's job market. Our focus will be on hands-on learning, modern methods, and ensuring your success post-graduation. I look forward to creating an engaging, collaborative, and supportive learning environment. I will commit to doing my part, but you also need to commit to doing your part for success.
Check out my profile here [Truc LinkedIn profile](https://www.linkedin.com/in/trucdev/). Please don't hesitate to contact me even after this course if you have any questions. I am here to help and am dedicated to your success.

## Getting Started

Please review the sections below and complete the tasks at the bottom of this page for course orientation.

## To Do:
- [Course Orientation](https://forms.gle/7Qv4hkFKeTDnkFNY6)
- [Discord Channel - Must Join](https://discord.gg/8VY5JZJrq4)
- [Respondus Lockdown Browser](https://instruction.austincc.edu/students/article/respondus-lockdown-browser/)

## Text and Teaching Materials

- **Textbook:** Starting out with Python – Fifth Edition, by Tony Gaddis. ISBN-13: 978-0-592903-2. Available online within Blackboard, covered by tuition.

## Course Requirements

- **Orientation:** Mandatory. Failure to complete will result in being dropped from the class. Please do **both** the form and the quiz
- **Class Progress:** Regular progress is crucial as each concept builds on the previous ones. Regularly check grades in Blackboard.
- **Assignments:** Grades based on concept mastery and practical application. Includes exams, exercises, discussions, and programming assignments. Lab assignments allow a two-day grace period post-due date with a 20% penalty.
- **Exams:** Must be taken during assigned dates. Online students will use Blackboard from home; classroom students will take exams in class.

## Instructor Communication Plan

- Weekly announcements with reminders, tasks, and encouragement.
- Feedback on exams, discussions, and lab assignments within five days.
- Immediate quiz feedback via auto-grading.

## Technology Requirements

1. Access to a Windows or Mac computer for home testing.
2. Reliable internet access.

## Python Development Environment Setup

We'll use Python for programming. Download the Python interpreter to your computer for free. Any version from 3.8 and higher is acceptable, avoid 2.x.xx versions. Online students must also download IDLE or another Python IDE.

- [Python IDLE](https://docs.python.org/3/library/idle.html)
- [Example of Python IDE](https://www.jetbrains.com/pycharm/download/?section=mac) (PLEASE Download the Community version/ Not the professional)

## Technical Support

Assistance is available for a variety of issues including ACCeID, ACCmail, Blackboard login issues, and more. Visit [ACC Student Services Help Desk](https://www.austincc.edu/helpdesk) for more information.

## Accessibility

Austin Community College is committed to student success and provides accommodations for students with disabilities. Contact the instructor or the Student Accessibility Services & Assistive Technology (SAS) Office at 512-223-5159 to coordinate accommodations.

## Useful Links

- [Blackboard Privacy Statement](https://www.anthology.com/trust-center/privacy-statement)
- [Microsoft Office 365 Free for ACC Students](https://sites.austincc.edu/newsroom/2014/12/05/microsoft-office-365-offered-free-to-acc-students-employees/)
- [ACC Accessibility Resources](https://www.austincc.edu/students/disability-services)
- [Financial Aid](https://students.austincc.edu/financial-aid/apply-for-financial-aid/)
- [Learning Lab](https://students.austincc.edu/learning-lab/)
- [Library Services](https://library.austincc.edu/)
- [Student Conduct](https://students.austincc.edu/student-rights-responsibilities/student-conduct/)
- [CIST Tutoring Schedule](https://sites.austincc.edu/cs/student-resources/csit-tutoring-schedule/)

I am looking forward to a great semester together!

## How to use the repos:
### Test linter local before push:

Run these for install pylint if you don't have 1
```bash
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
python3 -m pip install pylint
cd /path/to/your/project

pylint $(git ls-files '*.py')
```

Run this for local check
```bash
pylint $(git ls-files '*.py')
```
