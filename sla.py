from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
import os
import pickle
from time import sleep as slp
import threading

try:
    os.mkdir(r'C:\cookies_bot_loiola\imagens')
except:
    print("C:\cookies_bot_loiola\imagens ja existe")
# for i in range(11):
#     with open()

#
num_threads = int(input("oiiiieeeeeeeeeee tales\n"
      "numero de trheads amigo (rapido, nao tenho o dia inteiro...): "))

def algo(j) ->None:
    with open(f"C:/Users/Desktop/Downloads/videos{j}.txt", 'r') as f:
        videos = f.readlines()

    def forEachVideo(video, videos, attempt):
        # if f"imagem{j}-{video}.png" in os.listdir(r'C:\Users\Desktop\PycharmProjects\pythonProject6') and video+1 < len(videos):
        #     print(video)
        #     forEachVideo(video+1,videos,attempt)
        def recal():
            if attempt < 2:
                forEachVideo(video, videos, attempt+1)
            else:
                forEachVideo(video+1, videos, 0)
    # for video in range(len(videos)):

        chrome_options = Options()
        chrome_options.add_argument("--window-position=-1000,0")

        driver = webdriver.Chrome(f"C:/chromedriver{j}.exe", options=chrome_options)
        driver.maximize_window()
        a = ActionChains(driver)

        def saveCookies():
            cookies = driver.get_cookies()
            pickle.dump(cookies, open(f'C:/cookies_bot_loiola/cookies{j}.txt', 'wb'))

        def loadCoookies() -> None:
            cookies = pickle.load(open(f"C:\cookies_bot_loiola\cookies{j}.txt", 'rb'))
            for i in cookies:
                driver.add_cookie(i)
            driver.refresh()

        driver.get(videos[video])
        driver.maximize_window()
        # slp(1)
        # try:
        #     loadCoookies()
        # except:
        #     saveCookies()
        slp(2)
        loadCoookies()
        #     loadCoookies()
        # if driver.get_cookie("c_user") == None:
        #     for i in range(120):
        #         if driver.get_cookie("c_user") == None:
        #             slp(1)
        #         else:
        #             print(driver.get_cookie("c_user"))
        #             break
        if driver.get_cookie("c_user")!= None:
            print(f"login bem sucedido -- thread{j}")
        else:
            driver.close()
            recal()


        # def ele():
            # element = None
            # while element != None:
            #     try:
            #         element = driver.execute_script(
            #             "return document.getElementsByClassName('oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw')")
            #         return True
            #     except Exception as e:
            #         print(e)
            #         return False


        try:
            for tempo in range(5):
                element = driver.execute_script(
                    "return document.getElementsByClassName('oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw')")
                if len(element) > 0:
                    break
                else:
                    slp(1)
            a.move_to_element_with_offset(element[0], 50, 0).click().perform()

        except Exception as e:
            print(e)
            driver.close()
            recal()

        try:
            link = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div/div[2]/div[3]/a'))
            )
            link = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div/div[2]/div[3]/a'))
            )
            element = driver.execute_script(
                "return document.getElementsByClassName('cypi58rs pmk7jnqg fcg2cn6m tkr6xdv7')")
            if len(element) > 0:
                element[0].click()
            link.click()

        except Exception as e:
            try:
                a.move_to_element(link).click().perform()

            except Exception as e:
                slp(20)
                print(e)
                driver.close()
                recal()
            # try:
            #     print(e)
            #     slp(0.3)
            #     element = driver.execute_script(
            #         "return document.getElementsByClassName('oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw')")
            #     a.move_to_element_with_offset(element[0], 50, 0).click().perform()
            # except:
            #     driver.close()
            #     algo(j)

        # driver.set_window_position(-1100,0)
        # driver.maximize_window()
        try:
            driver.switch_to.window(driver.window_handles[1])
            link = WebDriverWait(driver, 100).until(
                EC.presence_of_element_located(
                    (By.TAG_NAME,
                     'video'))
            )
        except Exception as e:
            print(e)
            print("alog deu errado")
            recal()
        finally:
            try:
                element = driver.execute_script('return document.getElementsByClassName("autofocus _9l2h  layerCancel _4jy0 _4jy3 _4jy1 _51sy selected _42ft")')
                print(element)
                element.click()
            except:
                print(f'sem poppup na tela de grafico -- thread{j}')
            driver.execute_script("document.body.style.zoom='72%'")
            driver.save_screenshot(f'imagem{j}-{video}.png')
            print(f"imagem salva {j}-{video}")
            input()

        driver.quit()

        if video <= len(videos)-1:
            forEachVideo(video+1, videos, 0)
    forEachVideo(0, videos,0)
# for i in range(300):
#     print("aaa")
#     algo(webdriver.Chrome(r"C:/chromedriver1.exe"))
# for i in range(num_threads):
#     print(f'i {i+1}')
#     thread = threading.Thread(target=algo, args=[i+1])
#     thread.start()
lista_videos = []
for i in range(6):
    with open(f"C:/Users/Desktop/Downloads/videos{i+1}.txt", 'r') as videos:
        videos = videos.readlines()
        for video in range(len(videos)):
            if f"imagem{i+1}-{video}.png" not in os.listdir(r"C:\Users\Desktop\PycharmProjects\pythonProject6\imagens"):
                lista_videos.append(videos[video])
                print(f"imagem{i+1}-{video}.png")
with open(r"C:\Users\Desktop\PycharmProjects\pythonProject6\videos-pulados.txt",'w') as f:
    f.writelines(lista_videos)
with open(r"C:\Users\Desktop\PycharmProjects\pythonProject6\videos-pulados.txt",'r') as f:
    lines = f.readlines()
    print(len(lines))


