import csv
import sqlite3
conn = sqlite3.connect('/home/OPEN/sql_test1.db')
print("connect scuccessful")
c = conn.cursor()
# how many rows now
def print_now(table_name):    
   c.execute("SELECT COUNT(*) from {}".format(table_name));
   count = c.fetchone()[0]
   print("The {} has {} rows.".format(table_name, count))
   return count

# insert data
def insert_csv(data_csv, table_name, insert_num, count):
    
  if table_name == 'EVENT':
      with open(data_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i<count:
                continue
            if i>=insert_num:
                break
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = row
            c.execute("INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)".format(table_name),(col1, col2, col3, col4, col5, col6, col7, col8, col9))
    
  '''  
  if table_name == 'CAMERA':
      with open(data_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i<count:
                continue
            if i>=insert_num:
                break
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13 = row
            c.execute("INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(table_name),(col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13))
    '''
  if table_name == 'SEARCH':
    with open(data_csv, newline='') as csvfile:
       reader = csv.reader(csvfile)
       for i, row in enumerate(reader):
               if i<count:
                   continue
               if i>=insert_num:
                   break
               col1, col2, col3, col4 = row
               c.execute("INSERT INTO {} VALUES (NULL, ?, ? , ? , ?)".format(table_name),(col1, col2, col3, col4))
    
  if table_name == 'TCASE':
     with open(data_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
              if i<count:
                continue
              if i>=insert_num:
                break
              col1, col2, col3 = row
              c.execute("INSERT INTO {} VALUES (?, ?, ?)".format(table_name),(col1, col2, col3)) 
  ''' 
  if table_name == 'PERSON':
     with open(data_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
              if i<count:
                continue
              if i>=insert_num:
                break
              col1, col2 = row
              c.execute("INSERT INTO {} VALUES (?, ?)".format(table_name),(col1, col2))
  
  if table_name == 'LOG':
      with open(data_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i<count:
                continue
            if i>=insert_num:
                break
            col1, col2 = row
            c.execute("INSERT INTO {} VALUES (?, ?)".format(table_name),(col1, col2))
    
'''
# del data
def del_data(table_name, delta):
    c.execute("PRAGMA table_info({})".format(table_name))
    c.execute("DELETE FROM {} WHERE rowID IN (SELECT rowID FROM {} ORDER BY rowID DESC LIMIT {})".format(table_name, table_name, delta))


# how many rows now?
#count_CAMERA = print_now('CAMERA')
#count_REASON = print_now('REASON')
#count_LOG = print_now('LOG')




print("EVENT rows:(data:0~100000000 , no insert : -1)")
count_EVENT = print_now('EVENT')
insert_event = int(input())
if insert_event!=-1:
  if insert_event > count_EVENT:
      insert_csv('data.csv', 'EVENT', insert_event, count_EVENT);
  elif insert_event < count_EVENT:
      delta = count_EVENT - insert_event
      del_data('EVENT', delta)
count_EVENT = print_now('EVENT')
print("successful")

'''
if insert_camera!=-1:
#print("CAMERA rows:")
#insert_camera = int(input())
  if insert_camera > count_CAMERA:
      insert_csv('', 'CAMERA', insert_camera, count_CAMERA);
  elif insert_camera < count_CAMERA:
      delta = count_CAMERA - insert_camera
      del_data('CAMERA', delta))
}
count_CAMERA = print_now('CAMERA')
print("successful")
'''

print("SEARCH rows:(data:0~100000000 , no insert : -1)")
count_SEARCH = print_now('SEARCH')
insert_search = int(input())
if insert_search!=-1:
  if insert_search > count_SEARCH:
      insert_csv('SEARCH.csv', 'SEARCH', insert_search, count_SEARCH);
  elif insert_search < count_SEARCH:
      delta = count_SEARCH - insert_search
      del_data('SEARCH', delta)
count_SEARCH = print_now('SEARCH')
print("successful")


print("TCASE rows:(data:0~100000000 , no insert : -1)")
count_SEARCH = print_now('TCASE')
insert_case = int(input())
if insert_case!=-1:
  if insert_case > count_CASE:
      insert_csv('CASE.csv', 'TCASE', insert_case, count_CASE);
  elif insert_case < count_CASE:
      delta = count_CASE - insert_case
      del_data('CASE', delta)

count_CASE = print_now('TCASE')
print("successful")
'''
print("REASON rows:")
count_REASON = print_now('REASON')
insert_reason = int(input())
if insert_reason!=-1:
  if insert_reason > count_REASON:
      insert_csv('', 'REASON', insert_reason, count_REASON);
  elif insert_reason < count_REASON:
      delta = count_REASON - insert_reason
      del_data('REASON', delta)

count_REASON = print_now('REASON')
print("successful");

print("LOG rows:")
count_LOG = print_now('LOG')
insert_log = int(input())
if insert_log!=-1:
  if insert_log > count_LOG:
      insert_csv('', 'LOG', insert_log, count_LOG);
  elif insert_log < count_LOG:
      delta = count_LOG - insert_log
      del_data('LOG', delta)

count_LOG = print_now('LOG')
print("successful")
'''

print("done");
conn.commit()
conn.close()
