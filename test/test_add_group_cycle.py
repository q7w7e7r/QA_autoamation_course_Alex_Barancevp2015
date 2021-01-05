from model.group import Group


def test_add_group_cycle(app):
    quantity = 5
    while quantity != 0:
        app.group.create(Group(name="name "+str(quantity), header="header "+str(quantity), footer="footer "+str(quantity)))
        quantity = quantity-1
