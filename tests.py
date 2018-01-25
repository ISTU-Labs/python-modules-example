import register


class TestRegiter:
    
    def setUp(self):
        self.reg = register.Register(1000)
        
    def tearDown(self):
        pass

    def test_saldo(self):
        assert self.reg.amount == 1000

    def test_add_amount(self):
        self.reg.deposit(100)
        assert self.reg.amount == 1100

    def test_remove_amount(self):
        self.reg.withdraw(100)
        assert self.reg.amount == 900
