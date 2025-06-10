import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    #ゲームの初期化
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img_fly = pg.image.load("fig/3.png") #Surfaceインスタンス
    kk_img_fly = pg.transform.flip(kk_img_fly, True, False) #左右反転

    tmr = 0
    #ゲームのループ
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200

        screen.blit(bg_img, [-1 * x, 0])
        screen.blit(bg_img2, [-1 * x + 1600, 0])
        screen.blit(bg_img, [-1 * x + 3200, 0])
        screen.blit(kk_img_fly, [200, 300])
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()