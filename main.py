from Object3D import Object3D
import pygame


def main():
    pygame.init()
    pygame.display.set_caption("Linal")
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 700))
    model = Object3D(screen)

    modeling = True
    model.new_angle(.0005)

    mode = []

    while modeling:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                modeling = False
            if event.type == pygame.KEYDOWN and event.scancode not in (92, 90, 94, 96):
                match event.unicode:
                    case 'x':
                        if model.rotateX in mode:
                            mode.remove(model.rotateX)
                        else:
                            mode.append(model.rotateX)
                    case 'y':
                        if model.rotateY in mode:
                            mode.remove(model.rotateY)
                        else:
                            mode.append(model.rotateY)
                    case 'z':
                        if model.rotateZ in mode:
                            mode.remove(model.rotateZ)
                        else:
                            mode.append(model.rotateZ)
                    case 'a':
                        mode = [model.rotateY, model.rotateX, model.rotateZ]
                    case 'w' | 's':
                        pass
                    case _:
                        mode = []

        screen.fill((20, 20, 20))
        model.draw()

        if mode:
            [func() for func in mode]

        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            model.scale(1.015)
        if key[pygame.K_s]:
            model.scale(0.99)
        if key[pygame.K_KP8]:
            model.shear(0, 10)
        if key[pygame.K_KP4]:
            model.shear(-10, 0)
        if key[pygame.K_KP6]:
            model.shear(10, 0)
        if key[pygame.K_KP2]:
            model.shear(0, -10)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
