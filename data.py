from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from database_setup import *

engine = create_engine('sqlite:///catalogdb.db')
# Binds the engine to the metadata of the Base class such that the
# declaratives can be accessed via a DBSession instance

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.
# If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback() function.

session = DBSession()

# Deleting Categories, items and users if exisitng.
session.query(Category).delete()

session.query(Items).delete()

session.query(User).delete()

# Creating a fake user:
User1 = User(name="Arpit Malik",
              email="arpitmalik04@gmail.com",
              picture='static\img\blank_user.gif')

session.add(User1)

session.commit()

## User2 = User(name="Sandeep Malik",
##               email="Sandeep@gmail.com",
##               picture='http://dummyimage.com/200x200.png/cc0000/ffffff')
## session.add(User2)
## session.commit()


# Creating 4 fake categories
Category1 = Category(name="Cricket",
                      user_id=1)
session.add(Category1)
session.commit()

Category2 = Category(name="Tech Gadgets",
                      user_id=1)
session.add(Category2)
session.commit()

Category3 = Category(name="Food Items",
                      user_id=1)
session.add(Category3)
session.commit()

Category4 = Category(name="Books",
                      user_id=1)
session.add(Category4)
session.commit()

# Populate a category with items for testing
# Using different users for items also
Item1 = Items(name="Bat",
               date=datetime.datetime.now(),
               description="Good willow bat. Long Lasting",
               picture="http://www.khelmart.com/Cricket/zoomer_Image/SF_EN_000057_K_large_1.jpg",
               category_id=1,
               user_id=1)
session.add(Item1)
session.commit()

Item2 = Items(name="Concepts of Physics 2",
               date=datetime.datetime.now(),
               description=" Author: H.C. Verma ",
               picture="http://ecx.images-amazon.com/images/I/51AhGBwsz3L._SX381_BO1,204,203,200_.jpg",
               category_id=4,
               user_id=1)
session.add(Item2)
session.commit()

Item3 = Items(name="Oat Waffles",
               date=datetime.datetime.now(),
               description="A waffle is a dish made from leavened batter or dough that is cooked between two plates.",
               picture="http://cdn.awesomecuisine.com/wp-content/uploads/2012/01/oats_waffles.jpg",
               category_id=3,
               user_id=1)
session.add(Item3)
session.commit()

print "Your database has been populated with the sample data! (y)"
