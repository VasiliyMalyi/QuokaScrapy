import scrapy
from scrapy import Field


class TasksolveItem(scrapy.Item):
    Boersen_ID = Field()
    OBID = Field()
    erzeugt_am = Field()
    Anbieter_ID = Field()
    Anbieter_ObjektID = Field()
    Immobilientyp = Field()
    Immobilientyp_detail = Field()
    Vermarktungstyp = Field()
    Land = Field()
    Bundesland = Field()
    Bezirk = Field()
    Stadt = Field()
    PLZ = Field()
    Strasse = Field()
    Hausnummer = Field()
    Uberschrift = Field()
    Beschreibung = Field()
    Etage = Field()
    Kaufpreis = Field()
    Kaltmiete = Field()
    Warmmiete = Field()
    Nebenkosten = Field()
    Zimmeranzahl = Field()
    Wohnflaeche = Field()
    Monat = Field()
    url = Field()
    Telefon = Field()
    Erstellungsdatum = Field()
    Gewerblich = Field()




