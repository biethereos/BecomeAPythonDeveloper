#!/usr/bin/env python3
# Copyright 2021 BHG [bw.org]
# as of 2021-04-07 bw

import sqlite3


def main():
    print("SQLite starting ..... ....... .....")
    
    db = None   # satisfy the warnings monster
    cur = None

    try:
        # using SQLite's transient in-memory database
        db = sqlite3.connect(":memory:")
        cur = db.cursor()
        print("connected")

    except sqlite3.Error as e:
        print(f"could not open database: {e}")
        exit(1)

    try:
        # create a table
        sql_create = '''
            CREATE TABLE IF NOT EXISTS person (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT,
                gender TEXT NOT NULL,
                date_of_birth TEXT NOT NULL,
                country_of_birth TEXT NOT NULL
            ) 
        '''
        cur.execute(sql_create)
        print("table created")

    except sqlite3.Error as e:
        print(f"could not create table: {e}")
        exit(1)

    try:
        # insert rows into the table using executemany
        print("inserting rows")
        row_data = (
            ('Orly', 'Conneau', None, 'Female', '2021-04-09', 'Gabon'),
            ('Jillie', 'Weighell', None, 'Genderfluid', '2021-01-19', 'Bosnia and Herzegovina'),
            ('Chere', 'Waldram', 'cwaldram2@addtoany.com', 'Genderqueer', '2021-03-07', 'Tanzania'),
            ('Betsey', 'Carolan', 'bcarolan3@plala.or.jp', 'Genderqueer', '2020-10-19', 'Indonesia'),
            ('Julius', 'Medgewick', 'jmedgewick4@hp.com', 'Polygender', '2021-06-10', 'Russia'),
            ('Luciana', 'Discombe', 'ldiscombe5@dyndns.org', 'Bigender', '2020-12-07', 'China'),
            ('Gawain', 'Argo', None, 'Polygender', '2021-01-03', 'Denmark'),
            ('Dyanna', 'Whittaker', 'dwhittaker7@toplist.cz', 'Male', '2020-10-24', 'China'),
            ('Angelo', 'Smallacombe', None, 'Male', '2021-05-19', 'France'),
            ('Hortense', 'Steinson', 'hsteinson9@imdb.com', 'Bigender', '2021-04-27', 'Indonesia'),
            ('Myrtie', 'Hargrove', None, 'Female', '2021-08-28', 'Venezuela'),
            ('Guenevere', 'Wooton', None, 'Agender', '2020-12-29', 'Kazakhstan'),
            ('Philipa', 'Piffe', 'ppiffec@google.com.hk', 'Genderqueer', '2021-07-06', 'Argentina'),
            ('Sarina', 'Chown', None, 'Male', '2021-10-01', 'Indonesia'),
            ('Heidi', 'Linguard', 'hlinguarde@shareasale.com', 'Genderqueer', '2021-09-07', 'China'),
            ('Goldi', 'Fortman', 'gfortmanf@odnoklassniki.ru', 'Female', '2020-10-12', 'Colombia'),
            ('Manolo', 'Dreus', 'mdreusg@wisc.edu', 'Genderqueer', '2021-05-22', 'China'),
            ('Bat', 'Gierke', 'bgierkeh@deliciousdays.com', 'Bigender', '2021-10-02', 'China'),
            ('Kippy', 'Laydon', 'klaydoni@telegraph.co.uk', 'Female', '2020-12-29', 'Poland'),
            ('Rodolfo', 'Tideswell', None, 'Agender', '2021-09-16', 'France'),
            ('Jada', 'Cowley', 'jcowleyk@cnet.com', 'Genderqueer', '2021-03-22', 'Guatemala'),
            ('Etan', 'Glabach', 'eglabachl@dailymail.co.uk', 'Bigender', '2021-02-04', 'South Korea'),
            ('Fielding', 'Caulcott', None, 'Bigender', '2021-01-05', 'Thailand'),
            ('Marven', 'Taig', 'mtaign@edublogs.org', 'Bigender', '2020-10-28', 'Malawi'),
            ('Catrina', 'Strowther', 'cstrowthero@kickstarter.com', 'Genderfluid', '2020-11-30', 'Portugal'),
            ('Chandal', 'Malthouse', None, 'Genderfluid', '2021-03-31', 'Bosnia and Herzegovina'),
            ('Ernestus', 'Coker', 'ecokerq@businessinsider.com', 'Genderfluid', '2021-05-11', 'United Kingdom'),
            ('Sybilla', 'Huey', 'shueyr@ovh.net', 'Polygender', '2021-02-12', 'Canada'),
            ('Merilyn', 'Altofts', 'maltoftss@yolasite.com', 'Polygender', '2021-02-24', 'Morocco'),
            ('Inigo', 'Shakesby', 'ishakesbyu@mediafire.com', 'Male', '2021-06-17', 'Philippines'),
            ('Jerri', 'Rowlin', 'jrowlinv@nytimes.com', 'Bigender', '2021-05-25', 'Indonesia'),
            ('Ricky', 'Domone', None, 'Non-binary', '2020-10-16', 'Syria'),
            ('Bartholomeus', 'Guiett', 'bguiettx@washingtonpost.com', 'Agender', '2021-06-12', 'Russia'),
            ('Lothaire', 'MacGinley', 'lmacginleyy@google.co.jp', 'Genderqueer', '2020-11-25', 'Brazil'),
            ('Grenville', 'Wettern', 'gwetternz@exblog.jp', 'Non-binary', '2021-01-01', 'China'),
            ('Bond', 'Pittford', None, 'Male', '2021-08-11', 'China'),
            ('Evania', 'Pierce', 'epierce11@google.co.jp', 'Genderqueer', '2020-12-06', 'Peru'),
            ('Eddie', 'Gerrietz', 'egerrietz12@theatlantic.com', 'Female', '2020-12-11', 'Burkina Faso'),
            ('Kermy', 'Cabel', None, 'Male', '2021-02-09', 'Philippines'),
            ('Carmella', 'Yellowlees', None, 'Female', '2020-10-22', 'Spain'),
            ('Shem', 'Vipan', 'svipan15@wunderground.com', 'Polygender', '2020-11-17', 'China'),
            ('Allie', 'Rowes', None, 'Bigender', '2021-01-16', 'China'),
            ('Hester', 'Hackford', 'hhackford17@engadget.com', 'Female', '2021-06-02', 'Malawi'),
            ('Hermine', 'Dagworthy', 'hdagworthy18@samsung.com', 'Agender', '2021-04-16', 'Peru'),
            ('Lucie', 'Cawcutt', 'lcawcutt19@businesswire.com', 'Bigender', '2021-06-15', 'Czech Republic'),
            ('Annissa', 'Ryves', 'aryves1a@howstuffworks.com', 'Male', '2021-04-02', 'Indonesia'),
            ('Loria', 'Carlick', None, 'Polygender', '2020-11-18', 'Greece'),
            ('Wadsworth', 'Semark', 'wsemark1c@qq.com', 'Genderqueer', '2021-02-02', 'Palestinian Territory'),
            ('Mag', 'Baldacchino', 'mbaldacchino1d@harvard.edu', 'Genderqueer', '2021-08-31', 'China'),
            ('Gillan', 'Barthelme', 'gbarthelme1e@sohu.com', 'Polygender', '2020-11-20', 'China'),
            ('Aridatha', 'Colecrough', 'acolecrough1f@earthlink.net', 'Genderfluid', '2021-02-28', 'Poland')
        )
        cur.executemany("INSERT INTO person (first_name, last_name, email, gender, date_of_birth, country_of_birth) VALUES (?, ?, ?, ?, ?, ?)", row_data)
        count = cur.rowcount
        # cur.executemany("INSERT INTO person (first_name, last_name, email, gender, date_of_birth, country_of_birth) VALUES (?, ?, ?, ?, ?, ?)", row_data)
        # count += cur.rowcount
        # cur.executemany("INSERT INTO person (first_name, last_name, email, gender, date_of_birth, country_of_birth) VALUES (?, ?, ?, ?, ?, ?)", row_data)
        # count += cur.rowcount
        print(f"{count} rows added")
        db.commit()

    except sqlite3.Error as e:
        print(f"could not insert rows: {e}")
        exit(1)

    try:
        # count rows using SELECT COUNT(*)
        cur.execute("SELECT COUNT(*) FROM person")
        count = cur.fetchone()[0]
        print(f"there are {count} rows in the table")

        # get column names from SQLite meta-data table_info
        cur.execute("PRAGMA table_info(person);")
        row = cur.fetchall()
        colnames = [r[1] for r in row]
        print(f"column names are: {colnames}")

        # fetch rows using iterator
        print('\nusing iterator')
        cur.execute("SELECT * FROM person LIMIT 5")
        for row in cur:
            print(row)

        # fetch rows using row_factory
        print('\nusing row_factory')
        cur.execute("SELECT * FROM person LIMIT 5")
        cur.row_factory = sqlite3.Row
        print(cur.row_factory)
        for row in cur:
            print(f"as tuple: {tuple(row)}, as dict: id:{row['id']} first_name:{row['first_name']}, last_name:{row['last_name']}, email:{row['email']}")

        cur.row_factory = None  # reset row factory

        # fetch rows in groups of 5 using fetchmany
        print('\ngroups of 5 using fetchmany')
        cur.execute("SELECT * FROM person")
        rows = cur.fetchmany(5)
        while rows:
            for r in rows:
                print(r)
            print("====== ====== ======")
            rows = cur.fetchmany(5)

        # drop table and close the database
        print('\ndrop table and close connection')
        cur.execute("DROP TABLE IF EXISTS person")  # cleanup if db is not :memory:
        cur.close()
        db.close()

    except sqlite3.Error as e:
        print(f"sqlite3 error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
