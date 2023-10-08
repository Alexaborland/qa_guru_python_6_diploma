## Проект UI автотестов 

<!-- Технологии -->
<p  align="center">
  <code><img width="5%" title="Pycharm" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/pycharm.png"></code>
  <code><img width="5%" title="Python" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/python.png"></code>
  <code><img width="5%" title="Pytest" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/pytest.png"></code>
  <code><img width="5%" title="Selene" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/selene.png"></code>
  <code><img width="5%" title="Selenium" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/github.png"></code>
  <code><img width="5%" title="Jenkins" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/allure.png"></code>
  <code><img width="5%" title="Allure TestOps" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/allure_testops.png"></code>
  <code><img width="5%" title="Telegram" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/telegram.png"></code>
</p>

<!-- Тест кейсы -->

### Что проверяем
* Проверка авторизации
* Проверка добавления в корзину нескольких книг
* Проверка создания своего украшения
* Проверка выбора характеристик компьютера 
* Проверка добавления в корзину 
* Проверка заполнения данных для доставвки

### <img width="5%" title="Jenkins" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/jenkins.png"> Запуск проекта в Jenkins  
### [Job](https://jenkins.autotests.cloud/job/qa_guru_6_diploma/)

Тест можно собрать с параметрами. Доступны браузеры: firefox и chrome. Также доступно выбрать версии браузеров.

<img width="100%" title="parametrs" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/parametrs.png"></code>

При нажатии кнопки "Собрать с параметрами" открывается окно, где можно выбрать браузер и его версию.

<img width="50%" title="browser" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/browser.png"></code>

<img width="50%" title="browser_versions" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/browser_versions.png"></code>

После выбора параметров нужно нажать кнопку "Собрать". Тогда начнется сборка.

<img width="50%" title="sobrat" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/sobrat.png"></code>

После прохождения тестов можно увидеть результат и появившиеся отчеты в Allure и Allure TestOps

<code><img width="100%" title="jenkins_stats" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/jenkins_stats.png"></code>

<!-- Allure report -->
 ### <img width="5%" title="Allure Report" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/allure.png"> Allure
 
 ### [Report](https://jenkins.autotests.cloud/job/qa_guru_6_diploma/12/allure/)
 
 После прохождения теста результаты можно посмотреть в Allure отчете 
 
 <img width="100%" title="allure_main" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/allure_main.png"></code>
 
 Во вкладке Suites можно посмотреть собранныет тесты, у которых описаны шаги, приложены логи, скриншот и видео прохождения теста 
 
 <img width="100%" title="suites" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/suites.png"></code>
 
 Видео прохождения теста:
 
 ![allure_video](https://github.com/Alexaborland/qa_guru_python_6_diploma/assets/136263543/953d43b1-8715-4eed-8044-e29a450d0c13)

 <!-- Allure TestOps -->
 
 ### <img width="5%" title="Allure TestOps" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/allure_testops.png"> Интеграция с Allure TestOps
 
 ### [Allure Testops](https://allure.autotests.cloud/launch/30756)
 
 Также отчетность генерируется в Allure TestOps
 
 <img width="100%" title="allure_testops" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/allure_testops.png"></code>
 
 <img width="100%" title="allure_tests" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/allure_tests.png"></code>

<!-- Telegram -->

### <img width="5%" title="Telegram" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/telegram.png"> Интеграция с Telegram

После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.

<img width="50%" title="allure_tests" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/telegram_stats.png"></code>
 


