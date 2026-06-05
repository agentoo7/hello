from hello import greet, main


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_name():
    assert greet("Claude") == "Hello, Claude!"


def test_main_prints(capsys):
    main()
    assert capsys.readouterr().out == "Hello, World!\n"
