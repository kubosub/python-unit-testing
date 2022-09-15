import hello_world

def test_main(capsys):
    hello_world.main()

    out, err = capsys.readouterr()
    assert out == 'Hello World\n'
    assert err == ''
