class web_locators:

    c_username1 = "username"  #by name
    c_username = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'   #by xpath
    c_password = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'    #by xpath
    c_forget = 'div[class="orangehrm-login-forgot"]'     #by css selector
    c_submit = 'button[type="submit"]'     #by css selector
    c_admin = '//span[text()="Admin"]'     #by xpath
    c_admin_options = '//header//div//nav//ul//li'    #by xpath
    c_admin_option_more = '//*[@id="app"]/div[1]/div[1]/header/div[2]//span[text()="More "]'   #by xpath
    c_admin_more_option_visible = '//div//nav//ul//li//ul//div' #by xpath
    menu_list = '//aside//nav//div//ul//li//a//span'
