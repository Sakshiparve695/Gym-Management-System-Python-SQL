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
    # ----------------ATTENDANCE------------------
    def mark_attendance(self):
        try:
            member_id = int(input("Enter Member ID: "))
            visit_date = input("Enter visit date (YYYY-MM-DD): ")

            query = "INSERT INTO attendance(member_id, visit_date) VALUES (%s,%s)"
            values = (member_id, visit_date)

            self.cursor.execute(query, values)
            self.conn.commit()

            print("Attendance recorded successfully")

        except Exception as e:
            print("Error:", e)
    # -------------------ACTIVE MEMBERS-------------------
    def top_active_members(self):
        try:
            query = """
            SELECT member_id, COUNT(*) AS visits
            FROM attendance
            GROUP BY member_id
            ORDER BY visits DESC
            LIMIT 5
                """

            self.cursor.execute(query)
            rows = self.cursor.fetchall()

            print("\nTop Active Members:")

            for r in rows:
                print("Member ID:", r[0], "| Visits:", r[1])

        except Exception as e:
            print("Error:", e)

    # ---------------CHURN PREDICTION------------------
    def churn_prediction(self):

        import pandas as pd
        from sklearn.linear_model import LogisticRegression

        query = """
        SELECT member_id, COUNT(*) AS visits
        FROM attendance
        GROUP BY member_id
        """

        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        df = pd.DataFrame(rows, columns=["member_id","visits"])

        # simple churn rule
        df["churn"] = df["visits"].apply(lambda x: 1 if x < 5 else 0)

        X = df[["visits"]]
        y = df["churn"]

        model = LogisticRegression()
        model.fit(X, y)

        df["prediction"] = model.predict(X)

        print("\n=== Churn Prediction ===")

        for i,row in df.iterrows():
            if row["prediction"] == 1:
                print("Member", row["member_id"], "→ HIGH CHURN RISK")
            else:
                print("Member", row["member_id"], "→ LOW CHURN RISK")

    # ---------------- ATTENDANCE CHART ------------------
    def show_visit_chart(self):

        import pandas as pd
        import matplotlib.pyplot as plt

        query = """
        SELECT member_id, COUNT(*) AS visits
        FROM attendance
        GROUP BY member_id
        """

        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        df = pd.DataFrame(rows, columns=["member_id","visits"])

        plt.bar(df["member_id"], df["visits"])
        plt.xlabel("Member ID")
        plt.ylabel("Number of Visits")
        plt.title("Gym Attendance Analytics")

        plt.show()   

    # -----------------INACTIVE MEMBERS ---------------
    def gym_insights(self):

        import pandas as pd

        query = """
        SELECT member_id, COUNT(*) AS visits
        FROM attendance
        GROUP BY member_id
        """

        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        df = pd.DataFrame(rows, columns=["member_id","visits"])

        print("\n=== Gym Insights ===")

        avg_visits = df["visits"].mean()
        print("Average visits per member:", round(avg_visits,2))

        for i,row in df.iterrows():

            if row["visits"] >= 10:
                print("Member",row["member_id"],"is highly active")

            elif row["visits"] < 3:
                print("Member",row["member_id"],"has low attendance → Offer retention plan") 
# -------- MAIN PROGRAM --------
obj = GymDB()

while True:
    print("\n====== GYM MANAGEMENT SYSTEM ======")
    print("1. Add Member")
    print("2. View Members")
    print("3. Update Member")
    print("4. Delete Member")
    print("5. Mark Attendance")
    print("6. View Top Active Members")
    print("7. Predict Churn Risk")
    print("8. Show Attendance Chart")
    print("9. Generate Gym Insights")
    print("10. Exit")
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
        obj.mark_attendance()
    elif choice == "6":
        obj.top_active_members()

    elif choice == "7":
        obj.churn_prediction()

    elif choice == "8":
        obj.show_visit_chart()

    elif choice == "9":
        obj.gym_insights()

    elif choice == "10":
        print("Exiting program")
        break
