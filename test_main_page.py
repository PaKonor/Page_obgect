def test_guest_can_go_to_login_page(fixt):
    link = "http://selenium1py.pythonanywhere.com/"
    fixt.get(link)
    login_link = fixt.find_element_by_css_selector("#login_link")
    login_link.click()