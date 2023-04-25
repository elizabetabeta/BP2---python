from orm import session, Address, User

session.add_all(
    [
        Address(name="nekaadresa", user_id="1"),
        Address(name="nekaadresa2", user_id="2"),
        Address(name="nekaadresa3", user_id="3"),
    ]
)
session.commit()




"""
for address in session.query(Address, Address.id, Address.name, Address.user_id).all():
    print(address.Address)
"""
