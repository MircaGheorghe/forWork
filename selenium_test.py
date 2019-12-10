from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import include.test as test
from time import sleep as sleep

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
driver.get("https://makler.md/md/")
driver.maximize_window()

user_name = "37368035704"
password = "gheorghe1703"

#find login link
login_block = driver.find_element_by_id('logInDiv')
login_block.click()

#wait 3 second and then find email input and typing user_name
driver.implicitly_wait(3)
element = driver.find_element_by_name('login')
element.send_keys(user_name, Keys.ARROW_DOWN)

#find password input and typing it
element = driver.find_element_by_name('password')
element.send_keys(password)

#click to submit button and enter to site
element = driver.find_element_by_class_name("popupRedButton")
element.click()

#wait two second and redirect to add
sleep(2)
driver.get("https://makler.md/md/an/web/add")

#find select list and click to everyone
for i in range(len(test.list_cat)):
    element = driver.find_element_by_xpath("//select[@name='category']/option[text()='"+ test.list_cat[i] +"']").click()

#find and enter the name of post
element = driver.find_element_by_id("editorName")
element.send_keys(test.post_title)

#find and enter the describtion of the current post
element = driver.find_element_by_id("editorText")
element.send_keys(test.content)

# find and enter price
element = driver.find_element_by_id("price")
element.send_keys(test.post_price)

#work with currency
curency_tab = {
    '$':'USD',
    '₴':'UAH',
    '€':'EUR',
    'lei':'MDL'
}
sleep(1)
if test.currency in curency_tab.keys():
    get_currency_div = driver.find_element_by_class_name('newAdForm_radioBoxButtons')
    elements = get_currency_div.find_elements_by_tag_name('label')
    for element in elements:
        if element.text == curency_tab[test.currency]:
            element.click()

#upload image
sleep(1)
element = driver.find_element_by_class_name("qq-upload-button")

for i in range(test.img_count - 1):
    elm = driver.find_element_by_xpath("//input[@type='file']")
    elm.send_keys("C://Users/Gheorghe/OneDrive/Documents/Python/work/img/"+ str(i) +".jpg")


element = driver.find_element_by_class_name('zend_form')
#variabila ce contine elementele de pe pagina de incarcare a datelor
labels = element.find_elements_by_class_name('newAdForm_boxFieldLabel')
#variabila cu datele de pe pagina de luare a datelor
keys = test.specifications.keys()

#fell of the category inputs
for label in labels:
    for key in keys:
        if key in label.text or key == label.text:
            li = label.find_element_by_xpath('..')
            select_ = li.find_elements_by_tag_name('select')
            optgroup = li.find_elements_by_tag_name('optgroup')
            if select_:
                try:
                    li.find_element_by_xpath("//select/optgroup/option[text()='" + test.specifications[key] +"']").click()
                except:
                    li.find_element_by_xpath("//select/option[text()='" + test.specifications[key] +"']").click()
                break
            input_ = li.find_element_by_tag_name('input')
            if input_:
                input_.send_keys(test.specifications[key].replace('m²', '').strip())
                break

#check the telephone checkbox
element = driver.find_element_by_id('phone-37368035704').click()

#plaseaza postarea
# element = driver.find_element_by_class_name('saveBtn').click()