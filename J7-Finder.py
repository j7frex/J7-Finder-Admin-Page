#Coder Name : Abdulwahab Al-Ghamdi J7dol FREX
#Do not change rights , Remember the hacker who makes tools , The tools do not make a hacker
import urllib2,os
while True:

    print ("""
 ##############################################################################
 #         ____._________     __________ _______   _______   ___________      #
 #        |    |\______  \    \______   \\   _  \  \   _  \  \__    ___/       #
 #        |    |    /    /     |       _//  /_\  \ /  /_\  \   |    |         #
 #    /\__|    |   /    /      |    |   \\  \_/   \\  \_/   \  |    |           #
 #    \________|  /____/       |____|_  / \_____  / \_____  /  |____|         #
 #                                    \/        \/        \/                  #
 # version  : 1.0v                                                            #
 # coded by : AbdulWahab Al-Ghamdi J7dol FREX                                 #
 # Skype    : Live:J7r00t                                                     #
 # Facebook : J7FRX
 ##############################################################################
""")
    admin_site = list(open("admin.txt","r"))
    print (" - Warning : Add a link like this > [http://www.localhost.com] ")
    web_url = raw_input(" - URL : ")
    
    if "http://" not in web_url:
        if "https://" in web_url:
            web_url = web_url.replace("https://","http://")
        else:
            web_url = "http://"+web_url
            
    if not web_url.endswith("/"):
        web_url = web_url+"/"
    print("\n")

    admin_url_site = []
    for i in admin_site:
        try:
            open_web_url = urllib2.urlopen(web_url+i)
            if open_web_url:
                print " [+] Found : "+web_url+i 
                admin_url_site.append(web_url+i)
        except:
            print " [!] Not Found : "+i

    print "---------------------------------------------------\n - Found ones : "
    for found in admin_url_site:
        print (found)

    raw_input("\n ...")
    os.system("cls" or "clear")
    print "- Found ones : "
    for found in admin_url_site:
        print (found)