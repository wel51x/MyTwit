from mytwit.models import *

u2 = User(id=2, name='austen')
u3 = User(id=3, name='ryanh')
u4 = User(id=4, name='aaron')
u5 = User(id=5, name='troyb')
u6 = User(id=6, name='darwin')

t2 = Tweet(id=2, text='Plants capture CO2 naturally')
t3 = Tweet(id=3, text='You, yeah you – why aren’t you following me?')
t4 = Tweet(id=4, text='This is like harassment')
t5 = Tweet(id=5, text='Coming to Barcelona for your Easter holidays')
t6 = Tweet(id=6, text='Thanks for all the experiences')
t7 = Tweet(id=7, text='That’s dope man! Is it easy to get there?')
t8 = Tweet(id=8, text='Change is coming. Sooner than you think.')
t9 = Tweet(id=9, text='Look at how #5G is driving future innovations in the #IoT space')
t10 = Tweet(id=10, text='Another amazing day at Camp Nou!')
t11 = Tweet(id=11, text='8 Tips On How To Get Your #Home Ready To #Sell')
t12 = Tweet(id=12, text='Several teams are exploring ways to limit their matches versus Barça to 75 minutes.')
t13 = Tweet(id=13, text='@Toyota is upping our investment in U.S. manufacturing +$3 billion by 2021.')
t14 = Tweet(id=14, text='We announced that were forming the Automated Vehicle Safety Consortium™ (AVSC)')
t15 = Tweet(id=15, text='This basketball-loving robot by @Toyota is playing against pro ballers.')
t16 = Tweet(id=16, text='Thats a player the Bulls can draft that wont get hurt.')
t17 = Tweet(id=17, text='Boko Fiddleworth almost had a job once.')
t18 = Tweet(id=18, text='I dont want to be moulded. Im not a jelly.')
t19 = Tweet(id=19, text='It is young men like you who make a person with the future at heart despair.')
t20 = Tweet(id=20, text='If I ever win the lottery, I want a Jeeves.')

u2.tweets.append(t2)
u3.tweets.append(t3)
u4.tweets.append(t4)
u5.tweets.append(t5)
u6.tweets.append(t6)
u2.tweets.append(t7)
u3.tweets.append(t8)
u4.tweets.append(t9)
u5.tweets.append(t10)
u6.tweets.append(t11)
u2.tweets.append(t12)
u3.tweets.append(t13)
u4.tweets.append(t14)
u5.tweets.append(t15)
u6.tweets.append(t16)
u2.tweets.append(t17)
u3.tweets.append(t18)
u4.tweets.append(t19)
u5.tweets.append(t20)

DB.session.add(u2)
DB.session.add(u3)
DB.session.add(u4)
DB.session.add(u5)
DB.session.add(u6)

DB.session.add(t2)
DB.session.add(t3)
DB.session.add(t4)
DB.session.add(t5)
DB.session.add(t6)
DB.session.add(t7)
DB.session.add(t8)
DB.session.add(t9)
DB.session.add(t10)
DB.session.add(t11)
DB.session.add(t12)
DB.session.add(t13)
DB.session.add(t14)
DB.session.add(t15)
DB.session.add(t16)
DB.session.add(t17)
DB.session.add(t18)
DB.session.add(t19)
DB.session.add(t20)

DB.session.commit()

