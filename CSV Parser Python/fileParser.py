# from openpyxl import Workbook, load_workbook
# from openpyxl.styles import PatternFill, Border, Side, Font, Color
# from openpyxl.styles import colors
# from openpyxl.cell import Cell
# from openpyxl.utils import get_column_letter

# #DEFINE CELL COLORS
# DARKRED = 'FFC00000'
# RED = 'FFFF0000'
# ORANGE = 'FFFFC000'
# YELLOW = 'FFFFFF00'
# GREEN = 'FF00B050'
# BLUE = 'FF0070C0'
# LIGHTBLUE = 'FF00B0F0'
# PURPLE = 'FF7030A0'
# WHITE = '00000000'
# OTHERWHITE = 'FFFFFFFF'
# black = (0,0,0)
# white = (255,255,255)
# red = (255,0,0)
# green = (0,255,0)
# blue = (0,0,255)
# grey = (128,128,128)

# class cellEditor:
#     def __init__(self,xlsx,sheetIndex=0,row=1,column=65):
#         self.xlsx = xlsx                                    #e.g. "MultipleTimingSP500PMI_xlsx.xlsx"
#         self.workbook = load_workbook(O3filename = self.xlsx)                    #e.g. load_workbook(O3filename = "MultipleTimingSP500PMI_xlsx.xlsx")
#         if debug_CellEditor == True:
#             print("self.workbook: {}".format(self.workbook))
#         self.sheet = self.workbook.worksheets[sheetIndex]                                  #e.g. MyDistribution
#         if debug_CellEditor == True:
#             print("self.sheet: {}".format(self.sheet))
#         self.row = row                                      #e.g. 7
#         self.column = column                                #e.g. A
#         self.coordinates = "{}{}".format(chr(self.column),self.row)   #e.g. 'A7'
#         self.cell = self.sheet["{}".format(self.coordinates)]  #e.g. MyDistribution['A7']
#         self.value = self.cell.value                        #e.g. "this is the text contained in the current cell"

#     #Style change functions
#     def changeCellTextColor(self,color):
#         self.cell.font = Font(color=color)
#         self.saveWorkbook()
#         if (debug_changeCellTextColor == True):
#             self.printCellFont()
#     def changeCellBackgroundColor(self,color):
#         self.cell.fill = color
#         if (debug_changeCellBackgroundColor == True):
#             self.printCellFont()
#     def changeCellFont(self, name = "Calibri (Body)", sz = 11, bold = False, italic = False, underline = False, color = black):
#         self.cell.font = Font(name=name, sz=sz, bold=bold, italic=italic, underline=underline, color=color)
#     #Printing functions
#     def printCellCoordinates(self):
#         print("Current cell coordinates: {}".format(self.coordinates))
#     def printCellValue(self):
#         print("Cell {} value is now: {}".format(self.coordinates,self.cell.value))
#     def printCellBackgroundColor(self):
#         print("Cell {} background color is now: {}".format(self.coordinates,self.cell.fill))
#     def printCellFont(self):
#         print("Cell {} font is now: {}".format(self.coordinates,self.cell.font))

#     #Save xlsx file
#     def saveWorkbook(self, thisO3filename = 0):
#         if thisO3filename == 0:
#             thisO3filename = self.xlsx
#         self.workbook.save(O3filename = "{}".format(self.xlsx))
#         print("{} Saved as {}!".format( self.xlsx, thisO3filename ))

#     #Coordinate change functions
#     def cellCoordAdjust(self):
#         self.coordinates = "{}{}".format(chr(self.column),self.row)
#         self.cell = self.sheet["{}".format(self.coordinates)]
#         self.value = self.cell.value
#     def changeRow(self,value):
#         self.row = value
#         self.cellCoordAdjust()
#         if (debug_changeRow == True):
#             self.printCellCoordinates()
#     def changeColumn(self,value):
#         self.column = value
#         self.cellCoordAdjust()
#         if (debug_changeColumn == True):
#             self.printCellCoordinates()

#     #Value change functions
#     debugCellEditor_changeCellValue = False
#     def changeCellValue(self,text):
#         self.cell.value = text
#         if (debugCellEditor_changeCellValue == True):
#             self.printCellValue()

# O3Editor = cellEditor("O3.csv")
# zEditor = cellEditor("z.csv")

# importing csv module 
import csv 
import sqlite3
  
# csv file name 
O3filename = "molecule_csv.csv"
zfilename = "z_csv.csv"
  
# initializing the titles and rows list 
fields = [] 
O3rows = [] 
zrows = []

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_occulation(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO occulation()
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid

def create_plotData(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
 
    sql = ''' INSERT INTO plotData(occultation_name, altitude, concentration)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid
 

# def create_project(conn, project):
#     """
#     Create a new project into the projects table
#     :param conn:
#     :param project:
#     :return: project id
#     """
#     sql = ''' INSERT INTO projects(name,begin_date,end_date)
#               VALUES(?,?,?) '''
#     cur = conn.cursor()
#     cur.execute(sql, project)
#     return cur.lastrowid

# reading csv file 
with open(O3filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        O3rows.append(row) 
  
    # get total number of O3rows 
    print("Total no. of O3rows: %d"%(csvreader.line_num)) 

with open(zfilename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
    # print(csvreader)
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        zrows.append(row) 
  
    # get total number of rows 
    print("Total no. of zrows: %d"%(csvreader.line_num)) 
  
# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 
  
# create a database connection
conn = create_connection("measurements.db")

# con = sqlite3.connect('measurements.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS occultation")
c.execute("DROP TABLE IF EXISTS plotData")



sql_create_plotData_table = """ CREATE TABLE plotData (
                                        occultation_name text,
                                        altitude real,
                                        concentration text
                                        PRIMARY KEY (occultation_name, altitude)
                                    ); """

sql_create_occultation_table = """ CREATE TABLE occultation (
                                        occultation_name text PRIMARY KEY,
                                        latitude real,
                                        longitude real,
                                        event_type text, 
                                        start_time text,
                                        end_time text
                                    ); """
# cur.execute("CREATE TABLE occultation(occultation_name, latitude, longitude, event_type, start_time, end_time, beta_angle, month)")
# cur.execute("CREATE TABLE plotData(occultation_name, altitude, concentration)")

# create tables
if conn is not None:
    # create projects table
    create_table(conn, sql_create_occultation_table)

    # create tasks table
    create_table(conn, sql_create_plotData_table)
else:
    print("Error! cannot create the database connection.")

# tasks
# plotData_1 = (occultation_name, altitude, concentration)
# occultation_1 = (occultation_name, latitude, longitude, event_type, start_time, end_time)
    

# occultation_1 = (occultation_name, latitude, longitude, event_type, start_time, end_time)


print('\nThe rows are:\n') 
for index, O3row in enumerate(O3rows[:]): 
    if index == 0:
        continue
    zrow = zrows[index]
    # parsing each column of a O3row 
    for jndex, O3col in enumerate(O3row): 
        if jndex == 0:
            continue
        zcol = zrow[jndex]
        if O3col != "-999.0" and O3col != "-888.0":
            print("Concentration at altitude {}km: {}PPV".format(zcol,O3col))
            plotData_1 = (index*100+jndex, zcol, O3col)
            create_plotData(conn, plotData_1)

            # c.execute("INSERT INTO plotData values (?, ?, ?)", (index, zcol, O3col))
