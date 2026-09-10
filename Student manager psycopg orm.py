"""
Student Management System (SQLAlchemy ORM + psycopg3)
--------------------------------------------------------
Connects Python to PostgreSQL using SQLAlchemy's ORM, with
psycopg (v3) as the underlying database driver.
No raw SQL strings are written anywhere - all operations
use ORM objects, sessions, and query methods.

Requirements:
    pip install sqlalchemy "psycopg[binary]"

Before running:
    1. Make sure PostgreSQL is installed and running.
    2. Create a database (e.g. CREATE DATABASE studentdb;)
    3. Fill in the DB_CONFIG dictionary below with your credentials.

Run:
    python student_manager_psycopg_orm.py
"""

from datetime import date

from sqlalchemy import create_engine, Column, Integer, String, Date, CheckConstraint, func
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError, OperationalError


# ------------------------------------------------------------------
# 1. DATABASE CONFIGURATION - edit these values for your setup
# ------------------------------------------------------------------
DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "dbname": "studentdb",
    "user": "postgres",
    "password": "kavitha%40789",
}

# "+psycopg" tells SQLAlchemy to use psycopg (v3) as the driver,
# instead of the older psycopg2.
DATABASE_URL = (
    f"postgresql+psycopg://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


# ------------------------------------------------------------------
# 2. ORM MODEL (replaces the CREATE TABLE query)
# ------------------------------------------------------------------
class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    age = Column(Integer, CheckConstraint("age > 0"))
    email = Column(String(100), unique=True)
    course = Column(String(100))
    grade = Column(String(5))
    enrolled_on = Column(Date, default=date.today)

    def as_dict(self):
        return {
            "student_id": self.student_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "course": self.course,
            "grade": self.grade,
            "enrolled_on": str(self.enrolled_on),
        }


def create_table():
    """Create tables based on ORM models if they don't already exist."""
    try:
        Base.metadata.create_all(engine)
        print("[OK] 'students' table is ready.")
    except OperationalError as e:
        print(f"\n[ERROR] Could not connect to the database:\n{e}")


# ------------------------------------------------------------------
# 3. CREATE (Insert)
# ------------------------------------------------------------------
def add_student():
    print("\n--- Add New Student ---")
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    age = input("Age: ").strip()
    email = input("Email: ").strip()
    course = input("Course: ").strip()
    grade = input("Grade (optional): ").strip() or None

    if not first_name or not last_name:
        print("[ERROR] First and last name are required.")
        return

    try:
        age = int(age) if age else None
    except ValueError:
        print("[ERROR] Age must be a number.")
        return

    session = SessionLocal()
    try:
        student = Student(
            first_name=first_name,
            last_name=last_name,
            age=age,
            email=email or None,
            course=course or None,
            grade=grade,
        )
        session.add(student)
        session.commit()
        print(f"[OK] Student added with ID {student.student_id}.")
    except IntegrityError:
        session.rollback()
        print("[ERROR] A student with that email already exists.")
    except Exception as e:
        session.rollback()
        print(f"[ERROR] Could not add student: {e}")
    finally:
        session.close()


# ------------------------------------------------------------------
# 4. READ (View all / view one / search)
# ------------------------------------------------------------------
def view_all_students():
    print("\n--- All Students ---")
    session = SessionLocal()
    try:
        students = session.query(Student).order_by(Student.student_id).all()
        if not students:
            print("No students found.")
            return
        _print_table([s.as_dict() for s in students])
    except Exception as e:
        print(f"[ERROR] Could not fetch students: {e}")
    finally:
        session.close()


def view_student_by_id():
    print("\n--- View Student by ID ---")
    sid = input("Enter student ID: ").strip()
    if not sid.isdigit():
        print("[ERROR] ID must be a number.")
        return

    session = SessionLocal()
    try:
        student = session.get(Student, int(sid))
        if student:
            _print_table([student.as_dict()])
        else:
            print("[INFO] No student found with that ID.")
    except Exception as e:
        print(f"[ERROR] Could not fetch student: {e}")
    finally:
        session.close()


def search_students():
    print("\n--- Search Students ---")
    print("Search by: 1) Name  2) Course  3) Grade")
    choice = input("Choose an option: ").strip()

    field_map = {"1": Student.first_name, "2": Student.course, "3": Student.grade}
    field = field_map.get(choice)
    if field is None:
        print("[ERROR] Invalid option.")
        return

    keyword = input("Enter keyword to search: ").strip()

    session = SessionLocal()
    try:
        students = (
            session.query(Student)
            .filter(field.ilike(f"%{keyword}%"))
            .order_by(Student.student_id)
            .all()
        )
        if students:
            _print_table([s.as_dict() for s in students])
        else:
            print("[INFO] No matching students found.")
    except Exception as e:
        print(f"[ERROR] Search failed: {e}")
    finally:
        session.close()


# ------------------------------------------------------------------
# 5. UPDATE
# ------------------------------------------------------------------
def update_student():
    print("\n--- Update Student ---")
    sid = input("Enter student ID to update: ").strip()
    if not sid.isdigit():
        print("[ERROR] ID must be a number.")
        return

    session = SessionLocal()
    try:
        student = session.get(Student, int(sid))
        if not student:
            print("[INFO] No student found with that ID.")
            return

        print("Leave a field blank to keep its current value.")
        first_name = input(f"First name [{student.first_name}]: ").strip()
        last_name = input(f"Last name [{student.last_name}]: ").strip()
        age_input = input(f"Age [{student.age}]: ").strip()
        email = input(f"Email [{student.email}]: ").strip()
        course = input(f"Course [{student.course}]: ").strip()
        grade = input(f"Grade [{student.grade}]: ").strip()

        if first_name:
            student.first_name = first_name
        if last_name:
            student.last_name = last_name
        if age_input:
            student.age = int(age_input)
        if email:
            student.email = email
        if course:
            student.course = course
        if grade:
            student.grade = grade

        session.commit()
        print("[OK] Student updated successfully.")
    except IntegrityError:
        session.rollback()
        print("[ERROR] Another student already uses that email.")
    except Exception as e:
        session.rollback()
        print(f"[ERROR] Could not update student: {e}")
    finally:
        session.close()


# ------------------------------------------------------------------
# 6. DELETE
# ------------------------------------------------------------------
def delete_student():
    print("\n--- Delete Student ---")
    sid = input("Enter student ID to delete: ").strip()
    if not sid.isdigit():
        print("[ERROR] ID must be a number.")
        return

    confirm = input(f"Are you sure you want to delete student {sid}? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("[CANCELLED] Deletion aborted.")
        return

    session = SessionLocal()
    try:
        student = session.get(Student, int(sid))
        if student:
            session.delete(student)
            session.commit()
            print("[OK] Student deleted.")
        else:
            print("[INFO] No student found with that ID.")
    except Exception as e:
        session.rollback()
        print(f"[ERROR] Could not delete student: {e}")
    finally:
        session.close()


def delete_all_students():
    print("\n--- Delete ALL Students ---")
    confirm = input("This will remove ALL records. Type 'DELETE ALL' to confirm: ").strip()
    if confirm != "DELETE ALL":
        print("[CANCELLED] No records were deleted.")
        return

    session = SessionLocal()
    try:
        session.query(Student).delete()
        session.commit()
        print("[OK] All student records deleted.")
    except Exception as e:
        session.rollback()
        print(f"[ERROR] Could not delete all records: {e}")
    finally:
        session.close()


# ------------------------------------------------------------------
# 7. REPORTS / EXTRA OPERATIONS
# ------------------------------------------------------------------
def count_students():
    session = SessionLocal()
    try:
        total = session.query(func.count(Student.student_id)).scalar()
        print(f"\n[INFO] Total students: {total}")
    except Exception as e:
        print(f"[ERROR] Could not count students: {e}")
    finally:
        session.close()


def average_age():
    session = SessionLocal()
    try:
        avg = session.query(func.round(func.avg(Student.age), 2)).scalar()
        print(f"\n[INFO] Average age: {avg if avg is not None else 'N/A'}")
    except Exception as e:
        print(f"[ERROR] Could not compute average age: {e}")
    finally:
        session.close()


# ------------------------------------------------------------------
# 8. UTILITY - pretty print rows
# ------------------------------------------------------------------
def _print_table(rows):
    if not rows:
        return
    headers = list(rows[0].keys())
    col_widths = {h: max(len(h), max(len(str(r[h])) for r in rows)) for h in headers}

    header_line = " | ".join(h.ljust(col_widths[h]) for h in headers)
    print(header_line)
    print("-" * len(header_line))
    for r in rows:
        print(" | ".join(str(r[h]).ljust(col_widths[h]) for h in headers))


# ------------------------------------------------------------------
# 9. MAIN MENU
# ------------------------------------------------------------------
MENU = """
==========================================
   STUDENT MANAGEMENT SYSTEM (psycopg ORM)
==========================================
 1. Add student            (Create)
 2. View all students       (Read)
 3. View student by ID      (Read)
 4. Search students         (Read)
 5. Update student          (Update)
 6. Delete student          (Delete)
 7. Delete ALL students     (Delete)
 8. Count total students    (Report)
 9. Average age             (Report)
 0. Exit
==========================================
"""


def main():
    create_table()
    actions = {
        "1": add_student,
        "2": view_all_students,
        "3": view_student_by_id,
        "4": search_students,
        "5": update_student,
        "6": delete_student,
        "7": delete_all_students,
        "8": count_students,
        "9": average_age,
    }

    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("[ERROR] Invalid choice, try again.")


if __name__ == "__main__":
    main()