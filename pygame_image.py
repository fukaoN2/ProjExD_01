import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    tmr = 0

    #こうかとん初期化
    chr_img = pg.image.load("ex01/fig/3.png")
    chr_img = pg.transform.flip(chr_img, True, False)
    #chr_img2 = pg.transform.rotozoom(chr_img, 10, 1.0)
    chr_imgs = []
    for i in range(0, 11, 1):
        chr_img2 = pg.transform.rotozoom(chr_img, i, 1.0)
        chr_imgs.append(chr_img2)

    count = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(chr_imgs[count], [300, 200])
        pg.display.update()
        tmr += 1
        count += 1
        if count == len(chr_imgs):
            count = 0

        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()