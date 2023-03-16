from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Configurar o driver do Selenium para o Chrome
driver = webdriver.Chrome()

# Navegar até o site de teste
driver.get("https://www.example.com/login")

# Verificar se o título da página contém a palavra "Login"
assert "Login" in driver.title

# Encontrar os campos de entrada de usuário e senha e inserir valores
username_field = driver.find_element_by_name("username")
username_field.send_keys("usuario_teste")
password_field = driver.find_element_by_name("password")
password_field.send_keys("senha_teste")

# Enviar o formulário de login
password_field.send_keys(Keys.RETURN)

# Verificar se o usuário é redirecionado para a página inicial após o login
assert "Minha Conta" in driver.title

# Fechar o navegador
driver.close()