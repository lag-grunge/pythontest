class Key:
    passphrase = "zax2rulez"

    def __len__(self):
        return 1337

    def __getitem__(self, item):
        return 3

    def __gt__(self, other):
        return 1

    def __str__(self):
        return "GeneralTsoKeycard"

def test_len(k : Key):
    assert len(k) == 1337

def test_getitem(k : Key):
    assert k[404] == 3

def test_gt(k : Key):
    assert k > 9000

def test_passphrase(k : Key):
    assert k.passphrase == "zax2rulez"

def test_str(k : Key):
    assert str(k) == "GeneralTsoKeycard"

if __name__ == '__main__':
    key = Key()
    key.passphrase = "zax"
    test_len(key)
    test_getitem(key)
    test_gt(key)
    test_passphrase(key)
    test_str(key)
