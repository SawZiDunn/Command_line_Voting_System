from project import vote, remove_player, reset_data, read_data

dic_array: list = read_data("test_players.csv")


def test_vote(monkeypatch):
    global dic_array
    reset_data(dic_array)

    monkeypatch.setattr('builtins.input', lambda _: "5")  # voting ronaldo, No. 5
    vote(dic_array)
    monkeypatch.setattr('builtins.input', lambda _: "5")  # input voting number
    vote(dic_array)

    assert dic_array[0]["Vote"] == 5


def test_reset_data():
    global dic_array
    print(dic_array)
    dic_array[4]["Vote"] = 5
    reset_data(dic_array)
    assert dic_array[4]["Vote"] == 0


def test_remove_data(monkeypatch):
    global dic_array
    monkeypatch.setattr('builtins.input', lambda _: "5")
    remove_player(dic_array)

    assert len(dic_array) == 4



