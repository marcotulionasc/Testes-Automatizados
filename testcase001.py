from selenium import webdriver

# Configurar o driver do Selenium para o Chrome
driver = webdriver.Chrome()

# Navegar até o site de teste
driver.get("https://www.google.com")

# Verificar se o título da página contém a palavra "Google"
assert "Google" in driver.title

# Encontrar o campo de busca e inserir uma consulta de pesquisa
search_box = driver.find_element_by_name("q")
search_box.send_keys("Teste automatizado com Selenium")

# Enviar a consulta de pesquisa
search_box.submit()

# Verificar se a página de resultados contém pelo menos um resultado
assert "Nenhum resultado encontrado." not in driver.page_source

# Fechar o navegador
driver.close()