from behave import given, when, then, step


@given("Pusty koszyk")
def step_empty_cart(context):
    create_user_with_empty_cart()


@when("dodaje produkt {name} o wartosci {value:f}")
def step_add_product(context, name, value):
    # żeby nikt nie popełnił błędu
    assert value > 0

    # tu wysyłamy informację do sklepu
    # który testujemy
    post_order_to_shop(name, value)


@then("koszyk ma {count:d} rzecz")
def step_check_cart_item_count(context, count):
    # czy poprzedni krok zakończył się
    # niepowedzeniem.
    assert context.failed is False

    actual_count = get_shopping_cart_count()

    # czy ilosc rzeczy w koszyku
    # sie zgadza
    assert count == actual_count


@then("wartosc koszyka to {value:f}")
def step_check_cart_value(context, value):
    assert context.failed is False

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
