import sqlite3
<<<<<<< HEAD
conn = sqlite3.connect('/home/OPEN/sql_test1.db')
print("connect scuccessful")
c = conn.cursor()
c.executescript('''
DROP TABLE IF EXISTS EVENT;
-- DROP TABLE IF EXISTS CAMERA;
-- DROP TABLE IF EXISTS TCASE;
-- DROP TABLE IF EXISTS LOG;
-- DROP TABLE IF EXISTS PERSON;
=======
conn = sqlite3.connect('sql_test1.db')
print("connect scuccessful")
c = conn.cursor()
c.executescript('''
DROP TABLE IF EXISTS PLATE;
DROP TABLE IF EXISTS EVENT;
DROP TABLE IF EXISTS CAMERA;
DROP TABLE IF EXISTS TRACK;
DROP TABLE IF EXISTS LOG;
>>>>>>> 526c87d2e230a0a737753f958fe46384ff23d963
DROP TABLE IF EXISTS SEARCH;
''')

c.executescript('''

  CREATE TABLE EVENT (
<<<<<<< HEAD
    eventID	 INTEGER PRIMARY KEY AUTOINCREMENT, -- 事件編號
=======
    eventID	 NVARCHAR(40)  PRIMARY KEY, -- 事件編號
>>>>>>> 526c87d2e230a0a737753f958fe46384ff23d963
    plateNum    NVARCHAR(10) , -- 車牌
    carColor	INT,  -- 車色
    carType	INT,    -- 車型
    cameraID    NVARCHAR(40) , -- 監視器編號
    address     NVARCHAR(200)  NOT NULL,
    startTime 	DATETIME  NOT NULL, -- 起
    endTime     DATETIME  NOT NULL,  -- 末
    getFileURI  NVARCHAR(250)         NOT NULL, -- 影片連結
    getSnapshotURI NVARCHAR(250)      NOT NULL, -- 快照連結
    FOREIGN KEY(cameraID) REFERENCES CAMERA(cameraID)
); 
 CREATE TABLE CAMERA (
    cameraID      NVARCHAR(100)   PRIMARY KEY , -- 監視器編號
    cameraName    NVARCHAR(20), -- 監視器名稱
    
    district          NVARCHAR(50),  -- 行政區
    precinct          NVARCHAR(100)  NOT NULL, -- 管理該監視器的分局
    policeStation     NVARCHAR(100)  NOT NULL, -- 管理該監視器的派出所
    intersection      NVARCHAR(100)  NOT NULL, -- 管理該監視器的路口
    precinct_store  NVARCHAR(5)  NOT NULL,       --for computer
    policeStation_store  NVARCHAR(5)  NOT NULL,  --for computer
    intersection_store  NVARCHAR(5)  NOT NULL,   --for computer
    
    latitude      REAL  NOT NULL, 
    longitude     REAL  NOT NULL,
    azimuthAngle  INT CHECK( azimuthAngle>=0 AND  azimuthAngle<=360), -- 方位角,
    status 	   INT CHECK(status>=0 AND status<=2)  NOT NULL -- 監視器狀態
);
  
  
CREATE TABLE LOG(
    errorType    INT,       -- 錯誤類型
    msg          NVARCHAR(200)      -- 錯誤訊息
);

CREATE TABLE SEARCH (
<<<<<<< HEAD
    searchID           INTEGER PRIMARY KEY AUTOINCREMENT, -- 每次搜尋產生的ID
    eventID	       INT NOT NULL, -- 事件編號
=======
    searchID           NVARCHAR(40)   NOT NULL, -- 每次搜尋產生的ID
    eventID	        NVARCHAR(40)   NOT NULL, -- 事件編號
>>>>>>> 526c87d2e230a0a737753f958fe46384ff23d963
    personID           NVARCHAR(50)    NOT NULL, --查詢人 ID
    caseID 	        NVARCHAR(30)	 NOT NULL, -- 案號
    searchTime 	DATETIME        NOT NULL, -- 時間
    FOREIGN KEY(eventID) REFERENCES EVENT(eventID)
    FOREIGN KEY(personID) REFERENCES PERSON(personID)
    FOREIGN KEY(caseID) REFERENCES TCASE(caseID)
);

CREATE TABLE TCASE(
    caseID 	        NVARCHAR(5)	 PRIMARY KEY, -- 案號
    reason             NVARCHAR(200)   NOT NULL, -- 案由  : 選單
    reasonDetail       NVARCHAR(1000)   NOT NULL -- 案由 : 用填寫
);
<<<<<<< HEAD
CREATE TABLE PERSON(
    personID           NVARCHAR(50)    PRIMARY KEY, --查詢人 ID
    name	        NVARCHAR(30)    NOT NULL --查詢人名稱
);
=======
>>>>>>> 526c87d2e230a0a737753f958fe46384ff23d963
''')
print("create successful");
conn.commit()
conn.close()
<<<<<<< HEAD














=======
>>>>>>> 526c87d2e230a0a737753f958fe46384ff23d963
