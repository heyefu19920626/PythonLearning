import ibm_db

import ibm_db
conn = ibm_db.connect(
    "DATABASE=ump;HOSTNAME=192.168.51.17;PORT=50000;PROTOCOL=TCPIP;UID=db2admin;PWD=db2admin;", "", "")
if conn:
    print('连接上')
    sql = "SELECT ORGCODE,BL_CENTER,ORGSNAME,ORGFNAME,ORGTYPE,LASTVER,LANE FROM ETCGSGL.T_ORGCODE  WHERE ORGTYPE=22 AND LASTVER IN (SELECT MAX(LASTVER) FROM ETCGSGL.T_ORGCODE GROUP BY ORGCODE)"
    stmt = ibm_db.exec_immediate(conn, sql)
    result = ibm_db.fetch_both(stmt)
    i = 0
    datas = []
    while(result):
        sql_insert = "INSERT INTO ETCGSGL.T_RELATION(ORGCODE,SUPERCODE,ORGSNAME,ORGFNAME,ORGTYPE,LASTVER,LANE) VALUES('%s','%s','%s','%s',%d,'%s','%s')" % (
            result[0], result[1], result[2], result[3], result[4],result[5],result[6])
        try:
            stmt_insert = ibm_db.exec_immediate(conn, sql_insert)
            rows = ibm_db.num_rows(stmt_insert)
        except Exception:
            print(result)
        i += 1
        result = ibm_db.fetch_both(stmt)
    print("共" + i + "条!")
else:
    print('不能连接')
