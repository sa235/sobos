from asyncio.windows_events import NULL
import imp
import time
import mouse
from PIL import ImageGrab
from PIL import ImageChops



def equal(im1, im2):
    return ImageChops.difference(im1, im2).getbbox() is None

# dispaly resolution 1920x1080
def mouse_on_right_top_corn():
    mp = mouse.get_position()
    #print(mp)
    if mp[0] > 1918 and mp[1] < 2:
        return True

    return False

# mouse on next button
def mouse_on_next():
    while not mouse_on_right_top_corn():
        print('waiting')
        time.sleep(1)
    
        mp = mouse.get_position()
        if mp[0] > 410 and mp[1] > 1010 and mp[0] < 436 and mp[1] < 1023 :
            return True

    return False


def click_next():
    mouse.move(431, 1022, absolute=True, duration=0)
    mouse.click()
    print('click_next')


def screenshot_board_table():
    """
    Screenshot of the sales table area
    """
    img = ImageGrab.grab(bbox=(62, 84, 1370, 964))
    img.save(r'temp\{}_scan.png'.format(time.strftime("%Y%m%d-%H%M%S")))
    #img.show()  


def main():
    enable_next_button_img = None
    while mouse_on_next():
        click_next()
        if enable_next_button_img is None:
            enable_next_button_img = ImageGrab.grab(bbox=(410, 1010, 436, 1023))
            #active_next_button_img.show()
        
        disable_next_button_img = ImageGrab.grab(bbox=(410, 1010, 436, 1023))    
        screenshot_board_table()

        if not equal(enable_next_button_img, disable_next_button_img):
            print('scan complete')
            break

    print('scan end')


if __name__ == '__main__':
    main()


