from main import calculadora

def test_class_monkey(monkeypatch):
    monkeypatch.setattr(calculadora, "sumar", lambda x: 3)
    c = calculadora()
    
    assert c.sumar() == 4