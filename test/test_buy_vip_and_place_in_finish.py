

def test_vip_and_finish(app):
    app.page.open_contracts()
    app.session.login()
    app.contract.buy_vip()
    app.table.place_in_finish()
    app.session.logout()
