import PyQt4.QtSql as sql
import PyQt4.QtCore as QTC
DBDRIVER = 'QPSQL'
DBHOST = 'localhost'
DBPORT = 5432
DBNAME = 'mtgdb'
DBUSERNAME = 'postgres'
DBPASS = ''

def setupDB(driver=DBDRIVER, host=DBHOST, dbname=DBNAME, port=DBPORT, user=DBUSERNAME, pw=DBPASS):
	db = sql.QSqlDatabase(driver)
	db.setHostName(host)
	db.setDatabaseName(dbname)
	db.setPort(port)
	db.setUserName(user)
	db.setPassword(pw)
	bool = db.open()
	if bool:
		return db
	else:
		raise Exception(db.lastError().databaseText())

def insert(data, db, table):
	print db.driver()
	print db.databaseName()
	print db.hostName()
	print db.userName()
	print db.password()
	print db.isOpen()
	print db.connectionName()
	print db.connectOptions()
	query = sql.QSqlQuery(db)
	#db.database().transaction()
	for d in data:
		#print d
		q = 'INSERT INTO {0}'.format(table)
		q += ' ({0})'.format(', '.join([k.lower() for k in d.keys()]))
		q += ' VALUES'
		q += ' ({0});'.format(', '.join([":{0}".format(v.lower()) for v in d.keys()]))
		#print q
		query.prepare(q)
		for k, v in d.items():
			if k == 'cardIds':
				continue
			query.bindValue(":{0}".format(k.lower()), QTC.QVariant(v))
		if not query.exec_():
			print query.executedQuery()
			print query.lastError().text()
			db.close()
			return 
		#print query.executedQuery()
	print query.numRowsAffected()
	#db.database().commit()
	print db.lastError().databaseText()

def getColumnNames(db, table):
	query = sql.QSqlQuery("select column_name from information_schema.columns where table_name='{0}'".format(table), db);
	rtn = []
	while query.next():
		cname = query.value(0).toString()
		rtn.append(str(cname))
	return rtn

def fixString(str,replDbl=True,dblSlash=True,dblSingleQuotes=False):
	"""
	Strips string, and if an empty string, or 'null', sets it to None (NULL)
		# modified 5/22/07, Kerri Reno
		# can't replace double spaces on ks data, or it won't compare
		# properly

	modified 9/12/11, Kerri Reno
	sometimes we need only single slashes, so I added the dblSlash arg
	"""
	if str != None:
		str = r'%s' % str
		str = str.strip()
		if dblSingleQuotes:
			str = str.replace("'","''")
		elif dblSlash:
			str = str.replace("'","\\\'")
			str = str.replace('"','\\\"')
		else:
			str = str.replace("'","''")
			#str = str.replace('"','\"')
		#if ks:
		#	str = str.replace("=","-")
		if replDbl:
			while re.search('  ',str):
				str = re.sub('  ',' ',str)

	if str == '':
		return None
	if str == 'null':
		return None
	else:
		return str

def insertSets(data, db):
	return insert(data, db, 'sets')
	
def insertCards(data, db):
	rulings = []
	formats = []
	for d in data:
		d.pop('colors')
		for key in d:
			if d[key] == '':
				d[key] = None
		if d['flavor']:
			d['flavor'] = fixString(d['flavor'], replDbl=False,
					dblSingleQuotes=True)
		if d['name']:
			d['name'] = fixString(d['name'], replDbl=False,
					dblSingleQuotes=True)
		if d.has_key('rulings'):
			rules = d.pop('rulings')
			if rules and len(rules):
				for rule in rules:
					rule['cardid'] = d['id']
					rulings.append(rule)
		if d.has_key('formats'):
			format = d.pop('formats')
			if format and len(format):
				for f in format:
					f['cardid'] = d['id']
					formats.append(f)
	
	insert(data, db, 'cardinfo')
	insertRulings(rulings, db)
	insertFormats(formats, db)
	
	
def insertRulings(data, db):
	return insert(data, db, 'rulings')
	
def insertFormats(data, db):
	return insert(data, db, 'formats')

def getSets(db):
	rtn = []
	#print db.isOpen()
	query = sql.QSqlQuery( db)
	if not query.exec_('SELECT * FROM sets;'):
		print query.lastQuery()
		print query.lastError().text()
		return rtn
	#print db.isOpen()
	#print query
	#print query.isValid()
	while query.next():
		set = []
		set.append(query.value(1).toString())
		set.append(query.value(2).toString())
		#print set
		rtn.append(set)
	return rtn
	
def getCards(db, set):
	rtn = []
	#print db.isOpen()
	#print "SELECT * FROM where cardsetid = '{0}';".format(set)
	what = '*'
	query = sql.QSqlQuery("SELECT {0} FROM cardinfo where cardsetid = '{1}' order by id;".format(what, set), db)

	#print db.isOpen()
	#print query
	cnames = getColumnNames(db, 'cardinfo')
	while query.next():
		if query.isActive():
			card = {}
			for cname in cnames:
				idx = query.record().indexOf(cname)
				card[str(cname)] = query.value(idx).toString()
		else:
			print query.executedQuery()
			print query.lastError().text()	
		#print set
		rtn.append(card)
	return rtn

def getRulings(db, cardid):
	rtn = []
	query = sql.QSqlQuery("SELECT * FROM rulings WHERE cardid = {0}".format(cardid), db)
	cnames = getColumnNames(db, 'rulings')
	while query.next():
		if query.isActive():
			ruling = {}
			for cname in cnames:
				idx = query.record().indexOf(cname)
				ruling[str(cname)] = query.value(idx).toString()
		else:
			print query.executedQuery()
			print query.lastError().text()
		rtn.append(ruling)
	return rtn
