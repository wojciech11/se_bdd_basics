from behave import given, when, then, step


@given("Pusty koszyk")
def step_empty_cart(context):

    # dodanie atrybutu do przekazywanie
    # danych między krokami
    context.shopping_cart = []
    context.shopping_cart_value = 0

    # komunikacja z serwisem,
    # który testujemy
    create_user_with_empty_cart()


@when("dodaje produkt {name} o wartosci {value:f}")
def step_add_product(context, name, value):
    assert value > 0

    # Obliczanie
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

    # czy wyliczony stan zgadza się z wartością
    # podaną w teście
    assert len(context.shopping_cart) == count

    actual_count = get_shopping_cart_count()

    # czy ilosc rzeczy w koszyku
    # sie zgadza
    assert count == actual_count


@then("wartosc koszyka to {value:f}")
def step_check_cart_value(context, value):
    assert context.failed is False

    # czy wyliczony stan zgadza się z wartością
    # podaną w teście
    assert context.shopping_cart_value == value

    actual_value = get_shopping_cart_value()

    # czy wartosc koszyka jest taka
    # jak oczekiwana
    assert value == actual_value


def create_user_with_empty_cart():
    # jeśli musimy przygotować cokolwiek
    # przed testem
    pass


def post_order_to_shop(n, v):
    # wysylamy zapytanie do sklepu
    pass


def get_shopping_cart_value():
    # odpytujemy sklep o wartosc koszyka
    return 100.0


def get_shopping_cart_count():
    # odpytujemy sklep o wartosc koszyka
    return 1
