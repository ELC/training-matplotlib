from algorithms.Sorting.tests.testconf import per, a

import algorithms.Sorting.App.mysortings as my


def test_bubbleoriginal():
    for i in per():
        assert my.bubbleoriginal(list(i)) == a


def test_bubblesfalsefromi():
    for i in per():
        assert my.bubblesfalsefromi(list(i)) == a


def test_bubblesortfalsefrom0():
    for i in per():
        assert my.bubblesortfalsefrom0(list(i)) == a


def test_cocktailbubble():
    for i in per():
        assert my.cocktailbubble(list(i)) == a


def test_cocktailselection():
    for i in per():
        assert my.cocktailselection(list(i)) == a


def test_gnome():
    for i in per():
        assert my.gnome(list(i)) == a


def test_insertion():
    for i in per():
        assert my.insertion(list(i)) == a


def test_myquicksortinternet():
    for i in per():
        assert my.myquicksortinternet(list(i)) == a


def test_myquicksortmejorado():
    for i in per():
        assert my.myquicksortmejorado(list(i)) == a


def test_myquicksortslice():
    for i in per():
        assert my.myquicksortslice(list(i)) == a


def test_selection():
    for i in per():
        assert my.selection(list(i)) == a


def test_sorted():
    for i in per():
        assert sorted(list(i)) == a
