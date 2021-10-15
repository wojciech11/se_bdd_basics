from behave import given, when, then, step


@given("Pusty koszyk")
def step_empty_cart(context):
    context.shopping_cart = []
    context.shopping_cart_value = 0


@when("dodaje produkt {name} o wartosci {value:f}")
def step_add_product(context, name, value):
    assert value > 0

    # oczekiwany stan koszyka po dodaniu
    # nowego produktu
    context.shopping_cart_value = context.shopping_cart_value + value
    context.shopping_cart.append(name)

    # tu wysyłamy informację do sklepu
    # który testujemy
    post_order_to_shop(name, value)


@then("koszyk ma {count:d} rzecz")
def step_check_cart_item_count(context, count):
    assert context.failed is False
    assert len(context.shopping_cart) == count

    c = get_shopping_cart_count()

    # czy ilosc rzeczy w koszyku
    # sie zgadza
    assert len(context.shopping_cart) == c


@then("wartosc koszyka to {value:f}")
def step_check_cart_value(context, value):
    assert context.failed is False
    assert context.shopping_cart_value == value

    v = get_shopping_cart_value()

    # czy wartosc koszyka jest taka
    # jak oczekiwana
    assert context.shopping_cart_value == v


def post_order_to_shop(n, v):
    # wysylamy zapytanie do sklepu
    pass


def get_shopping_cart_value():
    # odpytujemy sklep o wartosc koszyka
    return 100.0


def get_shopping_cart_count():
    # odpytujemy sklep o wartosc koszyka
    return 1
