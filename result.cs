public class Student
{
    public int RollNumber { get; set; }
    public string Name { get; set; }
    public List<Course> Courses { get; set; }

    public Student(int rollNumber, string name)
    {
        RollNumber = rollNumber;
        Name = name;
        Courses = new List<Course>();
    }
}

public class Course
{
    public string CourseName { get; set; }
    public int Marks { get; set; }

    public Course(string courseName, int marks)
    {
        CourseName = courseName;
        Marks = marks;
    }
}
class Program
{
    static List<Student> students = new List<Student>();

    static void Main(string[] args)
    {
        bool exit = false;

        while (!exit)
        {
            Console.WriteLine("College Result Management System");
            Console.WriteLine("1. Add Student");
            Console.WriteLine("2. Add Course for Student");
            Console.WriteLine("3. Calculate Results");
            Console.WriteLine("4. Exit");
            Console.Write("Enter your choice: ");

            if (int.TryParse(Console.ReadLine(), out int choice))
            {
                switch (choice)
                {
                    case 1:
                        AddStudent();
                        break;
                    case 2:
                        AddCourseForStudent();
                        break;
                    case 3:
                        CalculateResults();
                        break;
                    case 4:
                        exit = true;
                        break;
                    default:
                        Console.WriteLine("Invalid choice. Try again.");
                        break;
                }
            }
            else
            {
                Console.WriteLine("Invalid input. Enter a valid choice.");
            }
        }
    }

    static void AddStudent()
    {
        Console.Write("Enter student roll number: ");
        int rollNumber = int.Parse(Console.ReadLine());
        Console.Write("Enter student name: ");
        string name = Console.ReadLine();

        students.Add(new Student(rollNumber, name));
        Console.WriteLine("Student added successfully.");
    }

    static void AddCourseForStudent()
    {
        Console.Write("Enter student roll number: ");
        int rollNumber = int.Parse(Console.ReadLine());
        var student = students.Find(s => s.RollNumber == rollNumber);

        if (student != null)
        {
            Console.Write("Enter course name: ");
            string courseName = Console.ReadLine();
            Console.Write("Enter marks: ");
            int marks = int.Parse(Console.ReadLine());

            student.Courses.Add(new Course(courseName, marks));
            Console.WriteLine("Course added for the student.");
        }
        else
        {
            Console.WriteLine("Student not found.");
        }
    }

    static void CalculateResults()
    {
        Console.WriteLine("Student Results:");
        foreach (var student in students)
        {
            Console.WriteLine($"Roll Number: {student.RollNumber}, Name: {student.Name}");
            foreach (var course in student.Courses)
            {
                Console.WriteLine($"Course: {course.CourseName}, Marks: {course.Marks}");
            }
            Console.WriteLine($"Total Marks: {student.Courses.Sum(c => c.Marks)}");
            Console.WriteLine($"Average Marks: {student.Courses.Average(c => c.Marks)}");
            Console.WriteLine();
        }
    }
}
