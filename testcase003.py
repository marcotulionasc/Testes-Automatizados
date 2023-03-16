from selenium import webdriver

# Configurar o driver do Selenium para o Chrome
driver = webdriver.Chrome()

# Navegar até o site de teste
driver.get("https://www.example.com")

# Encontrar o campo de pesquisa e inserir uma consulta de pesquisa
search_box = driver.find_element_by_id("search-box")
search_box.send_keys("produto de teste")

# Enviar a consulta de pesquisa
search_box.submit()

# Verificar se a página de resultados contém pelo menos um resultado
results = driver.find_elements_by_class_name("search-result")
assert len(results) > 0, "Nenhum resultado encontrado para a consulta de pesquisa"

# Clicar no primeiro resultado
results[0].click()

# Verificar se o título da página contém o nome do produto
product_name = driver.find_element_by_class_name("product-name").text
assert "produto de teste" in product_name, "O produto exibido não corresponde à consulta de pesquisa"

# Fechar o navegador
driver.close()
