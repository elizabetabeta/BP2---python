from orm import session, User, Address



session.add_all(
    [
        User(name="ana", lastname="anic"),
        User(name="marija", lastname="maric"),
        User(name="nikola", lastname="nikolic"),
    ]
)
session.commit()




"""
for user in session.query(User, User.id, User.name, User.lastname).all():
    print(user.User)

jack = User(name="jack", lastname="Jack Bean")
jack.addresses
jack.addresses = [
    Address(name="jack@google.com"),
    Address(name="j25@yahoo.com"),
]
jack.addresses[1]

jack.addresses[1].user
session.add(jack)
session.commit()
"""
for u, a in (
    session.query(User, Address)
    .filter(User.id == Address.user_id)
    .filter(Address.name == "nekaadresa@gmail.com")
    .all()
):
    print(u)
    print(a)

