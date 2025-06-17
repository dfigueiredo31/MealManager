import sqlite3 as db
import os
from entities.User import User
from entities.Diet import Diet
from entities.Intolerance import Intolerance

## DB Setup ##
with db.connect("appdata.db") as conn:
    cur = conn.cursor()
    cur.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            first_name TEXT,
            last_name TEXT,
            email TEXT UNIQUE,
            birthday TEXT,
            height REAL,
            weight REAL
        );

        CREATE TABLE IF NOT EXISTS diets (
            description TEXT UNIQUE
        );

        INSERT OR IGNORE INTO diets VALUES 
            ('Gluten Free'),
            ('Ketogenic'),
            ('Vegetarian'),
            ('Lacto-Vegetarian'),
            ('Ovo-Vegetarian'),
            ('Vegan'),
            ('Pescetarian'),
            ('Paleo'),
            ('Primal'),
            ('Whole30');

        CREATE TABLE IF NOT EXISTS intolerances (
            description TEXT UNIQUE
        );

        INSERT OR IGNORE INTO intolerances VALUES
            ('dairy'),
            ('egg'),
            ('gluten'),
            ('peanut'),
            ('sesame'),
            ('seafood'),
            ('shellfish'),
            ('soy'),
            ('sulfite'),
            ('tree nut'),
            ('wheat');

        CREATE TABLE IF NOT EXISTS user_diets (
            user_id INTEGER,
            diet_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES user(rowid),
            FOREIGN KEY (diet_id) REFERENCES diets(rowid)
        );
        
        CREATE TABLE IF NOT EXISTS user_intolerances (
            user_id INTEGER,
            intolerance_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES user(rowid),
            FOREIGN KEY (intolerance_id) REFERENCES intolerances(rowid)
        );

    """
    )

    conn.commit()

## User entities ##


## Create ##
def addUser(User: User):
    """Creates a new user

    Args:
        User (User): The user object to be saved into the database
    """
    with db.connect("appdata.db") as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users VALUES (?,?,?,?,?,?)",
            (
                User.firstname,
                User.lastname,
                User.email,
                User.birthday,
                User.height,
                User.weight,
            ),
        )
        conn.commit()


def addUserDiets(user: User):
    with db.connect("appdata.db") as conn:
        cur = conn.cursor()
        for diet in user.preferedDiets:
            cur.execute("INSERT INTO user_diets VALUES (?,?)", (user.id, diet.id))
        conn.commit()


def addUserIntolerances(user: User):
    with db.connect("appdata.db") as conn:
        cur = conn.cursor()
        for intolerance in user.intolerances:
            cur.execute(
                "INSERT INTO user_intolerances VALUES (?,?)", (user.id, intolerance.id)
            )
        conn.commit()


## Read ##
def getUser(email: str) -> User:
    """Given an email, returns the respective user

    Args:
        email (str): The user's email

    Returns:
        User: An user object
    """
    with db.connect("appdata.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT rowid,* FROM users WHERE email = ?", (email,))
        row = cur.fetchone()

        if row is None:
            return None

        user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

        user.preferedDiets = getUserDiets(user.id)
        user.intolerances = getUserIntolerances(user.id)
        return user


def getDiets(id: int = None) -> list:
    """If given an id, returns that specific diet, else returns all recorded diets

    Args:
        id (int, optional): diet id. Defaults to None.

    Returns:
        list: returns a list of diets
    """
    with db.connect("appdata.db") as conn:
        cur = conn.cursor()
        result = []
        if id == None:
            cur.execute("SELECT rowid, * FROM diets")
        else:
            cur.execute("SELECT rowid, * FROM diets WHERE rowid = ?", (id,))

        for row in cur.fetchall():
            result.append(Diet(row[0], row[1]))
        return result


def getIntolerances(id: int = None) -> list:
    """If given an id, returns that specific food intolerance, else returns all recorded intolerances

    Args:
        id (int, optional): intolerance id. Defaults to None.

    Returns:
        list: returns a list of intolerances
    """
    with db.connect("appdata.db") as conn:
        cur = conn.cursor()
        result = []
        if id == None:
            cur.execute("SELECT rowid, * FROM intolerances")
        else:
            cur.execute("SELECT rowid, * FROM intolerances WHERE rowid = ?", (id,))

        for row in cur.fetchall():
            result.append(Intolerance(row[0], row[1]))
        return result


def getUserDiets(userId: int) -> list:
    with db.connect("appdata.db") as conn:
        cur = conn.cursor()
        result = []
        cur.execute(
            """
            SELECT a.rowid, a.* FROM diets a 
            JOIN user_diets b ON a.rowid = b.diet_id 
            JOIN users c ON c.rowid = b.user_id 
            WHERE c.rowid = ?
            """,
            (userId,),
        )

        for row in cur.fetchall():
            result.append(Diet(row[0], row[1]))
        return result


def getUserIntolerances(userId: int) -> list:
    with db.connect("appdata.db") as conn:
        cur = conn.cursor()
        result = []
        cur.execute(
            """
            SELECT a.rowid, a.* FROM intolerances a 
            JOIN user_intolerances b ON a.rowid = b.intolerance_id 
            JOIN users c ON c.rowid = b.user_id 
            WHERE c.rowid = ?
            """,
            (userId,),
        )

        for row in cur.fetchall():
            result.append(Intolerance(row[0], row[1]))
        return result


## Update ##


def updateUser(user: User):
    with db.connect("appdata.db") as conn:
        cur = conn.cursor()
        cur.execute(
            "UPDATE users SET birthday = ?, height = ?, weight= ?  WHERE email = ?",
            (user.birthday, user.height, user.weight, user.email),
        )

    deleteUserDiets(user.id)
    addUserDiets(user)

    deleteUserIntolerances(user.id)
    addUserIntolerances(user)


## Delete ##


def deleteUserDiets(userId: int):
    with db.connect("appdata.db") as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM user_diets WHERE user_id = ?", (userId,))
        conn.commit()


def deleteUserIntolerances(userId: int):
    with db.connect("appdata.db") as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM user_intolerances WHERE user_id = ?", (userId,))
        conn.commit()


def deleteAllData():
    """Removes all user data

    Returns:
        bool: True if user data was removed, False otherwise
    """
    try:
        conn.close()
        os.remove("appdata.db")
        return True
    except Exception as err:
        print("erro delete", err)
        return False
