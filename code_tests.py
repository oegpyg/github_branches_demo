import pytest
from saludar import saludar


def test_saludar(capfd):
  saludar("¡Hola, bienvenido!")  # Call the function
  # Capture stdout
  out, err = capfd.readouterr()
    
  assert out.strip() == "¡Hola, bienvenido!"
