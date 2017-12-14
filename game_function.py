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
            elif event.key == pygame.K_f:
                temp_list = []
                for ball in group:
                    for index in range(3):
                        new_ball = Ball(settings=settings, screen=screen, controller=controller)
                        new_ball.setX_Y(ball.x, ball.y, index)
                        temp_list.append(new_ball)

                # 完成分裂之后.再添加到group当中
                for ball in temp_list:
                    group.add(ball)
                print(temp_list)


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
    # 判断当前的球是否与砖块发生碰撞,如果发生碰撞.进行角度的转换
    dic = pygame.sprite.groupcollide(group, blocks, False, False)
    # 返回的是字典.进行遍历操作
    # {<Ball sprite(in 1 groups)>: [<Block sprite(in 1 groups)>]}
    for key, value in dic.items():
        if (key.rect.top < value[0].rect.top) or (key.rect.bottom > value[0].rect.bottom):
            # 说明接触面在上面或下面
            key.make_turn(2)
        else:
            key.make_turn(True)
        # 移除砖块
        for v in value:
            # 如果是不能损毁的砖块移除
            if v.destory == False:
                value.remove(v)
        blocks.remove(value)

    dic2 = pygame.sprite.groupcollide(group, controller, False, False)
    for key, value in dic2.items():
        key.make_turn(2)
        # ball.make_turn(2)
    if len(blocks) == 0:
        # 说明砖块全部没有了
        print("game over!")
