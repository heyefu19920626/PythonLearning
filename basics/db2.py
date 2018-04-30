# 从一台主机上的db2数据库中读取一些数据插入到另一台主机上的数据库中
import ibm_db

import ibm_db
conn = ibm_db.connect(
    "DATABASE=ump;HOSTNAME=192.168.51.17;PORT=50000;PROTOCOL=TCPIP;UID=db2admin;PWD=db2admin;", "", "")
conn_ht = ibm_db.connect(
    "DATABASE=sdgstest;HOSTNAME=192.168.51.121;PORT=50000;PROTOCOL=TCPIP;UID=db2admin;PWD=db2admin;", "", "")
orgtype = 21
#if conn:
while orgtype < 24:
    pass
    print('连接上51.17数据库')
    print('正在转存orgtype = ' + str(orgtype) + '的数据')
    if orgtype == 23:
        sql = "SELECT ORGCODE,BL_SUBCENTER,ORGSNAME,ORGFNAME,ORGTYPE,LASTVER,LANE FROM ETCGSGL.T_ORGCODE  WHERE ORGTYPE=" + str(orgtype) + " AND LASTVER IN (SELECT MAX(LASTVER) FROM ETCGSGL.T_ORGCODE GROUP BY ORGCODE)"
    else:
        sql = "SELECT ORGCODE,BL_CENTER,ORGSNAME,ORGFNAME,ORGTYPE,LASTVER,LANE FROM ETCGSGL.T_ORGCODE  WHERE ORGTYPE=" + str(orgtype) + " AND LASTVER IN (SELECT MAX(LASTVER) FROM ETCGSGL.T_ORGCODE GROUP BY ORGCODE)"
    stmt = ibm_db.exec_immediate(conn, sql)
    result = ibm_db.fetch_both(stmt)
    i = 0
    datas = []
    while(result):
        sql_insert = "INSERT INTO T_RELATIONNEW(ORGCODE,SUPERCODE,ORGSNAME,ORGFNAME,ORGTYPE,LASTVER,LANE) VALUES('%s','%s','%s','%s',%d,'%s','%s')" % (
            result[0], result[1], result[2], result[3], result[4],result[5],result[6])
        try:
            stmt_insert = ibm_db.exec_immediate(conn_ht, sql_insert)
            rows = ibm_db.num_rows(stmt_insert)
        except Exception:
            print(result)
        i += 1
        result = ibm_db.fetch_both(stmt)
    print(i)
    orgtype += 1
if conn != None:
    ibm_db.close(conn)
    ibm_db.close(conn_ht)

