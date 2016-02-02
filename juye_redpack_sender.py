#coding:utf-8
from weixin import handler as HD
from weixin import WeixinHelper, JsApi_pub, WxPayConf_pub, UnifiedOrder_pub,Redpack_pub, Notify_pub, catch


if __name__ == '__main__':
	redpack_sender = Redpack_pub()
	redpack_sender.setParameter("re_openid","oTPeLwaIOjcJC1KSPKTvH_Xe28Wk")
	redpack_sender.setParameter("send_name","桔叶商城")
	redpack_sender.setParameter("total_amount","100")
	redpack_sender.setParameter("total_num","1")
	redpack_sender.setParameter("wishing","新年大吉！")
	redpack_sender.setParameter("client_ip","123.57.1.71")
	redpack_sender.setParameter("act_name","抢10元红包活动")
	redpack_sender.setParameter("remark","发红包啦")
	send_redpack = redpack_sender.send_pack()
	print send_redpack
