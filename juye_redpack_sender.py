#coding:utf-8
from weixin import handler as HD
from weixin import WeixinHelper, JsApi_pub, WxPayConf_pub, UnifiedOrder_pub,Redpack_pub, Notify_pub, catch
import DB


# Using DB Module Connect to the Mysql Server(localhost)
def Connect_Local_Mysql_By_DB(hostname,username,dbname):
	try:
		db = DB.DB(False,host=hostname,user=username,db=dbname) 
	except:
		logging.error('CONNECT TO LOCAL DB SERVER ERROR!');
		exit(1)
	return db

#db = connect_online_db('10.40.38.51',3306,'game','gametest','ads_res','/tmp/mysql.sock')
# Connect to Mysql Server (remote)
def Connent_Online_Mysql_By_DB(hostname,port,username,pwd,dbname,socket):
	try:
		db = DB.DB(False,host=hostname, port=port, user=username ,passwd=pwd, db=dbname,charset='gbk', unix_socket=socket) 
	except Exception,e: 
		logging.error('CONNECT TO MUSQL SERVER ERROR! | [EXCEPTION]:' +(str)(e) )
		exit(1)
	return db
	
# Release DB resource
def release_db(db):
	db.close()

def redpack_sender(db):
	# 尚未发送红包的用户
	redpack_send_users_infos = db.select('select a.id,b.wx_openid from hongbao_issue a,hongbao_user b where a.winner_user_id = b.id and a.prize_status=1 and a.id > 50 and a.status=0')
	for redpack_send_users_info in redpack_send_users_infos:
		issue_id = (int)(redpack_send_users_info[0])
		openid = redpack_send_users_info[1]
		redpack_sender = Redpack_pub()
		redpack_sender.setParameter("re_openid",openid)
		redpack_sender.setParameter("send_name","桔叶商城")
		redpack_sender.setParameter("total_amount","1000")
		redpack_sender.setParameter("total_num","1")
		redpack_sender.setParameter("wishing","新年大吉！")
		redpack_sender.setParameter("client_ip","123.57.1.71")
		redpack_sender.setParameter("act_name","抢10元红包活动")
		redpack_sender.setParameter("remark","发红包啦")
		send_redpack = redpack_sender.send_pack()
		print send_redpack
		# 存入数据库
		if 'result_code' in send_redpack and send_redpack['result_code'] == 'SUCCESS':
			result_dict = {}
			condition_dict = {}
			condition_dict['id'] = issue_id
			result_dict['prize_status'] = 0
			try:
				db.update('hongbao_issue',result_dict,condition_dict)
			except:
				print issue_id,"期发送红包出错！"



if __name__ == '__main__':
	db = Connent_Online_Mysql_By_DB('rdsjjuvbqjjuvbqout.mysql.rds.aliyuncs.com',3306,'dongsh','5561225','juye_hongbao','/tmp/mysql.sock')
	redpack_sender(db)
