import sqlite3


class QuokaPipeline(object):
    def __init__(self):
        self.setupDBCon()
        self.createTable()

    def setupDBCon(self):
        self.con = sqlite3.connect('test.db')
        self.cur = self.con.cursor()

    def createTable(self): # deleting and creating Table for avoiding more than one db file creation
        self.cur.execute("DROP TABLE IF EXISTS TaskTable")
        self.createQuokaTable()

    def createQuokaTable(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS TaskTable(id INTEGER PRIMARY KEY NOT NULL, \
            Boersen_ID INTEGER(8), \
            OBID INTEGER(8), \
            erzeugt_am REAL(8), \
            Anbieter_ID TEXT(40), \
            Anbieter_ObjektID TEXT(100), \
            Immobilientyp TEXT(50), \
            Immobilientyp_detail TEXT(200), \
            Vermarktungstyp TEXT(50), \
            Land TEXT(30), \
            Bundesland TEXT(50), \
            Bezirk TEXT(150), \
            Stadt TEXT(150), \
            PLZ TEXT(10), \
            Strasse TEXT(100), \
            Hausnummer TEXT(40), \
            Uberschrift TEXT(500), \
            Beschreibung TEXT(15000), \
            Etage REAL(30), \
            Kaufpreis REAL(8), \
            Kaltmiete REAL(8), \
            Warmmiete REAL(8), \
            Nebenkosten REAL(8), \
            Zimmeranzahl REAL(8), \
            Wohnflaeche REAL(8), \
            Monat INTEGER(8), \
            url TEXT(1000), \
            Telefon REAL(100), \
            Erstellungsdatum TEXT(40), \
            Gewerblich INTEGER(8) \
            )")


    def closeDB(self):
        self.con.close()

    def __del__(self):
        self.closeDB()

    def storeQuokaInDb(self, item):
        self.cur.execute("INSERT INTO TaskTable(\
            Boersen_ID,\
            OBID,\
            erzeugt_am,\
            Anbieter_ID,\
            Anbieter_ObjektID,\
            Immobilientyp,\
            Immobilientyp_detail,\
            Vermarktungstyp,\
            Land,\
            Bundesland,\
            Bezirk,\
            Stadt,\
            PLZ,\
            Strasse,\
            Hausnummer,\
            Uberschrift,\
            Beschreibung,\
            Etage,\
            Kaufpreis,\
            Kaltmiete,\
            Warmmiete,\
            Nebenkosten,\
            Zimmeranzahl,\
            Wohnflaeche,\
            Monat,\
            url,\
            Telefon,\
            Erstellungsdatum,\
            Gewerblich) \
        VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )", \
        (\
            item.get('Boersen_ID'),
            item.get('OBID', ''),
            item.get('erzeugt_am'),
            item.get('Anbieter_ID', ''),
            item.get('Anbieter_ObjektID'),
            item.get('Immobilientyp'),
            item.get('Immobilientyp_detail'),
            item.get('Vermarktungstyp'),
            item.get('Land'),
            item.get('Bundesland'),
            item.get('Bezirk'),
            item.get('Stadt', ''),
            item.get('PLZ', ''),
            item.get('Strasse'),
            item.get('Hausnummer'),
            item.get('Uberschrift', ''),
            ''.join(item.get('Beschreibung', '')),
            item.get('Etage'),
            ''.join(item.get('Kaufpreis', ''))[:-2],
            item.get('Kaltmiete'),
            item.get('Warmmiete'),
            item.get('Nebenkosten'),
            item.get('Zimmeranzahl'),
            item.get('Wohnflaeche'),
            item.get('Monat'),
            item.get('url'),
            ''.join(item.get('Telefon', '')),
            ''.join(item.get('Erstellungsdatum', '')).strip(),
            item.get('Gewerblich')
        ))

        self.con.commit()

    def process_item(self, item, spider):
        self.storeQuokaInDb(item)
        return item

    

