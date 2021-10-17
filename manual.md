# Ćwiczenia - BDD podstawy


## Przygotowanie środowiska

1. Uruchom `Terminal` i zainstaluj wymagane pakiety oraz [Atom](https://atom.io/):

   ```bash
   sudo apt-get install python3-venv python3-pip -y
   sudo snap install atom --classic
   
   mkdir -p workspace
   cd workspace
   
   # zauważ kropka
   atom .
   ```

2. Zainstaluj następujące pluginy w Atomie (Edit->Preferences):

  - `cucumber`
  - `platformio-ide-terminal`

## Pierwszy test

1. Utwórz następujące drzewo katalogów oraz jeden plik `example.features`:

   ```
   workspace/
     \- example/
          \- features/
               |- steps/
               \- example.feature
   ```

2. Napisz swój pierwszy opis zachowania dla twojej funkcjonalności:

   ```gherkin
   Feature: Healthy food
   
   Scenario: eating
     Given there were 5 cucumbers
     When I eat 3 cucumbers
     Then I should have 2 cucumbers
   ```

3. W terminalu z poziomu Atoma (Packages -> platformio-ide-terminal-> Toggle) uruchom:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -U behave
   
   cd example/
   behave -q
   ```

4. Zaimplementujmy teraz nasze kroki:

   ```python
   from behave import given, when, then, step
   
   
   @given("there were 5 cucumbers")
   def step_cucumber(context):
       pass
   
   
   @when("I eat 3 cucumbers")
   def step_eating(context):
       pass
   
   
   @then("I should have 2 cucumbers")
   def step_after(context):
       pass
   ```

   W terminalu:

   ```bash
   behave
   ```

5. Na zasadzie analogi utwórz drugi scenariusz w `example.features`. Skorzystaj z komendy `behave -q`, aby zobaczyć czy nie popełniłaś/popełniłeś błędów.
