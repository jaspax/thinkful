from tbay import User, Item, Bid, session

# Create Larisa
larisa = User(username='larisa', password='mormoloc')
session.add(larisa)

# Create Jesse
jesse = User(username='jesse', password='pickle')
session.add(jesse)

# Create Brendan
brendan = User(username='brendan', password='cheese')
session.add(brendan)

session.commit()

# Add a baseball
baseball = Item(name='baseball', description='A very nice baseball indeed', seller=jesse)
session.add(baseball)
session.commit()

# Larisa and Brendan bid
lbid = Bid(price=0.20, item=baseball, bidder=larisa)
bbid = Bid(price=0.25, item=baseball, bidder=brendan)
session.add(lbid)
session.add(bbid)
session.commit()

# Find the highest bid
highbid = session.query(Bid).filter(Bid.item == baseball).order_by(Bid.price.desc()).first()

print "{} bought a {} ('{}') for {}".format(highbid.bidder.username, highbid.item.name, highbid.item.description, highbid.price)
