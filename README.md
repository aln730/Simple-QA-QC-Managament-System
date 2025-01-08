Overview:

This code manages a warehouse inventory system using SQLite3 for database operations. It provides functionality to add, view, update, and delete records in a database table named table123.
Features:

    Table Initialization (table123Data):
        Ensures the table123 table exists with the following schema:
            id: Auto-incremented primary key.
            BNO: Batch number (text).
            PRODNAME: Product name (text).
            TYPE: Product type (text).
            IMPORT_DATE: Import date (text).
            SUPP: Supplier (text).
            selected_VALID: Test validity (Yes/No as text).
            STAB: Stability or cost (text).
            FEED: Feed or weight (text).

    Add Record (addStdRec):
        Inserts a new record with sequential IDs. Handles cases where no records exist.

    View Records (viewData):
        Fetches all rows from table123.

    Delete Record (deleteRec):
        Deletes a record by id and renumbers subsequent records to maintain sequential IDs.

    Update Record (dataUpdate):
        Modifies fields of an existing record identified by id.

Setup Instructions:

    Prerequisites:
        Python 3.x installed with SQLite3 (default library).
    Steps:
        Place the code in a Python script file.
        Run table123Data() to initialize the database if not already created.
