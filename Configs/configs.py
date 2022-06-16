from datetime import datetime

now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')[:-3]


class DriverPath:
    CHROME_EXECUTABLE_PATH = "/home/erida-employee/Desktop/Mart/Driver/chromedriver"
    FIREFOX_EXECUTABLE_PATH = "/home/erida-employee/Desktop/Mart/Driver/geckodriver"


class Urls:
    Fresno = "https://appliancerepair-fresno.com/"
    Vegas = 'https://www.appliancerepair-vegas.com/'
    Sacramento = 'https://fmx-appliance-repair.com/'
    Clovis = 'https://clovisappliancerepair.com/'
