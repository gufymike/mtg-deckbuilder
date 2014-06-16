from PyQt4 import QtGui as QTG
from PyQt4 import QtCore as QTC
from Ui_mainwindow import Ui_MainWindow
import lib.db as dbLib
import sys

class deckBuilder(QTG.QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(deckBuilder, self).__init__(parent)
		self.setupUi(self)
		self.init()
		self.show()
		
		
	def init(self):
		self.db = dbLib.setupDB()

		self.fillSets()
		
	def fillSets(self):
		sets = dbLib.getSets(self.db)
		for set in sets:
			self.setsComboBox.addItem(set[1], set[0])

	def on_setsComboBox_currentIndexChanged(self, idx):
		set = self.setsComboBox.itemData(self.setsComboBox.currentIndex(), QTC.Qt.UserRole)
		#print 'set', set.toString()
		cards = dbLib.getCards(self.db, set.toString())
		self.fillSetTable(cards)

	def on_setCardsTable_cellClicked(self, row, col):
		print row, col
		w = self.setCardsTable.item(row, col)
		print w
		if w:
			data = w.data(QTC.Qt.UserRole).toPyObject()
			self.showCardData(data)

	def fillSetTable(self, cards):
		print 'got card count:', len(cards)
		self.setCardsTable.clear()
		self.setCardsTable.setRowCount(len(cards))
		self.setCardsTable.setColumnCount(1)
		for row, card in enumerate(cards):
			#print card
			tw = QTG.QTableWidgetItem()
			tw.setData(QTC.Qt.DisplayRole, QTC.QVariant(card['name']))
			tw.setData(QTC.Qt.UserRole, QTC.QVariant(card))
			self.setCardsTable.setItem(row, 0, tw)
		self.setCardsTable.resizeColumnsToContents()

	def createTableWidget(self, data):
		tw = QTG.QTableWidgetItem()
		tw.setData(QTC.Qt.DisplayRole, QTC.QVariant(data))
		return tw
	
	def showCardData(self, card):
		self.cardDataTable.clear()
		self.cardDataTable.setColumnCount(2)
		self.cardDataTable.setRowCount(len(card))
		x = 0
		#print card
		rulings = dbLib.getRulings(self.db, int(card[QTC.QString('id')]))
		for k, v in card.items():
			w = self.createTableWidget(k)
			self.cardDataTable.setItem(x, 0, w)
			w = self.createTableWidget(v)
			self.cardDataTable.setItem(x, 1, w)
			x += 1
		self.cardDataTable.resizeColumnsToContents()
		self.rulingsTable.clear()
		self.rulingsTable.setColumnCount(2)
		self.rulingsTable.setRowCount(len(rulings))
		if len(rulings):
			for idx, rule in enumerate(rulings):
				w = self.createTableWidget(rule['releasedat'])
				self.rulingsTable.setItem(idx, 0, w)
				w = self.createTableWidget(rule['rule'])
				self.rulingsTable.setItem(idx, 1, w)
		self.rulingsTable.resizeColumnsToContents()

			
def run():
	app = QTG.QApplication([])
	w = deckBuilder()
	sys.exit(app.exec_())
	
	
if __name__ == '__main__':
	run()
	
