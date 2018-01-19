"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):
        self.first_name= first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<Customer: {first_name}, {last_name}, {email}, {password}"

