Feature: Zmiana wartosci koszyka

  Scenario: klient dodaje produkt do pustego koszyka
    Given pusty koszyk
     When dodaje produkt spodnie o wartosci 100.0
     Then koszyk ma 1 rzecz
      and wartosc koszyka to 100.0
