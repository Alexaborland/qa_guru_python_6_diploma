## Training project with Web autotests for [DemoWebShop](https://demowebshop.tricentis.com/) service

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

### Test coverage
* New user registration
* Registration of a new user with an existing email
* Checking a subscription to site news
* Adding multiple books to cart
* The creation of your decoration
* Adding a product to a wishlist
* Choosing different features for creating a new computer
* Adding something to cart
* Filling in delivery data

### <img width="5%" title="Jenkins" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/jenkins.png"> Running the project on Jenkins  
### [Job](https://jenkins.autotests.cloud/job/qa_guru_6_diploma/)

The test can be assembled with parameters. Available browsers: Firefox and Chrome. It is also possible to select browser versions.

<img width="100%" title="parametrs" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/parametrs.png"></code>

When you click the "Build With Parameters" button, a window opens where you can select the browser and its version.

<img width="50%" title="browser" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/browser.png"></code>

<img width="50%" title="browser_versions" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/browser_versions.png"></code>

After selecting the parameters, you need to click the “Collect” button. Then the assembly will begin.

<img width="50%" title="sobrat" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/sobrat.png"></code>

After tests passed you can see the result and the reports that appear in Allure and Allure TestOps.

<code><img width="100%" title="jenkins_stats" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/jenkins_stats.png"></code>

<!-- Allure report -->
 ### <img width="5%" title="Allure Report" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/allure.png"> Allure
 
 ### [Report](https://jenkins.autotests.cloud/job/qa_guru_6_diploma/12/allure/)
 
 After tests passed the results can be viewed in the Allure report.
 
 <img width="100%" title="allure_main" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/allure_test.png"></code>
 
 In the "Suites" tab you can see the collected tests, which describe the steps, attach logs, a screenshot and a video of the test.
 
 <img width="100%" title="suites" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/suites.png"></code>
 
 Video of the test:
 
 ![allure_video](https://github.com/Alexaborland/qa_guru_python_6_diploma/assets/136263543/953d43b1-8715-4eed-8044-e29a450d0c13)

 <!-- Allure TestOps -->
 
 ### <img width="5%" title="Allure TestOps" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/allure_testops.png"> Integration with Allure TestOps
 
 ### [Allure Testops](https://allure.autotests.cloud/launch/30756)
 
 Reporting is also generated in Allure TestOps.
 
 <img width="100%" title="allure_testops" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/allure_testops.png"></code>
 
 <img width="100%" title="allure_tests" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/allure_testops_test.png"></code>

<!-- Telegram -->

### <img width="5%" title="Telegram" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/images/telegram.png"> Integration with Telegram

After tests passed the Telegram bot receives a message with a schedule and some information about the tests.

<img width="50%" title="allure_tests" src="https://github.com/Alexaborland/qa_guru_python_6_diploma/blob/main/screenshots/telegram_stats.png"></code>
 


