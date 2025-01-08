import sqlite3
def table123Data():
    con = sqlite3.connect("qa_system.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS table123(id INTEGER PRIMARY KEY AUTOINCREMENT, BNO text, PRODNAME text, TYPE text, IMPORT_DATE text, SUPP text, selected_VALID text, STAB text, FEED text)")
    con.commit()
    con.close()

def addStdRec(BNO, PRODNAME, TYPE, IMPORT_DATE, SUPP, selected_VALID, STAB, FEED):
    con = sqlite3.connect("qa_system.db")
    cur = con.cursor()


    cur.execute("SELECT MAX(id) FROM table123")
    max_id = cur.fetchone()[0]

    if max_id is None:
        max_id = 0

    try:

        cur.execute("INSERT INTO table123 (id, BNO, PRODNAME, TYPE, IMPORT_DATE, SUPP, selected_VALID, STAB, FEED) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (max_id + 1, BNO, PRODNAME, TYPE, IMPORT_DATE, SUPP, selected_VALID, STAB, FEED))
        con.commit()
    except sqlite3.Error as e:
        print("Error:", e)
    finally:
        con.close()



def viewData():
    con = sqlite3.connect("qa_system.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM table123")
    rows = cur.fetchall()
    con.close()
    return rows
    
def deleteRec(id):
    con = sqlite3.connect("qa_system.db")
    cur = con.cursor()


    cur.execute("SELECT MAX(id) FROM table123")
    max_id = cur.fetchone()[0]


    cur.execute("DELETE FROM table123 WHERE id=?", (id,))
    con.commit()


    if id < max_id:

        cur.execute("UPDATE table123 SET id = id - 1 WHERE id > ?", (id,))
        con.commit()


    con.close()

    
def dataUpdate(id, BNO="", PRODNAME="", TYPE="", IMPORT_DATE="", SUPP="", selected_VALID="", STAB="", FEED=""):
    con = sqlite3.connect("qa_system.db")
    cur = con.cursor()
    try:
        cur.execute("UPDATE table123 SET BNO=?, PRODNAME=?, TYPE=?, IMPORT_DATE=?, SUPP=?, selected_VALID=?, STAB=?, FEED=? WHERE id=?",
                    (BNO, PRODNAME, TYPE, IMPORT_DATE, SUPP, selected_VALID, STAB, FEED, id))
        con.commit()
    except sqlite3.Error as e:
        print("Error:", e)
    finally:
        con.close()



table123Data()
