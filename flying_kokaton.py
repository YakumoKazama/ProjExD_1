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
    kk_rect = kk_img_fly.get_rect()
    kk_rect.center = 300, 200

    tmr = 0
    kk_x = 300
    kk_y = 200
    #ゲームのループ
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        #背景の描画
        x = tmr % 3200
        screen.blit(bg_img, [-1 * x, 0])
        screen.blit(bg_img2, [-1 * x + 1600, 0])
        screen.blit(bg_img, [-1 * x + 3200, 0])

        #キーボード操作の実装
        kk_move_x = -1 #何もキーを押していないときは左に動く.
        kk_move_y = 0
        key_lst = pg.key.get_pressed()

        if key_lst[pg.K_UP]: 
            kk_move_y -= 1
        if key_lst[pg.K_DOWN]: 
            kk_move_y += 1
        if key_lst[pg.K_LEFT]: 
            kk_move_x -= 1
        if key_lst[pg.K_RIGHT]: 
            kk_move_x += 2 #右にも動けるようにするため、さらに+2する

        kk_rect.move_ip((kk_move_x, kk_move_y))   
        screen.blit(kk_img_fly, kk_rect)

        #更新
        pg.display.update()
        tmr += 1        
        clock.tick(200)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()