class GenericLocators:
    """ header menu """
    menu_logo = "//div[@id='header_logo_block' or @class='header_logo_block']"
    home = "//a[@class='menu_item']/li[contains(text(), 'Home')]"
    about_header = "//a[@class='menu_item']/li[contains(text(), 'About Us')]"
    services_header = "//a[@class='menu_item']/li[contains(text(), 'Services')]"
    services_header_active = "//a[@class='menu_item active']/li[contains(text(), 'Services')]"
    brands_header = "//a[@class='menu_item']/li[contains(text(), 'Brands')]"
    contact_header = "//a[@class='menu_item']/li[contains(text(), 'Contact')]"
    schedule_service_header = "//button[contains(text(), 'Schedule Service')]"
    service_areas_header = "//a[@class='menu_item']/li[contains(text(), 'Service Areas')]"
    header_fb = "//*[@id='header']/div[1]/div/a[1]"
    header_insta = "//*[@id='header']/div[1]/div/a[2]"

    """single service page in pop-up"""
    popup_refrigerator = "//div/a[@class='sub' and contains(text(), 'Refrigerator')]"
    popup_dryer = "//div/a[@class='sub' and contains(text(), 'Dryer')]"
    popup_washer = "//div/a[@class='sub' and contains(text(), 'Washer')]"
    popup_microwave = "//div/a[@class='sub' and contains(text(), 'Microwave')]"
    popup_oven = "//div/a[@class='sub' and contains(text(), 'Oven')]"
    popup_stove = "//div/a[@class='sub' and contains(text(), 'Stove')]"
    popup_freezer = "//div/a[@class='sub' and contains(text(), 'Freezer')]"
    popup_dishwasher = "//div/a[@class='sub' and contains(text(), 'Dishwasher')]"
    popup_wine = "//div/a[@class='sub' and contains(text(), 'Wine')]"
    popup_trash = "//div/a[@class='sub' and contains(text(), 'Trash')]"
    popup_garbage = "//div/a[@class='sub' and contains(text(), 'Garbage')]"
    popup_range = "//div/a[@class='sub' and contains(text(), 'Range')]"
    schedule_service_banner = "//button/a[contains(text(), 'Schedule Service')]"

    """ page """
    schedule_service_text = "//a[contains(text(), 'schedule')]"

    """ footer """
    footer_top_button = "//div[contains(@class, 'footer-button')]"
    about_footer = "//div[@class='me-auto footer_nav_block nav']/a/li[contains(text(), 'About Us')]"
    contact_footer = "//div[@class='me-auto footer_nav_block nav']/a/li[contains(text(), 'Contact Us')]"
    services_footer = "//div[@class='me-auto footer_nav_block nav']/a/li[contains(text(), 'Services')]"
    brands_footer = "//div[@class='me-auto footer_nav_block nav']/a/li[contains(text(), 'Brands')]"
    service_areas_footer = "//div[@class='me-auto footer_nav_block nav']/a/li[contains(text(), 'Service Areas')]"

    """ contact us and schedule """
    first_name = "//input[@name='first_name']"
    last_name = "//input[@name='last_name']"
    email = "//input[@name='email']"
    phone_number = "//input[@name='phone_number']"
    message = "//textarea[@name='description']"
    send_button = "//button[contains(text(), 'Send')]"
    schedule_service_button = "//button[@class='contactButton btn btn-primary' and contains(text(), 'Schedule " \
                              "Service')] "
    contact_confirm_popup = "//div/h3[@class='h3Custom']"
    address = "//input[@name='address']"
    zip = "//input[@name='zip_code']"
    service_date = "//input[@name='service_date']"
    service_time = "//input[@name='service_time']"
    city = "//select[@name='city']"
    appliance = "//select[@name='appliance']"
    brand = "//select[@name='brand']"


class FresnoLocators:
    """ header menu """
    page_title = "//div/a[@class='padding15 pageTitle']"
    banner_title = "//div[@class='banner_title']"
    service_title = "//div[@class='padding15 servicesTitle']"

    """single service page in list"""
    list_refrigerator = "//div[@class='list-group-item']/a[contains(text(), 'Refrigerator')]"
    list_dryer = "//div[@class='list-group-item']/a[contains(text(), 'Dryer')]"
    list_washer = "//div[@class='list-group-item']/a[contains(text(), 'Washer')]"
    list_microwave = "//div[@class='list-group-item']/a[contains(text(), 'Microwave')]"
    list_oven = "//div[@class='list-group-item']/a[contains(text(), 'Oven')]"
    list_stove = "//div[@class='list-group-item']/a[contains(text(), 'Stove')]"
    list_freezer = "//div[@class='list-group-item']/a[contains(text(), 'Freezer')]"
    list_dishwasher = "//div[@class='list-group-item']/a[contains(text(), 'Dishwasher')]"
    list_wine = "//div[@class='list-group-item']/a[contains(text(), 'Wine')]"
    list_trash = "//div[@class='list-group-item']/a[contains(text(), 'Trash')]"
    list_garbage = "//div/[@class='list-group-item']/a[contains(text(), 'Garbage')]"
    list_range = "//div[@class='list-group-item']/a[contains(text(), 'Range')]"

    """ page """
    read_more = "//div/a[contains(text(), 'Read')]"
    read_more_index = "//div[contains(@data-index, '2')]/div/div/div/div/p/div/a"  # change index
    cart_title = "//div[contains(@data-index, '2')]/div/div/div/div/div"  # change index


class ClovisLocators:
    """ header menu """
    page_title = "//div/a[@class='padding15 bigLink']"
    banner_title = "//div[@class='banner_title_underLine']"
    service_title = "//div[@class='padding15 bigLink']"

    """ page """
    cart_title = "//*[@id='root']/div/div/section[3]/div/div[2]/div/div/div/div[6]/div/div/div/div[2]/div[2]/h3/a"  # tarber  vercnel texty click enel hamematel title-i het

    """ footer """
    footer_fb = "//*[@id='root']/div/div/div[2]/div[1]/div[1]/div/div/a[1]/svg"
    footer_insta = "//*[@id='root']/div/div/div[2]/div[1]/div[1]/div/div/a[2]/svg"
    footer_logo = "//*[@id='root']/div/div/div[2]/div[1]/div[1]/a/img"


class SacramentoLocators:
    menu_logo = "//div/a[@class='main_logo_block']"
    header_fb = "//*[@id='header']/div/div[2]/div/div[2]/a[1]"
    header_insta = "//*[@id='header']/div/div[2]/div/div[2]/a[2]"

    """ header menu """
    page_title = "//div/a[@class='padding15']"  # vercnel 1 indexi texty
    banner_title = "//div[@class='banner_title card-title h5']"
    service_title = "//div[@class='padding15']"

    """ page """
    cart_title = "//*[@id='wrapper']/div[2]/section[2]/div[2]/div/div/div/div[6]/div/div/div/div/div"  # tarber  vercnel texty click enel hamematel title-i het

    """ footer """
    footer_fb = "//*[@id='wrapper']/div[4]/div[1]/div[1]/div/div/a[1]"
    footer_insta = "//*[@id='wrapper']/div[4]/div[1]/div[1]/div/div/a[2]"
    footer_logo = "//*[@id='wrapper']/div[4]/div[1]/div[1]/a/img"


class VegasLocators:
    """ header menu """
    menu_logo = "//*[@id='header_nav_fixed']/div/div[1]/a"
    page_title = "//div/a[@class='padding15']"  # 1 index
    banner_title = "//p[@class='banner_title']"  # Trusted Appliance Repair Services In Vegas
    service_title = "//div[@class='padding15']"

    """ page """
    cart_title = "//*[@id='root']/div/div/div[2]/section[2]/div[1]/div[2]/div/div/div"

    """ footer """
    footer_fb = "//*[@id='root']/div/div/div[4]/div[1]/div[1]/div/div/a[1]"
    footer_insta = "//*[@id='root']/div/div/div[4]/div[1]/div[1]/div/div/a[2]"
