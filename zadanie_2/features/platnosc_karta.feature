Feature: Płatność kartą
  Jako użytkownik chcę dokonac płatności kartą

  Background:
    Given Jestem na stronie płatności online

  Scenario: Wykonanie poprawnej płatności online
    When Podaje poprawne dane karty płatniczej
    And Uzupełniam imie i nazwisko
    And Uzupełniam aktualną ważość karty
    And Klikam przycisk Zapłać
    Then Komunikat "Zamówienie opłacone" się wyświetla

  Scenario: Wykrycie nieprawidłowego kodu CVV
   When Uzupełniam niepoprawną wartość CVV
   And Uzupełniam imie i nazwisko
   And Uzupełniam aktualną ważość karty
   And Klikam przycisk Zapłać
   Then Komunikat "Zamówienie opłacone" się wyświetla

  Scenario: Wykrycie nieprawidłowego kodu CVV
    When Uzupełniam niepoprawną wartość CVV
    And Uzupełniam imie i nazwisko
    And Uzupełniam aktualną ważość karty
    And Klikam przycisk Zapłać
    Then Komunikat "Zamówienie opłacone" się wyświetla
