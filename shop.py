# Script Name	: shopping.py
# Author		: qicloud-jiangxp
# Created		: 2017.12.28
# Last Modified	: 
# Version		: 1.0
#_*_ coding=utf-8 _*_
shop_list = [['apple',2000],['bake',2222],['shoes',800],]
# slary = 9000 
 slary = input("please input moeny num:")
shop_list_list=[]
while True:
    for index,p in enumerate(shop_list):
        print index,p[0],p[1]
    print "input is num;input quit"
    choice = raw_input("choose sth to buy:").strip()
    if choice.isdigit():
        choice = int(choice)
        p_price=shop_list[choice][1]
        if p_price < slary:
            shop_list_list.append(shop_list[choice])
            print shop_list_list
            slary -= p_price
            print "haos added \033[31;1m%s\033[0m into shop list,your current balance is \033[31;1m%s\033[0m" %(shop_list[choice][0],slary)
        else:
            print "\033[41;1mMoney is not enough, try sth else dx \033[0m"
    elif choice == 'quit':
        print '--------shopping list--------'
        for k,v in enumerate(shop_list_list):
            print k,v
        print "your current balance is \033[41;1m%s\033[0m "% slary
        print '---------bye------'
        break
