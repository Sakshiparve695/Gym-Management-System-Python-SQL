import mysql.connector

class GymDB:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Sakshi@123",
                database="sakshi_project_db"
            )
            self.cursor = self.conn.cursor()
            print(" Connected to database successfully")

        except Exception as e:
            print(" Connection error:", e)

    # -------- CREATE MEMBER --------
    def add_member(self):
        try:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            plan = int(input("Enter membership plan ID (1/2/3): "))

            query = "INSERT INTO members(name, age,phone, email, plan) VALUES (%s, %s, %s, %s, %s)"
            values = (name, age, phone, email, plan)

            self.cursor.execute(query, values)
            self.conn.commit()

            print(" Member added successfully")

        except Exception as e:
            print(" Error:", e)

    # -------- VIEW MEMBERS --------
    def view_members(self):
        try:
            query = "SELECT * FROM members"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()

            print("\n--- Member List ---")
            for row in rows:
                print(row)

        except Exception as e:
            print(" Error:", e)

    # -------- UPDATE MEMBER --------
    def update_member(self):
        try:
            member_id = int(input("Enter Member ID to update: "))
            #new_plan = input("Enter new plan: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            plan = int(input("Enter membership plan ID (1/2/3): "))

            #query = "UPDATE members SET plan = %s WHERE id = %s"
            #values = (new_plan, member_id)
            query = """
            UPDATE members
            SET name = %s, age = %s , phone = %s, email = %s , plan = %s
            WHERE member_id = %s
            """
            values = (name, age, phone, email, plan, member_id)

            self.cursor.execute(query, values)
            self.conn.commit()

            print(" Member updated successfully")

        except Exception as e:
            print(" Error:", e)

    # -------- DELETE MEMBER --------
    def delete_member(self):
        try:
            member_id = int(input("Enter Member ID to delete: "))

            query = "DELETE FROM members WHERE member_id = %s"
            values = (member_id,)

            self.cursor.execute(query, values)
            self.conn.commit()

            print(" Member deleted successfully!")

        except Exception as e:
            print(" Error:", e)


# -------- MAIN PROGRAM --------
obj = GymDB()

while True:
    print("\n====== GYM MANAGEMENT SYSTEM ======")
    print("1. Add Member")
    print("2. View Members")
    print("3. Update Member")
    print("4. Delete Member")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        obj.add_member()

    elif choice == "2":
        obj.view_members()

    elif choice == "3":
        obj.update_member()

    elif choice == "4":
        obj.delete_member()

    elif choice == "5":
        print(" Exiting program")
        break

    else:
        print(" Invalid choice")