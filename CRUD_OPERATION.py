import mysql.connector
from datetime import datetime

# Database connection setup
def create_database_and_tables():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"
    )
    cursor = db.cursor()

    # Create database
    cursor.execute("CREATE DATABASE IF NOT EXISTS wedding_management")
    print("Database 'wedding_management' created.")

    # Select the database
    cursor.execute("USE wedding_management")

    # Create Event Management Team table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS EventManagementTeam (
            team_id INT AUTO_INCREMENT PRIMARY KEY,
            team_name VARCHAR(255) NOT NULL,
            contact_info VARCHAR(255) NOT NULL
        )
    """)
    print("Table 'EventManagementTeam' created.")

    # Create Photographer table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Photographer (
            photographer_id INT AUTO_INCREMENT PRIMARY KEY,
            photographer_name VARCHAR(255) NOT NULL,
            contact_info VARCHAR(255) NOT NULL,
            rating FLOAT NOT NULL CHECK (rating >= 0 AND rating <= 5)
        )
    """)
    print("Table 'Photographer' created.")

    # Create Catering table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Catering (
            catering_id INT AUTO_INCREMENT PRIMARY KEY,
            catering_name VARCHAR(255) NOT NULL,
            contact_info VARCHAR(255) NOT NULL,
            rating FLOAT NOT NULL CHECK (rating >= 0 AND rating <= 5)
        )
    """)
    print("Table 'Catering' created.")

    # Create Makeup Studio table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS MakeupStudio (
            studio_id INT AUTO_INCREMENT PRIMARY KEY,
            studio_name VARCHAR(255) NOT NULL,
            contact_info VARCHAR(255) NOT NULL,
            rating FLOAT NOT NULL CHECK (rating >= 0 AND rating <= 5)
        )
    """)
    print("Table 'MakeupStudio' created.")

    # Create Wedding Event table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS WeddingEvent (
            event_id INT AUTO_INCREMENT PRIMARY KEY,
            event_name VARCHAR(255) NOT NULL,
            date DATE NOT NULL,
            venue VARCHAR(255) NOT NULL,
            team_id INT,
            photographer_id INT,
            catering_id INT,
            studio_id INT,
            overall_rating FLOAT NOT NULL CHECK (overall_rating >= 0 AND overall_rating <= 5),
            FOREIGN KEY (team_id) REFERENCES EventManagementTeam(team_id),
            FOREIGN KEY (photographer_id) REFERENCES Photographer(photographer_id),
            FOREIGN KEY (catering_id) REFERENCES Catering(catering_id),
            FOREIGN KEY (studio_id) REFERENCES MakeupStudio(studio_id)
        )
    """)
    print("Table 'WeddingEvent' created.")

    # Close the database connection
    cursor.close()
    db.close()

# Main functionality
def main():
    # Create database and tables
    create_database_and_tables()

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="wedding_management"
    )
    cursor = db.cursor()

    while True:
        print("\nWedding Management System")
        print("1. Add Event Management Team")
        print("2. View Event Management Team")
        print("3. Update Event Management Team")
        print("4. Delete Event Management Team")
        print("5. Add Photographer")
        print("6. View Photographers")
        print("7. Update Photographer")
        print("8. Delete Photographer")
        print("9. Add Catering")
        print("10. View Catering")
        print("11. Update Catering")
        print("12. Delete Catering")
        print("13. Add Makeup Studio")
        print("14. View Makeup Studios")
        print("15. Update Makeup Studio")
        print("16. Delete Makeup Studio")
        print("17. Add Wedding Event")
        print("18. View Wedding Events")
        print("19. Update Wedding Event")
        print("20. Delete Wedding Event")
        print("21. Exit")

        choice = input("Select an option (1-21): ")

        if choice == '1':
            add_event_management_team(cursor, db)
        elif choice == '2':
            view_event_management_team(cursor)
        elif choice == '3':
            update_event_management_team(cursor, db)
        elif choice == '4':
            delete_event_management_team(cursor, db)
        elif choice == '5':
            add_photographer(cursor, db)
        elif choice == '6':
            view_photographers(cursor)
        elif choice == '7':
            update_photographer(cursor, db)
        elif choice == '8':
            delete_photographer(cursor, db)
        elif choice == '9':
            add_catering(cursor, db)
        elif choice == '10':
            view_catering(cursor)
        elif choice == '11':
            update_catering(cursor, db)
        elif choice == '12':
            delete_catering(cursor, db)
        elif choice == '13':
            add_makeup_studio(cursor, db)
        elif choice == '14':
            view_makeup_studios(cursor)
        elif choice == '15':
            update_makeup_studio(cursor, db)
        elif choice == '16':
            delete_makeup_studio(cursor, db)
        elif choice == '17':
            add_wedding_event(cursor, db)
        elif choice == '18':
            view_wedding_events(cursor)
        elif choice == '19':
            update_wedding_event(cursor, db)
        elif choice == '20':
            delete_wedding_event(cursor, db)
        elif choice == '21':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

    # Close the database connection
    cursor.close()
    db.close()

# CRUD Operations
def add_event_management_team(cursor, db):
    team_name = input("Enter team name: ")
    contact_info = input("Enter contact info: ")
    
    query = "INSERT INTO EventManagementTeam (team_name, contact_info) VALUES (%s, %s)"
    cursor.execute(query, (team_name, contact_info))
    db.commit()
    print("Event Management Team added.")

def view_event_management_team(cursor):
    cursor.execute("SELECT * FROM EventManagementTeam")
    results = cursor.fetchall()   #to display all the rows from table
    for row in results:
        print(f"Team ID: {row[0]}, Team Name: {row[1]}, Contact Info: {row[2]}")

def update_event_management_team(cursor, db):
    team_id = int(input("Enter Team ID to update: "))
    new_name = input("Enter new team name: ")
    new_contact = input("Enter new contact info: ")
    
    query = "UPDATE EventManagementTeam SET team_name = %s, contact_info = %s WHERE team_id = %s"
    cursor.execute(query, (new_name, new_contact, team_id))
    db.commit()
    print("Event Management Team updated.")

def delete_event_management_team(cursor, db):
    team_id = int(input("Enter Team ID to delete: "))
    query = "DELETE FROM EventManagementTeam WHERE team_id = %s"
    cursor.execute(query, (team_id,))
    db.commit()
    print("Event Management Team deleted.")

def add_photographer(cursor, db):
    name = input("Enter photographer name: ")
    contact = input("Enter contact info: ")
    rating = float(input("Enter rating (0-5): "))
    
    query = "INSERT INTO Photographer (photographer_name, contact_info, rating) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, contact, rating))
    db.commit()
    print("Photographer added.")

def view_photographers(cursor):
    cursor.execute("SELECT * FROM Photographer")
    results = cursor.fetchall()
    for row in results:
        print(f"Photographer ID: {row[0]}, Name: {row[1]}, Contact: {row[2]}, Rating: {row[3]}")

def update_photographer(cursor, db):
    photographer_id = int(input("Enter Photographer ID to update: "))
    new_name = input("Enter new photographer name: ")
    new_contact = input("Enter new contact info: ")
    new_rating = float(input("Enter new rating (0-5): "))
    
    query = "UPDATE Photographer SET photographer_name = %s, contact_info = %s, rating = %s WHERE photographer_id = %s"
    cursor.execute(query, (new_name, new_contact, new_rating, photographer_id))
    db.commit()
    print("Photographer updated.")

def delete_photographer(cursor, db):
    photographer_id = int(input("Enter Photographer ID to delete: "))
    query = "DELETE FROM Photographer WHERE photographer_id = %s"
    cursor.execute(query, (photographer_id,))
    db.commit()
    print("Photographer deleted.")

def add_catering(cursor, db):
    name = input("Enter catering name: ")
    contact = input("Enter contact info: ")
    rating = float(input("Enter rating (0-5): "))
    
    query = "INSERT INTO Catering (catering_name, contact_info, rating) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, contact, rating))
    db.commit()
    print("Catering Service added.")

def view_catering(cursor):
    cursor.execute("SELECT * FROM Catering")
    results = cursor.fetchall()
    for row in results:
        print(f"Catering ID: {row[0]}, Name: {row[1]}, Contact: {row[2]}, Rating: {row[3]}")

def update_catering(cursor, db):
    catering_id = int(input("Enter Catering ID to update: "))
    new_name = input("Enter new catering name: ")
    new_contact = input("Enter new contact info: ")
    new_rating = float(input("Enter new rating (0-5): "))
    
    query = "UPDATE Catering SET catering_name = %s, contact_info = %s, rating = %s WHERE catering_id = %s"
    cursor.execute(query, (new_name, new_contact, new_rating, catering_id))
    db.commit()
    print("Catering Service updated.")

def delete_catering(cursor, db):
    catering_id = int(input("Enter Catering ID to delete: "))
    query = "DELETE FROM Catering WHERE catering_id = %s"
    cursor.execute(query, (catering_id,))
    db.commit()
    print("Catering Service deleted.")

def add_makeup_studio(cursor, db):
    name = input("Enter makeup studio name: ")
    contact = input("Enter contact info: ")
    rating = float(input("Enter rating (0-5): "))
    
    query = "INSERT INTO MakeupStudio (studio_name, contact_info, rating) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, contact, rating))
    db.commit()
    print("Makeup Studio added.")

def view_makeup_studios(cursor):
    cursor.execute("SELECT * FROM MakeupStudio")
    results = cursor.fetchall()
    for row in results:
        print(f"Studio ID: {row[0]}, Name: {row[1]}, Contact: {row[2]}, Rating: {row[3]}")

def update_makeup_studio(cursor, db):
    studio_id = int(input("Enter Makeup Studio ID to update: "))
    new_name = input("Enter new makeup studio name: ")
    new_contact = input("Enter new contact info: ")
    new_rating = float(input("Enter new rating (0-5): "))
    
    query = "UPDATE MakeupStudio SET studio_name = %s, contact_info = %s, rating = %s WHERE studio_id = %s"
    cursor.execute(query, (new_name, new_contact, new_rating, studio_id))
    db.commit()
    print("Makeup Studio updated.")

def delete_makeup_studio(cursor, db):
    studio_id = int(input("Enter Makeup Studio ID to delete: "))
    query = "DELETE FROM MakeupStudio WHERE studio_id = %s"
    cursor.execute(query, (studio_id,))
    db.commit()
    print("Makeup Studio deleted.")

def add_wedding_event(cursor, db):
    event_name = input("Enter event name: ")
    date = input("Enter event date (YYYY-MM-DD): ")
    venue = input("Enter venue: ")
    team_id = int(input("Enter Event Management Team ID: "))
    photographer_id = int(input("Enter Photographer ID: "))
    catering_id = int(input("Enter Catering ID: "))
    studio_id = int(input("Enter Makeup Studio ID: "))
    overall_rating = float(input("Enter overall rating (0-5): "))
    
    query = """
        INSERT INTO WeddingEvent (event_name, date, venue, team_id, photographer_id, catering_id, studio_id, overall_rating)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (event_name, date, venue, team_id, photographer_id, catering_id, studio_id, overall_rating))
    db.commit()
    print("Wedding Event added.")

def view_wedding_events(cursor):
    query = """
        SELECT 
            WeddingEvent.event_id, 
            WeddingEvent.event_name, 
            WeddingEvent.date, 
            WeddingEvent.venue, 
            EventManagementTeam.team_name AS management_team, 
            Photographer.photographer_name AS photographer,
            Catering.catering_name AS catering,
            MakeupStudio.studio_name AS makeup_studio,
            WeddingEvent.overall_rating
        FROM WeddingEvent
        LEFT JOIN EventManagementTeam ON WeddingEvent.team_id = EventManagementTeam.team_id
        LEFT JOIN Photographer ON WeddingEvent.photographer_id = Photographer.photographer_id
        LEFT JOIN Catering ON WeddingEvent.catering_id = Catering.catering_id
        LEFT JOIN MakeupStudio ON WeddingEvent.studio_id = MakeupStudio.studio_id
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("\n--- Wedding Events ---")
    for row in results:
        print(f"Event ID: {row[0]}, Event Name: {row[1]}, Date: {row[2]}, Venue: {row[3]}, Management Team: {row[4]}, Photographer: {row[5]}, Catering: {row[6]}, Makeup Studio: {row[7]}, Overall Rating: {row[8]}")

def update_wedding_event(cursor, db):
    event_id = int(input("Enter Event ID to update: "))
    new_name = input("Enter new event name: ")
    new_date = input("Enter new event date (YYYY-MM-DD): ")
    new_venue = input("Enter new venue: ")
    new_team_id = int(input("Enter new Event Management Team ID: "))
    new_photographer_id = int(input("Enter new Photographer ID: "))
    new_catering_id = int(input("Enter new Catering ID: "))
    new_studio_id = int(input("Enter new Makeup Studio ID: "))
    new_rating = float(input("Enter new overall rating (0-5): "))
    
    query = """
        UPDATE WeddingEvent SET event_name = %s, date = %s, venue = %s, team_id = %s,
        photographer_id = %s, catering_id = %s, studio_id = %s, overall_rating = %s WHERE event_id = %s
    """
    cursor.execute(query, (new_name, new_date, new_venue, new_team_id, new_photographer_id, new_catering_id, new_studio_id, new_rating, event_id))
    db.commit()
    print("Wedding Event updated.")

def delete_wedding_event(cursor, db):
    event_id = int(input("Enter Event ID to delete: "))
    query = "DELETE FROM WeddingEvent WHERE event_id = %s"
    cursor.execute(query, (event_id,))
    db.commit()
    print("Wedding Event deleted.")

if __name__ == "__main__":
    main()
