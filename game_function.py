import sys
import pygame
from  ball import Ball


def check_event(controller, group, settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                controller.moving_right = True
            elif event.key == pygame.K_LEFT:
                controller.moving_left = True
            elif event.key == pygame.K_SPACE:
                # 如果按下了空格键,说明是要发射球了
                if len(group) == 0:
                    # 说明当前没有球.可以进行发射
                    new_bullet = Ball(settings=settings, screen=screen, controller=controller)
                    group.add(new_bullet)


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                controller.moving_right = False
            elif event.key == pygame.K_LEFT:
                controller.moving_left = False


def update_screen(settings, screen, controller, group, blocks):
    screen.fill(settings.screen_bg)
    controller.blitme()
    for ball in group:
        if ball.rect.bottom <= 0 or ball.rect.top >= settings.screen_height:
            group.remove(ball)
        if ball.rect.x <= settings.ball_speed or (
                    ball.rect.x + settings.ball_width) >= (settings.screen_width - settings.ball_speed):
            ball.make_turn(True)
        if ball.rect.top <= 0:
            ball.make_turn(2)
        ball.draw_ball()

    for block in blocks:
        block.blitme()
    pygame.display.flip()


# 消除砖块
def update_block(group, blocks, controller):
    for ball in group:
        if pygame.sprite.spritecollideany(ball, blocks):
            # 判断当前的球是否与砖块发生碰撞,如果发生碰撞.进行角度的转换
            dic = pygame.sprite.groupcollide(group, blocks, False, False)
            print(dic)
            # for block in blocks:
            #     if pygame.sprite.spritecollideany(block, group):
            #         if (block.rect.bottom - ball.rect.bottom) > 5 or (block.rect.bottom - ball.rect.bottom) < -5:
            #             ball.make_turn(2)
            #             break;
            #         else:
            ball.make_turn(True)

        if pygame.sprite.spritecollideany(ball, controller):
            # 判断当前的控制器是否与球发生碰撞
            ball.make_turn(2)

    if len(blocks) == 0:
        # 说明砖块全部没有了
        print("game over!")
