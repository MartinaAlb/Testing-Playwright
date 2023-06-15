def test_log_in_as_standart_user(page):
    page.goto("https://www.saucedemo.com/")
    username_input = page.query_selector("#user-name")
    username_input.type("standard_user")

    username_input = page.query_selector("#password")
    username_input.type("secret_sauce")

    page.query_selector("#login-button").click()
    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    expected_url = "https://www.saucedemo.com/inventory.html"

def test_log_in_as_locked_out_user(page):
    page.goto("https://www.saucedemo.com/")
    username_input = page.query_selector("#user-name")
    username_input.type("locked_out_user")

    username_input = page.query_selector("#password")
    username_input.type("secret_sauce")

    page.query_selector("#login-button").click()
    error_message_locked_out_user = page.query_selector("#login_button_container > div > form > div.error-message-container.error > h3")
    assert error_message_locked_out_user.inner_text() == "Epic sadface: Sorry, this user has been locked out."

def test_log_in_as_problem_user(page):
    page.goto("https://www.saucedemo.com/")
    username_input = page.query_selector("#user-name")
    username_input.type("problem_user")

    username_input = page.query_selector("#password")
    username_input.type("secret_sauce")

    page.query_selector("#login-button").click()
    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    expected_url = "https://www.saucedemo.com/inventory.html"

def test_log_in_as_performance_glitch_user(page):
    page.goto("https://www.saucedemo.com/")
    username_input = page.query_selector("#user-name")
    username_input.type("performance_glitch_user")

    username_input = page.query_selector("#password")
    username_input.type("secret_sauce")

    page.query_selector("#login-button").click()
    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    expected_url = "https://www.saucedemo.com/inventory.html"

def test_open_menu_about_page(page):
    page.goto("https://www.saucedemo.com/")
    username_input = page.query_selector("#user-name")
    username_input.type("standard_user")

    username_input = page.query_selector("#password")
    username_input.type("secret_sauce")

    page.query_selector("#login-button").click()
    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    expected_url = "https://www.saucedemo.com/inventory.html"

    page.query_selector("#react-burger-menu-btn").click()
    page.query_selector("#about_sidebar_link").click()

    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass
    expected_url_about = "https://saucelabs.com/"

def test_soring_products_by_name_from_a_to_z(page):
    page.goto("https://www.saucedemo.com/")
    username_input = page.query_selector("#user-name")
    username_input.type("standard_user")

    username_input = page.query_selector("#password")
    username_input.type("secret_sauce")

    page.query_selector("#login-button").click()
    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    expected_url = "https://www.saucedemo.com/inventory.html"

    select_element = page.query_selector(".product_sort_container")
    select_element.select_option('az')

    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    product_elements = page.query_selector_all(".inventory_item_name")
    product_names = [element.text_content() for element in product_elements]

    assert product_names == sorted(product_names), "Products are not sorted form A to Z."

def test_soring_products_by_name_from_z_to_a(page):
    page.goto("https://www.saucedemo.com/")
    username_input = page.query_selector("#user-name")
    username_input.type("standard_user")

    username_input = page.query_selector("#password")
    username_input.type("secret_sauce")

    page.query_selector("#login-button").click()
    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    expected_url = "https://www.saucedemo.com/inventory.html"

    select_element = page.query_selector(".product_sort_container")
    select_element.select_option('za')

    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    product_elements = page.query_selector_all(".inventory_item_name")
    product_names = [element.text_content() for element in product_elements]

    assert product_names == sorted(product_names, reverse=True), "Products are not sorted form Z to A."

def test_soring_products_by_price_low_to_high(page):
    page.goto("https://www.saucedemo.com/")
    username_input = page.query_selector("#user-name")
    username_input.type("standard_user")

    username_input = page.query_selector("#password")
    username_input.type("secret_sauce")

    page.query_selector("#login-button").click()
    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    expected_url = "https://www.saucedemo.com/inventory.html"

    select_element = page.query_selector(".product_sort_container")
    select_element.select_option('lohi')

    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    product_elements = page.query_selector_all(".inventory_item_price")
    product_price = [element.text_content() for element in product_elements]
    sorted_price = sorted(product_price, key=lambda x: float(x.strip('$')))

    assert product_price == sorted_price, "Products are not sorted by price from low to high"

def test_soring_products_by_price_high_to_low(page):
    page.goto("https://www.saucedemo.com/")
    username_input = page.query_selector("#user-name")
    username_input.type("standard_user")

    username_input = page.query_selector("#password")
    username_input.type("secret_sauce")

    page.query_selector("#login-button").click()
    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    expected_url = "https://www.saucedemo.com/inventory.html"

    select_element = page.query_selector(".product_sort_container")
    select_element.select_option('hilo')

    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    product_elements = page.query_selector_all(".inventory_item_price")
    product_price = [element.text_content() for element in product_elements]
    sorted_price = sorted(product_price, key=lambda x: float(x.strip('$')), reverse=True)

    assert product_price == sorted_price, "Products are not sorted by price from high to low."

def test_logout(page):
    page.goto("https://www.saucedemo.com/")
    username_input = page.query_selector("#user-name")
    username_input.type("standard_user")

    username_input = page.query_selector("#password")
    username_input.type("secret_sauce")

    page.query_selector("#login-button").click()
    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    expected_url = "https://www.saucedemo.com/inventory.html"

    page.query_selector("#react-burger-menu-btn").click()
    page.query_selector("#logout_sidebar_link").click()
    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    expected_url = "https://www.saucedemo.com/"

def test_add_item_to_cart(page):
    page.goto("https://www.saucedemo.com/")
    username_input = page.query_selector("#user-name")
    username_input.type("standard_user")

    username_input = page.query_selector("#password")
    username_input.type("secret_sauce")

    page.query_selector("#login-button").click()
    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    expected_url = "https://www.saucedemo.com/inventory.html"
    page.query_selector("#add-to-cart-sauce-labs-backpack").click()
    page.query_selector("#add-to-cart-sauce-labs-bike-light").click()
    page.query_selector("#add-to-cart-sauce-labs-bolt-t-shirt").click()

    assert page.query_selector(
        "#remove-sauce-labs-backpack") is not None, "Button did not change from Add to cart to Remove"
    assert page.query_selector(
        "#remove-sauce-labs-bike-light") is not None, "Button did not change from Add to cart to Remove"
    assert page.query_selector(
        "#remove-sauce-labs-bolt-t-shirt") is not None, "Button did not change from Add to cart to Remove"

def test_remove_item_from_cart(page):
    page.goto("https://www.saucedemo.com/")
    username_input = page.query_selector("#user-name")
    username_input.type("standard_user")

    username_input = page.query_selector("#password")
    username_input.type("secret_sauce")

    page.query_selector("#login-button").click()
    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    expected_url = "https://www.saucedemo.com/inventory.html"
    page.query_selector("#add-to-cart-sauce-labs-backpack").click()
    page.query_selector("#add-to-cart-sauce-labs-bike-light").click()
    page.query_selector("#add-to-cart-sauce-labs-bolt-t-shirt").click()

    page.query_selector("#remove-sauce-labs-backpack").click()
    page.query_selector("#remove-sauce-labs-bike-light").click()
    page.query_selector("#remove-sauce-labs-bolt-t-shirt").click()

    assert page.query_selector(
        "#remove-sauce-labs-backpack") is None, "Button did not change from Remove to Add to cart"
    assert page.query_selector(
        "#remove-sauce-labs-bike-light") is None, "Button did not change from Remove to Add to cart"
    assert page.query_selector(
        "#remove-sauce-labs-bolt-t-shirt") is None, "Button did not change from Remove to Add to cart"


def test_check_number_of_items_in_cart(page):
    page.goto("https://www.saucedemo.com/")
    username_input = page.query_selector("#user-name")
    username_input.type("standard_user")

    username_input = page.query_selector("#password")
    username_input.type("secret_sauce")

    page.query_selector("#login-button").click()
    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    expected_url = "https://www.saucedemo.com/inventory.html"
    page.query_selector("#add-to-cart-sauce-labs-backpack").click()
    page.query_selector("#add-to-cart-sauce-labs-bike-light").click()
    page.query_selector("#add-to-cart-sauce-labs-bolt-t-shirt").click()

    cart_count_element = page.query_selector("#shopping_cart_container > a > span")
    cart_count = int(cart_count_element.text_content())

    expected_count = 3  # The expected number of items in the cart.

    assert cart_count == expected_count, "The number of items in the cart does not match the expected count."


def test_check_content_of_cart(page):
    page.goto("https://www.saucedemo.com/")
    username_input = page.query_selector("#user-name")
    username_input.type("standard_user")

    username_input = page.query_selector("#password")
    username_input.type("secret_sauce")

    page.query_selector("#login-button").click()
    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    expected_url = "https://www.saucedemo.com/inventory.html"
    page.query_selector("#add-to-cart-sauce-labs-backpack").click()
    page.query_selector("#add-to-cart-sauce-labs-bike-light").click()
    page.query_selector("#add-to-cart-sauce-labs-bolt-t-shirt").click()

    page.query_selector("#remove-sauce-labs-backpack").click()

    page.query_selector("#shopping_cart_container > a").click()

    try:
        page.wait_for_load_state()
    except Error.TimeoutError:
        pass

    expected_url = "https://www.saucedemo.com/cart.html"

    expected_products = ["Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"]
    cart_elements = page.query_selector_all(".cart_item_label .inventory_item_name")
    cart_products = [element.text_content() for element in cart_elements]

    assert cart_products == expected_products, "The content of the cart does not match the expected products."

