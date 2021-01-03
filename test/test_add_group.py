from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="1qaz", header="2wsx", footer="3edc"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))



