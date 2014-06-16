import PyQt4.QtCore as QTC
from lib import getJson, db
import sys


def insertSets():
	data = getJson.decodeData(getJson.getData(getJson.MTGDBURLSETS))
	dbase = db.setupDB()
	db.insertSet(data, dbase)
	dbase.close()

def insertCards():
	data = getJson.decodeData(getJson.getData(getJson.MTGDBURLCARDS))
	dbase = db.setupDB()
	db.insertCards(data, dbase)
	dbase.close()

if __name__ == '__main__':
	app = QTC.QCoreApplication([])
	insertCards()
	
	sys.exit()