import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    tmr = 0

    #こうかとん初期化
    chr_img = pg.image.load("ex01/fig/3.png")
    chr_img = pg.transform.flip(chr_img, True, False)
    chr_img2 = pg.transform.rotozoom(chr_img, 10, 1.0)
    chr_imgs = [chr_img, chr_img2]

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        x = -tmr
        screen.blit(bg_img, [x, 0])
        screen.blit(chr_imgs[tmr%2], [300, 200])
        pg.display.update()
        tmr += 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()